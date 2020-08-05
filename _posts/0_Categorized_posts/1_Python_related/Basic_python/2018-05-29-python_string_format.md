---
title: python에서 string을 다양한 방식으로 출력하기
category: python-basic
tags: python python-basic format string 
---

## python에서 string format 조절하기

- python에서 string을 출력할 때, 그냥 값만 출력하는 것이 아니라, 왼쪽/오른쪽/중간 정렬을 사용하거나, `0003`과 같이 앞에 0을 padding하여 출력하는 것 등 다양한 기능등리 포함되어 있습니다.
- 본 글에서는 몇 가지 기능들을 중심으로 정리해봤습니다.

## examples 

```python
# 번호를 붙이면, 입력된 변수들의 순서에 따라 다르게 출력 
test_str = "{0}, {2}, {2}, {1}".format(1,2,3)
print(test_str)
# 1, 3, 3, 2
```

```python
#변수 이름을 함께 넘겨 주면, 해당 변수 값을 출력 
test_str = "{a}, {a}, {b}, {c}".format(a=1, b=2, c=3)
print(test_str)
# 1, 1, 2, 3
```

```python
# 30칸으로 고정하고 왼쪽 정렬
test_str = '{:<30}'.format('left aligned')
print(test_str+"remain")
# left aligned                  remain
```

```python
# 오른쪽 정렬 
test_str = '{:>30}'.format('right aligned')
print("remain"+test_str)
# remain                 right aligned
```

```python
# 중간 정렬 - 빈칸은 공백으로 채움 
test_str = '{:^30}'.format('centered')
print('rem'+test_str+'rem')

# rem           centered           rem
```

```python
# 중간 정렬인데, 빈칸은 *으로 채움 
test_str = '{:*^30}'.format('centered')
print(test_str)
# ***********centered***********
```

```python
# float 출력 
print("{:f}".format(10)) # 10.000000
# float을 출력하는데 sign도 모두 표시하도록 
print("{:+f}".format(10)) # +10.000000
print("{:.3%}".format(0.25666)) # 25.666%
```

## wrap-up

- 정리하고 보니, 너무 간단한 것이군요 하하하핫.
- 또한, 요즘에는 윗글에서 쓴 것처럼 `.format`를 이용하는 것보다, f-string을 사용해서 쓰는 것이 더 장려되는 것 같아요.

## references

- [python3 - string - common string operation](https://docs.python.org/3.4/library/string.html)
