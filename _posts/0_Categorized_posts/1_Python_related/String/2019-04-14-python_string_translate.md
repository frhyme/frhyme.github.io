---
title: string) transalte vs. replace
category: python-basic
tags: python string python-libs python-basic
---

## why use translate?

- 우선, 저는 python의 string method 중에 translate라는 것을 써본 적이 없습니다.
- 이름에서 알 수 있는 것처럼 해당 메소드는 스트링을 다른 스트링으로 변환시켜주는 기능을 수행합니다. 
- 그러나, 그런건 그냥 간단한 변환 딕셔너리를 만들고 읽으면서 `replace`를 사용해서 처리해주는 것이 더빠르지 않을까요? 

## do it

- 이해를 돕기 위해서 간단하게 만들어 봤습니다. 

```python
import time 

a = "abcdcdcdaaaa"*20000000

# timeit: 시간을 제기 위한 magic command 
# string의 method인 maketrans라는 것을 만들고 길이가 같은 두 스트링을 넘겨줌.
# 즉, a==> c, b==>d 로 매핑되어 변환됨. 
%timeit a.translate("".maketrans("ab", "cd"))

# 여기서는 각각 key => value의 형태로 만들어서 처리해줌. 
trans_dict = {"a":"b", "c":"d"}
def trans_with_dict(input_s):
    for k, v in trans_dict.items():
        input_s = input_s.replace(k, v)
    return input_s
    
%timeit trans_with_dict(a)
```

- 속도 차이는 약 1.5배 정도 납니다. 

```plaintext
1 loop, best of 3: 267 ms per loop
1 loop, best of 3: 513 ms per loop
```

## wrap-up

- 그냥 참고삼아 작성했습니다만. 저는 이정도 속도차이라면 굳이 사용할 필요가 없다고 생각합니다. 
- 가독성도 떨어지고, 세부적인 조작도 어려운데 이런 펑션이 꼭 파이썬에 있어야 하나 싶기도 하구요. 
