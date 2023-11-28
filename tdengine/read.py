import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine, text

def run(connection_str: str, database: str):
    engine = create_engine(connection_str)
    conn = engine.connect()
    for symbol in ["BNBUSDT", "BTCUSDT", "ETHUSDT"]:
        statement = f"select first(OpenTime) as BucketTime, first(open) as open, max(High) as High, min(Low) as Low, last(Close) as Close, sum(Volume) as Volume from {database}.{symbol} interval(5m);"
        df = pd.read_sql(text(statement), conn)
        print(df)
    conn.close()

if __name__=="__main__":
    now = datetime.utcnow()
    run("taos://username}:{password}@{host}:{port}/{database}", "{database}")
    end_now = datetime.utcnow()
    print(f"Time elapsed: {end_now - now}")
    