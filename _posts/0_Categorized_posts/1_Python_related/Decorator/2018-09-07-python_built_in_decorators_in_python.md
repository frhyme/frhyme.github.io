---
title: built-in decorator in python3
category: python-basic
tags: python python-basic decorator oop class python-libs static inheritance
---

## decorator?? 

- 우선 decorator가 무엇인지 모르는 분들에게 decorator가 무엇인지 알려줍니다. 

> 장식해주는 놈

- 입니다. 하하하하핫. 
- 우리가 함수를 간단하게 짜고 그냥 앞에 `@decorator`만 붙여주면 알아서 더 좋은 놈으로 만들어주는 종류의 아이에요. 

> 함수를 먹고 확장된 더 좋은 함수를 리턴해주는 함수

- 라고 생각하시면 됩니다. 혹시 더 궁금하시다면, 제가 예전에 쓴 [python-basic) Decorator in python](https://frhyme.github.io/python-basic/python-basic)-Python_decorator/)를 참고하시면 좋습니다 하하핳

- 아무튼, 여기서는 decorator의 개념들보다, [python3에 기본적으롷 설치되어 있는 built-in decorator들에 대해서 알아보려고 합니다](http://buildingskills.itmaybeahack.com/book/python-2.6/html/p03/p03c06_decorators.html#objects-decorators-available). 

## staticmethod

> The `@staticmethod` decorator modifies a method function so that it does not use any self variable.

- self를 사용하지 않는다, 즉 instance를 참조하지 않는 객체 내에 존재하는 method입니다. 
- 이후에 class method와 헷갈릴 수 있는데, 아주 간단하게 어떤 method가 `@staticmethod` 데코레이터와 함께 사용되었다면, 해당 메소드의 경우는 함수 자체가 클래스 내부에 존재하기는 하지만, 클래스도, 클래스 인스턴스와도 전혀 관계 없다고 생각하시면 됩니다. 
- 외부에서 해당 코드를 그대로 함수로 정의해도 문제가 되지 않는다는 말입니다. 그냥 뭐 **name space를 구분하기 위해서 내부에 있다**, 라고 생각해도 문제가 없습니다. 

## classmethod 

> The `@classmethod` decorator modifies a method function so that it receives the class object as the first parameter instead of an instance of the class. This method function wil have access to the class object itself.

- self를 이용해서 instance에 접근할 수 있는 권한을 받는게 아니라, class object에 직접 접근할 수 있는 권한을 받는다. 
- 즉, staticmethod와 매우 유사하게 보이지만, 이 데코레이터는 해당 메소드를 클래스 메소드화 시킵니다. 

### staic vs. class method 

- 우선 staticmethod와의 공통점이라면 **class object**가 없어도 해당 메소드가 수행될 수 있다는 것이고. 
- 차이점이라면, class 내부의 변수들에 대해서 접근할 수 있다는 말이겠죠. 

- 정확하게는 [이 포스트](https://www.programiz.com/python-programming/methods/built-in/classmethod)에서 그 차이를 명확하게 알수 있는데요. 
  - class method의 경우 class를 참조할 수 있으므로(`cls`의 형태로) 특히 상속될 때 해당 class의 특성에 따라서 해당 객체가 속한 클래스의 특성을 자동으로 이용할 수 있는 반면
  - static method의 경우는 해당 메소드가 수행될 때 해당 메소드가 어떤 클래스에서 콜되었는지를 파악할 수 없죠. 

- 따라서, 해당 메소드가 어떤 클래스에서 불러지느냐에 따라서 달라질 수 있다면 `@classmethod`를 사용하고, 
- 어떤 클래스에서 불러져도 아무 상관이 없다면, `@staticmethod`를 사용합니다. 

### example 

- 더 헷갈리기 전에 코드를 통해 비교해봅시다. 간단하게 정리하자면 
  - decorator는 여러 개를 동시에 씌울 수도 있고
  - `@classmethod`의 경우 `cls`를 통해 class attribute에 접근하고 
  - `@staticmethod`의 경우 `cls`, `self`를 argument로 받지 못하며, 억지로 받을 경우 에러가 발생한다. 
- 정도로 정리되겠네요. 

```python
class AAA(object):
    cls_count = 0 ## class variable 
    def __init__(self, name):
        AAA.cls_count+=1
        self.name = name
        print(f"{AAA.cls_count:2d} class generated")
    @classmethod## classmethod
    def print_class_count(cls):
        print(f"There are {cls.cls_count} class instance")
    @staticmethod
    @functools.lru_cache(25)## 이렇게 여러개 decorator를 동시에 사용할 수도 있음. 
    def print_fibonacci(n):
        def fibonacci(n):
            if n==1 or n==2:
                return 1
            else:
                return fibonacci(n-2) + fibonacci(n-1)
        print(f"fibonacci number of {n}: {fibonacci(n)}")
    @staticmethod
    def print_class_count_static(cls):
        ## staticmethod이므로 class parameter에 접근할 수 없음, 따라서 실행하면 에러 
        print(AAA.cls_count)

## class instance가 있기 전에도 static/class method는 사용되어질 수 있음. 
AAA.print_class_count()
AAA.print_fibonacci(30)## 진짜 뜬금없는 
for i in range(0, 3):
    AAA(f"n{i}")
AAA.print_class_count_static()
```

```plaintext
There are 0 class instance
fibonacci number of 30: 832040
 1 class generated
 2 class generated
 3 class generated
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-391-24c6c8b0efdf> in <module>()
     27 for i in range(0, 3):
     28     AAA(f"n{i}")
---> 29 AAA.print_class_count_static()

TypeError: print_class_count_static() missing 1 required positional argument: 'cls'
```

## property 

### attribute depends on `__init__`

- 다음과 같이 `Student`라는 class가 있다고 해봅시다. 또 해당 class는 `__init__`에서 `name`, `marks`라는 두 가지 argument를 전달받고, `__init__`메소드 내에서 새로운 변수인 `gotmarks`를 생성해주죠. 
- 그러나, 새롭게 만들어진 attribute는 다시 name, marks가 바뀌었다고 해서 얘도 바뀌지는 않습니다. 

```python
## 경우에 따라서, __init__를 이용할 때 몇가지 argument를 넘기고, 다시 새로운 argument를 만들어주는 경우들이 있습니다. 
## 아래에서는 name, marks를 argument로 받고, 그걸 이용해서 gotmarks라는 새로운 변수를 만들어주죠. 

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.gotmarks = self.name + ' obtained ' + self.marks + ' marks'


st = Student("frhyme", "33")

print(st.name)
print(st.marks)
print(st.gotmarks)
print("="*20)
## gotmarks는 name, marks에 의해 생성된 attribute인데 ㅏ나만 바뀐다고 다른 property도 바뀌지는 않음. 
st.name = "freerhein" 
print(st.name)
print(st.marks)
print(st.gotmarks)

```

```plaintext
frhyme
33
frhyme obtained 33 marks
====================
freerhein
33
frhyme obtained 33 marks
```

### attribute as method

- 따라서, attribute로 만들지 않고, 메소드로 만드는 것도 하나의 방법입니다. 다음처럼, 실행될때마다 메소드로 세팅해서 저장해둘 수 있죠. 
- 단 이 경우에는 해당 attribute를 콜할 때, 뒤에 `()`가 들어갑니다. 사소하지만 저는 별로라고 생각해요. 

```python
## 아래처럼 값을 저장하지 않고, 함수로 만들어서 필요할 때 직접 생성하는 형태로 수행할 수도 있습니다. 
## 그런데, 이 경우에는 attribute가 있는게 아니라 함수잖아요, 좀 별로네요. 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        # self.gotmarks = self.name + ' obtained ' + self.marks + ' marks'

    def gotmarks(self):
        return self.name + ' obtained ' + self.marks + ' marks'

st = Student("frhyme", "33")

print(st.name)
print(st.marks)
print(st.gotmarks())
print("="*20)
st.name = "freerhein" 
print(st.name)
print(st.marks)
print(st.gotmarks())
```

```plaintext
frhyme
33
frhyme obtained 33 marks
====================
freerhein
33
freerhein obtained 33 marks
```

### using Property 

- 자 이제 아래처럼 `@property` 데코레이터를 써주면 됩니다. 그냥 메소드를 정의해주고, 앞에 @property를 붙여주면, `()`없이도 해당 값을 잘 부를 수 있습니다. 
- 또한 다른 attribute를 바꾸면 알아서 잘 바뀌고요. 
- 추가로, 방식은 ()없이 사용해서 attribute처럼 값을 어딘가에 저장해두고, 관련된 변수들이 업데이트될때만 값을 자동으로 업데이트하는, 그런 방식으로 바뀐다고 생각하실 수 있는데, **그렇지 않습니다**. 
  - 그냥 메소드로 선언하는 것과 비슷하고, 계산속도도 `@property`를 붙이거나, 붙이지 않거나 큰 차이가 없습니다. 

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        # self.gotmarks = self.name + ' obtained ' + self.marks + ' marks'

    @property #똑같이 메소드를 정의해주고, 여기 앞에 @property를 붙여주면 됨미다. 
    def gotmarks(self):#
        return self.name + ' obtained ' + self.marks + ' marks'


st = Student("frhyme", "33")
print(st.name)
print(st.marks)
print(st.gotmarks)## 함수인데, 마치 attribute인 것처럼 접근할 수 있음. 
print("##################")
st.name = "freerhein" ##바뀌어도 알아서 잘 바뀜. 
print(st.name)
print(st.marks)
print(st.gotmarks)
print("##################")

## 그러나, assignment에 대해서는 따로 정의되어 있지 않으므로 에러가 발생함. 
st.gotmarks = 'Golam obtained 36'

```

```plaintext
frhyme
33
frhyme obtained 33 marks
##################
freerhein
33
freerhein obtained 33 marks
##################
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-437-3f566499f91e> in <module>()
     21 print("##################")
     22 
---> 23 st.gotmarks = 'Golam obtained 36'

AttributeError: can't set attribute
```

- 또한 코드의 마지막 부분을 보시면, `AttributeError: can't set attribute`라는 에러가 발생한 것을 알 수 있습니다. 이는 `gotmarks`가 마치 attribute인 것처럼 사용되고 있기는 하지만, setter 함수가 적용되지 않았다는 것을 말해주고 있는 것이죠. 
- 따라서, `@gotmarks.setter`를 이용해서 setter 함수를 만들어줍니다. 그냥 함수명은 똑같이 세팅하고, 앞에 `@gotmarks.setter` 데코레이터만 붙여주면 단순히 `=`만으로 해당 attribute값읇 변경할 수 있습니다. 정확히는, `=`만으로 내부 변수를 마음대로 조절할 수 있다는 이야기죠. 
  - 여기에서는 어차피 `gotmarks`가 name과 marks의 조합이므로, 이 조합을 입력받아서 알아서 쪼개고 이를 나누어 내부 attribute에 재할당해주는 방식으로 사용하고 있습니다. 

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        # self.gotmarks = self.name + ' obtained ' + self.marks + ' marks'

    @property ##이건 기본적으로 getter
    def gotmarks(self):
        return self.name + ' obtained ' + self.marks + ' marks'
    ## 이건 setter, assignment로 값을 변경하고 싶을 때. 
    
    @gotmarks.setter
    def gotmarks(self, sentence):
        name, rand, marks = sentence.split(' ')
        self.name = name
        self.marks = marks


st = Student("frhyme", "25")
print(st.name)
print(st.marks)
print(st.gotmarks)## 함수인데, 마치 attribute인 것처럼 접근할 수 있음. 
print("##################")
st.name = "freerhein" ##바뀌어도 알아서 잘 바뀜. 
print(st.name)
print(st.gotmarks)
print("##################")
st.gotmarks = 'frhyme obtained 1000'
print(st.gotmarks)
print(st.name)
print(st.marks)
```

```plaintext
frhyme
25
frhyme obtained 25 marks
##################
freerhein
freerhein obtained 25 marks
##################
frhyme obtained 1000 marks
frhyme
1000
```

## wrap-up

- `@staticmethod`와 `@classmethod`의 차이점을 다시 명확하게 알게 되었다는 것이 작은 소득이고, 
- 그전에는 몰랐던 `@property`를 그래도 좀 정확하게 이해하게 되었다는 점이 또 하나의 소득입니다. 
- 물론 제가 사용할 줄은 아는데, 이게 왜 나왔는지, 어떤 이유로 나왔는지에 대해서 명확하게 이해하고 있는지에 대해서는 약간 혼란스럽군요 하하하핫. 

## reference

- [journaldev - python property decoratr](https://www.journaldev.com/14893/python-property-decorator)
- [programiz - python programming - property](https://www.programiz.com/python-programming/property)
