---
title: # python - datetime
category: python-lib
tags: python python-lib datetime

---

## intro

- `pandas`에서 바로 datetime을 처리하는 것이 더 편할 때도 있지만, 저는 datetime을 쓰는 편이 더 좋아서, 이쪽을 선호합니. 
- 단순하게, datetime 은 date object 와 time object을 합친 것이고, datetime - datetime은 timedelta라는 시간의 변화량을 나타내는 객체를 의미합닏. 
- 스트링을 datetime으로, datetime을 스트링을 변환하는 것 또한 가능하며, 이는 뒤쪽엣 설명합니다. 


- 최근에 코딩하면서, 날짜, 시간 을 다루는데 불편함이 좀 있어서, Python에서 날짜/시간 다루는 모듈을 좀 정리해봄.
- datetime 모듈에는 아래와 같은 총 다섯 가지의 클래스가 존재
- classes
    - date: 날짜에 대한 class, attribute: year, month, day
    - time: 시간에 대한 class, attribute: hour, minute, second 등
    - datetime: date와 time의 조합 class
    - timedelta: 두 date, time, datetime instance 간의 차이를 표현, days, seconds 속성을 가짐
    - tzinfo: time zone class, datetime class 내의 속성으로 존재(여기서는 따로 설명하지 않음)


### datetime.date

```python
import datetime as dt
today_date = dt.date.today()
print(today_date, type(today_date))
print(today_date.min, dt.date.min)
print(today_date.max, dt.date.max)
print(today_date.resolution)
print(today_date.year, today_date.month, today_date.day)
```

```
    2017-03-05 <class 'datetime.date'>
    0001-01-01 0001-01-01
    9999-12-31 9999-12-31
    1 day, 0:00:00
    2017 3 5
```

#### datetime.date.weekday

```python
days  = [ dt.date(2017, 3, 6+i).weekday() for i in range(0,7) ]
week_num_to_str_dict = {0:"mon", 1:"tue", 2:"wed", 3:"thu", 4:"fri", 5:"sat", 6:"sun"}
week_days = [ week_num_to_str_dict[week_num] for week_num in days]
print( days )
print( week_days )
```

```
    [0, 1, 2, 3, 4, 5, 6]
    ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
```

#### date formatting

```python
format_type1 = "%y/%m/%d"
format_type2 = "%y-%m-%d"
print( today_date.strftime(format_type1) )
print( today_date.strftime(format_type2) )
```

```
    17/03/05
    17-03-05
```


### datetime from timestamp

-  timestampepoch 시간(1970년 1월 1일 자정)이후로 즉 Unix 가 탄생한 사건을 기준으로 ==초 단위로  측정한 절대 시간==
- timestamp는 실수 형태로 저장되기 때문에, 모든 날짜시간 데이터를 timestamp로 고려하고 연산하는게 더 편할 때도 있음
    - 특시, 사칙연산시에 편함


```python
import time
now_timestamp = time.time() #1970년 1월 1일 0:00부터 지금까지 흐른 '초'시간
print("date of timestamp {}: {}".format(now_timestamp, dt.date.fromtimestamp( now_timestamp )))
print("date of timestamp {}: {}".format(now_timestamp+60*60*24, dt.date.fromtimestamp( now_timestamp+60*60*24 )))
```

```
    date of timestamp 1488720265.2891612: 2017-03-05
    date of timestamp 1488806665.2891612: 2017-03-06
```

- date object의 경우 사칙연산이 안되기 때문에 하루 뒤의 날짜를 출력하는 것이 조금 불편함
  - time datetime object의 경우도 마찬가지

```python
print(dt.date.today() + 1)
```

```
    -----------------------------------------------------------------

    TypeError                       Traceback (most recent call last)

    <ipython-input-225-1627af73a4f7> in <module>()
    ----> 1 print(dt.date.today() + 1)


    TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
```

- 따라서 datetime 내의 object를 timestamp로 변환하여 처리하는 것이 편한 경우가 있음
    - timestamp는 실수 값이므로 덧셈 뺄셈이 상대적으로 자유로움
##### date to timestamp to date


```python
import time

print(today_date)
today_timestamp = time.mktime(today_date.timetuple())
print( dt.date.fromtimestamp(today_timestamp + 60*60*24*31) )
```

```
    2017-03-05
    2017-04-05
```


- 사실 쉬운 다른 방법이 있음 헤헤 😄

```python
print( today_date+dt.timedelta(days=2))
```

```
    2017-03-07
```

- datetime.timedelta 는 두 시각 간의 차이를 의미하는 class

```python
td1 = dt.timedelta(weeks = 2, days = 31, hours = 2, minutes=13, seconds = 3)
dt1 = dt.datetime.now()
print(dt1)
print(dt1+td1)
```

```
    2017-03-05 22:24:31.945162
    2017-04-20 00:37:34.945162
```


```python
import datetime
d1 = datetime.date(2017, 11, 18) #my birthday
d2 = datetime.date.today()
print("내 생일까지 {} 남았습니다.".format( (d2-d1 if d1<d2 else d1-d2) ))
print(type(d2-d1))

```

```
    내 생일까지 258 days, 0:00:00 남았습니다.
    <class 'datetime.timedelta'>
```

### datetime.time

```python
import datetime as dt
now_time = dt.datetime.today().time()
print(now_time)
print(now_time.min)
print(now_time.max)
print(now_time.resolution)
print(now_time.hour, now_time.minute, now_time.second)
```

```
    22:24:34.050164
    00:00:00
    23:59:59.999999
    0:00:00.000001
    22 24 34
```

#### datetime.time formatting

```python
format_type1 = "%H:%M:%S"
format_type2 = "%I:%M:%S %p"
print( now_time.strftime(format_type1) )
print( now_time.strftime(format_type2) )
```

```
    22:24:34
    10:24:34 PM
```

### datetime.datetime

- date와 time을 모두 가지는 class
-  now today은 timezone에 따라서 의미가 조금 다른데, 여기서는 다루지 않았음(일단은 같다고 생각해도 됨)


```python
import datetime as dt
print( dt.datetime.today(), type(dt.datetime.today()) )
print( dt.datetime.now(), type(dt.datetime.now()) )
print( dt.datetime.utcnow(), type(dt.datetime.utcnow() ))
```

```
    2017-03-05 22:24:34.945165 <class 'datetime.datetime'>
    2017-03-05 22:24:34.945165 <class 'datetime.datetime'>
    2017-03-05 13:24:34.945165 <class 'datetime.datetime'>
```


```python
print( dt.datetime.min )
print( dt.datetime.max )
print( dt.datetime.resolution, dt.datetime.resolution == dt.time.resolution )

dt1 = dt.datetime.today()
print(dt1.year, dt1.month, dt1.day, dt1.hour, dt1.minute, dt1.second)
```

```
    0001-01-01 00:00:00
    9999-12-31 23:59:59.999999
    0:00:00.000001 True
    2017 3 5 22 24 35
```

- datetime 역시 timestamp로부터 생성할 수 있음


```python
import time
ts1 = time.time()
print( dt.datetime.fromtimestamp(ts1) )
print( dt.datetime.fromtimestamp(ts1+60*60*24*31) )
```

```
    2017-03-05 22:24:35.713165
    2017-04-05 22:24:35.713165
```

- date, time object로부터 datetime을 생성

```python
dt1 = dt.datetime.today()
print( dt1 )
d1 = dt1.date()
t1 = dt1.time()
print( dt.datetime.combine(d1, t1) )
print( dt.datetime.combine(d1, t1) == dt1 )
```

```
    2017-03-05 22:24:37.570165
    2017-03-05 22:24:37.570165
    True
```

#### datetime.datetime formatting

###### strftime: datetime => string


```python
import datetime as dt
dt1 = datetime.datetime.now()
print(dt1)
format_type = "%d %b %Y %I:%M:%S %p"
formated_dt_str = dt1.strftime( format_type )
print( formated_dt_str )
```

```
    2017-03-05 22:24:38.209165
    05 Mar 2017 10:24:38 PM
```

###### strptime: string => datetime

```python
dt2 = dt.datetime.strptime(formated_dt_str, format_type )
print(dt2)
```

```
    2017-03-05 22:24:38
```

## Reference

- https://docs.python.org/3/library/datetime.html
