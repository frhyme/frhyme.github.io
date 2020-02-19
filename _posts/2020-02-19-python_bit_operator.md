---
title: python bit operator 
category: python-basic
tags: python python-basic bit bit-operator
---

## python bit operator. 

- 사실, bit operator를 쓸 일이 거의 없기는 한데, 잠깐 써야할 일이 있어서 이 때 정리해두기로 합니다. 
- 내용 자체가 복잡하지 않으므로, 코드에 주석을 달아서 그대로 정리하였습니다. 

```python
A = 10
B = 3

print("=="*20)
# 다음으로 4칸의 bit 형식으로 표현할 수 있음.
# 04b : "4칸짜리, binary형식으로 없는 칸은 0을 채워서"
print(f"A    : {A: 08b}")
print(f"B    : {B: 08b}")
print("--"*10)
# Bitwise NOT ~A
# A의 보수, complement는 ~A-1
print(f"NOT A: {~A: 08b}")
print(f"NOT B: {~B: 08b}")
# Bitwise AND A & B
# 칸 별로 둘다 1이어야 1, 아니면 0
print(f"A & B: {A&B: 08b}")

# Bitwise OR A | B
# 칸 별로 둘 중 하나라도 1이면 1
print(f"A | B: {A|B: 08b}")

# Bitwise XOR A ^ B
# 다르면 1, 같으면 0.
print(f"A ^ B: {A^B: 08b}")

# Bitwise left or right shifter.
# A << n: left shifter, A를 bit로 왼쪽으로 n칸 이동
# A >> n: right shifter, A를 bit로 오른쪽으로 n칸 이동
print(f"A<<2 : {A<<2: 08b}")
print(f"A>>2 : {A>>2: 08b}")
print("==" * 20)
```

- 결과는 다음과 같죠. 

```
========================================
A    :  0001010
B    :  0000011
--------------------
NOT A: -0001011
NOT B: -0000100
A & B:  0000010
A | B:  0001011
A ^ B:  0001001
A<<2 :  0101000
A>>2 :  0000010
========================================
```

## reference

- [geeoksforgeeks - python bitwise operators](https://www.geeksforgeeks.org/python-bitwise-operators/)