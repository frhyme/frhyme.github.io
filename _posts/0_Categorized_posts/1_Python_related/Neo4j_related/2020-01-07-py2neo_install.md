---
title: py2neo를 설치해봅니다. 
category: python-libs
tags: database graphdb neo4j py2neo python python-libs
---

## install py2neo

- 요즘 neo4j의 graphacademy에서 제공하는 [data-science](https://neo4j.com/graphacademy/online-training/data-science/) 수업을 듣고 있습니다. 직접 py2neo등의 라이브러리를 로컬에 설치할 필요 없이, 그냥, jupyter notebook에서 설치해서 돌려볼 수 있어서 편한 부분이 있기도 합니다만.
- 동시에 jupyter notebook(정확히는 Google collaboratory)는 일정 시간이 지나면 꺼집니다. 그래서, 라이브러리들을 다시 설치해줘야 한다거나 하는 번거로움이 발생합니다. 
- 그러함에도 조금 미뤘던 것은, 약간 검색해본 결과, `py2neo`가 그다지 안정적이라고 생각되지는 않아서인데, 위에서 언급한 링크에서 py2neo를 실행할 때, 다음의 명령어를 사용하여 관련 라이브러리들을 실행해야 합니다. 라이브러리의 특정한 버전만을 설정하도록 하는 것이, 저에게는 약간 불안정한 라이브러리라고 생각하게 하는 것 같아요.

```python
!pip install py2neo==4.1.3 pandas matplotlib sklearn
```

- 아무튼간에 설치하기로 했으니까, 다음 명령어를 실행합니다. 

```plaintext
pip install py2neo 
```

- 의외로, 별 문제없이 그냥 실행이 됩니다.

## test it

- 간단하게 실행해서 잘 실행되는지를 확인해봅니다. 

```python
#!pip install py2neo==4.1.3 pandas matplotlib sklearn
from py2neo import Graph
import pandas as pd

# Change the line of code below to use the IP Address, Bolt Port, and Password of your Sandbox.
# graph = Graph("bolt://<IP Address>:<Bolt Port>", auth=("neo4j", "<Password>")) 
 
graph = Graph("bolt://18.207.236.58:35753", auth=("neo4j", "<password>"))

# finding popular authors

popular_authors_query = """
MATCH (author:Author)<-[rel:AUTHOR]-()
RETURN author.name AS authorName, count(rel) AS articlesPublished
ORDER BY articlesPublished DESC
LIMIT 10
"""
for k_v in graph.run(popular_authors_query).data():
    print(k_v)
print("=="*30)
```

- 아래와 같이 문제없이 잘 실행되는 군요. 

```plaintext
{'authorName': 'Peter G. Neumann', 'articlesPublished': 89}
{'authorName': 'Peter J. Denning', 'articlesPublished': 80}
{'authorName': 'Moshe Y. Vardi', 'articlesPublished': 72}
{'authorName': 'Pamela Samuelson', 'articlesPublished': 71}
{'authorName': 'Bart Preneel', 'articlesPublished': 65}
{'authorName': 'Vinton G. Cerf', 'articlesPublished': 56}
{'authorName': 'Barry W. Boehm', 'articlesPublished': 53}
{'authorName': 'Mark Guzdial', 'articlesPublished': 49}
{'authorName': 'Edwin R. Hancock', 'articlesPublished': 47}
{'authorName': 'Josef Kittler', 'articlesPublished': 46}
```
