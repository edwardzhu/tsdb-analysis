# Dolphin

## Prerequisite

* Python Version: 3.8-3.10 (Recommended)
* NumPy: 1.18 - 1.23.4
* pandas: 1.0.0 or higher (version 1.3.0 is not supported)

## Database

Dolphin version: v2.00.10.1
Server:

* OS: Ubuntu 22.04 amd64
* AWS VM family: m6i.large (2 vCPU, 8 GB RAM)

Database build script: build.script

## Features

|   Feature        |      Status        |           Comments                           |
|:----------------:|:------------------:|----------------------------------------------|
|  Live Stream     |  &#x2714;          | [Document](https://github.com/dolphindb/Tutorials_EN/blob/master/streaming_tutorial.md)|
|  SQL Support     |  &#x2714;          | Support special SQL.                         |
|  Documentation   |  English, Chinese  | [Tutorial(English)](https://github.com/dolphindb/Tutorials_EN), [Tutorial(Chinese)](https://github.com/dolphindb/Tutorials_CN), [Help(English)](https://www.dolphindb.com/help/index.html), [Help(Chinese)](https://docs.dolphindb.cn/zh/help/index.html) |
|  SDK Support     | Python, Java, C++, C#, Go, Javascript | [gitHub](https://github.com/orgs/dolphindb) |
|  Decimal Support |  &#x2714;          |  From 2.0+                                   |
|  Client          |  Web               |  The web client is quite simple.             |
|  Backup & Restore|  S3, NFS           | [Document](https://github.com/dolphindb/dolphindb-k8s/blob/master/dolphindb_cloud_portal.md) |
