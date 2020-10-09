


## joblib



- joblib을 사용해서 python의 간단한 프로그램을 병렬로 프로그래밍해보자.
- 크게 두 가지 라이브러리가 있는데, 하나는 `multiprocessing`, 다른 하나는 `joblib`. 다만, joblib은 `multiprocessing`를 이용하는 다른 레벨의 helper class라고 보는 것이 맞음.
  - 다만, 동시성이랑 병렬성은 다르다. 동시성은 multiple, 병렬성은 parallel
  - 그리고, 동시성의 경우는 메모리를 이용하는 것 같기도 하고, 병렬성은 cpu 코어를 사용한ㄴ 것 같기도 하고....아 아니지. 결국 메모리에서 바로 계산할 수는 없으니까, cpu로 넘어갔다 오기는 해야함.