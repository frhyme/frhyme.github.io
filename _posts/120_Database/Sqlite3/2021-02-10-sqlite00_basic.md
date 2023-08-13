---
title: DB - SQLite - Basic
category: database
tags: database sql sqlite
---

## DB - SQLite - Basic

- 보통 DB들은 설치하고, 다양한 값들을 설정해주고 하는 번거로운 일들이 있지만, SQLite의 경우는 그런 것 없이 그냥 다운 받으면 끝납니다. SQlite는 1개의 파일 내에 DB와 metadat까지 모두 포함되어 있습니다. 따라서, 그냥 그 파일을 그대로 복사해서 다른 컴퓨터로 가져가면 DB 자체가 그대로 복사되어서 넘어오게 되는 것이죠. 즉 '파일 기반의 DB'라고 이해하시면 됩니다.

## Example

- 간단하게 `students.db` 테이블을 만들고 query를 날려 봤습니다.

```sqlite
$ sqlite3 students.db
SQLite version 3.31.1 2020-01-27 19:55:54
Enter ".help" for usage hints.
sqlite> create table student(id text, name text);
sqlite> insert into student(id, name) values ("1", "LSH");
sqlite> select * from student;
1|LSH
sqlite> save;
```
