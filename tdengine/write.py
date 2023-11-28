import taos
import pandas as pd
from datetime import datetime
from typing import List
from multiprocessing import Pool

STEP: int = 8000
CHUNK: int = STEP * 20

def format_record(instrument, tablename, timestamp, metrics, row: pd.Series):
    return f"{instrument} USING {metrics} TAGS('{instrument}') VALUES ('{timestamp}', {row['Open']}, {row['High']}, {row['Low']}, {row['Close']}, {row['Volume']})"

def df2json(df: pd.DataFrame, template: str, tablename: str):
    records = []
    for _, row in df.iterrows():
        timestamp = row["OpenTime"]
        instrument = row["Instrument"]
        records.append(format_record(instrument, tablename, timestamp, template, row))
    return records

def commit(records: List[str], database: str, url: str, port: int = 6030, username: str = "", password: str = ""):
    conn = taos.connect(host = url, port = port, user = username, password = password, database = database)
    counter = 0
    r = 0
    len_records = len(records)
    while True:
        start = counter * STEP
        last = min((counter + 1) * STEP, len_records)
        statement = "INSERT INTO " + ' '.join(records[start:last]) + ";"
        r += conn.execute(statement)
        if last == len_records:
            break
        else:
            counter += 1
    conn.close()
    return r

    
def run(database: str, tablename: str, template: str, url: str, port: int = 6030, username: str = "", password: str = "", data_file: str = "marketdata.csv"):
    df = pd.read_csv(data_file)
    records = df2json(df, tablename, template)
    length = len(records)
    print(f"{length} records are loaded!")
    now = datetime.utcnow()
    maps = [[records[i:i+CHUNK], database, url, port, username, password] for i in range(0, length, CHUNK)]
    with Pool(4) as p:
        r = p.starmap(commit, maps)
    end_now = datetime.utcnow()
    print(f"Time elapsed: {end_now - now}, total records: {sum(r)}")


if __name__ == "__main__":
    run("<database name>", "<table name>", "<stable/template name>", "<server url>", username="<username>", password="<password>", data_file="<data file>")
