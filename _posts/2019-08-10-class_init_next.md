---
title: python class에서 next, iter
category: python-basic
tags: python class iterator
---

## iter, next

- 간단하게 iter, next 메소드를 클래스에서 정의하는 방법과 그 필요성을 알아봅니다. 
- iterator는 쉽게, 순차적으로 연결되어 있는 값을 의미합니다. 흔히들 리스트처럼 만들어줄때 많이 쓰게 되는데, 저는 기껏 클래스로 잘 정의한 객체를 list로 다시 만들기 위해서 일일이 지정하거나, 아니면 클래스로 만들지도 않고, 리스트로 만들어서 처리하거나 하는 일들이 많았습니다. 
- 즉, 클래스를 사용해서 iterator로 간단히 말하면, `list()`의 형태로 쉽게 변환하려면 메소드만 하나 추가로 정의해주면 됩니다. 

## let's do it. 

```python
class TEMP(object):
    def __init__(self, num_lst):
        self.num_lst = num_lst
        self.i = 0
    def __iter__(self):
        # __iter__ 메소드는 해당 클래스가 리스트 등으로 불러졌을때, 이게 어떤 값을 리턴할지를 의미함
        # 따라서, 값을 만들고 해당 리스트를 iter로 감싸고 리턴함. 
        # 즉 안에서 유지되는 값을 iter로 묶어서 내보내면 됨. 
        return iter(self.num_lst)
    def __next__(self):
        """
        - next는 한번에 값을 다 불러서 리턴하는 것이 아니고, 하나씩 순차적으로 읽어야 함. 
        - 이 과정에서 지금 어디까지 일힌 것인지를 파악하는 index value가 필요함. 이 값이 self.i임. 
        - 또한 그 값이 일정 이상 커지면, StopIteration이라는 예외를 발생시켜야 함.
        """
        if self.i<len(self.num_lst):
            temp = self.num_lst[self.i]
            self.i+=1
            return temp
        else:
            raise StopIteration
a = TEMP([1, 2, 3, 4, 5])

print(list(a)) # by __iter__ method
for x in a: # by __iter__ method
    print(x)
print("=="*20)
for i in range(0, 5): 
    print(next(a))
```

```
[1, 2, 3, 4, 5]
1
2
3
4
5
========================================
1
2
3
4
5
```

## wrap-up

- 매우 간단한 방법입니다. next보다는 iter가 더 유용할 것 같구요. 
