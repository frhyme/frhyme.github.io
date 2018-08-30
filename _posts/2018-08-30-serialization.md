---
title: python - serialization
category: python-lib
tags: python python-lib serialization pickle json xml dictioanry yaml 
---

## serialization합시다. 

- Data Serialization은 구조화되어 있는 데이터(리스트, 딕셔너리, 객체 등)를 특정 포맷으로 밀어 넣는 것을 말합니다. 여기서 특정 포맷이란 XML, json, yml 등이 포함되구요. 
- 특히 서로 다른 api간에 통신을 할 경우에 해당 데이터를 현재 프로그램 내에서 관리되는 형태로 보내는 것이 아니라, 표준화된 형태로 보내는 것이 필요하고, 이를 data serialization을 통해 진행한다 라고 보시면 됩니다. 
- 이 포스트에서는 pickle, json, XML 등으로 serialization하는 기본적인 방법을 정리합니다. 

## data to serialize

- 클래스 인스턴스를 리스트로 묶은 컨테이너를 시리얼라이즈 할 계획입니다. 
- 코드는 대략 다음과 같습니다. 

```python
class A(object):
    def __init__(self, name, input_lst, input_dict):
        ## 이후 serialization을 편하게 하기 위해서는 
        ## __init__의 argument와 attribute name을 같에 가는 게 좋습니다. 
        self.name = name
        self.input_lst = input_lst.copy()
        self.input_dict = input_dict.copy()
    def __repr__(self):
        return self.name
As = [A("ID_{:0>2d}".format(i), [j for j in range(i, 20)], {chr(o):o for o in range(ord("A"), ord("A")+10)}) for i in range(0, 10)]
print(As)
```


## pickle

- [pickle](https://docs.python.org/3/library/pickle.html)은 python native data serialization module을 말합니다. 
- json과 비교했을때의 강점은, python에서 정의되는 거의 모든 데이터 타입에 대해서 serialization이 된다는 것인데요, 
- 예를 들어서 파이썬의 특정 콘테이너를 json으로 변환하려고 할 때 리스트의 원소가 클래스 인스턴스일 경우 바로 data serialization할 수 없습니다.
- 하지만 pickle은 serialization하려는 대상이 파이썬으로 만들어져 있기만 하다면, 함수 or 객체 or 리스트 등 대부분의 경우에 대해서 문제없이 serialization해줍니다. 
- 몇 가지 단점? 이라면 json의 경우 human-readable한 형태로 값을 생성하는 반면, pickle의 경우는 결과 값이 binary format이라서 읽을 수 없는 것이 있고 
- [Don't pickle your data](https://www.benfrederickson.com/dont-pickle-your-data/)에서는 속도가 매우 느리다는 것과, 함수등을 모두 pickling할 수 있기 때문에, 위험한 자료를 unpickling했을 때의 문제점 을 지적하고 있습니다. 매우 타당한 이야기죠. 
- 아무튼, 일단은 매우 유용하기 때문에, 혼자 예전에 코딩해놓은 것들을 불러오기도 편하고 해서 저는 개인적으로 쓰겠습니다. 

- `dump`와 `loads`로 가난하게 serialize, de-serialize 합니다. 

```python
As_pickled = pickle.dumps(As)
print(As_pickled)
print("="*50)
print(pickle.loads(As_pickled))
```

```
b'\x80\x03]q\x00(c__main__\nA\nq\x01)\x81q\x02}q\x03(X\x04\x00\x00\x00nameq\x04X\x05\x00\x00\x00ID_00q\x05X\t\x00\x00\x00input_lstq\x06]q\x07(K\x00K\x01K\x02K\x03K\x04K\x05K\x06K\x07K\x08K\tK\nK\x0bK\x0cK\rK\x0eK\x0fK\x10K\x11K\x12K\x13eX\n\x00\x00\x00input_dictq\x08}q\t(X\x01\x00\x00\x00Aq\nKAX\x01\x00\x00\x00Bq\x0bKBX\x01\x00\x00\x00Cq\x0cKCX\x01\x00\x00\x00Dq\rKDX\x01\x00\x00\x00Eq\x0eKEX\x01\x00\x00\x00Fq\x0fKFX\x01\x00\x00\x00Gq\x10KGX\x01\x00\x00\x00Hq\x11KHX\x01\x00\x00\x00Iq\x12KIX\x01\x00\x00\x00Jq\x13KJuubh\x01)\x81q\x14}q\x15(h\x04X\x05\x00\x00\x00ID_01q\x16h\x06]q\x17(K\x01K\x02K\x03K\x04K\x05K\x06K\x07K\x08K\tK\nK\x0bK\x0cK\rK\x0eK\x0fK\x10K\x11K\x12K\x13eh\x08}q\x18(h\nKAh\x0bKBh\x0cKCh\rKDh\x0eKEh\x0fKFh\x10KGh\x11KHh\x12KIh\x13KJuubh\x01)\x81q\x19}q\x1a(h\x04X\x05\x00\x00\x00ID_02q\x1bh\x06]q\x1c(K\x02K\x03K\x04K\x05K\x06K\x07K\x08K\tK\nK\x0bK\x0cK\rK\x0eK\x0fK\x10K\x11K\x12K\x13eh\x08}q\x1d(h\nKAh\x0bKBh\x0cKCh\rKDh\x0eKEh\x0fKFh\x10KGh\x11KHh\x12KIh\x13KJuubh\x01)\x81q\x1e}q\x1f(h\x04X\x05\x00\x00\x00ID_03q h\x06]q!(K\x03K\x04K\x05K\x06K\x07K\x08K\tK\nK\x0bK\x0cK\rK\x0eK\x0fK\x10K\x11K\x12K\x13eh\x08}q"(h\nKAh\x0bKBh\x0cKCh\rKDh\x0eKEh\x0fKFh\x10KGh\x11KHh\x12KIh\x13KJuubh\x01)\x81q#}q$(h\x04X\x05\x00\x00\x00ID_04q%h\x06]q&(K\x04K\x05K\x06K\x07K\x08K\tK\nK\x0bK\x0cK\rK\x0eK\x0fK\x10K\x11K\x12K\x13eh\x08}q\'(h\nKAh\x0bKBh\x0cKCh\rKDh\x0eKEh\x0fKFh\x10KGh\x11KHh\x12KIh\x13KJuubh\x01)\x81q(}q)(h\x04X\x05\x00\x00\x00ID_05q*h\x06]q+(K\x05K\x06K\x07K\x08K\tK\nK\x0bK\x0cK\rK\x0eK\x0fK\x10K\x11K\x12K\x13eh\x08}q,(h\nKAh\x0bKBh\x0cKCh\rKDh\x0eKEh\x0fKFh\x10KGh\x11KHh\x12KIh\x13KJuubh\x01)\x81q-}q.(h\x04X\x05\x00\x00\x00ID_06q/h\x06]q0(K\x06K\x07K\x08K\tK\nK\x0bK\x0cK\rK\x0eK\x0fK\x10K\x11K\x12K\x13eh\x08}q1(h\nKAh\x0bKBh\x0cKCh\rKDh\x0eKEh\x0fKFh\x10KGh\x11KHh\x12KIh\x13KJuubh\x01)\x81q2}q3(h\x04X\x05\x00\x00\x00ID_07q4h\x06]q5(K\x07K\x08K\tK\nK\x0bK\x0cK\rK\x0eK\x0fK\x10K\x11K\x12K\x13eh\x08}q6(h\nKAh\x0bKBh\x0cKCh\rKDh\x0eKEh\x0fKFh\x10KGh\x11KHh\x12KIh\x13KJuubh\x01)\x81q7}q8(h\x04X\x05\x00\x00\x00ID_08q9h\x06]q:(K\x08K\tK\nK\x0bK\x0cK\rK\x0eK\x0fK\x10K\x11K\x12K\x13eh\x08}q;(h\nKAh\x0bKBh\x0cKCh\rKDh\x0eKEh\x0fKFh\x10KGh\x11KHh\x12KIh\x13KJuubh\x01)\x81q<}q=(h\x04X\x05\x00\x00\x00ID_09q>h\x06]q?(K\tK\nK\x0bK\x0cK\rK\x0eK\x0fK\x10K\x11K\x12K\x13eh\x08}q@(h\nKAh\x0bKBh\x0cKCh\rKDh\x0eKEh\x0fKFh\x10KGh\x11KHh\x12KIh\x13KJuube.'
==================================================
[ID_00, ID_01, ID_02, ID_03, ID_04, ID_05, ID_06, ID_07, ID_08, ID_09]
```

## json 

- 이제 json으로 시리얼라이즈 하겠습니다. 
- json은 javascript object notation의 약자고, 웹에서 많이 사용되는 통신 포맷이죠. 

- 다만 피클과 다르게, 에러가 발생합니다. 이는, `A`라는 클래스 인스턴스가 serializable하지 않기 때문이죠. 

```python
import json 
json.dumps(As)
```

```
TypeError: Object of type 'A' is not JSON serializable
```

- 그래서 이때는 클래스 인스턴스를 통째로 넘겨주는 것이 아니라, `__dict__`메소드로 내부에 존재하는 값들만 딕셔너리로 변환하여 이를 시리얼라이즈해줍니다. 

```python
As_json = json.dumps([x.__dict__ for x in As])
print(As_json)
```

```
[{"name": "ID_00", "input_lst": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], "input_dict": {"A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71, "H": 72, "I": 73, "J": 74}}, {"name": "ID_01", "input_lst": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], "input_dict": {"A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71, "H": 72, "I": 73, "J": 74}}, {"name": "ID_02", "input_lst": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], "input_dict": {"A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71, "H": 72, "I": 73, "J": 74}}, {"name": "ID_03", "input_lst": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], "input_dict": {"A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71, "H": 72, "I": 73, "J": 74}}, {"name": "ID_04", "input_lst": [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], "input_dict": {"A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71, "H": 72, "I": 73, "J": 74}}, {"name": "ID_05", "input_lst": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], "input_dict": {"A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71, "H": 72, "I": 73, "J": 74}}, {"name": "ID_06", "input_lst": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], "input_dict": {"A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71, "H": 72, "I": 73, "J": 74}}, {"name": "ID_07", "input_lst": [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], "input_dict": {"A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71, "H": 72, "I": 73, "J": 74}}, {"name": "ID_08", "input_lst": [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], "input_dict": {"A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71, "H": 72, "I": 73, "J": 74}}, {"name": "ID_09", "input_lst": [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], "input_dict": {"A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71, "H": 72, "I": 73, "J": 74}}]
```

- 그럼 여기서 다시 json을 디시리얼라이즈할때는 딕셔너리가 읽힙니다. 읽은 딕셔너리를 다시 인스턴스를 생성하는 쪽으로 진행해야 합니다. 
    - 물론 이를 위해서는 해당 class의 `__init__` function에서 argument와 attribute의 변수 이름이 같아야 합니다. 
    - 다르면 약간의 전처리가 더 필요해지겠죠. 

```python
[A(**x) for x in json.loads(As_json)]
```

```
[ID_00, ID_01, ID_02, ID_03, ID_04, ID_05, ID_06, ID_07, ID_08, ID_09]
```


## xml 

- 이제 xml로 serializa하는 방법을 정리합니다. 이전에 보신 것처럼, 딕셔너리의 경우는 json으로 잘 변환이 되는데, xml로 변환할때는 몇 가지 문제점들이 있습니다. 
- 우선 간단한 딕셔너리를 xml로 변환하고 xml을 다시 dictionary로 변환해보겠습니다. 

```python
import dicttoxml
import xmltodict

a_dict = {"a":1, "b":2}
a_dict_xml = dicttoxml.dicttoxml(a_dict).decode('utf-8')
print(a_dict_xml)
print("="*20)

a_dict_xml_dict = xmltodict.parse(a_dict_xml)
print(a_dict_xml_dict)
```

- xml로 변환하는 건 그럭저럭 되는데, xml을 다시 딕셔너리로 변활할때는 두 가지 문제점이 발생합니다. 
    - dictionary로 변환되는 것이 아니라, OrderedDict로 변환되는 것
    - int를 제대로 인식하지 못하고, 모두 텍스트로 처리한다는 것 

```
<?xml version="1.0" encoding="UTF-8" ?><root><a type="int">1</a><b type="int">2</b></root>
====================
OrderedDict([('root', OrderedDict([('a', OrderedDict([('@type', 'int'), ('#text', '1')])), ('b', OrderedDict([('@type', 'int'), ('#text', '2')]))]))])
```

- 따라서 우선 dictionary를 OrderedDict로 변환해줍니다. 예전 파이썬에서는 딕셔너리가 순서를 고려하지 못했지만, 지금은 순서를 고려하고 있어서 아무 문제가 없습니다(처음에 들어온 순서가 고정됩니다). 

```python
def OD_to_dict(input_OD):
    ## from collections import OrderedDict required
    if type(input_OD)==OrderedDict:
        return {k: OD_to_dict(v) for k, v in input_OD.items()}
    elif type(input_OD)==list:
        return [OD_to_dict(x) for x in input_OD.copy()]
    else:
        return input_OD
print(OD_to_dict(a_dict_xml_dict))
```

- 다음처럼 변환해서 사용할 수 있습니다. 결과는 너무 길어서 제외했습니다. 

```python
import dicttoxml
import xmltodict

target_dict = json.loads(As_json) ##dictionary 
xml = dicttoxml.dicttoxml(target_dict)## dictionary를 xml로 변환 
xml = xml.decode('utf-8')## bytes를 스트링으로 변환 
OD_to_dict(xmltodict.parse(xml))

```

## YAML 

- json, xml 말고 다른 포맷은 없는지 찾아보다가 YAML이라는 것을 발견했습니다. 
- 보통 지킬에서 configuration이 어떤 식으로 되는지 정리하는 파일로 많이 쓰이죠. 
- xml과 비슷한데 훨씬 문법적으로 간소하고, human-readable하다는게 중요합니다. 

- 아무튼, 다음처럼 매우 간단하게 할 수 있어요. json, xml처럼 딕셔너리로 변환한다음 넣을 필요없이, 아래처럼 알아서 잘 가져오고 변환해줍니다. 

```python
import yaml 

As_yaml = yaml.dump(As)
print(As_yaml)
print("="*30)

As_yaml_load = yaml.load(As_yaml)
print(As_yaml_load)
```

```
- !!python/object:__main__.A
  input_dict: {A: 65, B: 66, C: 67, D: 68, E: 69, F: 70, G: 71, H: 72, I: 73, J: 74}
  input_lst: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
  name: ID_00
- !!python/object:__main__.A
  input_dict: {A: 65, B: 66, C: 67, D: 68, E: 69, F: 70, G: 71, H: 72, I: 73, J: 74}
  input_lst: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
  name: ID_01
- !!python/object:__main__.A
  input_dict: {A: 65, B: 66, C: 67, D: 68, E: 69, F: 70, G: 71, H: 72, I: 73, J: 74}
  input_lst: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
  name: ID_02
- !!python/object:__main__.A
  input_dict: {A: 65, B: 66, C: 67, D: 68, E: 69, F: 70, G: 71, H: 72, I: 73, J: 74}
  input_lst: [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
  name: ID_03
- !!python/object:__main__.A
  input_dict: {A: 65, B: 66, C: 67, D: 68, E: 69, F: 70, G: 71, H: 72, I: 73, J: 74}
  input_lst: [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
  name: ID_04
- !!python/object:__main__.A
  input_dict: {A: 65, B: 66, C: 67, D: 68, E: 69, F: 70, G: 71, H: 72, I: 73, J: 74}
  input_lst: [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
  name: ID_05
- !!python/object:__main__.A
  input_dict: {A: 65, B: 66, C: 67, D: 68, E: 69, F: 70, G: 71, H: 72, I: 73, J: 74}
  input_lst: [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
  name: ID_06
- !!python/object:__main__.A
  input_dict: {A: 65, B: 66, C: 67, D: 68, E: 69, F: 70, G: 71, H: 72, I: 73, J: 74}
  input_lst: [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
  name: ID_07
- !!python/object:__main__.A
  input_dict: {A: 65, B: 66, C: 67, D: 68, E: 69, F: 70, G: 71, H: 72, I: 73, J: 74}
  input_lst: [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
  name: ID_08
- !!python/object:__main__.A
  input_dict: {A: 65, B: 66, C: 67, D: 68, E: 69, F: 70, G: 71, H: 72, I: 73, J: 74}
  input_lst: [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
  name: ID_09

==============================
[ID_00, ID_01, ID_02, ID_03, ID_04, ID_05, ID_06, ID_07, ID_08, ID_09]
```


## wrap-up

- 필요하다면 json으로 변환하여 처리하는 것이 제일 좋은 것 같네요. 딕셔너리랑 호환이 매우 잘됩니다. 
- 단 pickle이 보안이 유지되는 방식으로 개선되면 좋겠네요. 
- 물론 지금 yaml만으로도 꽤 만족합니다. 