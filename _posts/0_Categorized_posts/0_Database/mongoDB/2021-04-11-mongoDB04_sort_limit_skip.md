---
title: mongoDB - find - sort, limit, skip
category: mongoDB
tags: mongoDB python pymongo database db sql nosql
---

## mongoDB - sort, limit, skip

- mongoDB의 find method에서 정렬(sort), 처음 n개로 제한(limit), 처음 n개를 제외(skip)하여 결과를 리턴하는 방법을 정리합니다.
- 저는 python에서 mongoDB에 접속하기 때문에, pymongo를 사용하고, 아래 코드들은 pymongo를 사용하여 해당 메소드들을 사용한 결과물이죠. 코드는 비슷합니다.

```python
import pymongo

# pymongo를 사용하여 mongoDB, Collection을 가져옵니다.
# 저는 DB가 Local에 설치되어 있기 때문에 아래처럼 localhost에서 가져왔습니다.
client = pymongo.MongoClient('localhost', 27017)

database_name = ""
target_DB = client.get_database(database_name)

# collection을 가져옵니다
target_collection_name = ""
target_collection = target_DB.get_collection(target_collection_name)

# ========================================================================
# key1을 오름차순(Ascending)으로 정렬하기
sort_list = [("key1", pymongo.ASCENDING)]
# 순서대로 limit_n으로 제한하기
limit_n = 3
cursor = target_collection.find().sort(sort_list).limit(limit_n)

# ========================================================================
# key1을 내림차순(Descending)으로 정렬하고,
# 처음 나오는 document를 skip_n만큼 제외하고
# 제외한 다음부터 limit_n 개를 가져오기
# 가령 doc1, 2, 3, 4, 5, 6, 7이 있다면
# 여기서는 2개를 건너 띄우고 5개를 가져오므로 3, 4, 5, 6, 7 문서가 리턴됩니다.
sort_list = [("key1", pymongo.DESCENDING)]
skip_n = 2
limit_n = 5
cursor = target_collection.find().sort(sort_list).skip(skip_n).limit(limit_n)

# ========================================================================
# key1은 오름차순(Ascending), key2는 내림차순(Descending)으로 정렬하고
# 
sort_list = [
    ("key1", pymongo.ASCENDING),
    ("key2", pymongo.DESCENDING)
]
cursor = target_collection.find().sort(sort_list)

# 출력하고 싶으면 다음 코드를 사용하면 됨.
for i, each_doc in enumerate(cursor):
    print(f"== Row {i:6d} ========")
    print(each_doc)
```
