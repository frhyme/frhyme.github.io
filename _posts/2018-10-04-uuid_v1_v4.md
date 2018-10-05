---
title: uuidv1 vs. uuidv4
category: others
tags: uuid python
---

## intro

- recursive하게 그래프를 만드는 코딩을 하고 있습니다. 
- 처음에는 a -> b -> c -> 로 시작하는데, 각 노드가 확장이 가능할 경우, 해당 노드는 확장됩니다. 
- 이 과정에서, 각 node에 이름을 붙여야 하는데, recursive하게 풀고 있기 때문에 각 노드의 이름이 중복되면 안되요. 
- 이걸 막기 위해서, uuid를 사용하고 있습니다. 

## uuid in python

- python에서 uuid를 사용하려고 보면, 여러 버전이 있습니다. 
- 설명하는 것보다는 눈으로 보는 게 더 빠른데, `uuidv1` 과 `uuidv4`를 각각 여러번 실행해보겠습니다.

```python
import uuid

print("=="*20)
for i in range(0, 10):
    print(uuid.uuid1())
print("=="*20)
for i in range(0, 10):
    print(uuid.uuid4())
print("=="*20)
```

```
========================================
220f38d0-c796-11e8-9062-9a000138b130
220f3b82-c796-11e8-8ab2-9a000138b130
220f3df8-c796-11e8-bc55-9a000138b130
220f4050-c796-11e8-8e89-9a000138b130
220f42f8-c796-11e8-84eb-9a000138b130
220f453a-c796-11e8-a108-9a000138b130
220f4726-c796-11e8-bfdd-9a000138b130
220f4968-c796-11e8-bfee-9a000138b130
220f4ba4-c796-11e8-b132-9a000138b130
220f4df4-c796-11e8-aaf7-9a000138b130
========================================
79d74721-eae6-4423-8d4b-10dd90f3faa7
aede7b76-f5be-46f0-8a19-b78baf69a1fe
ef27b58a-ba2c-4701-9c0e-c9361b712d96
f56c0d67-3d26-4756-a7c5-2b54668757b5
cb39ba38-9c5d-4c04-9470-976c13459d23
43174ef3-3117-45ce-ab84-2babc71e054d
c94ac892-a639-4151-8e64-c98a9f40a020
d6e9e353-8dd3-4a0c-9ae2-365d68726462
558373eb-b374-48ce-913a-cc5ff80ba8c8
c5d40fa4-c007-48ef-8133-fee4941607fd
========================================
```

- 대략 봐도, 아시겠지만, `uuid1`의 경우는 앞부분이 대부분 비슷합니다. 
- 즉, 순차적으로 값이 커지면서 랜덤니스를 확보한다고 볼 수 있겠죠.
    - 이때의 강점이라면, uniqueness가 확보된다는 것이고
- `uuid4`의 경우는 완전히 서로 다른 값이 나옵니다. 
    - 이 때의 강점이라면, randomness가 확보된다는 것이겠죠. 


## wrap-up

- [더 자세한 이야기는 여기에서](https://www.sohamkamani.com/blog/2016/10/05/uuid1-vs-uuid4/) 보시는 것이 더 좋습니다. 

## reference

- <https://www.sohamkamani.com/blog/2016/10/05/uuid1-vs-uuid4/>