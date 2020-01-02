---
title: html 내에 코드 embed하기.
category: others
tags: html code embeded 
---

## code

- 간단한 파이썬 코드, 혹은 json 등을 html에 콘텐츠로 표시하려고 합니다. 
- 현재 사용하고 있는 블로그에서는 비교적 간단하게, 할 수 있는 반면 html에서는 제가 직접 해본적이 없더라구요. 

## pre and code 

- 우선 위 두 태그의 개념을 알면 좋습니다. 
- [code](https://www.w3schools.com/tags/tag_code.asp) 태그의 경우 해당 태그가 컴퓨터 코드임을 의미하면 태그이고, 
- [pre](https://www.w3schools.com/tags/tag_pre.asp) 태그는 preformatted text의 약자로, 해당 태그 내에 들어가 있는 문자들은 줄바꿈, 스페이스 등을 무시하지 않는다는 것을 의미합니다.
- 예를 들면 다음과 같습니다. 

```html 
<pre>
import pandas as pd
import networkx as nx
def temp_func():
    return ""
</pre>
<code>
import pandas as pd
import networkx as nx
def temp_func():
    return ""
</code>
```
- 아래에서 보는 것처럼, `pre`태그는 기존의 줄바꿈, 들여쓰기등을 모두 인식하는 반면, `code`태그에서는 이 부분이 반영되어 있지 않습니다. 

<pre>
import pandas as pd
import networkx as nx
def temp_func():
    return ""
</pre>
<code>
import pandas as pd
import networkx as nx
def temp_func():
    return ""
</code>


## wrap-up

- 간단하게, `pre` 태그 내에 `code` 태그를 쓰는 방향으로 진행하는 것이 좋을 것 같네요.