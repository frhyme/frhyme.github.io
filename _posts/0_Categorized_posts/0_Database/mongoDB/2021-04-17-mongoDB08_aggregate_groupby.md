---
title: mongoDB - aggregation
category: mongoDB
tags: mongoDB python pymongo database db sql nosql python 
---

## mongoDB - aggregation

- mongoDB의 aggreation을 정리합니다. 의미적으로는 SQL의 group by 라고 생각하셔도 됩니다.
- 저는 python을 사용해서 mongoDB에 접속합니다.

## aggregation - basic 

- `.aggregate()`를 사용하기 위해서는 pipeline이라는 parameter를 넘겨줘야 합니다.
- pipeline은 대략 다음과 같이 구성되죠. parameter 이름이 pipeline인 것에서 볼 수 있듯이, aggregate를 한 번 적용하고 끝내는 것이 아니라, 적용한 결과를 사용해서 연쇄적으로 새로운 메소드들을 적용하거나 할 수 있습니다. sql을 생각해보면 group by 를 한 다음 그 결과에 다시 group by를 적용할 수 있는 것과 동알하다는 이야기죠.
  - pipeline의 type은 `list`이며 dictionary를 원소로 가집니다.
  - `_id`는 어떤 원소들에 대해서 값을 합산해줄 것이냐는 이야기죠. 저는 제 document의 `Category`, `Date`를 함께 활용해서 aggregate해줍니다. 만약 1개만 aggregate해주려면 하나만쓰면 되죠. 그리고 이렇게 document의 key를 참고하는 경우 앞에 `$`를 사용하죠.

```json
pipeline = [
    {
        "$group": {
            "_id": {
                "key_A": "$Category", 
                "key_B": "$Date"
            }, 
            "sum_col_name": {
                "$sum": "$Comments_count"
            }
        }
    }
]
```

- 다음과 같이 간단한 코드를 실행한 결과를 보는 것이 더 이해하기 쉬울 수 있습니다.

```python
import pymongo

# pymongo를 사용하여 mongoDB, Collection을 가져옵니다.
# 저는 DB가 Local에 설치되어 있기 때문에 아래처럼 localhost에서 가져왔습니다.
client = pymongo.MongoClient('localhost', 27017)

database_name = ""
collection_name = ""

target_DB = client.get_database(database_name)
target_collection = target_DB.get_collection(collection_name)

pipeline = [
    {
        "$group": {
            "_id": {
                "key_A": "$Category", 
                "key_B": "$Date"
            }, 
            "sum_col_name": {
                "$sum": "$Comments_count"
            }
        }
    }
]

cursor = target_collection.aggregate(
    pipeline=pipeline
)

for i, each_doc in enumerate(cursor):
    if i == 5:
        break
    print(each_doc)
```

- 아래 결과를 보시면, "key_A", "key_B"에 대해서 aggregation이 실행되었고, `Comments_count`라는 key값에 대해서 `sum`을 실행하여 그 결과를 다음처럼 보여주었습니다.

```json
{'_id': {'key_A': '리뷰', 'key_B': '2016.08.03'}, 'sum_col_name': 58}
{'_id': {'key_A': '일반', 'key_B': '2021.02.02'}, 'sum_col_name': 1082}
{'_id': {'key_A': '일반', 'key_B': '2020.05.12'}, 'sum_col_name': 530}
```

## aggregation - sum, avg, count, min, max

- sum외에도, avg, min, max 등을 사용할 수도 있습니다.
- 그러나, 어떤 이유인지 몰라도 count는 없어요. 얘는 그래서 sum을 이용해 줘야 합니다.

```python
import pymongo

# pymongo를 사용하여 mongoDB, Collection을 가져옵니다.
# 저는 DB가 Local에 설치되어 있기 때문에 아래처럼 localhost에서 가져왔습니다.
client = pymongo.MongoClient('localhost', 27017)

database_name = ""
collection_name = ""

target_DB = client.get_database(database_name)
target_collection = target_DB.get_collection(collection_name)


pipeline = [
    {
        "$group": {
            "_id": {
                "ColumnA": "$Category", 
                "ColumnB": "$Date"
            }, 
            "count": {
                "$sum": 1
            },
            "total_sum": {
                "$sum": "$Comments_count"
            }, 
            "mean": {
                "$avg": "$Comments_count"
            }, 
            "min": {
                "$min": "$Comments_count"
            },
            "max": {
                "$max": "$Comments_count"
            }
        }
    }
]

cursor = target_collection.aggregate(
    pipeline=pipeline
)

for i, each_doc in enumerate(cursor):
    print(each_doc)
    if i == 3:
        break
```

- 결과는 다음과 같습니다.

```json
{'_id': {'ColumnA': '리뷰', 'ColumnB': '2021.03.17'}, 'count': 1, 'total_sum': 11, 'mean': 11.0, 'min': 11, 'max': 11}
{'_id': {'ColumnA': '일반', 'ColumnB': '2018.05.23'}, 'count': 13, 'total_sum': 146, 'mean': 11.23076923076923, 'min': 1, 'max': 67}
{'_id': {'ColumnA': '음악', 'ColumnB': '2018.04.06'}, 'count': 43, 'total_sum': 226, 'mean': 5.255813953488372, 'min': 0, 'max': 55}
{'_id': {'ColumnA': '일반', 'ColumnB': '2019.08.05'}, 'count': 36, 'total_sum': 392, 'mean': 10.88888888888889, 'min': 0, 'max': 41}
```

## aggregate chaining

- parameter가 pipeline인 것에서 알 수 있듯이 aggregate를 연쇄적으로 적용할 수 있습니다.
- pipelin은 다음과 같이 구성됩니다. 
  - 첫번째 dictionary에서는 "Cateogry", "Date"를 사용해서 aggregate하죠.
  - 첫번째 dictionary가 적용된 결과 document들에 대해서 두번째 dictionary를 적용합니다.

```json
pipeline = [
    {
        "$group": {
            "_id": {
                "key_A": "$Category", 
                "key_B": "$Date", 

            }, 
            "count": {
                "$sum": 1
            },
            "total_sum": {
                "$sum": "$Comments_count"
            }
        }
    }, 
    {
        "$group": {
            "_id": {
                "new_key": "$_id.key_A"
            },
            "avg": {
                "$avg": "$total_sum"
            },
        }
    }
]
```

- python 코드로 보면 다음과 같죠.

```python
import pymongo

# pymongo를 사용하여 mongoDB, Collection을 가져옵니다.
# 저는 DB가 Local에 설치되어 있기 때문에 아래처럼 localhost에서 가져왔습니다.
client = pymongo.MongoClient('localhost', 27017)

database_name = ""
collection_name = ""

target_DB = client.get_database(database_name)
target_collection = target_DB.get_collection(collection_name)

#  { $group: { _id: "$cust_id", total: { $sum: "$amount" } } }
pipeline = [
    {
        "$group": {
            "_id": {
                "key_A": "$Category", 
                "key_B": "$Date", 

            }, 
            "count": {
                "$sum": 1
            },
            "total_sum": {
                "$sum": "$Comments_count"
            }
        }
    }, 
    {
        "$group": {
            "_id": {
                "new_key": "$_id.key_A"
            },
            "avg": {
                "$avg": "$total_sum"
            },
        }
    }
]

cursor = target_collection.aggregate(pipeline=pipeline)

for i, each_doc in enumerate(cursor):
    print(each_doc)
    if i == 3:
        break
```

## Wrap-up

- 간단하게, `.aggregate`를 사용해서 document들에 대해서 groupby 하는 방법을 정리하였습니다.

## Reference

- [mongodb - manual - aggregation](https://docs.mongodb.com/manual/aggregation/)
