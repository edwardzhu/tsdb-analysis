from questdb.ingress import Sender
import pandas as pd;
from datetime import datetime;

def add(host: str, port: int = 9009, path: str = "marketdata.csv"):
    df = pd.read_csv(path)
    df["OpenTime"] = pd.to_datetime(df["OpenTime"])
    with Sender(host, port) as sender:
        print("setup the connection!")
        now = datetime.utcnow()
        sender.dataframe(df, table_name = "spot", at='OpenTime')
        sender.flush()
        end_now = datetime.utcnow()
        print(f"Time Elapsed: {end_now - now}")

if __name__ == "__main__":
    add("<uri>", path="<filename>")
