---
title: mongoDB - dump to pickle by python
category: mongoDB
tags: mongoDB python pymongo database db sql nosql python pickle
---

## mongoDB - dump to pickle by python

- 얼마 전에 mongoDB tools의 `mongodump`를 사용하여 백업하는 방법을 정리했습니다. 그런데, 이 `mongodump`를 사용한 백업이 결국 그냥 모든 document를 읽어서 json과 같은 파일로 저장해주는 것처럼 보이더라고요. 
- 이럴 거면 그냥 내가 직접 mongoDB에 접근해서 pickle등으로 저장해주면 된는 것 아닌가 싶어서, 이를 직접 코드로 만들어 봤습니다.

```python
import pickle
import pymongo
import datetime


def make_collection_backup(client, target_DB_name, collection_name):
    """
    clinet에서 target_DB_name에 접속하여, collection_name에 접속하고
    해당 collection에 있는 모든 document를 저장한다.
    mongoDB에는 _id 칼럼도 함께 저장되는데, 백업할때는 이 _id 칼럼은 제외한다.
    """
    target_DB = client.get_database(target_DB_name)
    target_collection = target_DB.get_collection(collection_name)

    print(f"== BACKUP for - DB: {target_DB_name}, collection: {collection_name}")
    print(f"==== backup start at {datetime.datetime.now()}")

    backup_dict_list = []
    for i, each_doc in enumerate(target_collection.find()):
        # 백업할 때는 각 document의 _id key를 지우고 가져옴.
        try:
            del each_doc['_id']
        except KeyError:
            print("key '_id' doesn't exist")
        backup_dict_list.append(each_doc)
    this_time = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    backup_pickle_file_name = collection_name + "_BU_at_" + this_time

    with open("backup_files/" + backup_pickle_file_name, "wb") as f:
        pickle.dump(backup_dict_list, f)
    print(f"==== backup end   at {datetime.datetime.now()}")


if __name__ == "__main__":
    # get mongoDB
    target_DB_name = ""
    client = pymongo.MongoClient('localhost', 27017)
    make_collection_backup(client, target_DB_name, collection1_name)
    make_collection_backup(client, target_DB_name, collection2_name)
```
