---
title: python-lib) python - datetime.datetime
category: python-lib
tags: python python-lib datetime
---

## datetime.datetime

- `datetime.datetime`은 날짜를 나타내는 `datetime.date`과 시각을 나타내는 `datetime.time`을 모두 가지는 class입니다. 가장 범용적으로 많이 쓰이는, class죠.

### now or today

- 현재의 시각을 알고 싶을 때는 `datetime.datetime.today()`나 `datetime.datetime.now()`를 사용합니다.
- `datetime.datetime.utcnow()`는 "협정세계시"를 의미하는 Coordinated Universal Time 을 의미합니다. 그리치니 표준시(GMT, Greenich Mean Time)과 동일하다고 봐도 상관없고, 그냥 "런던 시간대"라고 생각해도 문제없어요.

```python
import datetime

# 아래는 모두 datetime.datetime object
print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())

# utc는 세계 표준시를 의미하며, 여기에 +9를하면 서울시
print(datetime.datetime.utcnow() + datetime.timedelta(hours=9))
```

```plaintext
2020-08-05 14:56:47.543090
2020-08-05 14:56:47.543181
2020-08-05 05:56:47.543193
2020-08-05 14:56:47.543454
```

## datetime.datetime formatting

- 프로그래밍을 하다보면 필요에 따라서, 문자열을 datetime object로 변형하기도 혹은 그 반대를 수행하기도 합니다.
- 그 두 방법을 모두 아래에서 셜명합니다. 다만, 이 때 문자열의 각 부분이 어떤 것을 의미하는지 mapping해주는 작업이 필요하죠. 이 부분은 [Python's strftime directives](https://strftime.org/)를 참고하시면, 자세히 알 수 있습니다.

### strftime: datetime.datetime => string

- 아래 코드에서는 `datetime.datetime()`을 원하는 형식에 맞춰서 string으로 변형했습니다.

```python
import datetime as dt

dt1 = datetime.datetime.now()
print(dt1)
format_type = "%d %b %Y %I:%M:%S %p"
formated_dt_str = dt1.strftime( format_type )
print( formated_dt_str )
```

```plaintext
2017-03-05 22:24:38.209165
05 Mar 2017 10:24:38 PM
```

### strptime: string => datetime

- 아래 코드에서는 string으로 되어 있는 날짜를 `datetime.datetime()`으로 읽습니다.

```python
dt2 = dt.datetime.strptime(formated_dt_str, format_type )
print(dt2)
```

```plaintext
2017-03-05 22:24:38
```

## wrap-up

- `datetime` 라이브러리에서 가장 많이 쓰이는 클래스가 바로 `datetime.datetime`죠. 그리고 필요한 형식의 문자열으로 내보내기 위해서 `.strftime`을 사용하고, 문자열을 정확히 날짜로 읽기 위해서 `.strptime`을 사용합니다.

## reference

- [Python's strftime directives](https://strftime.org/)
