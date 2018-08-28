---
title: 차번호판의 숫자를 사칙연산으로 0으로 만들 수 있을까요? 
category: python-lib
tags: python python-lib numpy 
---

## 이상한 짓을 합니다. 

- 저만 그러는지는 모르겠는데, 저는 숫자 4개로 구성된 차 번호판을 보면 사칙연산을 해보는 버릇이 있습니다. 제가 공대에 속해 있어서 그런지는 모르겠는데, 제 주위에도 이런 친구들이 몇몇 있습니다. 
- 아무튼, 하다보면 대부분 되는 것 같은데 몇 개는 안되는 것들이 있어요. 그럴 때, "내가 못하는 건가 저게 안되는건가"라는 생각이 들곤 합니다. 
- 그래서 간단하게 코딩해보기로 했습니다. 

- constraint는 다음과 같아요. 
    - 사칙연산(+, /, *, -)만 가능
    - 순서 바꾸기 불가
    - 괄호는 가능 

```python
import numpy as np 

def calc_a_b(a, b):## a, b에 대한 사칙연산 결과를 리스트로 리턴
    a, b = float(a), float(b)
    r_lst = [a+b, a-b, a*b]
    return set(r_lst+[a/b]) if b!=0 else set(r_lst)
def calc_a_b_c(a, b, c):## a, b, c의 사칙연산 결과를 리스트로 리턴
    r_lst = [y for x in calc_a_b(a, b) for y in calc_a_b(x, c)]
    return set(r_lst + [y for x in calc_a_b(b, c) for y in calc_a_b(a, x)])
def calc_a_b_c_d(a, b, c, d):## a, b, c, d의 사칙연산 결과를 리스트로 리턴 
    r_lst = [ y for x in calc_a_b_c(a, b, c) for y in calc_a_b(x, d)]
    r_lst += [ y for x in calc_a_b_c(b,c,d) for y in calc_a_b(a, x)]
    r_lst += [ x for bc in calc_a_b(b, c) for x in calc_a_b_c(a, bc, d)]
    return set(r_lst)
    
car_plate_nums = [f'{i:0>4d}' for i in range(0, 10000)]
result = [True if 0 in calc_a_b_c_d(*plate_num) else False for plate_num in car_plate_nums ]
print(f"0으로 만들어지는 비율: {np.mean(result):.4f}")
```

```
0으로 만들어지는 비율: 0.8500
```

- 만약, `%`가 가능하다고 하면 어떻게 될까요? 

```python
import numpy as np 

def calc_a_b(a, b):
    a, b = float(a), float(b)
    r_lst = [a+b, a-b, a*b]
    return set(r_lst+[a/b, a%b]) if b!=0 else set(r_lst)
def calc_a_b_c(a, b, c):
    r_lst = [y for x in calc_a_b(a, b) for y in calc_a_b(x, c)]
    return set(r_lst + [y for x in calc_a_b(b, c) for y in calc_a_b(a, x)])
def calc_a_b_c_d(a, b, c, d):
    r_lst = [ y for x in calc_a_b_c(a, b, c) for y in calc_a_b(x, d)]
    r_lst += [ y for x in calc_a_b_c(b,c,d) for y in calc_a_b(a, x)]
    r_lst += [ x for bc in calc_a_b(b, c) for x in calc_a_b_c(a, bc, d)]
    return set(r_lst)
    

car_plate_nums = [f'{i:0>4d}' for i in range(0, 10000)]
result = [True if 0 in calc_a_b_c_d(*plate_num) else False for plate_num in car_plate_nums ]
print(f"0으로 만들어지는 비율: {np.mean(result):.4f}")
```

- 다 되는군요. 

```
0으로 만들어지는 비율: 1.0000
```

## wrap-up

- 간단하네요. 앞으로는 하다 안되면 modulo를 사용해서 하도록 하겠습니다. 약간 뭔가 tricky하기는 한데 그래도. 