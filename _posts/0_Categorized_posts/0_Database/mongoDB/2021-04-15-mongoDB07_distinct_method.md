---
title: mongoDB - get Distinct(unique)
category: mongoDB
tags: mongoDB python pymongo database db sql nosql python pickle
---

## mongoDB - distinct 

- `target_collection.distinct(key_name)`를 사용하여 특정 칼럼의 distinct list를 가져올 수 있습니다.
- 아주 간단한 코드는 다음과 같습니다. `.distinct()`는 결과로 `list`를 반환합니다.
- 보통의 sql에서는 2개 이상에 대해서 distinct tuple을 가져올 수 있지만, pymongo에서 `.distinct()`로는 이를 사용할 수 없습니다.

```python
import pymongo

# pymongo를 사용하여 mongoDB, Collection을 가져옵니다.
# 저는 DB가 Local에 설치되어 있기 때문에 아래처럼 localhost에서 가져왔습니다.
client = pymongo.MongoClient('localhost', 27017)

# database, collection을 가져오고
database_name = ""
collection_name = ""

target_DB = client.get_database(database_name)
target_collection = target_DB.get_collection(collection_name)

# collection.distinct(key_name)
key_name = "key1"
distinct_list = target_collection.distinct(key_name)
print(type(distinct_list))  # <class 'list'>
print(len(distinct_list))  # 175392
```

## 칼럼 내 distinct 수에 따른 속도 차이

- 심심해서 칼럼 내 distinct 수에 따라 속도가 달라지는지를 확인해봤는데요. 
- 매우 당연히도, distinct 수가 적을 수록 속도가 빠릅니다 하하하.

```python
import pymongo
import time

# pymongo를 사용하여 mongoDB, Collection을 가져옵니다.
# 저는 DB가 Local에 설치되어 있기 때문에 아래처럼 localhost에서 가져왔습니다.
client = pymongo.MongoClient('localhost', 27017)

database_name = ""
collection_name = ""

target_DB = client.get_database(database_name)
target_collection = target_DB.get_collection(collection_name)

# 이 collection에는 175392 개의 document가 존재합니다.
print(f"# of item: {target_collection.count_documents({})}")


def get_distinct_lst(key_name):
    print(f"== Get Distinct {key_name}")
    start_time = time.time()
    # .distinct 메소드는 결과로 <class 'list'>를 반환합니다.
    distinct_list = target_collection.distinct(key_name)
    duration = time.time() - start_time
    print(f"# of distinct: {len(distinct_list)}")
    print(f"== Duration: {duration}")
    print("-----------------------------------------")


get_distinct_lst("URL_num_PK")
get_distinct_lst("Title")
get_distinct_lst("Author")
get_distinct_lst("Date")
```

- `URL_num_PK`의 경우 unique index가 걸려 있는데도 distinct 수가 비슷한 `Title`에 비해 속도가 많이 걸리고, `Date`의 경우 distinct의 수가 적어서 금방 끝나는 것을 알 수 있습니다.
- 아무튼 그냥 대충 칼럼 내 distinct 수가 많을 수록 오래 걸린다, 정도로 해석하면 됩니다.

```plaintext
# of item: 175392
== Get Distinct URL_num_PK
# of distinct: 175392
== Duration: 0.8157391548156738
-----------------------------------------
== Get Distinct Title
# of distinct: 173324
== Duration: 0.6424126625061035
-----------------------------------------
== Get Distinct Author
# of distinct: 12980
== Duration: 0.17502212524414062
-----------------------------------------
== Get Distinct Date
# of distinct: 2435
== Duration: 0.011368989944458008
-----------------------------------------
```

## distinct with filter

- `distinct`와 `filter`를 함께 쓰고 싶다면, 다음처럼 두 가지 방법이 있습니다.
  - `collection.find(filtered_dict).distinct(key_name)`
  - `collection.distinct(key_name, filter_dict`

```python
key_name = "Title"
filter_dict = {"Category": ""}

print("== cursor1")
start_time1 = time.time()
cursor1 = target_collection.find(filter_dict)
cursor1 = cursor1.distinct(key_name)
print(len(cursor1))
print(f"Duration: {time.time() - start_time1}")

print("== cursor2")
start_time2 = time.time()
cursor2 = target_collection.distinct(key_name, filter_dict)
print(len(cursor2))
print(f"Duration: {time.time() - start_time2}")
```

- 소요 시간은 별 차이 없어요.

```plaintext
# of item: 175392
== Case 1 start
== cursor1
24203
Duration: 0.1614992618560791
== cursor2
24203
Duration: 0.16252899169921875
```

## without distinct: 그냥 python으로 쓰면 안되나

- 뭐, `.distinct()`가 그렇게 구현하기 어려운 것도 아니고, 그냥 for loop를 사용해서 처리해보면 어떨까요.
- 코드는 대략 다음과 같습니다. 

```python
def compare_for_and_distinct(key_name):
    print("=======================================================")
    print("== Case 1: Distinct")
    start_time = time.time()
    title_distinct_lst = target_collection.distinct(key_name)
    print(len(title_distinct_lst))
    print(f"Duration: {time.time() - start_time}")
    
    print("-------------------------------------------------------")

    print("== Case 2: Find and For")
    start_time = time.time()
    title_set = set()
    for i, each_doc in enumerate(target_collection.find()):
        title_set.add(each_doc[key_name])
    print(len(title_set))
    print(f"Duration: {time.time() - start_time}")
    print("=======================================================")


compare_for_and_distinct("Title")
compare_for_and_distinct("Date")
```

- 매우 당연하게도, for + set로 돌리는 경우가 훨씬 오래 걸립니다. 당연하죠. 사실 이것보다 느리면 상품으로 내면 안되는거란 말이죠

```plaintext
== Case 1 start
=======================================================
== Case 1: Distinct
173324
Duration: 0.6859488487243652
-------------------------------------------------------
== Case 2: Find and For
173324
Duration: 0.9843268394470215
=======================================================
=======================================================
== Case 1: Distinct
2435
Duration: 0.01310420036315918
-------------------------------------------------------
== Case 2: Find and For
2435
Duration: 0.897752046585083
=======================================================
```

## Wrap-up

- 그냥 `.distinct`만 땅 하고 끝내면 되는데, 저란 인간 또 덕지덕지 쓸데없는걸 붙여버렸습니다 호호.
- 다만, 아쉽게도 여러 key에 대해서 distinct한 값을 찾을 수는 없어요. 이건 groupby 를 사용해야 할 것 같아요.

## Reference

- [stackoverflow - how to efficiently perform distinct with multiple keys](https://stackoverflow.com/questions/11973725/how-to-efficiently-perform-distinct-with-multiple-keys)
