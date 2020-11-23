---
title: python - self referencing list
category: data-structure
tags: python python-libs data-struture list shallow_copy python-basic
---

## python - self referencing list

- 이상한 짓을 합니다.
  - 비어 있는 list `lst`를 만들고요.
  - reference variable `ref_lst`가 `lst`를 지칭하도록 합니다.
  - 그리고 `lst` 안에 `ref_lst`를 넣어줍니다.

```python
lst = []  # 비어 있는 lst를 만들고요
ref_lst = lst  # reference variable ref_lst는 lst를 가리키고요
lst.append(ref_lst)  # lst에 ref_lst를 넣어줍니다. 그런데, 사실 ref_lst와 lst는 같죠 
```

- 좀 이상하지 않나 싶지만, 오류 없이 잘 돌아갑니다. 그냥 print해서 안에 있는 값을 보면 다음과 같죠.

```python
print(lst)  # [[...]]
```

- `[[...]]`은 매우 깊은, 끝나지 않는 list를 말합니다.
- 가령, 다음 코드를 보면 무슨 말인지 알 수 있습니다. 그냥 `[[[[[[[[...]]]]]]]]` 처럼 까도 까도 또 값이 있는 거죠.

```python
print(lst[0])  # [[...]]
print(lst[0][0])  # [[...]]
print(lst[0][0][0])  # [[...]]
print(lst[0][0][0][0])  # [[...]]
print(lst[0][0][0][0][0])  # [[...]]
```

- 조금 더 자세히보기 위해서 `id()`를 사용해서 메모리 주소를 확인해보겠습니다. 물론, 엄밀히 따지면 `id()`가 메모리 주소를 말하지는 않습니다만.

```python
print(id(lst) == id(lst[0]))  # True
print(id(lst[0]) == id(lst[0][0][0][0]))  # True
```

## Wrap-up

- 아무튼 뭐 list가 list를 직접 참조하는 식으로도 만들 수 있다, 라는 것이 흥미로운 점이네요 호호.