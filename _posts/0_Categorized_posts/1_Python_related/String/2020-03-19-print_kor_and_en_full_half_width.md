---
title: python에서 한글과 영어를 줄 맞춰서 예쁘게 출력하자.
category: python-libs
tags: python python-basic unicode python-libs
---

## python에서 한글과 영어를 함께 출력할 때, 줄이 안 맞습니다 

- 간단한 코드를 보여드리겠습니다. 종종, 한글과 영어가 혼재되어 있는 결과들을 칼럼별로 다음처럼 출력할 때가 있죠. 

```python
simple_dict = {
    '이승훈frhyme이승훈': 10,
    'abc': 20,
    'abcdefg': 20
}
for k, v in simple_dict.items():
# k를 왼쪽 정렬하여, 최대 20칸 만큼 출력하며, 빈칸은 _ 로 채운다. 는 의미. 
    print(f"{k:_<30s}, {v:5d}")

```

- 하지만, 결과를 보면 마음같지 않습니다. 분명히, `{k:_<30s}`를 사용하였으니, 딱 맞게 출력되어야 하는데 칼럼이 어긋나 있죠. 
- 이는, 한글과 영어를 저장하는 방식이 서로 다르기 때문이죠.

```plaintext
이승훈frhyme이승훈__________________,    10
abc___________________________,    20
abcdefg_______________________,    20
```

## full, half-width 

- 간단하게 말하면, 한글로 된 문자열의 경우 가령 `"이승훈"`이 있다면 길이는 3이지만, 출력될 때는 6칸이 출력됩니다. 이를 full-width character라고 합니다. 
- 영어로 된 문자열의 경우 가령 `"abc"`는 길이는 3이며, 출력될 때도 3입니다. 

- `이승훈`과 `abc`는 동일하게 같은 length를 가지고 있지만, 출력되어 질 때는 한글의 경우가 더 많은 공간이 필요하게 되고, 따라서, 밀려서 표현된다는 것이죠.
- 아래 코드를 보면, `a`와 `b`의 길이는 같지만, 출력은 다르게 됩니다. "5칸을 출력하라고 했고 공백은 *으로 채워라"라는 명령을 내렸고 정확히 명령을 수행했지만, "이승훈"은 6칸이 되고, "abc"는 3칸이므로 문제가 발생하죠(다만, jekyll의 마크다운에서는 한글을 1.5칸, 영어를 1칸으로 이해하는 것 같네요. )

```python
a = '이승훈'
b = 'abc'
assert len(a)==len(b)
print(f"{a:*<5s}")
print(f"{b:*<5s}")
```

```plaintext
이승훈**
abc**
```

## solution: unicodedata.east_asian_width

- `print(f"{a:*<5s}")`를 사용해서 바꿀 수는 없고, full-width char과 half-width char를 체크해서 해당 문자열의 출력 길이를 정확하게 재고, 남은 빈칸을 채워주는 식으로 처리합니다. 
- 해당작업은 `unicodedata.east_asian_width()`를 사용하여, 이 함수에 문자를 넘겨주면 해당 문자가 어느 정도의 간격을 차지하는지 출력해줍니다. 실행 결과는 다음으로 분류 됩니다.
  - A: Ambiguous
  - F: Fullwidth
  - H: Halfwidth
  - N: Neutral
  - Na: Narrow
  - W: Wide
- 이렇게 문자열을 변환해서 출력해주면 한글의 경우도, 영어의 경우도 줄을 맞춰서 깔끔하게 나옵니다.

```python
import unicodedata

def fill_str_with_space(input_s="", max_size=40, fill_char="*"):
    """
    - 길이가 긴 문자는 2칸으로 체크하고, 짧으면 1칸으로 체크함. 
    - 최대 길이(max_size)는 40이며, input_s의 실제 길이가 이보다 짧으면 
    남은 문자를 fill_char로 채운다.
    """
    l = 0 
    for c in input_s:
        if unicodedata.east_asian_width(c) in ['F', 'W']:
            l+=2
        else: 
            l+=1
    return input_s+fill_char*(max_size-l)


a = "abc"
b = "이승훈"

print(fill_str_with_space("abc", max_size=40))
print(fill_str_with_space("이승훈", max_size=40))
```

- 아래 결과가 블로그에서는 예쁘게 나올 수 있습니다. 블로그에서 표시해줄 때는 한글 하나의 길이를 1.5로 잡는 것 같아요. 그래서, 그 결과가 다르게 표현되는 것 같습니다.

```plaintext
abc*************************************
이승훈**********************************
```
