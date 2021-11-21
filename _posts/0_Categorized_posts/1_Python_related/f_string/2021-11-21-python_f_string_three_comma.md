---
title: python - f_string - 숫자 3개마다 comma 넣어서 출력하기. 
category: python
tags: python f_string string number print locale
---

## python - f_string - 숫자 3개마다 comma 넣어서 출력하기

- 일반적으로 숫자를 표기할 때, 3 digit마다 comma를 집어넣습니다.
- 이는 1000을 기본 단위로 하는 미국식 숫자 쓰기 방식인데요. thousand -> million -> billion 으로 되어 있어 3 digit마다 comma를 찍어야 숫자를 읽기가 편하기 떄문이죠.
- 사실 한국이라면 10000을 단위로 comma를 찍어야 일기 편합니다만 호호 이미 저게 나름 표준처럼 자리잡혀 있기에 우리만 마음대로 4자리마다 comma를 찍도록 하기는 어렵죠.

```plaintext
123,456,789
```

- 아무튼, 숫자를 표기할 때, comma가 표기되도록 하려면 다음처럼 해주면 됩니다. 
- `:` 뒤에 comma를 집어너헝주면 되고, 만약 최대 digit 길이를 표시해주는 경우(아래에서는 `9`)에는 그 숫자 뒤에 넣어주면 되죠.

```python
numbers = [
    123, 123456, 123456789
] 

for num in numbers:
    print(
        f"{num} - {num:,} - {num:9,d}"
    )
"""
123 - 123 -       123
123456 - 123,456 -   123,456
123456789 - 123,456,789 - 123,456,789
"""
```

### locale aware - 지역에 따른 변화를 고려하기

- 다만, 위 방법은 지역별 차이를 고려하지 않는다는 문제가 있습니다. 흥미롭게도, 긴 숫자에 대해서 구분자(separator)를 넣어주는 방식은 국가별로 조금씩 다른데요, 자세한 내용은 [oracle - Decimal and Thousands Separators](https://docs.oracle.com/cd/E19455-01/806-0169/overview-9/index.html)에서 읽어보실 수 있습니다.
- 위에서 작성한 코드로는 어떤 경우에도 항상 미국 식의 thousand comma separator를 사용하게 되죠.
- 따라서, 현재의 locale에 따라 알아서 separator를 변경해주려면 다음과 같이 처리하면 됩니다.
- `'n'`은 기본적으로 `'d'`와 동일합니다. 다만, `'n'`은 현재 OS 위치한 곳의 locale에 따라 출력방식이 달라지도록 설계되어 있습니다.
- 현재 환경에서 사용 가능한 locale 목록을 확인해보려면, terminal에서 `locale -a`를 사용하면 됩니다.

```python
import locale

# local.LC_ALL 은 현재 프로그램 전체의 local을 어떻게 설정할지를 의미합니다. 

number = 123456

print(f"{number:n}")

# '': 현재 OS의 위치를 인식해서 locale을 처리해줍니다.
locale.setlocale(locale.LC_ALL, '')
print(locale.getlocale(), f" - {number:n}")
# output: 123,456,789

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
print(locale.getlocale(), f" - {number:n}")

locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')
print(locale.getlocale(), f" - {number:n}")

locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')
print(locale.getlocale(), f" - {number:n}")

locale.setlocale(locale.LC_ALL, 'en_CA.UTF-8')
print(locale.getlocale(), f" - {number:n}")

locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
print(locale.getlocale(), f" - {number:n}")

# Hindi 문화권의 경우 맨 뒤에는 2 digit 에 대해 comma를 넣고
# 그 다음에는 3 digit으로 comma를 넣습니다.

locale.setlocale(locale.LC_ALL, 'hi_IN.ISCII-DEV')
print(locale.getlocale(), f" - {number:n}")
```

- 위 코드의 수행 결과는 다음과 같습니다.

```python
123456
('ko_KR', 'UTF-8')  - 123,456
('en_US', 'UTF-8')  - 123,456
('de_DE', 'UTF-8')  - 123456
('it_IT', 'UTF-8')  - 123456
('en_CA', 'UTF-8')  - 123,456
('es_ES', 'UTF-8')  - 123456
('hi_IN', 'ISCII-DEV')  - 1,234,56
```

## reference

- [stackoverflow - how to print number with commas as thousands separators](https://stackoverflow.com/questions/1823058/how-to-print-number-with-commas-as-thousands-separators)
- [oracle - Decimal and Thousands Separators](https://docs.oracle.com/cd/E19455-01/806-0169/overview-9/index.html)
