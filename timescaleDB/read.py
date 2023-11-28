import asyncio
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from datetime import datetime

def run(connection_str: str, tablename: str):
    engine = create_engine(connection_str)
    with engine.connect() as conn:
        for symbol in ["BNBUSDT", "BTCUSDT", "ETHUSDT"]:
            script = """
                select time_bucket('5 minutes', "OpenTime") as "BucketTime", "Instrument", first("Open", "OpenTime"), max("High"), min("Low"), last("Close", "OpenTime"), sum("Volume") 
                from {tablename} where "Instrument" = '{symbol}' group by "BucketTime", "Instrument" order by "BucketTime"
            """.format(tablename=tablename, symbol=symbol)
            df = pd.read_sql_query(text(script), conn)
            print(df)
        

if __name__=="__main__":
    now = datetime.utcnow()
    run("{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}", "spot")
    end_now = datetime.utcnow()
    print(f"Time elasped: {end_now - now}")
    