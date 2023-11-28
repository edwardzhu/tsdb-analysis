import dolphindb as ddb
import pandas as pd
import dolphindb.settings as keys
from decimal import *
from datetime import datetime
    
def run(dbname: str, tablename: str, url: str, port: int = 8902, username: str = "", password: str = "", path: str = "marketdata.csv"):
    session = ddb.session(protocol=keys.PROTOCOL_DDB, enableASYNC=True)
    status = session.connect(url, port, userid=username, password=password, reconnect=True)
    if not(status) :
        print("Fail to connect to the server.")
        return None
    print("Sessiont established!")
    df = pd.read_csv(path)
    df["OpenTime"] = pd.to_datetime(df["OpenTime"])
    df.iloc[:, 2:] = df.iloc[:, 2:].apply(lambda x: x.apply(lambda y: Decimal(y).quantize(Decimal('0.00000000'))))
    print(df)
    now = datetime.utcnow()
    session.run("append!{{loadTable('{db}', `{tb})}}".format(db=dbname, tb=tablename), df)
    end_now = datetime.utcnow()
    print(f"Time elapsed: {end_now - now}")
    session.close()
        
if __name__ == "__main__":
    #asyncio.run(read_entry("BNBUSDT_1m_2019-1-1_2020-1-1.json", "BNBUSDT"))
    run("dfs://marketdata", "spot", "13.215.240.48", port=31845, username="admin", password="123456")