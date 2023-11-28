# TDEngine

## Prerequisite

* Python 3.7+
* taospy latest
* taos driver (same version of database)

## Database

TDEngine version: 3.1.1.0
Server:

* OS: Ubuntu 22.04 amd64
* AWS VM family: m6i.large (2 vCPU, 8 GB RAM)

Database build script:

1. create.sql

## Features

|   Feature        |      Status        |           Comments                           |
|:----------------:|:------------------:|----------------------------------------------|
|  Live Stream     |  &#x2714;          | [Document](https://docs.tdengine.com/taos-sql/stream/)|
|  SQL Support     |  &#x2714;          | Support Postgre SQL.                         |
|  Documentation   |  English           | [Tutorial](https://docs.tdengine.com/)      |
|  SDK Support     | C/C++, Java, Rust, Node.js C#, Go | [Document](https://docs.tdengine.com/reference/connector/) |
|  Decimal Support |  &#x10102;         | [Issue](https://github.com/taosdata/TDengine/issues/3247) |
|  Client          |  Application       | Can use QBeaver to access.                   |
|  Backup & Restore| TDengine cluster, taosdump | [taosdump](https://docs.tdengine.com/reference/taosdump/), [Disaster Recovery](https://docs.tdengine.com/operation/tolerance/) |
