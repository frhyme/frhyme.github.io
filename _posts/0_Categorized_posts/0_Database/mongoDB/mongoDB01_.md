---
title: 
category: 
tags: 
---

## Brew mongoDB

- Brew를 사용해서 mongoDB를 키고 끌 수 있는 것처럼 보임.

```bash
$ brew services start mongodb-community@4.4
$ brew services stop mongodb-community@4.4
```

- mongo

```plaintext
$ mongo
MongoDB shell version v4.4.3
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("be35156f-4fd3-4613-bb55-55ddaa2c9a00") }
MongoDB server version: 4.4.3
---
The server generated these startup warnings when booting: 
        2021-03-26T00:04:22.320+09:00: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
        2021-03-26T00:04:22.321+09:00: Soft rlimits too low
        2021-03-26T00:04:22.321+09:00:         currentValue: 2560
        2021-03-26T00:04:22.321+09:00:         recommendedMinimum: 64000
---
---
        Enable MongoDB's free cloud-based monitoring service, which will then receive and display
        metrics about your deployment (disk utilization, CPU, operation statistics, etc).

        The monitoring data will be available on a MongoDB website with a unique URL accessible to you
        and anyone you share the URL with. MongoDB may use this information to make product
        improvements and to suggest MongoDB products and deployment options to you.

        To enable free monitoring, run the following command: db.enableFreeMonitoring()
        To permanently disable this reminder, run the following command: db.disableFreeMonitoring()
---
> 
```

## Reference

- [mongodb - tutorial - install mongodb on OS X](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)