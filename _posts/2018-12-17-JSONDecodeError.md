---
title: JSONDecodeError를 처리합시다. 
category: python-libs
tags: python python-libs json jsondecodeerror UTF-8
---

## intro

- 요즘에는 csv보다 json을 이용해서 데이터를 전달받을 때가 더 많은 것 같습니다. 
- 다양한 이유가 있겠지만, 웹에서 데이터를 크롤링해서 가져올 때가 많기 때문이겠죠. 

## using json 

- 그냥 json을 이용해서 다음처럼 돌려버리면 될것 같은데, 잘 안됩니다. 
    - `CURRENT_WORKING_DIRECTORY`은 제가 정의한 폴더명입니다. 

```python
import json
json.loads(f"{CURRENT_WORKING_DIRECTORY}result_year_nation.json")
```

```
---------------------------------------------------------------------------
JSONDecodeError                           Traceback (most recent call last)
<ipython-input-15-4e52098b565d> in <module>()
----> 1 json.loads(f"{CURRENT_WORKING_DIRECTORY}result_year_nation.json")

/usr/lib/python3.6/json/__init__.py in loads(s, encoding, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook, **kw)
    352             parse_int is None and parse_float is None and
    353             parse_constant is None and object_pairs_hook is None and not kw):
--> 354         return _default_decoder.decode(s)
    355     if cls is None:
    356         cls = JSONDecoder

/usr/lib/python3.6/json/decoder.py in decode(self, s, _w)
    337 
    338         """
--> 339         obj, end = self.raw_decode(s, idx=_w(s, 0).end())
    340         end = _w(s, end).end()
    341         if end != len(s):

/usr/lib/python3.6/json/decoder.py in raw_decode(self, s, idx)
    355             obj, end = self.scan_once(s, idx)
    356         except StopIteration as err:
--> 357             raise JSONDecodeError("Expecting value", s, err.value) from None
    358         return obj, end

JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

- [스택오버플로우](https://stackoverflow.com/questions/16573332/jsondecodeerror-expecting-value-line-1-column-1-char-0)를 참고해보면 이 문제는 `json`이 UTF-8을 디폴트로 인식하기 때문이랍니다. 
- 따라서, UTF-8로 인코딩을 바꿔주면 해결됩니다. 

## solve it. 

- 다음처럼 json파일을 그냥 파일로 UTF-8로 읽은 다음 이걸 json으로 다시 읽어주면 됩니다. 

```python
f = open(f"{CURRENT_WORKING_DIRECTORY}result_year_nation.json", encoding="UTF-8")
raw_data = json.loads(f.read())
```

## reference 

- <https://stackoverflow.com/questions/16573332/jsondecodeerror-expecting-value-line-1-column-1-char-0>