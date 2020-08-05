---
title: python-lib) python - datetime.time
category: python-lib
tags: python python-lib datetime
---

## datetime.time

- `datetime.time` class는 그저, '시간'만을 표시하는 class입니다. 날짜나 요일등은 전혀 중요하지 않고 그냥 시간만이 중요할 때 쓰는 class죠.
- 다음 코드에서와 같이, time object을 정의하고 사용할 수 있습니다.

```python
import datetime

t1 = datetime.time(hour=3, minute=10, second=24, microsecond=10)
print(t1) # 03:10:24.000010
```

- 또한, `datetime.datetime()` object로부터, `datetime.time()`만을 따로 떼어서 가져오는 것도 가능해요.
- 이는 다시 말해서, `datetime.datetime()`이라는 개체가, `datetime.date()`와 `datetime.time()`이라는 두 클래스의 합으로 구성되어 있다는 이야기이기도 합니다. 물론, 몰라도 됩니다. 보통 그냥 `datetime.datetime()`만을 사용하게 되니까요.

```python
import datetime

now_time = datetime.datetime.now().time()

print(now_time)  # 14:36:54.165709
print(type(now_time))  # <class 'datetime.time'>
```

## supported operation only for comparison

- `datetime.time` class는 단지, 크고 작은 비교 연산 밖에 지원하지 않습니다. 현재 시각에서 일정 시간이 경과된 시간을 찾고 싶다면, 그 값을 연산하여 새로운 `datetime.time()` 객체를 만들어줘야 하죠. 

```python
import datetime

time1 = datetime.time(hour=3, minute=10, second=20)
time2 = datetime.time(hour=3, minute=30, second=20)

# TypeError: unsupported operand type(s) for -: 'datetime.time' and 'datetime.time'
print(time1 - time2)
```

## datetime.time formatting

- `datetime.time`을 원하는 형식대로 출력해주기 위해서는 `.strftime()` 메소드를 사용합니다.

```python
format_type1 = "%H:%M:%S"
format_type2 = "%I:%M:%S %p"
print( now_time.strftime(format_type1) )
print( now_time.strftime(format_type2) )
```

```plaintext
22:24:34
10:24:34 PM
```

## wrap-up

- `datetime.time()`을 정리하기는 했지만, 냉정히 말해서 별로 쓸 일은 없습니다. 기본적인 연산을 지원하지 않기 때문이죠.
