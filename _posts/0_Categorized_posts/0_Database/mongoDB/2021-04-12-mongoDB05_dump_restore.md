---
title: mongoDB - dump, restore
category: mongoDB
tags: mongoDB python pymongo database db sql nosql brew
---

## mongoDB - dump, restore

- mongoDB를 사용하여 특정 DB를 백업하고 복구하는 방법을 정리합니다.
- 그냥 mongodump를 사용하여 백업하면 된다고 하는데 실제로 해보니까 다음과 같은 오류가 발생합니다.

```plaintext
> mongodump
uncaught exception: ReferenceError: mongodump is not defined :
@(shell):1:1
```

- 구글에서 찾아봐서 [stackoverflow - mongodb - mongodump is not defined](https://stackoverflow.com/questions/34875913/mongodb-mongodump-is-not-defined) 포스팅을 확인해 보니, 다음과 같은 답변이 있습니다.
- 해석하자면 대충 "mongodump는 mongo-shell command가 아니야, 원래 깔려 있는 애가 아니니까 mongodb-tools라는 패키지를 설치해줘야 쓸 수 있어"인 것 같네요. mongorestore도 마찬가지인 것 같습니다.

```plaintext
'mongodump' is a command/tool which is included in the 'mongodb-tools' package. If you don't have this package installed on your machine, it makes sense that it is not defined. The mongodb-tools also provide several other tools used for importing and exporting DBs (like mongorestore).

That being said, 'mongodump' is not a mongo-shell command, you shouldn't be using it in mongo-shell. It's a whole different command that you would be executing just like you execute 'mongod' or 'mongo' etc.
```

## mongodb tools 

- [mongodb - database tools](https://docs.mongodb.com/database-tools/)에서 확인해 본 결과, 다음과 같은 내용을 확인했습니다.
- mongoDB 4.4 버전부터는 mongoDB db Tools는 더이상 함께 할 수 없습니다(오열). 이라는 얘기죠. 
- 그리고 버전은 100.0.0부터 시작한다고 합니다 호호호. 이는 4부터 시작하는 mongoDB와 완전히 별개임을 명확히 하기 위한 것으로 보이네요. 100과 4는 헷갈릴 수가 없으니까요.

> Starting with MongoDB 4.4, the MongoDB Database Tools are now released separately from the MongoDB Server and use their own versioning, with an initial version of 100.0.0. Previously, these tools were released alongside the MongoDB Server and used matching versioning.

### Why - Separating Database Tools from MongoDB Server

- [mongodb - separating database tools server](https://www.mongodb.com/blog/post/separating-database-tools-server)를 확인해보면 mongoDB와 mongoDB tools가 분리된 이유가 나옵니다.
- 대강 정리하자면, 다음과 같습니다.
  - 사람들은 이미 직접 mongoDB를 local에 설치해서 사용하는 것보다, mongoDB Atlas를 사용하는 경우가 더 많아지고 있다.
  - 그러나, mongoDB Atlas를 사용하는 경우에도, 종종 local의 데이터를 Atlas로 보내거나 하는 이유로 mongoDB tools가 필요한 경우들이 있다.
  - 그러나, mongoDB tools와 mongoDB는 오랫동안 통합되어 관리해 왔기 때문에, mongoDB tools만 필요한 경우에도, mongoDB를 설치해야 하는 번거로움이 있었다.
  - 또한, mongoDB tools에서 발생한 버그를 고친 후, 이를 통합하려면 mongoDB server가 릴리즈될때까지 기다려야 한다는 등의 문제가 있었다.
  - 따라서, 최종적으로는 mongoDB Server와 mongoDB tools를 구분하기로 하였다, 라는 이야기네요.

### Install mongoDB tools 

- shell에서 `mongo --version`을 사용해서 확인해보면 역시 제 버전은 4.4 버전입니다.
  - mongo shell에서 실행하지 말고 외부에서 실행해야 버전이 정확하게 나옵니다.

```bash
$ mongo --version
MongoDB shell version v4.4.3
Build Info: {
    "version": "4.4.3",
    "gitVersion": "",
    "modules": [],
    "allocator": "system",
    "environment": {
        "distarch": "x86_64",
        "target_arch": "x86_64"
    }
}
```

- [mongodb - download - database tools](https://www.mongodb.com/try/download/database-tools)에서 mongoDB tools를 다운받아서 사용해도 됩니다만, 저는 mac 유저라서 `brew` 를 사용해서 설치합니다.

```bash
$ brew list | grep mongodb-database-tools
mongodb-database-tools

$ brew install mongodb-database-tools
Updating Homebrew...
Warning: mongodb/brew/mongodb-database-tools 100.3.1 is already installed and up-to-date.
To reinstall 100.3.1, run:
  brew reinstall mongodb-database-tools

$ brew upgrade mongodb-database-tools
Warning: mongodb/brew/mongodb-database-tools 100.3.1 already installed
```

- 그런데, 저는 mongoDB도 brew를 사용해서 설치했습니다. 따라서, 이미 mongoDB tool도 설치되어 있는 상황이었죠. 그런데 왜 안되는걸까요?

### 그냥 shell에서 실행해야 합니다

- 후...지금가지는 `mongodump`를 mongodb Shell에서 실행해줬습니다. 따라서 다음 오류가 발생했던 것이죠.

```bash
uncaught exception: ReferenceError: mongodump is not defined :
@(shell):1:1
```

- 이걸 그냥 shell에서 실행하면 잘 실행됩니다.
- 아래 커맨드는 `target_DB_name`을 현재 경로 밑에 `dump`라는 폴더 내에 백업해주는 것을 말합니다.

```bash
$ mongodump --db target_DB_name
2021-04-12T20:14:02.379+0900    writing target_DB_name.collection_A to dump/target_DB_name/collection_A.bson
2021-04-12T20:14:02.383+0900    writing target_DB_name.collection_B to dump/target_DB_name/collection_B.bson
2021-04-12T20:14:02.867+0900    done dumping target_DB_name.collection_A (174124 documents)
2021-04-12T20:14:04.016+0900    done dumping target_DB_name.collection_B (173955 documents)
```

- 다른 커맨드들도 많은데, 저는 일단 restore는 필요하지 않아서, backup만 해둡니다.

## Wrap-up

- 그냥 shell에서 실행해야 하는 것을 mongoDB shell에서 실행하여 먼 길을 돌아왔습니다 호호. 뭐 어쩄거나 좋게 보면 그 덕분에 mongoDB와 mongoDB tool이 분리되었다거나 하는 것들도 알게 되었으니 뭐 좋다고 봐야겠죠 호호.
- 사실 mongoDB와 mongoDB tools가 개별적이라면, `mongo`를 통해 실행하는 mongoDB와 mongoDB tools는 다르다는 게 당연한 것처럼 보입니다. 제가 그걸 늦게 알아차린 것이죠 호호.
- 백업이라고 되어 있지만, 사실 `bson`이라고 하는 json과 유사한 파일로 저장해주는 거라고 보면 됩니다. 이럴 거면 그냥 제가 몽고DB에 접속해서 데이터를 다 긁어와서 저장하는 것이랑 딱히 큰 차이가 있다고 하기는 어려울 것 같아요. 그냥 복사해두는 거니까요 호호.

## Reference

- [stackoverflow - mongodb - mongodump is not defined](https://stackoverflow.com/questions/34875913/mongodb-mongodump-is-not-defined)
- [mongodb - database tools](https://docs.mongodb.com/database-tools/)
- [mongodb - database tools installation macos](https://docs.mongodb.com/database-tools/installation/installation-macos/)
