---
title: mongoDB - python으로 mongoDB 사용하기
category: mongoDB
tags: mongoDB python pymongo database db sql nosql
---

## mongoDB - python

- python에서 mongoDB에 접속해서 데이터를 insert, select, update 등을 해보려고 합니다.
- 우선 `pymongo`를 설치해줍니다.

```shell
conda install pymongo
```

## Basic Usage

- pymongo를 사용해서 서버에 접속하고, collection을 연결합니다.

```python
import pymongo

client = pymongo.MongoClient('localhost', 27017)
# client = MongoClient('mongodb://localhost:27017/')

# Get DB
# test(DB)는 mongoDB를 설치하면 처음부터 만들어져 있는 DB
testDB = client.test
# --------------------------------------------
# Drop Collection
# 이미 존재하는 Collection을 Drop(삭제)합니다.
testDB.drop_collection("testCollection")

# -------------------------------------------- 
# Create Collection
testDB.create_collection("testCollection")
# Get Collection
testCollection = testDB.get_collection("testCollection")
```

- collection의 method인 `insert_one`, `insert_many`를 사용해서 데이터를 Insert해줍니다.

```python
# -------------------------------------------- 
# Insertion
# PK가 따로 존재하지 않고, dictionary의 key set가 달라도 문제없이 Insert됩니다.
# 내부 dictionary에 `_id`라는 칼럼이 생성되는데, 이 값이 PK라고 생각하면 됩니다.
print("-------------------------------------")

# Insert one documents
print("-- insert a row -------------------")
testCollection.insert_one({"k1": "v1", "k2": "v2"})
# Insert many documents
print("-- insert a row -------------------")
testCollection.insert_many([
    {"col1": "v1", "col2": "v1"}, 
    {"col1": "v2", "col2": "v3"}, 
    {"col1": "v3", "col2": "v3"}
])
```

- `.find()`를 사용해서 데이터를 검색해서 가져올 수 있습니다.
- `.find(filter_dict)`를 사용하면, `filter_dict`와 동일한 key-value pair를 가진 dict만을 선택해서 가져옵니다.

```python
# -------------------------------------------- 
# Select all row
print("-------------------------------------")
print("-- Select all row -------------------")

for each_document in testCollection.find():
    print(f"Row: {each_document}")
"""output
Row: {'_id': ObjectId('605df2d40d183dff03122a84'), 'k1': 'v1', 'k2': 'v2'}
Row: {'_id': ObjectId('605df2d40d183dff03122a85'), 'col1': 'v1', 'col2': 'v1'}
Row: {'_id': ObjectId('605df2d40d183dff03122a86'), 'col1': 'v2', 'col2': 'v3'}
Row: {'_id': ObjectId('605df2d40d183dff03122a87'), 'col1': 'v3', 'col2': 'v3'}
"""

# -------------------------------------------- 
# Select filtered rows
# filter_dict라는, 검색하려는 key-value pair들을 넣어주면
# 해당 key-value pair들을 가진 row들을 검색해서 가져옵니다.
print("-------------------------------------")
print("-- Select filtered Rows -------------")
filter_dict = {"col2": "v3"}

for each_document in testCollection.find(filter_dict):
    print(f"Row: {each_document}")
"""output
Row: {'_id': ObjectId('605df35d362746f73484a3c0'), 'col1': 'v2', 'col2': 'v3'}
Row: {'_id': ObjectId('605df35d362746f73484a3c1'), 'col1': 'v3', 'col2': 'v3'}
"""
```

- `.update_one()`을 사용하면 document를 찾아서 값을 업데이트해주면 됩니다.
- 그냥 python dictionary와 동일한 방식으로 업데이트 된다고 생각하시면 됩니다.

```python
# -------------------------------------------- 
# Update row 
# 기존 key-value pair가 있을 경우 그대로 존재하고 새로운 dict가 업데이트 된다.
# 이건 python의 dictionary와 동일하다고 보면 됨.
print("-------------------------------------")
print("-- Update ---------------------------")
filter_dict = {"k1": "v1"} 
testCollection.update_one(filter_dict, {"$set": {"col1": "new_column"}})

for each_document in testCollection.find():
    print(f"Row: {each_document}")
"""output
Row: {'_id': ObjectId('605df66bfb148936b0af08b2'), 'k1': 'v1', 'k2': 'v2', 'col1': 'new_column'}
Row: {'_id': ObjectId('605df66bfb148936b0af08b3'), 'col1': 'v1', 'col2': 'v1'}
Row: {'_id': ObjectId('605df66bfb148936b0af08b4'), 'col1': 'v2', 'col2': 'v3'}
Row: {'_id': ObjectId('605df66bfb148936b0af08b5'), 'col1': 'v3', 'col2': 'v3'}
"""
```

- `.replace()`는 기존에 있던 row를 새로운 값으로 대채헤줍니다.

```python
# -------------------------------------------- 
# Replace
# replace는 기존에 있떤 Row를 새로운 값으로 대체해 줍니다.
print("-------------------------------------")
print("-- Replace --------------------------")
filter_dict = {'k1': 'v1'}
new_dict = {'col1': 'new_column'}
testCollection.replace_one(filter_dict, new_dict)

for each_document in testCollection.find():
    print(f"Row: {each_document}")
"""output
Row: {'_id': ObjectId('605dfeec830e27cdbb6acf5a'), 'col1': 'new_column'}
Row: {'_id': ObjectId('605dfeec830e27cdbb6acf5b'), 'col1': 'v1', 'col2': 'v1'}
Row: {'_id': ObjectId('605dfeec830e27cdbb6acf5c'), 'col1': 'v2', 'col2': 'v3'}
Row: {'_id': ObjectId('605dfeec830e27cdbb6acf5d'), 'col1': 'v3', 'col2': 'v3'}
"""
```

## Wrap-up

- 간단하게 mongoDB에 접속해서 데이터를 insert, select, update, replace 등을 하는 방법을 정리하였습니다.

## Reference

- [mongoDB - drivers - pymongo](https://docs.mongodb.com/drivers/pymongo/)
- [pymongo - readthedocs - tutorial](https://pymongo.readthedocs.io/en/stable/tutorial.html)

---

## Raw code

```python
import pymongo

client = pymongo.MongoClient('localhost', 27017)
# client = MongoClient('mongodb://localhost:27017/')

# Get DB
# test(DB)는 mongoDB를 설치하면 처음부터 만들어져 있는 DB
testDB = client.test
# --------------------------------------------
# Drop Collection
# 이미 존재하는 Collection을 Drop(삭제)합니다.
testDB.drop_collection("testCollection")

# -------------------------------------------- 
# Create Collection
testDB.create_collection("testCollection")
# Get Collection
testCollection = testDB.get_collection("testCollection")

# -------------------------------------------- 
# Insertion
# PK가 따로 존재하지 않고, dictionary의 key set가 달라도 문제없이 Insert됩니다.
# 내부 dictionary에 `_id`라는 칼럼이 생성되는데, 이 값이 PK라고 생각하면 됩니다.
print("-------------------------------------")

# Insert one documents
print("-- insert a row -------------------")
testCollection.insert_one({"k1": "v1", "k2": "v2"})
# Insert many documents
print("-- insert a row -------------------")
testCollection.insert_many([
    {"col1": "v1", "col2": "v1"}, 
    {"col1": "v2", "col2": "v3"}, 
    {"col1": "v3", "col2": "v3"}
])

# -------------------------------------------- 
# Select all row
print("-------------------------------------")
print("-- Select all row -------------------")

for each_document in testCollection.find():
    print(f"Row: {each_document}")
"""output
Row: {'_id': ObjectId('605df2d40d183dff03122a84'), 'k1': 'v1', 'k2': 'v2'}
Row: {'_id': ObjectId('605df2d40d183dff03122a85'), 'col1': 'v1', 'col2': 'v1'}
Row: {'_id': ObjectId('605df2d40d183dff03122a86'), 'col1': 'v2', 'col2': 'v3'}
Row: {'_id': ObjectId('605df2d40d183dff03122a87'), 'col1': 'v3', 'col2': 'v3'}
"""

# -------------------------------------------- 
# Select filtered rows
# filter_dict라는, 검색하려는 key-value pair들을 넣어주면
# 해당 key-value pair들을 가진 row들을 검색해서 가져옵니다.
print("-------------------------------------")
print("-- Select filtered Rows -------------")
filter_dict = {"col2": "v3"}

for each_document in testCollection.find(filter_dict):
    print(f"Row: {each_document}")
"""output
Row: {'_id': ObjectId('605df35d362746f73484a3c0'), 'col1': 'v2', 'col2': 'v3'}
Row: {'_id': ObjectId('605df35d362746f73484a3c1'), 'col1': 'v3', 'col2': 'v3'}
"""

# -------------------------------------------- 
# Update row 
# 기존 key-value pair가 있을 경우 그대로 존재하고 새로운 dict가 업데이트 된다.
# 이건 python의 dictionary와 동일하다고 보면 됨.
print("-------------------------------------")
print("-- Update ---------------------------")
filter_dict = {"k1": "v1"} 
testCollection.update_one(filter_dict, {"$set": {"col1": "new_column"}})

for each_document in testCollection.find():
    print(f"Row: {each_document}")
"""output
Row: {'_id': ObjectId('605df66bfb148936b0af08b2'), 'k1': 'v1', 'k2': 'v2', 'col1': 'new_column'}
Row: {'_id': ObjectId('605df66bfb148936b0af08b3'), 'col1': 'v1', 'col2': 'v1'}
Row: {'_id': ObjectId('605df66bfb148936b0af08b4'), 'col1': 'v2', 'col2': 'v3'}
Row: {'_id': ObjectId('605df66bfb148936b0af08b5'), 'col1': 'v3', 'col2': 'v3'}
"""

# -------------------------------------------- 
# Replace
# replace는 기존에 있떤 Row를 새로운 값으로 대체해 줍니다.
print("-------------------------------------")
print("-- Replace --------------------------")
filter_dict = {'k1': 'v1'}
new_dict = {'col1': 'new_column'}
testCollection.replace_one(filter_dict, new_dict)

for each_document in testCollection.find():
    print(f"Row: {each_document}")
"""output
Row: {'_id': ObjectId('605dfeec830e27cdbb6acf5a'), 'col1': 'new_column'}
Row: {'_id': ObjectId('605dfeec830e27cdbb6acf5b'), 'col1': 'v1', 'col2': 'v1'}
Row: {'_id': ObjectId('605dfeec830e27cdbb6acf5c'), 'col1': 'v2', 'col2': 'v3'}
Row: {'_id': ObjectId('605dfeec830e27cdbb6acf5d'), 'col1': 'v3', 'col2': 'v3'}
"""
```
