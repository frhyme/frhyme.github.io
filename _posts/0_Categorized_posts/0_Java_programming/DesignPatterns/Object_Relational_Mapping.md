---
title: Object Relational Mapping(ORM)
category: database
tags: object DataBase ORM DB tuple
---

## Object Relational Mapping

- RDB와 프로그래밍 언어들을 데이터를 읽고 쓰는 방법이 다릅니다. 따라서, 이 둘간의 데이터 교환을 효과적으로 하기 위한 방법이 바로 Object Relaional Mapping(ORM)이죠. 즉, DB에서의 SQL 접근과, 프로그래밍에서의 객체지향적인 방법간의 상호 접근을 편하게 하기 위한 방법이죠.
- 즉, 데이터베이스에 있는 객체 정보들을 가져와서, 프로그래밍에서 객체로 변환해주고, 프로그래밍에서 객체를 데이터베이스에 넣어주는 것을 ORM이라고 하며, 대부분의 프로그래밍 언어들은 이미 ORM library를 가지고 있죠.
- 일반적으로 Relational DB에서는 Table의 각 Row에 값을 저장합니다. 이 Row는 tuple을 의미하는데, 이미 대부분의 프로그래밍 언어에서는 tuple이 존재하죠. OOP에서의 Object를 Table의 Row에 tuple로 넣어 줍니다. 그런데 보통 Database에서는 테이블 간에 관계가 존재하죠. 가령 "학생"이라는 테이블이 있고, "학생들의 성적"이라는 테이블이 있다고 가정합시다. 이 때, 학생의 특정 row가 사라지면 학생 테이블을 참조하는 학생들의 성적의 Row들은 삭제되어야 겠죠. "삭제된 학생이 학생 테이블에는 없고, 학생 성적테이블에만 존재"하면 얼마나 무서운가 말이죠. 따라서 ORM Library들은 객체에서 생긴 변화가 DB 상에서 연속적으로 반영되도록 설계되어야 합니다. 사실 cascade deletion등이 가능하도록 해라, 라는 말이죠.

## ORM을 사용할 때의 장점

- 우선, Object에서 정의된 method들에 따라서 DB에 반영된다는 점, 굳이 SQL을 사용하지 않아도 된다는 점, 데이터베이스 단에서의 동작과 코드에서의 동작을 독립화할 수 있다는 것 정도가 장점이죠.
- 그러나, 쿼리를 직접 작성하는 것이 아니기 때문에, 상황에 따라서 비효율적인 쿼리가 발생할 수 있다는 점, 데이터베이스 에 직접 연결해서 사용하는 것이 아니기 때문에, 해당 데이터베이스의 장점을 모두 이용할 수 있는 것이 아니라는 것 정도의 단점이 있죠.
- ORM library는 python에서는 SQLAlchemy이 있고, Java에는 Hibernate, JPA 그리고 Javascript에는 TypeORM이 있습니다.
