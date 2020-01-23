---
title: Proof of Work(PoW, 작업증명) 알고리즘을 알아보자.
category: others
tags: blockchain pow algorithm hash hashlib
---

## intro 

- 이번 주는 집에서 휴가를 보내고 있습니다. 어쩌다 이런 인간이 되어버렸는지는 잘 모르겠지만, 저는 휴가에도 제가 평소에 관심이 있던 공부를 합니다. 아주 좋은 습관이라고 생각하고 있기는 한데 또 어쩌다 이런 인간이 되어버렸는지, 약간 양가적인 마음이에요. 
- 아무튼, 그래서 블록체인을 좀 보고 있습니다. 제가 원래 데이터베이스를 연구하던 연구실에 있었는데, 저에게 블록체인은 분산DB의 일종이라고 해석이 되거든요. 막연하게, 그리고 대략적으로는 알고 있지만 정확히 모르는 것 같아서 이번에 좀 공부해보려고 합니다. 
- 그 과정에서 일단은 작업증명 알고리즘(Proof of Work)을 먼저 정리해야 할 것 같아요. 

## 작업 증명 알고리즘 

- 우선 **작업증명 알고리즘**이 왜 필요할까요? 블록체인은 말 그대로 블록들이 연결되어 있는 네트워크 구조를 말합니다. 블록이란 어떤 데이터 단위(혹은 transaction 묶음)를 말하죠. 하나의 블록이 완성되고, 해당 블록이 commit이 된 다음에야 다른 블록이 해당 네트워크(블록체인)에 커밋될 수 있습니다. 만약 스팸메일처럼 여러 개의 블록들이 동시에 마구 생성된다면, 해당 블록체인은 일종의 무결성 확보에 어려움을 겪게 됩니다. 
- 이를 막기 위해서 작업 증명 알고리즘이 필요합니다. 

### capcha

- 작업증명 알고리즘을 간단하게 표현하면, 대략 capcha와 유사하다고 할 수 있습니다. 어떤 특정한 문제를 풀어야 회원가입을 하거나 글을 쓸 수 있는 capcha처럼, CPU를 사용해서 일정 이상의 연산 시간이 필요한 문제를 풀어야, "아 이 사람은 스팸이 아니다"라는 것이 증명되는 것이죠. 

![capcaha](https://d585tldpucybw.cloudfront.net/sfimages/default-source/productsimages/asp.net-ajax/productitemfeatures/captcha_various-protection-modes-_screenshot-gif.png?sfvrsn=5c04c917_3)

- 도식화하면 대략 다음과 같다고 할 수 있을 것 같아요 

![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Proof_of_Work_challenge_response.svg/825px-Proof_of_Work_challenge_response.svg.png)

### hashcash

- [hashcash](https://en.wikipedia.org/wiki/Hashcash)라는 것이 있습니다. 

> Hashcash is a proof-of-work system used to limit email spam and denial-of-service attacks, and more recently has become known for its use in bitcoin (and other cryptocurrencies) as part of the mining algorithm. Hashcash was proposed in 1997 by Adam Back.

- 나온 지 오래된 기술이긴 한데, 사실 작업증명 알고리즘은 원래 스팸메일을 걸러내고, DDos 공격 같은것을 막기 위해서 많이 사용되었습니다. 지금은 물론 비트코인에서 많이 사용되고 있지만. 
- 아무튼 다양한 작업증명 알고리즘이 있습니다. 그중에서 hashcash를 설명하려고 해요. 

- 해시캐시 알고리즘 
    1. 공개적으로 알려진 데이터(e-mail 등)를 가져오고 
    2. 여기에 카운터를 추가하고(초기에는 0)
    3. data+카운터의 해시 값을 구하고 
    4. 해시가 특정 요구사항을 충족하는지를 파악합니다
        - 충족할 경우 ==> 알고리즘 종료
        - 충족하지 못할 경우 ==> 카운터에 1을 더하고 step3으로 이동 
- 여기서 해당 컴퓨터가 카운터 값을 정확하게 계산했을 경우에는 이메일을 보낸다거나, 서버에서 무엇인가를 할 수 있다거나, 블록을 생성할 수 있다거나 하는 작업이 가능합니다. 

### hashcash in python 

- 이를 파이썬으로 구현해보도록 하겠습니다. 
- 이메일 주소를 데이터로 사용하고, counter를 올려가면서 해시값을 찾습니다. 이 과정에서 종료조건은 해시값의 앞에 0이 몇 개 나오느냐 로 결정되죠. 블록체인에서 이 difficulty는 점점 올라갑니다. 
- 비트코인의 경우 10분 내에 생성해야 하는 블록의 개수를 이 difficulty를 변경하면서 제한합니다. 즉, 이 난이도가 올라가면 점점 더 많은 컴퓨팅 파워를 필요로 하고, 따라서 여기에 많은 기여를 한 컴퓨터(이를 채굴이라고 합니다)에게 비트코인이 주어지죠. 
- 즉 비트코인에서의 채굴이란, "블록의 생성을 어렵게 하고, 네트워크가 무결성있게 유지되도록 기여했다"라고 해석할 수 있겠습니다. 

```python
import hashlib 

input_str = "frhyme@postech.ac.kr"
counter = 0 
difficulty = 1 
for difficulty in range(1, 8):
    while hashlib.sha256(f"{input_str}{counter}".encode()).hexdigest()[:difficulty] != "0"*difficulty:
        counter+=1
    print(f"difficulty: {difficulty}, counter: {counter}")
    print(hashlib.sha256(f"{input_str}{counter}".encode()).hexdigest())
    print("="*20)
```

```
difficulty: 1, counter: 31
0113874c1b00d69a418cd054838f777f03e4bb663875194415e1f78b92285b6e
====================
difficulty: 2, counter: 44
00e303bb0c290571a80c17288bc24f92735e4f2d31e896861668e5c34a5316ad
====================
difficulty: 3, counter: 2847
000a7f13b0e01db317752808b3b2071ce50ee8b498ce743f59a8a43a4b90d557
====================
difficulty: 4, counter: 35380
00005cd778f31d265b9bfbfc60a5498fcc8661e2ab70b8ab0ab7c9d7ed4850ac
====================
difficulty: 5, counter: 604339
00000421b91f9a0fd93650f6a8bf0a3c50fe27c10309986fd48784c6ebbcf6f4
====================
difficulty: 6, counter: 18367275
0000000eec8a2372250b1494668c1d7ee3201787e1bf4d752c3958a212db88c5
====================
difficulty: 7, counter: 18367275
0000000eec8a2372250b1494668c1d7ee3201787e1bf4d752c3958a212db88c5
====================
```

## wrap-up

- 정리하면, 다음과 같아요.
    - "작업증명알고리즘은 스팸메일, 서비스 공격 등을 막기 위해서 일정 이상의 컴퓨팅 파워를 기여하도록 하는 capcha와 유사한 방법"이며, 
    - "작업증명알고리즘은 블록체인에서 새로운 블록이 동시에 생기지 않도록 하기 위해서 사용되고", 
    - "시간이 지나면서 난이도를 올려서 일정 단위 시간 내에 생성되는 블록의 수를 제한한다"
- 따라서, POW를 사용하는 코인들(이더리움, 비트코인)의 경우는 일정 단위 시간 내에 생성하는 블록의 수가 제한되고(보통 10분에 블록이 1 - 2개 생깁니다), 따라서 제가 비트코인을 이용해서 결제를 했다면 이 결제가 완결되려면 블록이 생성되어야 하므로 약 10분 정도 소요되어야 한다고 할 수 있습니다. 사실 이게 좀 문제에요. 커피 하나 사먹으려는데 결제 시간이 10분 정도 걸린다면 이게 진짜 화폐로써의 존재가치가 있는걸까요? 
- 또한 POW이외에 Proof of Stake(POS)라는 것도 있는데, 이는 일종의 주주총회 같은 방식인 것 같아요. 자세한 내용은 [여기](http://www.itworld.co.kr/insight/109209)를 읽어보시는 것이 좋습니다. 저도 아직 이 부분까지는 어렵네요. 





## reference

- <http://www.itworld.co.kr/insight/109209>
- <https://mingrammer.com/building-blockchain-in-go-part-2/>