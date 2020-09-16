---
title: tqdm이라는 라이브러리를 사용해보자. 
category: python-libs
tags: python tqdm python-libs python-basic
---

## tqdm?

- [tqdm](https://pypi.org/project/tqdm/)은, 뭐 사실 꼭 필요한 건 아닌데, 현재 for 문이 얼마나 실행되었는지를 알려주는 라이브러리입니다. 
- 사실, 자세하게 설명할 필요는 없으니, 그냥 바로 소개할게요 

## DO IT

- 아래처럼 loop가 돌아갈때, 지금 얼마나 돌아가고 있는지 보여지면 좋을 때 씁니다. 보통 다음처럼 이렇게 쓰잖아요. 

```python
N = 100000
for i in range(0, N):
    if N%100==0:
        print(N)
    continue
```

- 그런데, 은근히 몇 줄 있는게 존나 성가시니까요. 아래처럼 간단하게 바꿀 수 있습니다. 아래를 실행하면, 실행하면서, 현재 어느정도나 실행되었는지를 %로 볼 수 있습니다.

```python
from tqdm import tqdm 

N = 100000
for i in tqdm(range(0, N)):
    continue
```

- 아래 처럼 보여지죠. 

```plaintext
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 9000000/9000000 [00:04<00:00, 2069913.89it/s]
```

- `conda install tqdm`으로 설치하면 됩니다. 어렵지 않죠.

## wrap-up

- 사소하지만 큰 실수인데, 저는 해당 내용을 테스트해보려고 만든 python 파일명이 `tqdm.py`이었습니다. 
- `from tqdm import tqdm`을 실행했는데 계속 안되던데, 그 이유가 생각해보니 파일명이 tqdm이라서 뭔가 문제가 발생하는 것 같더군요.
