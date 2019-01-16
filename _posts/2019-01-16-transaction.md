---
title: transaction에 대해서 알아봅시다. 
category: others
tags: transaction database oracle
---

## intro

- transaction을 과거 학부 DB시간에 들었지만, 기억이 가물가물해서 정리할겸 포스팅하고 있습니다. 
- 오라클의 online documentation에서 [transaction management](https://docs.oracle.com/cd/B19306_01/server.102/b14220/transact.htm) 부분을 아주 많이 참고하여 작성하였습니다. 

### Definition of Transaction 

- **Transaction**은 commit(해당 명령이 유효하다고 인식하고 database에 영속적으로 집어넣는 것) 혹은 roll-back(해당 명령이 유효하지 않으므로 반쯤 넣었다고 해도 데이터베이스에 적용하지 않는 것)이 될 수 있는 명령들의 집합이라고 할 수 있습니다. 여기서 "명령"이라는 것은 SQL command들의 합, 이라고 할 수 있습니다. 
- 일반적으로는 은행 시스템에서의 transaction을 많이 언급합니다. 
    - 1) 계좌 A에서 10000원을 빼서, 2) 계좌 B로 10000원을 넣고, 3) 계좌 A에서 계좌 B로 10000원이 옮겨졌다는 기록을 남기고, 4) commit or roll-back. 의 순으로 진행이 되죠. 
    - 즉, 여기서 1) 부터 3)까지의 업무는 연속된 업무이며, 개별적으로 수행이 되어서는 안됩니다. 1)만 실행되거나, 2)만 실행되거나 하는 일이 발생하면, 오류가 발생하죠. 

![](https://docs.oracle.com/cd/B19306_01/server.102/b14220/img/cncpt025.gif)

- 간단하게 생각하면, 함께 수행되어야 하는 SQL statement들을 묶어놓은 것을 **transaction**이라고 생각할 수 있습니다. 실행되면, 다 실행되거나, 실행되지 않으면, 다 실행되지 않아야 하는 것들이 transaction을 의미하죠. 


### savepoints in transaction 

- 그런데, 여기에 savepoint라는 개념이 있습니다. 게임을 많이 해보신 분들은 이미 익숙하실텐데, savepoint는 일종의 commit같은 것이죠. 여기까지는 유효하다, 라는 것에 대한 증명이니까요. 
- 여기서는 transaction 내에 savepoint라는 것을 만들 수 있다고 하고 있습니다. 만약 엄청 큰 규모의 transaction을 수행하고 있는데, 끝쯤에 발생한 어떤 오류로 인해서, 전체 transaction을 roll-back해야 하는 경우가 발생할 수 있습니다. 이 때 전체 transaction을 모두 roll-back하면 이는 비효율적이죠. 
- 따라서, 큰 transaction인 경우에(뭐 꼭 클 필요는 없습니다) transaction의 중간중간에 savepoint라는 개념을 집어넣습니다. 만약 이 transaction을 rollback해야 하더라도, savepoint를 지나 왔으면 이 savepoint까지는 유효하다고 한다, 라는 것이죠.

## conclusion

- 매우 기본적인 것들만 정리해두었습니다.


## reference

- <https://docs.oracle.com/cd/B19306_01/server.102/b14220/transact.htm>