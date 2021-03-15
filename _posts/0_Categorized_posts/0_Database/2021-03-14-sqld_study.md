---
title: 
category: 
tags: 
---

## SQL D study

- SQL D를 공부하고 있습니다. 공부하면서 배운 것들을 짧게 정리합니다.

## Lesson Learned

- DDL(alter) 문은 암시적으로 commit을 수행합니다. 따라서, insert -> insert -> alter 가 수행되었다면 사실 insert -> insert -> alter -> (commit)가 동일한 의미라는 것이죠. 이전에 수행된 것 까지 모두 수행됩니다.
- Number 타입의 경우 이미 row가 입력되어 있는 경우에는 Alter 문을 사용해서 데이터 타입의 크기를 축소할 수 없습니다. 데이터 타입의 크기를 변경하여 기존의 데이터의 퀄리티가 문제가 될 수도 있으니까요.
- Drop 을 사용하여 테이블 T1을 삭제하려고 할때, 만약 테이블 T2가 T1의 PK를 FK로서 사용하고 있다면, T1을 삭제할 수 없습니다. 그래도 삭제하려면, `CASCADE CONSTRAINTS`를 사용하면 되기는 하죠.
- PK는 null을 허용하지 않지만, Unique Constraint의 경우는 null을 허용합니다. 따라서, PK로 설정된 column에는 Null 값이 들어올 수 없지만, unique constraint로 설정된 column에는 Null값이 들어올 수 있습니다. 그리고, 이미 null이 이미 들어와 있더라도 또 null이 들어오는 것도 문제가 없죠.
- CHAR(4)의 경우는 4칸보다 작은 크기의 스트링이 들어오면 빈칸을 채워서 4칸으로 만들고, VARCHAR(4)의 경우는 1칸이 들어오면 1칸을 그대로 저장합니다.
- DELETE는 DML 문이고, TRUNCATE는 DDL문입니다. `DELETE Table`을 하면, 아직 commit이 되지 않았으므로 rollback이 가능한데, `TRUNCATE Table`은 commit이 되었기 때문에 Rollback이 불가능하죠.
