---
title: PyCharm - Disable typo in Comment
category: python
tags: python PyCharm IDE typo comment
---

## PyCharm - Disable typo in Comment

- [typo](https://en.wikipedia.org/wiki/Typographical_error) "typographical Error"의 약자로 "오탈자"를 말한다고 보시면 됩니다.
- 많은 IDE에서 기본적으로 typo에 대해서 알림고치라고 말해주기는 하는데, Comment에 대해서도 고치라고 말합니다. 


```python
def quack(each_duck: Duck):
    # duck을 전달받아서 .quack method를 실행합니다.
    each_duck.quack()
```

- 가령 위 코드에서 `"duck을"` 부분을 고리차는 거죠. 따라서, 이 걸 수정합니다.

```plaintext
Typo: In word 'duck을' 
```

- **설정(Preference) > Inspection > Proofreading > Typo > Process Comments 해제** 를 하시면 됩니다.
