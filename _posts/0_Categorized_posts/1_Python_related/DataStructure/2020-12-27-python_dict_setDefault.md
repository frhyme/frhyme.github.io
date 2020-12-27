---
title: python - dictionary - setdefault
category: data-structure
tags: python dictionary python-programming python-basic
---

## python - dictionary - setdefault

- python에서 dictionary는 매우 유용한 자료구조이기는 한데, `key`가 dictionary에 존재하지 않는 경우를 고려해야 해서 꽤 귀찮죠.
- 가령, `list`에 있는 원소들의 빈도를 센다고 하면 다음과 같이 코딩해야 합니다. 별것 아닌데 꽤 귀찮죠.

```python
lst = [1, 2, 3, 12, 5, 6, 2]
number_counter = dict()
for k in lst:
    if k not in number_counter.keys():
        number_counter[k] = 1
    else:
        number_counter[k] += 1
print(number_counter)
# {1: 1, 2: 2, 3: 1, 12: 1, 5: 1, 6: 1}
```

- 하지만, `setdefault`를 사용하면 다음처럼 깔끔하게 만들 수 있죠.

```python
lst = [1, 2, 3, 12, 5, 6, 2]
number_counter = dict()
for x in lst:
    # .setdefault는 key가 없으면 자동으로 key, value를 집어넣어줌.
    number_counter.setdefault(x, 0)
    number_counter[x] += 1
print(number_counter)
# {1: 1, 2: 2, 3: 1, 12: 1, 5: 1, 6: 1}
```
