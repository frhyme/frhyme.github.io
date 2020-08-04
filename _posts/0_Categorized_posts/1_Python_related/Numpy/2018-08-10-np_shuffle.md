---
title: list 섞기. 
category: python-lib
tags: python python-lib list shuffle random numpy 
---

## 리스트 내부 값을 섞읍시다. 

- 간단하게 말 그대로, 리스트의 값들을 죽 섞는 것을 말합니다. 가끔 이런게 필요하죠. 
- `np.random.shuffle`를 이용하면 되긴 하는데, 아쉬운 것이, 값을 리턴해주는 형식이 아닙니다. 
- 즉, 전달받은 array를 셔플해서 원래 메모리에 그대로 저장해주는 방식이죠. 
- 만약 원래 어레이는 그대로 두고 복사해서 리턴하려면 새로운 변수에 어레이를 복사해서 넣고 하는 조금 귀찮은 일이 발생합니다. 

```python
## 리스트 섞기 
a = [1,2,3,4]
print(np.random.shuffle(a)) ## None을 리턴함 
print(a)
print("="*20)
```

```
None
[3, 2, 4, 1]
====================
```

## np.random.choice

- 조금 트리키한 방법인 것 같기는 한데 `np.random.choice`를 이용해서 처리합니다. 
- 즉, 어레이의 크기가 10개짜리라면 랜덤하게 10개를 뽑으면 되는거죠. 
- 단 결과값이 `list`가 아니라, `np.array`로 변경됩니다. 

```python
a = [1,2,3,4]
b = np.random.choice(a, 4, replace=False)
print(a, type(a))
print(b, type(b))
```

```
None
[3, 4, 1, 2]
====================
[1, 2, 3, 4] <class 'list'>
[4 2 3 1] <class 'numpy.ndarray'>
```