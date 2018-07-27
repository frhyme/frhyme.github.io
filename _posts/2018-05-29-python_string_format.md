---
title: python에서 string format 조절하기
category: python-basic
tags: python python-basic format string 

---

## python에서 string format 조절하기

- 예를 들어보면, 
    - 왼쪽/오른쪽/중간 정렬
    - '03' 이런 식으로 숫자에 0을 넣어서 출력하기 등등
- 을 해보려고 합니다. 

## examples 

```python
# 번호를 붙이면, 입력된 변수들의 순서에 따라 다르게 출력 
test_str = "{0}, {2}, {2}, {1}".format(1,2,3)
print(test_str)
#변수 이름을 함께 넘겨 주면, 해당 변수 값을 출력 
test_str = "{a}, {a}, {b}, {c}".format(a=1, b=2, c=3)
print(test_str)
# 30칸으로 고정하고 왼쪽 정렬
test_str = '{:<30}'.format('left aligned')
print(test_str+"remain")
# 오른쪽 정렬 
test_str = '{:>30}'.format('right aligned')
print("remain"+test_str)
# 중간 정렬 
test_str = '{:^30}'.format('centered')
print('rem'+test_str+'rem')
# 중간 정렬인데, 빈칸은 *으로 채움 
test_str = '{:*^30}'.format('centered')
print(test_str)
print()
# float 출력 
print("{:f}".format(10))
# float을 출력하는데 sign도 모두 표시하도록 
print("{:+f}".format(10))
print("{:.3%}".format(0.25666))
```

```
1, 3, 3, 2
1, 1, 2, 3
left aligned                  remain
remain                 right aligned
rem           centered           rem
***********centered***********

10.000000
+10.000000
25.666%
```

## wrap-up

- 정리하고 보니, 너무 간단한 것이군요 하하하핫. 

## references

- <https://docs.python.org/3.4/library/string.html>