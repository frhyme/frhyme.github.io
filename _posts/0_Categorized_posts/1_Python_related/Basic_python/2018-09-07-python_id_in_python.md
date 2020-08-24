---
title: value type vs. reference type 
category: python-basic
tags: python memory python-basic id object value-type reference-type 
---

## what is id function??

- 저도 잘 사용하지는 않는데, 파이썬에 `id`라는 built-in 함수가 있습니다. 해당 펑션에 **object**를 넣어주면, 해당 object가 위치한 메모리 주소를 리턴해줍니다. C++에서 포인터를 출력하면, 메모리 주소가 출력되잖아요. 그런거라고 생각하셔도 됩니다. 
- 간단한 예를 들면 다음과 같습니다. 아래에서는 List를 shallow copy했기 때문에, 주소값이 똑같은 상황인것이죠. 

```python
lst_a = [i for i in range(0, 10)]
lst_b = lst_a
print(id(lst_a))
print(id(lst_b))
```

```plaintext
4470632200
4470632200
```

- 따라서, 지금 내가 shallow copy를 했는지, 안했는지를 파악하려면 id function을 이용하면 좋습니다. 

## id(1)

- 조금 특이한 것은 id function이 그냥 integer 1에도 문제없이 먹힌다는 것이죠.
- 이는 python에서 number가 모두 object라는 것을 말합니다. primitive type이 없습니다, 파이썬에는. 

```python
## 값이 같으면 같은 객체, 값이 다르면 다른 객체 
for x in [1, 1.0, 1.00, 1.1, -0.3]:
    print(f"{x:6.2f} ==> {id(x)}, Is instance of object?? {isinstance(x, object)}")
```

```plaintext
  1.00 ==> 4422870368, Is instance of object?? True
  1.00 ==> 4470793152, Is instance of object?? True
  1.00 ==> 4470793152, Is instance of object?? True
  1.10 ==> 4470793080, Is instance of object?? True
 -0.30 ==> 4470793128, Is instance of object?? True
```

## primitive data types??

- primitive data type은 한국말로 변형하면 "기본 데이터 타입"이 됩니다. [위키피디아의 정의](https://en.wikipedia.org/wiki/Primitive_data_type)를 빌리자면 다음 둘 중 하나와 같아요. 

> a basic type is a data type provided by a programming language as a basic building block. Most languages allow more complicated composite types to be recursively constructed starting from basic types.
> a built-in type is a data type for which the programming language provides built-in support.

- 해당 언어에서 기본적으로 제공하는 data type, 보통 이 기본 형태를 중심으로 복잡한 형태(class 등)로 나아간다. 
- built-in type. 
- 그러니까, 그냥 해당 언어를 설치했을때 기본적으로 깔려 있는 데이터타입이면 그것이 primitive data type이라는 것인것 같아요. 

## built-in vs. primitive 

- 자, 위키피디아에서 정의한 것에 따르면, "그냥 맨처음에 깔려 있으면(built-in) ==> primitive data type"이라는 것처럼 읽힙니다. 좀 이상하지 않나요? 이전에 파이썬 관련 문서에서는 

> **"everything is object in python"**

- 라고 떠들었던 것 같아요. primitive type이 없다는 것을 명확히는 문장인 셈이죠. 
- 즉, 단순히 어떤 object가 built-in 이라고 해서 그것을 마냥 primitive datat type이라고 부를 수는 없는 것 같아요. 

## value types vs. reference types

- 오히려 이 문제는 여기로 넘어오게 되는 것 같아요. [해당 data의 type이 value type이냐, reference type이냐?(당연히 위키피디아에 있는 내용입니다)](https://en.wikipedia.org/wiki/Value_type_and_reference_type)
  - `value type`: value type은 메모리에 값을 그대로 저장하는 것을 말하고
  - `reference type`: reference type은 메모리에 해당 값을 저장한 메모리의 위치를 저장하는 것을 말합니다(포인터))
- 즉, 앞서 말한 primitive data type은 value type을 말하는 것이었던 것이죠. 

- 즉, **Everything is object in python**이라는 말은 사실 **the type of everything is reference**라고 변형할 수 있습니다. 즉 파이썬에서의 모든 변수는, 값을 저장하는 것이 아니라, 값이 저장되는 메모리들을 저장한다. 라고요. 
- 실제로 [위키피디아](https://en.wikipedia.org/wiki/Value_type_and_reference_type#Classification_per_language)의 테이블을 보시면,  python의 경우 value type이 전혀 없는 것을 알 수 있습니다. 

## Is value type faster? 

- 보통 primitive type이 더 빠르다는 이야기가 많습니다. 뭐 직관적으로 얘기하면 1) 메모리에서 값을 바로 읽는 경우와, 2) 메모리에서 해당 값이 저장된 메모리주소를 읽어서, 다시 그 값들을 다 읽어오는 경우를 비교하면, 당연히 메모리에서 값을 바로 읽는 경우가 훨씬 빠르겠죠. 
- 또한 보통 연산의 컴퓨터가 32 비트인 것을 고려해봅시다. C에서의 value type인 int의 크기는 32비트죠. 즉, 해당 컴퓨터 구조에 적합한 32비트의 값을 가지는 int는 해당 아키텍쳐에 최적화되어 있다고 할 수 있습니다. 당연히, int를 잘 쓸 수록 훨씬 빨라지겠죠. 너무 당연한 이야기입니다. 
  - [아래는 해당 내용을 참고한 위키피디아를 인용한 부분입니다](https://en.wikipedia.org/wiki/Primitive_data_type). 

> In particular, the C standard mentions that "a 'plain' int object has the natural size suggested by the architecture of the execution environment". This means that int is likely to be 32 bits long on a 32-bit architecture. 

## wrap-up

- python에는 reference type밖에 없습니다. 즉, 존재하는 모든 것은 객체가 되고, 다시, `=`(assignment operator)를 잘못 쓰면 shallow copy가 되기 쉬운 구조라는 것이죠. 
- data type이 value type일 경우에는 `=`를 사용하면 알아서 deep copy가 됩니다. 다만, reference type일 때는 메모리 주소가 복사되죠. 이런 종류의 에러들이 쌓이기 시작하면 해당 코드를 유지보수하는 부분이 너무 어려워지게 되죠. 

- 즉, 두 가지 정도를 명확하게 인지하는 것이 필요할 것 같습니다. 
  - 내가 지금 쓰고 있는 아이는 value type이냐, reference type이냐 
  - 그래서, 지금 나는 shallow copy를 하고 있느냐, deep copy를 하고 있느냐? 

## reference 

- [Wikipedia - Value type and reference type](https://en.wikipedia.org/wiki/Value_type_and_reference_type)
- [Wikipedia - Primitive data](https://en.wikipedia.org/wiki/Primitive_data_type)
- [Stackoverflow - Why do people still use primitive types in java](https://stackoverflow.com/questions/5199359/why-do-people-still-use-primitive-types-in-java)
