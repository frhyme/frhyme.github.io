---
title: json에 줄바꿈 등의 문자가 있는 경우 
category: python-libs
tags: python-libs python json string
---

## json 형식의 파일에서는 스트링 내에 줄바꿈이나 탭이 있으면 안됩니다. 

- 되게 간단한 것이기는 한데, 예를 들어서, json 파일이 다음처럼 되어 있다고 해봅시다. 

```json
{
    "a":"b\n\n\t", 
    "c":"d"
}
```

- 문자열 내에 탭이나, 줄바꿈이 있는게 이상한건 아닌데, 여기서 아래와 같은 오류가 발생합니다. control character가 유효하지 않다는 것이죠. 
- [control character](https://en.wikipedia.org/wiki/Control_character)는 한글로 변환하면 '제어문자'를 말하고, 데이터 전송시에 필요한 뭔가를 처리한다고 하는데, 그냥 여기까지 알 필요는 없을 것 같아요. 의미적으로는 json을 전송할때 사용하는 어떤 문자들이 값으로 존재해서 뭔가가 꼬인다는 이야기겠죠. 

```
json.decoder.JSONDecodeError: Invalid control character at: line 1 column 8 (char 7)
```

## how to fix it?

- 방법은 간단합니다. 그냥 `\n`를 `\\n`으로 바꾸어주면 됩니다. 
- 혹은, 그냥 무시하고 진행해도 되고요 호호

```python
raw_str = """{"a":"b
", "c":"d"}"""

#json_str = json_str.replace("\n", '\\n')
#json_str = json_str.replace("\t", '____ddd_____')
# way1: \n을 \\n으로 변경 
json_str = raw_str.replace("\n", '\\n').replace("\t", "\\t")
json_dict = json.loads(json_str)
print(json_dict)

#way2: 그냥 무시하고 진행
json_dict = json.loads(json_str, strict=False)
print(json_dict)

```

