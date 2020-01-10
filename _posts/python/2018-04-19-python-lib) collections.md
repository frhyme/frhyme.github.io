---
title: python - data structure
category: python-basic
tags: python python-basic collections data-structure python-basic

---

## intro

- 예전에는 python의 다양하 자료구조를 잘 아는 것이 중요하다고 생각해서, 정리해두었는데, 한참 쓰다보니, 다 필요없고.
- 결국 back to basic인데, 기본인, list, dictionary, 그리고 pd.DataFrame이 가장 중요한 것 같습니다. 
  - `Counter`, `OrderDict`는 그래도 좀 유용한 편이죠. 
- 효율적인 데이터 처리, 데이터 관리를 위해서는 적절한 자료구조를 활용하는 것이 매우 중요함.
- 특히 "python은 느리다"는 편견 아닌 편견이 있는데, 많은 자료구조들은 이미 c와 유사항 정도의 상당히 빠른 연산 속도를 보장함.
- 따라서 적합한 자료구조를 잘 골라서 활용하는 것이 매우 중요함.

## Data Structure

- ***basic data structure(built-in)***
    - list
    - tuple
    - set
    - dictionary
- ***collections***
    - Counter
    - deque
    - ordered dictionary
    - named tuple
    - defaultdict
    - ChainMap
- ***bidict***
    - bidict

## basic data structure - list

`[value, value]`
- 어떤 오브젝트든 대충 마음대로 때려박고 빼는 정리되어 있지 않은 창고


```python
print(type([]))
lst1=["z", "a", "index", "index","b", "A","pop", "rem"]
lst1.pop(6)
# Remove the item at the given position in the list, and return it.
# If no index is specified, a.pop() removes and returns the last item in the list.
lst1.append("ap") # add an item to the end of the list
lst1.insert(1,"ins") # insert and item at a given position
print("lst1:", lst1)
print("index:", lst1.index("index"))
# return zero-baed index in the list of the first item whose value is x
print("count:", lst1.count("index")) #return the number of times x appears in the list
lst1.remove("rem")# equivalent to "del lst1[ lst1.index("rem") ]"
print("lst1:", lst1)
```

    <class 'list'>
    lst1: ['z', 'ins', 'a', 'index', 'index', 'b', 'A', 'rem', 'ap']
    index: 3
    count: 2
    lst1: ['z', 'ins', 'a', 'index', 'index', 'b', 'A', 'ap']


- 아마 대부분의 object가 그렇겠지만, "="을 이용해서는 같은 값을 가진 새로운 오브젝트를 생성해주지 못한다.
- 이 경우 shallow copy가 일어나서(대충 메모리 위치가 지정되는 개념) shallow copied object는 copying object와 같은 메모리를 공유하기 때문에 copying object가 변경되면 shallow copied object도 변경됨.
- 따라서 복사할 때는 반드시 ***copy method*** 를 사용할 것


```python
lst_by_copy = lst1.copy()
lst_by_assignment = lst1
lst1.clear() # remove all items, equivalent to "del lst1"
print("cleared_lst1:", lst1)
print("lst_by_copy:", lst_by_copy)
print("lst_by_assignment:", lst_by_assignment)
```

    cleared_lst1: []
    lst_by_copy: ['z', 'ins', 'a', 'index', 'index', 'b', 'A', 'ap']
    lst_by_assignment: []


### list - basic sorting method

- list는 sorted, sort method를 이용해서 소팅할 수 있음
- sorted: 소팅된 새로운 리스트를 생성하여 리턴하는 함수
- sort: 해당 리스트의 method로 해당 리스트 자체를 소팅.
- sorted, sorte 모두 key, reverse 를 argument로 각각 가짐


```python
lst1= ["index","a","A", "b","index", "z"]
print("source list:", lst1)
print("by sorted(upper):", sorted(lst1, key=str.upper))# return the sorted list
print("source list:", lst1)
lst1.sort(key=str.lower, reverse=True)# sort the items of the list
print("by sort method(lower):", lst1)
```

    source list: ['index', 'a', 'A', 'b', 'index', 'z']
    by sorted(upper): ['a', 'A', 'b', 'index', 'index', 'z']
    source list: ['index', 'a', 'A', 'b', 'index', 'z']
    by sort method(lower): ['z', 'index', 'index', 'b', 'a', 'A']



### list - advanced sorting method


```python
import random
num_lst = [ (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)) for i in range(1, 5)]
num_chr_lst = [ [random.randint(1, 10), chr(random.randint(ord("A"), ord("Z")))] for i in range(1, 5)]

print("num_lst", num_lst)
print("num_chr_lst:", num_chr_lst)

print()
print("sorted by sum :",  sorted(num_lst, key=sum) )
print("sorted by x[0] :", sorted(num_chr_lst, key=lambda x: x[0]) )
print("sorted by x[1] :", sorted(num_chr_lst, key=lambda x: x[1]) )

print()
print("num_chr_lst:", num_chr_lst)
num_chr_lst.sort(key = lambda x: x[0])
print("using sort method")
print("num_chr_lst:", num_chr_lst)
```

    num_lst [(8, 2, 3), (2, 4, 9), (7, 5, 2), (10, 10, 8)]
    num_chr_lst: [[2, 'T'], [2, 'M'], [6, 'Q'], [3, 'V']]

    sorted by sum : [(8, 2, 3), (7, 5, 2), (2, 4, 9), (10, 10, 8)]
    sorted by x[0] : [[2, 'T'], [2, 'M'], [3, 'V'], [6, 'Q']]
    sorted by x[1] : [[2, 'M'], [6, 'Q'], [2, 'T'], [3, 'V']]

    num_chr_lst: [[2, 'T'], [2, 'M'], [6, 'Q'], [3, 'V']]
    using sort method
    num_chr_lst: [[2, 'T'], [2, 'M'], [3, 'V'], [6, 'Q']]


## basic data structure - tuple

`(value, value)`
- ***simple immutable list***


```python
print(type(()))

lst1 = [1,2,3]
tup1 = tuple(lst1)
print(lst1, tup1)
del lst1[0]
print(lst1, tup1)
del tup1[0] # error
tup1.sort() # error
tup1[0]=2
```

    <class 'tuple'>
    [1, 2, 3] (1, 2, 3)
    [2, 3] (1, 2, 3)



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-10-1f37ebb578c1> in <module>()
          6 del lst1[0]
          7 print(lst1, tup1)
    ----> 8 del tup1[0] # error
          9 tup1.sort() # error
         10 tup1[0]=2


    TypeError: 'tuple' object doesn't support item deletion


## basic data structure - set

`{value, value, value}`
- ***unique unordered set***
- 순서가 유지되지 않고, 중복이 허용되지 않는 자료구조
- 나는 리스트에서 unique한 값을 보려고 할때 종종 사용


```python
lst1 = [1,1,1,1,2,2,3,4,5,6]
print(type({1,2,3}))
print("lst to set:", set(lst1))
print("union:", set(lst1).union([7,8]))
print("intersection:", set(lst1).intersection([1,2,3,10]))
print("difference:", set(lst1).difference([1,2,3,4]))
```

    <class 'set'>
    lst to set: {1, 2, 3, 4, 5, 6}
    union: {1, 2, 3, 4, 5, 6, 7, 8}
    intersection: {1, 2, 3}
    difference: {5, 6}


## basic data structure - dictionary

`{key:value, key:value}`
- (key, value) pair unordered list indexed by unique key
- item, keys(), values() 모두 integer position으로 접근할 수 없음.
    - 따라서, integer position으로 접근하려면 list로 변환하여 접근해야함
- 어떤 object도 key, value가 될 수 있음


```python
import datetime
dict1 = {"name":"original", "phone":123, "birth":datetime.date(1986, 11, 18)}
dict1[datetime.date(1986, 11, 18)]="birth"

for item in dict1.items():
    print(item)
print()
for k in dict1.keys():
    print("{}: {}".format(k, dict1[k]))
print()
print(dict1.keys())
print(list(dict1.keys())[0])
print( datetime.date(1986, 11, 18) in dict1 )
```

    ('name', 'original')
    ('phone', 123)
    (datetime.date(1986, 11, 18), 'birth')
    ('birth', datetime.date(1986, 11, 18))

    name: original
    phone: 123
    1986-11-18: birth
    birth: 1986-11-18

    dict_keys(['name', 'phone', datetime.date(1986, 11, 18), 'birth'])
    name
    True


- list와 마찬가지로, copy할 때는 copy method를 사용해야함


```python
dict2 = dict1 # assignment
print("original dict:", dict1)
dict_by_copy = dict1.copy()
dict_by_assignment = dict1
dict1.clear() # remove all items, equivalent to "del lst1"
print("cleared_dict1:", dict1)
print("dict_by_copy:", dict_by_copy)
print("dict_by_assignment:", dict_by_assignment)
```

    original dict: {'name': 'original', 'phone': 123, datetime.date(1986, 11, 18): 'birth', 'birth': datetime.date(1986, 11, 18)}
    cleared_dict1: {}
    dict_by_copy: {'name': 'original', 'phone': 123, datetime.date(1986, 11, 18): 'birth', 'birth': datetime.date(1986, 11, 18)}
    dict_by_assignment: {}

## collections - High performance container data types

- Counter
- deque
- ordered dictionary
- named tuple
- defaultdict


## collections.Counter

- dict subclass for counting hashable objects
-  리스트에 있는 값들을 셀 때 좋음


```python
import collections
target = ["a", "a", "a", "b", "b", "c", "f"]
target_cnt = collections.Counter(target)
print("target_cnt:", target_cnt)
print("count of b:", target_cnt["b"])
print("target_cnt.most_common():", target_cnt.most_common())
```

    target_cnt: Counter({'a': 3, 'b': 2, 'c': 1, 'f': 1})
    count of b: 2
    target_cnt.most_common(): [('a', 3), ('b', 2), ('c', 1), ('f', 1)]


## collections.deque

- list-like container with fast appends and pops on either end
- 양쪽으로 값을 넣고 뺄 수 있는 queue
- list와 유사하게 사용할 수 있지만, memory movement cost에서 차이가 발생
    - deque: O(1), list: O(n)


```python
import collections

print(dq)
dq.append("app") # add x to right side
dq.appendleft("app_lft") # add x to left side
dq.extend(["ex1", "ex2"]) # add Xs to right side
dq.extendleft(["exlft1", "exlft2"]) # add Xs to left side
print("both append, extend:", dq)
dq.pop() # takes no argument
dq.popleft() # takes no argument
print("pop, popleft:", dq)
dq.reverse()
print("after reverse:", dq)
dq.rotate(len(dq))# rotate clockwise, n steps to right
print("rotate(len(dq)):", dq)
dq.clear()
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-15-994441cf98e1> in <module>()
          1 import collections
          2
    ----> 3 print(dq)
          4 dq.append("app") # add x to right side
          5 dq.appendleft("app_lft") # add x to left side


    NameError: name 'dq' is not defined


## collections.OrderedDict

- dict subclass that remembers the order entries were added
- dictionary subclass 이며, 당연히 dictionary의 method를 모두 활용가능
- dictionary에 값이 넣어진 순서가 그대로 유지됨.
    - 하지만 integer position indexing이 불가한 건 똑같음


```python
import collections

dict1 = {chr(i):ord(chr(i))-64 for i in range(65, 70)}
dict_to_lst = [(key, dict1[key]) for key in dict1.keys()]
sorted_lst_by_key = sorted(dict_to_lst, key=lambda x: x[0])

ordict = collections.OrderedDict( sorted_lst_by_key )
print(dict1)
print(ordict)
ordict["F"]=6
ordict["G"]=7
print(ordict)
print("2nd item in ordict:", list(ordict.items())[2] )
```

    {'C': 3, 'D': 4, 'B': 2, 'E': 5, 'A': 1}
    OrderedDict([('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5)])
    OrderedDict([('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5), ('F', 6), ('G', 7)])
    2nd item in ordict: ('C', 3)


## collections.namedtuple

- ==factory function for creating tuple subclasses with named fields==
- simple profile, document(like json)과 같은 형태의 자료가 필요할 때, 만듬
- dictionary와 유사하고 변환도 쉽게 가능하지만, immutability 를 보장함.
    - OrderedDict로 변환됨
- 그리고 미묘하게 dictionary보다 쓰기 편함(bracket 이 없고, ""를 쓰지 않아도 되고 등)
    - object의 attribute처럼 사용
- 다만 dictionary의 경우 key를 object로 지정할 수 있었는데, namedtuple의 경우는 이것이 불가능함
- 하지만 이미 dictionary가 더 편하고, 더 많은 method가 있는 상황에서, 이 자료구조를 쓸 필요가 있는지는 의문.


```python
import collections
import datetime

Profile = collections.namedtuple("profile", ["name", "phone", "birth"])
# typename, fieldnames
p1 = Profile("shlee", "01074858611", datetime.date(1986, 11, 18))

print(type(p1))
print(p1._fields)
print(p1)
print(p1.name)
print(p1.phone)
print(p1.birth)

print()
dict1 = p1._asdict()
print(type(dict1))
print(dict1)
```

    <class '__main__.profile'>
    ('name', 'phone', 'birth')
    profile(name='shlee', phone='01074858611', birth=datetime.date(1986, 11, 18))
    shlee
    01074858611
    1986-11-18

    <class 'collections.OrderedDict'>
    OrderedDict([('name', 'shlee'), ('phone', '01074858611'), ('birth', datetime.date(1986, 11, 18))])


## collections.defaultdict

- dict subclass that calls a factory function to supply missing values
- basic dictionary는 key 값이 없으면 에러를 발생시킴.
- 그러나 defaulttdict는 key가 없을 경우 해당 key에 대한 값을 넘겨받은 함수(factory 함수)를 사용해서 만들어줌.
- default 를 지정해줄 수 있기 때문에 defaultdict


```python
dict1 = {"a":1, "b":2}
print(dict1["c"])
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-18-7a816c5c328d> in <module>()
          1 dict1 = {"a":1, "b":2}
    ----> 2 print(dict1["c"])


    KeyError: 'c'



```python
import collections
dd = collections.defaultdict(lambda :"default_value")
print("if key is not in defaultdict:", dd["a"] )
print("if key is not in defaultdict:", dd["b"] )
print(dd)
print(dict(dd))
print()

dd = collections.defaultdict(lambda : [])
print(dd)
lst1 = [("a", 1), ("a", 2), ("b", 2), ("b", 3), ("c", 3)]

for x in lst1:
    dd[x[0]].append(x[1])
print("by defaultdict:", dd.items())

# above is simpler than below
dict1 = {}
for x in lst1:
    if x[0] in dict1.keys():
        dict1[x[0]].append(x[1])
    else:
        dict1[x[0]]=[x[1]]
print("by list:", dict1)
```

    if key is not in defaultdict: default_value
    if key is not in defaultdict: default_value
    defaultdict(<function <lambda> at 0x00000244F2E5ED08>, {'a': 'default_value', 'b': 'default_value'})
    {'a': 'default_value', 'b': 'default_value'}

    defaultdict(<function <lambda> at 0x00000244F2E819D8>, {})
    by defaultdict: dict_items([('c', [3]), ('a', [1, 2]), ('b', [2, 3])])
    by list: {'c': [3], 'a': [1, 2], 'b': [2, 3]}

### make infinite dictionary??

- 심연까지 끝없이 뚫고 들어가는 dictionary를 만든다!!
- key가 없을 때, defaultdict를 가지는 defaultdict
- 이걸 어디에 쓸 수 있냐고? 그건 몰라....


```python
import collections
def print_inf_dict(levs, input_inf_dict):
# infinite dictionary를 print하기 위한 recursive func
    print( "level:{} - ".format(levs), input_inf_dict.keys() )
    for key in input_inf_dict.keys():
        print_inf_dict( levs+","+key, input_inf_dict[key] )
def inf_dict():
    return collections.defaultdict(inf_dict)
inf = inf_dict()
inf["a"]
inf["a"]["b"]
inf["a"]["b"]["c"]
inf["a"]["b"]["c"]["d0"]
inf["a"]["b"]["c"]["d1"]
inf["a"]["b"]["c"]["d2"]
inf["a"]["b"]["c"]["d3"]
inf["a"]["b"]["c"]["d4"]["e"]["f"]["g"]["h"]["i"]

print_inf_dict( "",inf )
```

    level: -  dict_keys(['a'])
    level:,a -  dict_keys(['b'])
    level:,a,b -  dict_keys(['c'])
    level:,a,b,c -  dict_keys(['d2', 'd0', 'd1', 'd4', 'd3'])
    level:,a,b,c,d2 -  dict_keys([])
    level:,a,b,c,d0 -  dict_keys([])
    level:,a,b,c,d1 -  dict_keys([])
    level:,a,b,c,d4 -  dict_keys(['e'])
    level:,a,b,c,d4,e -  dict_keys(['f'])
    level:,a,b,c,d4,e,f -  dict_keys(['g'])
    level:,a,b,c,d4,e,f,g -  dict_keys(['h'])
    level:,a,b,c,d4,e,f,g,h -  dict_keys(['i'])
    level:,a,b,c,d4,e,f,g,h,i -  dict_keys([])
    level:,a,b,c,d3 -  dict_keys([])


## collections.ChainMap

- dict-like class for creating a single view of multiple mappings
- managing dictionary sequence
- dictionary에 대한 버전관리 라고 생각하면 편함.
- 이걸 어디에 어떻게 활용할 수 있지??? :anguished:
    - 여러 가지 dictionary를 listf에 넣어서 관리하고, 각각의 리스트를 dictionary의 method를 이용해서 처리해도 비슷하게 처리할 수 있음.
    - 물론 조금 더 편하기는 한데, 이렇게 사용했을 때의 이점이 현재로서는 분명하게 보이지 않음.


```python
import collections

x_dict = {"weather":"hot", "temp":34}
y_dict = {"temp":27, "population":1000}
z_dict = {"humid":34}

cm1 = collections.ChainMap(x_dict)
cm2 = cm1.new_child(y_dict)
cm3 = cm2.new_child(z_dict)

print(cm1.maps)
print(cm2.maps)
print(cm3.maps)

print(list(cm1.items()))
print(list(cm2.items()))
print(list(cm3.items()))
print(cm3.parents == cm2)
print(cm2.parents == cm1)
```

    [{'weather': 'hot', 'temp': 34}]
    [{'population': 1000, 'temp': 27}, {'weather': 'hot', 'temp': 34}]
    [{'humid': 34}, {'population': 1000, 'temp': 27}, {'weather': 'hot', 'temp': 34}]
    [('weather', 'hot'), ('temp', 34)]
    [('weather', 'hot'), ('population', 1000), ('temp', 27)]
    [('weather', 'hot'), ('population', 1000), ('humid', 34), ('temp', 27)]
    True
    True



```python
x_dict = {"weather":"hot", "temp":34}
y_dict = {"temp":27, "population":1000}
z_dict = {"humid":34}
x_dict.update(y_dict)
print(x_dict)
```

    {'weather': 'hot', 'population': 1000, 'temp': 27}


## bidict.bidict

- dictionary를 쓰다보면, key => value가 아니라, value => key를 찾아야 할 때가 발생함.
- bidict는 그러한 경우 유용함.
- 그러나, 따라서, bidict는 key, value 모두 unique해야 함.


```python
from bidict import bidict
bdct1 = bidict({"a":1, "b":2, "c":3})
print("bdct1['a']:", bdct1["a"])
print("bdct1.inv[1]:", bdct1.inv[1]) #inverse
```

    bdct1['a']: 1
    bdct1.inv[1]: a


## Reference

- https://docs.python.org/3/library/collections.html#collections.ChainMap
- http://www.webpagefx.com/tools/emoji-cheat-sheet/
