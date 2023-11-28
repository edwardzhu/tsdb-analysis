import dolphindb as ddb
import dolphindb.settings as keys
import asyncio
from datetime import datetime

async def run(dbname: str, tablename: str, url: str, port: int = 8903, username: str = "", password: str = ""):
    session = ddb.Session(protocol=keys.PROTOCOL_DDB)
    status = session.connect(url, port, userid=username, password=password, keepAliveTime=3600, reconnect=True)
    if not(status):
        print("Fail to connect to the server.")
        return
    print("Connection established")
    for symbol in ["BTCUSDT", "BNBUSDT", "ETHUSDT"]:
        table = session.loadTable(tablename, dbname)
        # Add `$STRING` to convert the result to string. If not, `pandas.dataframe` will raise the error: Not allowed to create a vector with type DECIMAL128.
        # Since the `Open`, `High`, `Low` and `Close` value are stored as DECIMAL on the server side.
        table = table.select(['atImin(timestamp, open)$STRING', 'max(high)$STRING', 'min(low)$STRING', 'atImax(timestamp, close)$STRING', 'sum(buyVolume)$STRING', 'sum(sellVolume)$STRING']).where(f'symbol = "{symbol}"').groupby('symbol, bar(OpenTime, 5*60)')
        df = table.toDF()
        print(df)
    session.close()
    

if __name__ == "__main__":
    now = datetime.utcnow()
    asyncio.run(run("<db servername>", "<db>", "<server url>", username="<user name>", password="<password>"))
    end_now = datetime.utcnow()
    print(f"Time elapsed: {end_now - now}")
