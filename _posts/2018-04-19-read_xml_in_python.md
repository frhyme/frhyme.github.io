# read xml in python

## intro

- 'python에서 xml을 어떻게 읽고 어떻게 처리하는가'를 정리해보려고 합니다. 
- 보통 csv, excel의 자료를 많이 처리하시는데, 웹에서 데이터를 가져오거나, 아니면 ERP와 같은 정보시스템에서 데이터를 가져와야 할때는 html, xml의 형태로 데이터를 가져올 때가 많습니다. 
    - html, xml이 다르기는 한데, 모두 ml, mark-up language이며 DOM(Document-oriented Model)로 표현되어 있습니다. 

- 말이 어려운데, 쉽게 표현하면, **문서의 개별 정보들이 계층적인 형태로, 태그로 표현되어 있다** 라고만 생각하셔도 상관없습니다. 
	- 더 간단하게는 그냥, 일반적인 파일구조의 형태로 담겨져 있다고...생각하셔도 일단은 상관없을 것 같네요. 
	- 다만, 개별 폴더명들이 임의로 주어져 있다면, markup language에서는 개별 요소들에 대해서 semantic을 부여합니다. 
		- 물론 많은 사람들이 이 semantic을 무시합니다만...

- 아래에 간단하게, xml의 형태를 만들고, 파이썬에 파일로 만들어두었습니다. 
- 개별 정보들이 계층적구조로 표현되어 있는데, 이런 형태를 DOM이라고 하고, html, xml이 이런 형태로 표현되어 있습니다. 

``` python
test_xml = """
<tag1>
    <tag2>
        <tag3 attr1='b'>
        Content1
        </tag3>
    </tag2>
    <tag2>
        <tag3 attr1='b'>
        Content2
        </tag3>
        <tag3 attr1='b'>
        Content3
        </tag3>
    </tag2>
    <tag2_1>
        <tag3 attr1='b'>
        Content3
        </tag3>
    </tag2_1>
</tag1>
"""
f = open("test_xml.xml", 'w')
f.write(test_xml)
f.close()
```


## xml to dictionary 

- 파일을 보니, 왠지, python에서의 dictionary와 유사하게 생기지 않았는지에 대한 생각이 들죠? 굉장히 간단하게는 markup language를 dictionary라고 생각하셔도 일단은 상관없을 것 같아요. 
- 그래서 일단은 xml을 딕셔너리로 변환하려고 합니다. 
- 위 문서의 구조는 대략 다음과 같습니다.
    - tag1
        - tag2
            - tag3
        - tag2
            - tag3
        - tag2_1
            - tag3
-  dictionary로 변환할 경우, 첫번째 key는 tag1 이 될텐데, 두번째 key들은 tag2, tag2, tag_2이 되어야 합니다. 
    - 단, 이 때, tag2는 중복되죠? 이 경우에는 tag2의 키 밑의 value가 list로 구성됩니다. 
    - 같은 위치에(계층적인 구조가 같은 경우를 의미합니다) 같은 tag가 여러개 있을 경우, 묶어서 하나의 tag 를 키로 가지는 원소에 list로 구성됩니다. 

#### code 

- 간단하기 `xmltodict.parse()`으로 해당 텍스트를 dictioanry로 변환할 수 있습니다. 
	- 다만, dictionary의 subclass인 `OrderDict`의 형태로 변환되는데, 이는 순서를 지키는 딕셔너리입니다. 
- 앞서 말씀드린 바와 같이, tag2의 경우는 여러 개 들어있기 때문에 value type이 list이고, tag1의 경우는 하나만 들어있기 때문에, OrderDict를 리턴하는 것을 알 수 있습니다. 

```python
import xmltodict
xmlD = xmltodict.parse(open("test_xml.xml", 'r').read())

print(type(xmlD['tag1']))
print(type(xmlD['tag1']['tag2']))
print(type(xmlD['tag1']['tag2_1']))
print(type(xmlD['tag1']['tag2'][1]['tag3']))
```
    
#### code result

```
<class 'collections.OrderedDict'>
<class 'list'>
<class 'collections.OrderedDict'>
<class 'list'>
```


- 간단하게 제대로 변환되었는지를 확인하는 함수를 만들었고, 다음의 결과처럼 제대로 들어가 있는 것을 알 수 있습니다. 
- 필요한 key 값에 인덱싱하여 값을 찾아서 정리하면 되겠네요. 

#### code 

```python
def DeepPrintDict(d, tab):
    if type(d) is list:
        for i, nested_d in enumerate(d):
            #print("{}element {}: {}".format(tab, i, nested_d))
            DeepPrintDict(nested_d, tab)
    elif type(d) is collections.OrderedDict:
        d_items = list(d.items())
        for k, v in d_items:
            if type(v) is collections.OrderedDict:
                print(tab+"key: {}".format(k))
                DeepPrintDict(v, tab+"    ")
            elif type(v) is list:
                print(tab+"key: {}".format(k))
                DeepPrintDict(v, tab+"    ")
            else:
                print(tab+"key: {}, value: {}".format(k, v))
    else:
        print()

DeepPrintDict(xmlD, "")
```


#### code result

```
key: tag1
    key: tag2
        key: tag3
            key: @attr1, value: b
            key: #text, value: Content1
        key: tag3
            key: @attr1, value: b
            key: #text, value: Content2
            key: @attr1, value: b
            key: #text, value: Content3
    key: tag2_1
        key: tag3
            key: @attr1, value: b
            key: #text, value: Content3
```


## html to dictionary?? 

- k,v 의 구조를 dictionary의 형태로 바꿔주는 아주 단순한 형태이기 때문에, xml의 형태를 가진 html에도 같은 방식으로 적용할 수 있다. 
	- 다만, html 데이터 분석을 잘하기 위해서라면, `xmldict` 보다는 `beautifulsoup`등이 훨씬 범용적이기 때문에, 다른 것들을 쓰는 편이 훨씬 좋다. 

#### code 

- file을 임의로 만들 필요가 없어서, string stream을 만들어줬다. 

```python
html_txt = """
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
"""

import io
output = io.StringIO()
output.write(html_txt)

xmlD = xmltodict.parse(output.getvalue())
DeepPrintDict(xmlD, "")
```

#### code result 

```
key: html
    key: head
        key: title, value: Page Title
    key: body
        key: h1, value: This is a Heading
        key: p, value: This is a paragraph.
```








