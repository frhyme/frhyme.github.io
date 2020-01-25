---
title: Universlly Unique IDentifier(범용 고유 식별자)
category: others
tags: uuid network 
---

## UUID 

- UUID라는 것이 있습니다. 저는 블록체인을 간단하게 만들어 보다가, UUID가 나오는데 몰라서 일단 정리해봤습니다. 
- [위키피디아에 의하면 정의는 대략 다음과 같습니다](https://en.wikipedia.org/wiki/Universally_unique_identifier). 

> A universally unique identifier (UUID) is a 128-bit number used to identify information in computer systems. The term globally unique identifier (GUID) is also used.

- 컴퓨터 시스템에서 정보를 식별하기 위한, 128 bit의 숫자라는 것이죠. 

> UUIDs are standardized by the Open Software Foundation (OSF) as part of the Distributed Computing Environment (DCE).

- Open Software Foundation(OSF)에서 분산컴퓨팅환경을 위한 표준으로 등록을 했습니다.

> When generated according to the standard methods, UUIDs are for practical purposes unique, without depending for their uniqueness on a central registration authority or coordination between the parties generating them, unlike most other numbering schemes. While the probability that a UUID will be duplicated is not zero, it is close enough to zero to be negligible.

- UUID를 만드는 표준적인 방법에 따라서 생성을 하면 되는데 사실 UUID의 경우 다름 numbering scheme(IP address 등)처럼 중앙에서 관리해주지 않습니다. 즉, 중복으로 발생할 수도 있다는 이야기죠. 다만, 중복이 될 확률이 거의 0에 가깝기 때문에, 무시해도 된다라고 말하고 있습니다. 

## UUID in python

- 뭐 대충 됐습니다. 그냥 식별자라는 것 같은데, 아마도 IoT환경등에서 유용하게 쓰이겠죠 뭐 하하핫. 
- 저는 UUID를 python에서 어떻게 생성하고 사용하는지를 알아보려고 합니다. 
- 자세한 내용은 [UUID in python](https://docs.python.org/3/library/uuid.html)에서 보실 수 있습니다. 


```python
import uuid
## make a random UUID
print(uuid.uuid4())
```

```
633db812-2df2-438d-b126-7da2eec680c4
```