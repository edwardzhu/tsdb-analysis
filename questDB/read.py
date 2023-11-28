import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime

#def read(url: str, port: int = 8812, user: str = "admin", password = ""):
def read(url):
    #conn = psycopg.connect(dbname = "questdb", host = url, port = port, user = user, password = password)
    engine = create_engine(url)
    conn = engine.connect()
    print("Connection established")
    try:
        for symbol in ["BNBUSDT", "ETHUSDT", "BTCUSDT"]:
            statement = "SELECT OpenTime, Instrument, first(Open) as Open, max(High) as High, min(Low) as Low, last(Close) as Close, SUM(Volume) as Volume FROM spot WHERE Instrument = '{symbol}' SAMPLE BY 5m;".format(symbol=symbol)
            print(statement)
            df = pd.read_sql(text(statement).execution_options(autoflush=True, autocommit=True), conn)
            print(df)
    finally:
        conn.close()

if __name__ == "__main__":
    now = datetime.utcnow()
    read("postgresql+psycopg2://<username>:<password>@<ip>:<port>/qdb")
    end_now = datetime.utcnow()
    print(f"Time elapsed: {end_now - now}")
    