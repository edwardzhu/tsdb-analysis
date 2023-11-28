import pandas as pd
from datetime import datetime
from decimal import Decimal
from sqlalchemy import create_engine

def run_to_sql(connection_str: str, tablename: str, path: str = "."):
    engine = create_engine(connection_str)
    df = pd.read_csv(path)
    df["OpenTime"] = pd.to_datetime(df["OpenTime"])
    df.iloc[:, 2:] = df.iloc[:, 2:].apply(lambda x: x.apply(lambda y: Decimal(y).quantize(Decimal('0.00000000'))))
    print(df)
    now = datetime.now()
    r = df.to_sql(tablename, engine, if_exists='append', index=False)
    end_now = datetime.now()
    print(f"Time elapsed: {end_now - now}")    

            
if __name__ == "__main__":
    ## copy command does not support remote connection.
    run_to_sql("{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}", "spot", "<data file>")
    