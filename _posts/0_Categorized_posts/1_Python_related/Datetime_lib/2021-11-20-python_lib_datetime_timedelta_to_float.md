---
title: python - lib - datetime - timedelta를 float로 변환하기 
category: python-lib
tags: python python_lib datetime timedelta float
---

## python - lib - datetime - timedelta를 float로 변환하기 

- python에서 시간을 다룰 때는 보통 `datetime` library를 사용합니다.
- `datetime.datetime()`은 "날짜 + 시각"을 `datetime.timedelta()`는 시간 차이를 표현하죠. 
- 간단하게 다음처럼 사용할 수 있습니다.

```python
import datetime as dt


def to_datetime(input_str):
    """
    Argument Example: 2016-05-02 14:21:36
    Return: to datetime
    """
    r = dt.datetime.strptime(input_str, "%Y-%m-%d %H:%M:%S")
    return r


dt_a = to_datetime("2021-05-06 13:11:33")
dt_b = to_datetime("2021-05-06 18:45:33")

time_diff = dt_b - dt_a
print(f"time_diff: {time_diff}")
print(f"type: {type(time_diff)}")
# time_diff: 5:34:00
# type: <class 'datetime.timedelta'>
```

- 즉, 시간 차이를 표현하고 연산을 사용하려면, `datetime.timedelta`를 사용하면 되긴 하는데요. 그냥 간단히 "시간 차이가 1일보다 큰가?"를 확인하기 위해서도 다음의 형태로 표현해야 합니다.

```python
if time_diff > dt.timedelta(days=1):
    print("time_diff > 1 day")
```

- 이게 약간 귀찮은데요, 암묵적으로 1일은 1.0으로 처리되므로, 아래와 같이 해주면 연산자 오류가 발생합니다. `float`와 `datetime.timedelta`사이에 적합한 연산자가 존재하지 않는다는 얘기죠.

```python
if time_diff > 1.0: 
    print("time_diff > 1 day")
"""
Traceback (most recent call last):
  File "/Users/seunghoonlee/PythonProjects/2021_09_cide_proj/code/test.py", line 20, in <module>
    if time_diff > 1.0: 
TypeError: '>' not supported between instances of 'datetime.timedelta' and 'float'
"""
```

- 그럴 때는 그냥 다음처럼 처리하면 됩니다. `datetime.timedelta`간의 연산은 가능하고 그 결과는 `float`으로 리턴되거든요.

```python
dt_a = to_datetime("2021-05-06 13:11:33")
dt_b = to_datetime("2021-05-07 18:45:33")

time_diff = dt_b - dt_a
time_diff = time_diff / datetime.timedelta(days=1)

if time_diff > 1.0: 
    print("time_diff > 1 day")
```

## wrap-up

- `datetime.timedelta`를 `float`으로 자동변환되도록 혹은 연산이 가능하도록 지원하는 것은 기능상으로 어려운 점이 아닐 겁니다. 다만, 서로 다른 type 간에 변환이 너무 자유롭게 된다면, 개발상 error prone한 경우가 발생할 수 있으므로 이런 경우를 미연에 방지하도록 설계한게 아닐까 싶어요. 따라서 앞으로도 서로 다른 type이 연산 가능하도록은 바뀌지 않을 것이라고 생각됩니다.
- 위에서는 `days=1`로 고정하여 1일은 1.0으로 처리하였지만, 매우 당연히도 저 값을 변경하면 1.0을 1분 혹은 1년으로 바꿔서 처리하는 것도 가능합니다.

## reference

- [stackoverflow - convert timedeltat to floating point](https://stackoverflow.com/questions/21414639/convert-timedelta-to-floating-point)
