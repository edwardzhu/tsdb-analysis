# Time series Database Comparison

## Dataset

The testing data is 1-m historical spot from Binance for BTCUSDT, ETHUSDT and BNBUDST. Total size is: 473 MB. The data file is at [huggingface](https://huggingface.co/datasets/edzhu/binance_eth_bnb_btc_usdt_marketdata/blob/main/marketdata.csv).

## Test Case

* **Write Case**: Write the above data set to the database.
* **Read Case**: Read the 5-min aggregated OLHC value for 3 instruments.

## Result

| DB Type                 | Write Time (s)          | Write Storage (MB)           | Read Time (s) |
| ----------------------- | ----------------------- | ---------------------------- | ------------- |
| DolphinDB (TSDB)        |  39.767 s               |      265 MB                  |    7.719 s    |
| Timescale               |  229.066 s (to-sql)     |      813 MB                  |   23.684 s    |
| TDengine (multi-thread) |  23.253 s               |   626 MB (cooldown: 243 MB)  |   15.938 s    |
| QuestDB                 |  13.313 s               |      560 MB                  |    7.556 s    |
| ArcticDB                |  15.759 s               |      272 MB                  |   12.719 s    |
