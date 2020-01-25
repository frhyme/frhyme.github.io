---
title: latine alphabet 지우기.
category: python-libs
tags: python python-libs string unicodedata string
---

## intro

- 저는 키워드를 분석하는 작업을 많이 하는데, 키워드, 즉 문자열에 '라틴 알파벳'이 등장하는 경우들이 있습니다. 
- 아래 그림에서처럼 액센트도 있고, 합니다. 

![](https://www.omniglot.com/images/writing/latin_accents.gif)

- 이걸 다 삭제하고 싶어서 찾아보니, [이미 스택오버플로우에 비슷한 질문이 있습니다](https://stackoverflow.com/questions/4512590/latin-to-english-alphabet-hashing). 

- 해봅시다. 

## 라틴 문자 지우기 

- 아래 코드가 약간 복잡해보일 수도 있지만, 설명하면 다음과 같습니다. 

- 텍스트를 정규화함: 텍스트를 정규화하여 분해하면, 각각의 캐릭터들을 분리할 수 있음
    - ﬁ 처럼 캐릭터가 합쳐져 있는 경우, f, i로 분해 
    - 엑센트+캐릭터인 경우 엑센트와 캐릭터로 분해 
- 분해된 텍스트에서 필요없는 카테고리에 속한 캐릭터를 삭제
- 텍스트 생성 

```python
import unicodedata 

target_text = 'ﬁ áé nnn íñóúü'
# 캐릭터들을 각각 출력해보면, 아래처럼 엑센트가 포함되어 있는 것을 알 수 있다. 
print(f"characters in target text: {list(target_text)}")
for c in target_text:
    print(c, unicodedata.category(c)) # LU: Letter, upper case Ll: lower case

#unicodedata.normalize("NFKD", 'áéíñóúü')

"""
- 엄밀히 따지면, 액센트와 알파벳은 서로 다른 문자입니다. 
- 또한, ﬁ 처럼 두 문자가 합쳐져 있는 경우도 구분하는 것이 필요하죠. 
- 두 문자를 혼합하여 새로운 문자를 생성해냈다고 보는 편이 정확하죠. 
- 따라서, 이 두 문자를 분해하는 작업이 필요합니다. 
- 분해를 위해서 normalize를 사용합니다. 
"""
print("=="*20)
## 모두 분리된 것을 알 수 있습니다. 
NFKD_normalzed_text = unicodedata.normalize("NFKD", target_text)
print(f"characters in normalized target text: {list(NFKD_normalzed_text)}")
## 각 캐릭터의 카테고리를 보면 엑센트의 카테고리는 'Mn'인 것을 알 수 있습니다. Mn은 Mark, no spacing 의미라고 하네요. 
for c in NFKD_normalzed_text:
    print(c, unicodedata.category(c))

## 그럼 이제 Mn인 것만 제외하면 되지 않을까요? 
remove_latin_text = "".join(
    [c for c in list(NFKD_normalzed_text) if unicodedata.category(c) != 'Mn']
)
print("=="*20)
print(remove_latin_text)
print("=="*20)
```

## wrap-up

- 처음에는 조금 복잡하다고 생각했는데, 써보니까 그렇게 막 복잡하지는 않군요 하하핫.

## reference 

- <https://stackoverflow.com/questions/4512590/latin-to-english-alphabet-hashing>
- <https://docs.python.org/2/library/unicodedata.html#unicodedata.normalize>