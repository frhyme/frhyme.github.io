---
title: python - F632 - string은 == 로 비교하세요!
category: 
tags: 
---

## 2-line summary 

- python은 string에 대해서 object interning의 방식으로 관리를 한다. 이는, 메모리의 효율적인 관리를 위해 같은 문자열을 중복으로 메모리 공간에 확보하지 않으려는 기법이다. 
- `is`는 identity testing이며, 두 변수의 메모리 공간이 같은지를 확인하는 방법이고, `==`는 값이 같은지를 확인하는 equality testing이다.
- 스트링을 비교할 때, `==`을 사용해도, `is`를 사용해도 모두 잘 되는 것처럼 보이는 것은, python이 object interning을 통해서, 같은 문자열을 단 하나의 공간에만 확보해두기 때문에 그런 것이다.
- 따라서, `"".join(['a', 'b', 'c']) is "abc`와 같은 경우에는 `False`가 나오는 등의 문제가 발생하 ㄹ수 ㅣㅇㅆ다.
- 따라서, 값을 체크할 때는 반드시 `==`을 사용하도록 한다.

---

## Intro

- flake8을 통해서 현재 코드의 문제점 혹은 개선사항을 정리하는데, 다음과 같은 종류의 코드에서 문제가 있다고 알려주더군요.

```python 
k = "abc"
if k is "abc":
    print("correct")
```

- 딱히 문제가 있어 보이지는 않는데, 여기서 언급한 문제는 다음과 같습니다.
- `F632`에 해당되는 문제고, **"string 등을 비교할 때는 is 가 아니라, ==를 사용해라"**라는 말이죠.

```plaintext
use ==/!= to compare str, bytes, and int literalsflake8(F632)
```

## 뭐가 문제인데?

- 딱히 큰 차이가 없어 보이는데, 그 이유를 확인해보도록 합니다.
- 우선 아래 코드를 실행해서는 딱히 차이가 없어요. `==`과 `is`에 차이가 있어 보이지 않습니다.

```python
print(str1 == "abc") # True
print(str1 is "abc") # True

print(str1 == "abcd") # False
print(str1 is "abcd") # False
```

- 다만, 아래 코드에서는 그 결과가 달라지죠.

```python
print(str1 == "".join(['a', 'b', 'c'])) # True
print(str1 is "".join(['a', 'b', 'c'])) # False
```

## `is` means `id(a)==id(b)`

- 이를 확인하기 위해서는 `is`가 어떤 것을 수행하는지 살펴볼 필요가 있습니다.
- `is`는 identity testing을 합니다. 즉, `a is b` 라는 코드는 `id(a) == id(b)`를 의미한다는 것이고, 두 변수 가 동일한 ID를 가지고 있는지 확인한다는 것이죠.
- python에서 `id()`는 다음을 의미합니다. 
  
> "an integer (or long integer) which is guaranteed to be unique and constant for this object during its lifetime"

- 동일하지는 않지만, 개념적으로는 C에서의 메모리 주소 같은 개념이라고 생각해도 됩니다. 
- 모든 변수에 대해서 각각 고유의 ID가 존재하는 것이죠.
- 여기서, 그 말에 따라서 다음 코드를 실행해 봅니다.
  
```python 
s1 = "abc"
s2 = "abc"

print(id(s1)) # 4422470000
print(id(s2)) # 4422470000
```

- 다만, 두 string이 서로 다른 변수에 저장되어 있음에도 불구하고 그 결과는 같습니다.
- 즉, 같음 메모리 공간에 두 변수가 할당되어 있다고 봐도 되는 것이죠.

```plaintext
4422470000
4422470000
```

## Object interning

- 여기서, 흥미로운 개념인 **Object Interning**이 등장하게 됩니다.
- Object Interning은 "이미 생성된 객체를 재사용하는 것"을 말하며, 당연하지만 immutable한 객체에 대해서 사용하게 됩니다. 
- 즉 스트링의 경우 immutable하고, 혹시 이 아이들이 여러 변수에 동시에 메모리로 할당되어 있다면, 메모리 낭비가 발생하므로, Object Interning을 통해서 하나의 메모리 공간을 동시에 가리키도록 한다는 것이죠.

### python Default Interning

- 조금씩 다르지만, 기본적으로는 문자열과, 정수, 들에 대해서 Interning으로 처리합니다. 
- 다만, 문자열의 길이, 정수의 크기에 따라서 Interning이 되는 경우가 있고 되지 않는 경우가 있죠.
- 가령, 새로운 스트링이 발생하면, python에서는 Intern 내에 해당 스트링이 존재하는지를 화인하고, 있으면 그 메모리 주소를 자동으로 할당받게 됩니다. 만약 없으면 새로운 Intern 컬렉션 내에서 새로운 문자열을 생성하고, 그 주소를 할당하게 되죠.

## wrap-up

- 따라서, 정리를 하자면 다음과 같습니다.
- python은 string에 대해서 object interning의 방식으로 관리를 한다. 이는, 메모리의 효율적인 관리를 위해 같은 문자열을 중복으로 메모리 공간에 확보하지 않으려는 기법이다. 
- `is`는 identity testing이며, 두 변수의 메모리 공간이 같은지를 확인하는 방법이고, `==`는 값이 같은지를 확인하는 equality testing이다.
- 스트링을 비교할 때, `==`을 사용해도, `is`를 사용해도 모두 잘 되는 것처럼 보이는 것은, python이 object interning을 통해서, 같은 문자열을 단 하나의 공간에만 확보해두기 때문에 그런 것이다.
- 따라서, `"".join(['a', 'b', 'c']) is "abc`와 같은 경우에는 `False`가 나오는 등의 문제가 발생하 ㄹ수 ㅣㅇㅆ다.
- 따라서, 값을 체크할 때는 반드시 `==`을 사용하도록 한다.

## Reference

- [stackoverflow - why does comparing strings using ==](https://stackoverflow.com/questions/1504717/why-does-comparing-strings-using-either-or-is-sometimes-produce-a-differe)
- [stackoverflow - what is the id function used for](https://stackoverflow.com/questions/15667189/what-is-the-id-function-used-for)
- [pythonstudy - Object 인터닝](http://pythonstudy.xyz/python/article/512-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Object-Interning)
