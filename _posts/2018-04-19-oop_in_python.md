---
title: Object Oriented Programming in Python
category: python-basic
tags: python python-basic OOP object-oriented-programming

---

## intro

- 다음 내용을 (아주 간단히) 소개할 계획
    - basic
    - inheritance
    - method overriding
    - class method
    - static method

## basic

- object = 관련있는 데이터와 메소드의 합
- `__init__` method는 생성자 라고 생각을 하면 됨(실제로는 조금 다르게 운영이 된다고 하지만, 거기까지 우리가 알 필요는 없을듯)


#### code 

```python
class Rectangle(object):
    def __init__(self, h, v):# constructor 
        self.h = h
        self.v = v
    def area(self):
        return self.h * self.v
a = Rectangle(3, 4)
print(a.h, a.v, a.area())
```

#### code result 

```
    3 4 12
``` 

## inheritance and method overriding

- 기존에 있는 클래스를 상속하는 것, 
- 개와 오리는 동물 클래스를 상속받는다.
- 당연한 이야기지만, method는 instance, class, super class 순으로 탐색해서 실행됨. 
    - 하위 클래스에 해당 이름의 method가 있을 경우에는 그 method가 실행되고, 그렇지 않을 때는, 상위 클래스가 수행됨
    - `super(class type, instance)`를 사용하면, 상위 클래스의 method를 실행할 수 있음.


#### code 

```python
class Animal(object):
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("what?")
class Dog(Animal):
    def speak(self):
        print("Bark")
class Duck(Animal):
    def speak(self):
        print("Quak")
animals = [Dog("dog"), Duck("duck")]

for x in animals:
    super(type(x), x).speak() # class의 super class의 instance method를 실행
    x.speak()
```

#### code 

```
    what?
    Bark
    what?
    Quak
``` 

## overloading? 

- overriding 은 기존에 있던 메소드를 덮어 쓰는 것
- 오버로딩은 자료형이나 인수에 따라서 다르게 작동하도록 하는 것
- C++에서 생각해보면 `func(int a, int b)`, `func(int a, int b, int c)`를 둘다 정의하여 사용할 수 있음
- 그러나, 파이썬에서는 이렇게 서로 다른 인수를 받는 함수를 동시에 사용할 수 없음 
    - 아래를 보면, `test(a, b)` 가 `test(a, b, c)`에 덮어씌워져서 사라짐. 

#### code

```python
def test(a, b):
    return a+b
def test(a, b, c):
    return a+b+c
test(1, 2)
```

#### code result 

```
    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-55-28f4e14470a5> in <module>()
          3 def test(a, b, c):
          4     return a+b+c
    ----> 5 test(1, 2)
    

    TypeError: test() missing 1 required positional argument: 'c'
```

## public/private/protected

- private method를 콜하면 문제가 발생한다. 
  - `_`: protected
  - `__`: private

#### code

```python
class test(object):
    def __init__(self, name):
        self.name = name
        self.__private_name = "".join(list(reversed(name)))
    def __private_method(self):
        print("this is private method")
        print(self.__private_name)
    def public_method(self):
        print("this is public method")
        self.__private_method()
a = test("seunghoon")
a.public_method()
a.__private_method()
```

#### code result 

```

    this is public method
    this is private method
    noohgnues
    


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-56-88c0d54e0d0d> in <module>()
         11 a = test("seunghoon")
         12 a.public_method()
    ---> 13 a.__private_method()
    

    AttributeError: 'test' object has no attribute '__private_method'
```

## class variable과 특수 메소드

- 그런데, 기존에 정의된 특수 메소드들의 경우는 `__`가 붙어있지만 외부에서도 접근 가능함.
- 주요 operator를 정의하기 위한 메소드
- class variable; 인스턴스가 아니라, 클래스에 속한 변수
    - 따라서, self, 가 아니라, 클래스이름으로 접근함
    - 물론 인스턴스 이름으로 접근해도 문제는 없음

#### code

```python
# 특수 메소드 : __ 이 있는 메소드 
class Complex(object):
    count = 0 #class 변수, self가 없음
    def __init__(self, real, img):# 생성자
        Complex.count+=1
        self.r = real
        self.i = img
    def __str__(self): # string으로 바꾸었을때 어떻게 변환되는지에 대한 부분 
        return str(self.r)+"+"+str(self.i)+"i"
    def __getitem__(self, key):# []으로 접근가능하게 만들 때, 
        if key=="r":
            return self.r
        if key=="i":
            return self.i
    def __add__(self, other): # + 
        return Complex(self.r + other.r, self.i + other.i)
    def __sub__(self, other): # = 
        return Complex(self.r - other.r, self.i - other.i)
    def __gt__(self, other): # >
        return (self.r > other.r)
    def __ge__(self, other): # >=
        return (self.r >= other.r)
    def __lt__(self, other): # <
        return (self.r < other.r)
    def __le__(self, other): # <=
        return (self.r <= other.r)
    def __eq__(self, other): # ==
        return (self.r == other.r)
    def __ne__(self, other): # !=
        return (self.r != other.r)

c = Complex(1, 2)
print(c["r"], c["i"])

for i in range(0, 10):
    Complex(1, 2)

print(c.count, Complex.count)

print( c+Complex(2, 3))
print( c-Complex(2, 3))
print( c>Complex(2, 3))
print( c>=Complex(0, 0))
print( c==Complex(1, 2))
```

#### code result

```
    1 2
    11 11
    3+5i
    -1+-1i
    False
    True
    True
``` 

### class method static method

- instance method: 인스턴스를 통해 호출이 되고, 첫번째 인자로 인스턴스 자신(self)을 자동으로 전달함
- class method: 클래스를 통해 호출이 되고, @classmethod 라는 데코레이터로 정의함, 클래스 자체가 인수로 전달되고, 이를 관습적으로 cls라고 칭함
    - decorator가 뭔지를 공부하려면 좀 시간이 걸리고, 그냥 '기존에 정의된 데코레이터를 이용하면, 함수의 특성을 확장할 수 있다' 정도로만 이해하면 됨. 
- static method: 클래스 내부에 있지만, 클래스 네임스페이스에만 있을 뿐, 일반 함수와는 다른게 없음. 다만 클래스 내부에 있어야 관리하는 것이 편함. 

#### code

```python
class Animal(object):
    def __init__(self, name):
        self.name = name
    @classmethod
    def other_constructor_using_classmethod(cls, name):
        return cls(name)
    @staticmethod
    def other_constructor_using_staticmethod(name):
        return Animal(name)
    def speak(self):
        print(self.name, ": speak")
class Dog(Animal):
    def speak(self):
        print(self.name, ": Bark")
class Duck(Animal):
    def speak(self):
        print(self.name, ": Quak")
Animal.other_constructor_using_classmethod("na1").speak()
Animal.other_constructor_using_staticmethod("na2").speak()
```

#### code result 

```
    na1 : speak
    na2 : speak
```    

- static, class 가 큰 차이가 없다고 느껴질 수 있지만, class method의 경우 상속된 클래스를 자동으로 넘길 수 있고
- static method의 경우는 이것을 자동으로 넘길 수가 없다.

#### code

```python
Dog.other_constructor_using_classmethod("dd").speak()
Dog.other_constructor_using_staticmethod("dd").speak()
```

#### code result 

    dd : Bark
    dd : speak
    
## Reference 

- http://schoolofweb.net/blog/posts/파이썬-oop-part-3-클래스-변수class-variable/
- https://datascienceschool.net/view-notebook/fdbe01932ce74b7983f1862a56e32104/
- https://www.slideshare.net/dahlmoon/20160310
- http://pythonstudy.xyz/python/article/19-%ED%81%B4%EB%9E%98%EC%8A%A4
- https://docs.python.org/3/tutorial/classes.html
