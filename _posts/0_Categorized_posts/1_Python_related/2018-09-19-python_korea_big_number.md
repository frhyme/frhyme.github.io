---
title: 한국의 큰 수 체계를 알아봅시다. 
category: others
tags: python number big-number zip
---

## intro

- 왠지, 또 이상한 걸 하게 된것 같은데요. 파이썬으로 코딩할때, 수를 출력할 때면, 다음처럼 출력됩니다. 

```plaintext
12345678901234
```

- 이게 너무 길기도 하고, 끊어읽을 수가 없어서 어느 정도로 큰지 가늠하기가 좀 어려웠습니다. 
- 그래서, 수를 입력받고 해당 값을 [한국 수 체계](https://ko.wikipedia.org/wiki/%ED%81%B0_%EC%88%98%EC%9D%98_%EC%9D%B4%EB%A6%84)로 변환해서 출력해주면 좋지 않을까 생각했습니다. 

## 두잇두잇츄우

- 간단하게 다음처럼 코딩했습니다. 

```python
def korea_big_number(n):
    rlst = []
    original_n = n 
    while True:
        if n<(10**8):
            rlst.append(n)
            break
        else:
            rlst.append(n%(10**8))
            n = n//(10**8)
    rlst = zip(rlst, ["", '억', '조', '경', '해', '자', '양', '구', '간', '정', '재', '극', '항하사', '아승기', '나유타', '불가사의', '무량대수'])
    rlst = list(reversed(list(rlst)))
    r = " ".join([str(x)+y for x, y in rlst])
    print(f"{original_n} ==> {r}")
    return r

korea_big_number(1234)
korea_big_number(123456789)
korea_big_number(123456789123456789)
```

```plaintext
1234 ==> 1234
123456789 ==> 1억 23456789
123456789123456789 ==> 12조 34567891억 23456789
Out[448]:
'12조 34567891억 23456789'
```

## wrap-up

- [어려운 코딩이 아니므로, 영어로도 해줄 수 있는데](https://namu.wiki/w/%EC%98%81%EC%96%B4/%EC%88%98%20%EB%8B%A8%EC%9C%84#s-2.6), 귀찮네요 쿠쿠
