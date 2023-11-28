# TimescaleDB

## Prerequisite

* Python 3.7+
* psycopg2 latest

## Database

Timescale version: 2.11.2 Postgresql 15
Server:

* OS: Ubuntu 22.04 amd64
* AWS VM family: m6i.large (2 vCPU, 8 GB RAM)

Database build script:

1. build.script
2. createTable.sql

## Features

|   Feature        |      Status        |           Comments                           |
|:----------------:|:------------------:|----------------------------------------------|
|  Live Stream     |  &#x2714;          | [Document](https://docs.timescale.com/use-timescale/latest/continuous-aggregates/)|
|  SQL Support     |  &#x2714;          | Support Postgre SQL.                         |
|  Documentation   |  English           | [Tutorial](https://docs.timescale.com/)      |
|  SDK Support     | Java, Javascript, Python, Go | [Document](https://docs.timescale.com/quick-start/latest/) |
|  Decimal Support |  &#x2714;          | PostgreSQL supports, but `numeric` isn't optimized and recommended. [Link](https://www.timescale.com/blog/best-practices-for-picking-postgresql-data-types/) |
|  Client          |  Application       | You can use QBeaver to access.               |
|  Backup & Restore|  S3, Azure Blob, Google Stroage, Swift, Filesystem | [Wale-E](https://github.com/wal-e/wal-e) |
