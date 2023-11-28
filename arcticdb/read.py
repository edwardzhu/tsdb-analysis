from arcticdb import Arctic, QueryBuilder
from datetime import datetime
import pandas as pd

def get_library(ac: Arctic, dbname: str):
    if dbname not in ac.list_libraries():
        ac.create_library(dbname)
    return ac[dbname]

def run(s3_url: str, dbname: str, table: str):
    ac = Arctic(s3_url)
    library = get_library(ac, dbname)
    for i in ["BNBUSDT", "BTCUSDT", "ETHUSDT"]:
        q = QueryBuilder()
        q = q[q["Instrument"] == i]
        df = library.read(table, query_builder=q).data
        df['OpenTime'] = pd.to_datetime(df["OpenTime"])
        df = df.groupby(pd.Grouper(key="OpenTime", freq="5T")).agg({
            "Open": "first", "High": "max", "Low": "min", "Close": "last", "Volume": "sum"
        })
        print(df)

if __name__ == "__main__":
    now = datetime.utcnow()
    run("s3://s3.ap-southeast-1.amazonaws.com:{s3_bucket}?aws_auth=true", "{dbname}", "{tablename}")
    end_now = datetime.utcnow()
    print(f"Time Elapsed: {end_now - now}")
