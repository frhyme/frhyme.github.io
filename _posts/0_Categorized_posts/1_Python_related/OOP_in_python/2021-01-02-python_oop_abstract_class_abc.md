---
title: python - OOP - ABC(Abstract Base Class)
category: python-basic
tags: python python_basic, class OOP ABC inheritance
---

## python - OOP - ABC(Abstract Base Class)

- ABC(Abstract Base Class)는 "구현되지 않고, 선언만 되어 있는 method가 포함된 class"를 말합니다. 구현되어 있지 않고 선언만 되어 있다는 것은, 이 ABC를 상속받은 Child Class에서 해당 method를 정의해줘야 한다는 것을 말하죠. 또한, 새롭게 child class에서 정의하지 않는 한, ABC는 고유의 instance를 만들 수 없습니다.
- 이게, 무슨 의미가 있나? 싶지만, 코딩을 할 때 모든 class에서 동일하게 사용되는 interface를 ABC를 사용해서 구현하고 다른 class들에서 이 ABC를 모두 상속받도록 할 경우, 모든 class들이 한데 묶여서 관리됩니다. 만약, ABC에서 정의된 method가 상속받은 class에서 새롭게 정의되지 않았을 경우 에러를 발생하게 되죠.
- 다만, 저는 OOP를 제대로 사용하고 싶다면 그냥 java를 사용하는 게 낫지 않나...싶기는 합니다. 
- 아래는 간단히 Abstract Base Class `People`를 만들고, 애를 상속받는 `Engineer`를 만들고 메소드를 실행해본 예제입니다.

```python
from abc import ABC, abstractmethod

class People(ABC):
    # ABC를 상속하고
    def __init__(self, name):
        super().__init__()
        self.name = name

    # @abstractmethod decorator를 붙여줍니다.
    # 이를 통해 만약 해당 code가 구현되지 않았을 경우 error를 발생시키죠
    @abstractmethod
    def say_hello(self):
        ...

    # Abstract Base class의 모든 method가 미구현되는 것은 아닙니다.
    # `say_bye`처럼 구현되어 있는 method도 있죠.
    def say_bye(self):
        print("Bye, Bye, Bye")

class Engineer(People):
    def __init__(self, name, occupation):
        super().__init__(name)
        self.occupation = occupation

    # Abstract Base Class인 People, 
    # 즉 @abstractmethod 가 포함된 People을 상속받았으므로
    # say_hello를 구현해줘야 합니다.
    def say_hello(self):
        print(f"Hi, my name is {self.name}, I work as an {self.occupation}")

e1 = Engineer("frhyme", "engineer")

e1.say_hello()
# Hi, my name is frhyme, I work as engineer
e1.say_bye()
# Bye, Bye, Bye
```
