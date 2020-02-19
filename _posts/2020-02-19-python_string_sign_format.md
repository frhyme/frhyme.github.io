---
title: python 숫자 출력시에, 부호(sign) 출력하는 옵션. 
category: python-basic
tags: python python-basic string string-format
---

## 3-line summary 

- `+`: +, - 모두 표시함. 
- `-`: -만 표시함. 
- ` `: -만 표시하고, +경우에는 그냥 공백. 

## 부호때문에 칸이 달라지는 것이 꼴보기 싫습니다. 

- 가령, 우리가, 음수와 양수가 섞여 있고 서로 다른 자릿수가 섞여 있는 리스트들을 출력한다고 합시다. 대략 다음과 같은 코드가 되겠죠. 

```python
nums = [-10, 100, 42]
for a in nums:
    print(a)
```

```
-10
100
42
```

- 결과를 보면, 자리수가 엉망이네요. 따라서, format으로 자릿수를 설정(`4d`), 빈칸을 0으로 채워주는 식으로 출력합니다(zero-padding). 

```python
nums = [-10, 100, 42]
for a in nums:
    print(f"{a:04d}")
```
```
-010
0100
0042
```

- 그런데, 부호가 들어가야 할 자리와 0이 들어가 있는 자리가 혼재되어 있죠. 물론 별거 아닙니다만, 저는 신경쓰이네요. 

## sign format option

- 다음의 3가지로 구분됩니다. 
    - `+`: 양수와 음수에 대해서 항상 +, -를 출력하는 경우.
    - `-`: 음수에 대해서만 출력,
    - ` `: 음수에 대해서 "-" 를 출력, 음수에 대해서는 " "(공백)을 출력함. 
- 따라서, 다음의 코드를 실행하면 되죠. 그러면 제가 원하는대로 예쁘게 나옵니다.


```python
nums = [-10, 100, 42]
for a in nums:
    print(f"{a: 04d}")
```

```
-010
 100
 042
```

## reference

- [python - string](https://docs.python.org/3.4/library/string.html)