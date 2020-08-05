---
title: python-lib) python - datetime.date
category: python-lib
tags: python python-lib datetime
---

## intro - datetime 라이브러리 대한 설명

- `pandas`에서 바로 datetime을 처리하는 것이 더 편할 때도 있지만, 저는 datetime을 쓰는 편이 더 좋아서, 이쪽을 선호합니다.
- 단순히 말하자면, datetime 이라는 object는 날짜만을 관리하는 date object와 시간을 관리하는 time object를 합친 것을 말합니다. 이름 그대로죠. 
- 그리고, datetime object A에서 datetime object B를 빼면, timedelta라는 시간의 변화량을 담은 객체가 나타납니다.
- 최근에 코딩하면서, 날짜, 시간을 다루는 데 불편함이 생겨서, python에서 날짜/시간을 다루는 모듈들을 정리해봤습니다.
- datetime 라이브러리에는 아래와 같은 총 다섯 가지의 클래스들이 존재합니다.
  - **date**: 날짜에 대한 class, attribute: year, month, day
  - **time**: 시간에 대한 class, attribute: hour, minute, second 등
  - **datetime**: date와 time의 조합 class
  - **timedelta**: 두 date, time, datetime instance 간의 차이를 표현, days, seconds 속성을 가짐
  - **tzinfo**: time zone class, datetime class 내의 속성으로 존재(여기서는 따로 설명하지 않음)

## datetime.date

- `datetime.date`는 말 그대로, '날짜'만을 담은 class입니다. 시간은 중요하지 않고 날짜만이 중요할 때 이 class를 사용하면 됩니다.

```python
import datetime as dt

today_date = dt.date.today()

print(today_date, type(today_date)) # 2017-03-05 <class 'datetime.date'>
print(today_date.min, dt.date.min)  # 0001-01-01 0001-01-01
print(today_date.max, dt.date.max)  # 9999-12-31 9999-12-31
print(today_date.resolution)        # 1 day, 0:00:00
print(today_date.year, today_date.month, today_date.day) # 2017 3 5
```

### datetime.date.weekday

- `datetime.date` class는 "요일을 확인할 수 있는 내부 method", `.weekday()`를 가지고 있습니다.
- 0부터 월요일, ..., 6은 일요일로 정리되어 있습니다.

```python
days  = [ dt.date(2017, 3, 6+i).weekday() for i in range(0,7) ]

week_num_to_str_dict = {0:"mon", 1:"tue", 2:"wed", 3:"thu", 4:"fri", 5:"sat", 6:"sun"}
week_days = [ week_num_to_str_dict[week_num] for week_num in days]

print( days ) # [0, 1, 2, 3, 4, 5, 6]
print( week_days ) # ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
```

### datetime.date.strftime()

- 또한, 현재의 시간을 원하는 format의 string으로 변환하여 출력하는 것도 가능합니다. 이를 위해서는 다음과 같이, `.strftime` 메소드를 사용하면 됩니다.

```python
format_type1 = "%y/%m/%d"
format_type2 = "%y-%m-%d"
print( today_date.strftime(format_type1) ) # 17/03/05
print( today_date.strftime(format_type2) ) # 17-03-05
```

### datetime from timestamp

- datetime이외에도, python에는 `time` 라이브러리도 있습니다. 여기서 `time.time()`은 Unix가 탄생한 시간인 "1970년 1월 1일 자정부터 지금까지 초 단위로 측정된 절대 시간"을 의미하죠.
- 이 값은 실수 형태로 저장되기 때문에, 상황에 따라서, `time.time()`을 사용해서 연산하는 게 더 편할 수도 있습니다. 
- 하지만, 반대로 이를 출력하는 일 또한 필요하기 때문에, 이를 `datetime.date` 클래스로 변환하는 것도 가능하죠.
- 이를 위해서는 `datetime.date.fromtimestamp()`을 사용합니다.

```python
import time
now_timestamp = time.time() #1970년 1월 1일 0:00부터 지금까지 흐른 '초'시간
print("date of timestamp {}: {}".format(now_timestamp, dt.date.fromtimestamp( now_timestamp )))
print("date of timestamp {}: {}".format(now_timestamp+60*60*24, dt.date.fromtimestamp( now_timestamp+60*60*24 )))
```

```plaintext
date of timestamp 1488720265.2891612: 2017-03-05
date of timestamp 1488806665.2891612: 2017-03-06
```

### datetime.date로부터 일정 시간이 경과된 날짜를 보고싶다면? 

- 만약, 오늘 날짜에서 하루 뒤 날짜를 알고 싶다면 어떻게 해야 할까요? 간단하게 생각하면 그냥 1을 더하면 되는 것 아니야? 라고 생각할 수 있지만, `datetime.date`와 `int`간에는 연산이 되지 않습니다. 다음처럼, 실행하면 에러가 발생하죠

```python
import datetime

date1 = datetime.date(year=2020, month=8, day=5)
print(date1 + 1)
```

- 앞서 말했지만, datetime 라이브러리에서 모든 시간의 간격은 `datetime.timedelta`를 이용해서 정의됩니다. 따라서, 단 하루를 추가하는 것일지라도 그 간격을 `datetime.timedelta`을 통해 정의하고 연산을 해줘야 한다는 것이죠.
- 즉, `datetime.date()`에 `datetime.timedelta`를 더해야 된다는 이야기입니다.

```python
import datetime

date1 = datetime.date(year=2020, month=8, day=5)
# 아래와 같이, datetime.timedelta를 사용하여 그 간격을 정의함.
more_day = datetime.timedelta(days=1)
date2 = date1 + more_day
print(date2) # 2020-08-06
print(type(date2)) # <class 'datetime.date'>
```

- 또한, `datetime.date()`에서 `datetime.date()`를 빼도 `datetime.timedelta`가 나옵니다.

```python
import datetime

MyBirthDate = datetime.date(year=2020, month=11, day=18)
Today = datetime.date.today()
Days_to_HBD = MyBirthDate - Today
print(Days_to_HBD)  # 105 days, 0:00:00
print(type(Days_to_HBD))  # <class 'datetime.timedelta'>
```
