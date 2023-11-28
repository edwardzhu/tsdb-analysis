# QuestDB

## Prerequisite

* Python 3.7+

## Database

QuestDB version: v7.3.1
Server:

* OS: Ubuntu 22.04 amd64
* AWS VM family: m6i.large (2 vCPU, 8 GB RAM)

Database build script:

1. create.sql
2. query.sql

## Features

|   Feature        |      Status        |           Comments                           |
|:----------------:|:------------------:|----------------------------------------------|
|  Live Stream     |  &#x10102;         | Can't find the document.                     |
|  SQL Support     |  &#x2714;          | Support SQL.                                 |
|  Documentation   |  English           | [Tutorial](https://questdb.io/docs/)         |
|  SDK Support     | C/C++, Java, Rust, Node.js C#, Go | [Document](https://questdb.io/docs/develop/connect/) |
|  Decimal Support |  &#x10102;         | Can't find the decimal. [https://questdb.io/docs/reference/sql/datatypes/] |
|  Client          |  Web               | Only use the web form.                       |
|  Backup & Restore|  Filesystem        | [Document](https://questdb.io/docs/operations/backup/) |
