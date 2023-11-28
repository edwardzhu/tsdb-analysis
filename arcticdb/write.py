from arcticdb import Arctic
from datetime import datetime
import pandas as pd
import numpy as np

def get_library(ac: Arctic, dbname: str):
    if dbname not in ac.list_libraries():
        ac.create_library(dbname)
    return ac[dbname]

def run(s3_url: str, dbname: str, table: str, path: str = "marketdata.csv"):
    df = pd.read_csv(path)
    print(df.columns)
    df["OpenTime"] = pd.to_datetime(df["OpenTime"]).values.astype(np.int64)
    df = df.set_index(df["OpenTime"])
    ac = Arctic(s3_url)
    library = get_library(ac, dbname)
    now = datetime.utcnow()
    library.write(table, df, staged=True)
    library.finalize_staged_data(table)
    end_now = datetime.utcnow()
    print(f"Time elasped: {end_now - now}")


if __name__ == "__main__":
    run("s3://s3.ap-southeast-1.amazonaws.com:{s3_bucket}?aws_auth=true", "{dbname}", "{tablename}")
