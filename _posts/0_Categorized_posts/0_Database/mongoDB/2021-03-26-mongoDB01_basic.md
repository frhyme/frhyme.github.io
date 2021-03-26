---
title: mongoDB - basic
category: mongoDB
tags: database sql nosql mongodb macOS brew 
---

## mongoDB - Start mongoDB

- Brew를 사용해서 mongoDB를 키고 끌 수 있는 것처럼 보입니다. 아래처럼 직접 키고 또 끌 수 있죠.

```shell
> brew services start mongodb-community@4.4
> brew services stop mongodb-community@4.4
```

- terminal에서 mongodb server를 켜면, 다음처럼 mongoshell로 접속됩니다.

```shell
> mongo
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
```

- 간단히 데이터를 insert하고, query하기 위해서는 다음처럼 사용할 수 있습니다.
  - `db.createCollection(<collectionName>)`: `collectionName`이라는 이름의 Collection을 만들어줍니다. Collection은 일단은 그냥 table이라고 생각하셔도 상관없습니다.
  - `db.<collectionName>.insert( json )`: collection에 새로운 document를 집어넣어줍니다.
  - `db.<collectionName>.find( queryCondition )`: collection에 document를 query합니다.

```shell
> db.createCollection("testCollection")
{ "ok" : 1 }
> db.testCollection.insert({"title": "제목", "content": "내용"})
WriteResult({ "nInserted" : 1 })
> db.testCollection.find()
{ "_id" : ObjectId("605dae22b93205a932683c2d"), "title" : "제목", "content" : "내용" }
> db.testCollection.insert({"title": "제목", "content": "내용"})
WriteResult({ "nInserted" : 1 })
> db.testCollection.find()
{ "_id" : ObjectId("605dae22b93205a932683c2d"), "title" : "제목", "content" : "내용" }
{ "_id" : ObjectId("605daf00b93205a932683c2e"), "title" : "제목", "content" : "내용" }
```

### Create new Database

- 다만, 그냥 db만 쳐 보면 그냥 `test`라고 뜨는 것을 알 수 있죠. 앞서 말한 것처럼 Collection이 table이라면, db는 tablespace라고 생각해도 되겠죠. 제 기억이 맞다면 저는 `test`라는 db를 따로 만들어준 적이 없습니다. 그렇다면 아마도 기본으로 설정되어 있는 db의 이름이 `test`인 것 같아요.

```shell
> db
test
```

- 다음처럼 `show dbs`를 쳐 보면, 현재 사용가능한 db들이 쭉 뜨는 것을 알 수 있습니다.

```shell
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
test    0.000GB
```

- `use <database_name>`을 치면, local db로 들어가게 되죠. 만야 `<database_name>`이 존재하지 않는다면, 해당 이름의 database를 만들어 주게 됩니다.
- 아래에서 `abc`라는 db를 새롭게 만들었지만, `show dbs`에서는 뜨지 않습니다. 이는 아직 `abc` db에 아무것도 들어가 있지 않기 때문이죠. 
- collection을 하나 만들어준 다음 다시 `show dbs`를 치게 되면 잘 나오는 것을 알 수 있습니다.
- 현재 db를 날려버리려면 `db.dropDatabase()`를 사용하면 되죠.

```shell
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
test    0.000GB
> use abc
switched to db abc
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
test    0.000GB
> db
abc
> db.createCollection("collection1")
{ "ok" : 1 }
> show dbs
abc     0.000GB
admin   0.000GB
config  0.000GB
local   0.000GB
test    0.000GB
> db.dropDatabase()
{ "dropped" : "abc", "ok" : 1 }
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
test    0.000GB
> 
```

## Wrap-up

- 아주 간단하게 mongoDB를 사용해봤습니다 호호.

## Reference

- [mongodb - tutorial - install mongodb on OS X](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)
- [mongodb - basics - create database](https://www.mongodb.com/basics/create-database)
