---
title: jupyter notebook에서  import ipynb
category: other
tags: jupyter-notebook python not-yet

---

## does it possible to import .ipynb 

- 일반적으로는 `.py`파일을 다른 `.py` 파일에서 `import` 하는 것은 매우 쉽고 간단하다. 그냥 파일 내부에서 경로만 제대로 하여 `import filename` 해주면 끝임. 만약 사람들이 대부분 `.py` 파일을 만든다면 아무 문제가 없으나, 여기서 문제는 많은 사람들이 `jupyter notebook`으로 작업을 하기 때문에, `.py` 파일이 아니라 .ipynb 파일이 남는다는데 문제가 있다. 
    - 물론 .ipynb 파일을 .py 파일로 변경하는 것은 어렵지 않음. 그러나 매번 변경은 ipynb에서 하는데 할때마다 다시 converting하여 저장하는 식으로 하면 version control 이 어려워질 수 있음
- 따라서 여기서는 다른 `.ipynb`, `.py` 파일에서 `.ipynb`파일을 import 하는 방법을 알아보려고 합니다

## `.ipynb`의 구조 

- 먼저, `.ipynb`의 구조를 파악하는 것이 중요하지 않을까 싶어요. 
- 해당 파일은 딕셔너리의 형태로 구성되어 있습니다(혹은 json). 대략 다음의 형태이며, 코드만 가져오고 싶다면, "cell_type"이 "code"인 부분만 가져오면 됩니다. 다만, 내부는 줄별로 줄바꿈이 되어 있으므로 이를 고려해서 합치면 될것 같네요. 음 `ipynb`파일을 `.py`파일로 바꾸는 건 그렇게 어려운 문제가 아닐것 같아요. 일단 제 생각에는 그렇습니다


```
{
    "cells":[
        {
            "cell_type": "markdown", 
            "source":[
                "## 1st session - alpha algorithm\n",
                "\n",
            ]
        },
        {
            "cell_type":"code", 
            "source":[
                "def return_P_L(input_log):\n",
                "    T_L, T_I, T_O = return_transitions(input_log)\n",
                "    Y_L = return_Y_L(input_log)\n",
            ]
        }
    ]
    "metadata": {
    }
}
```

- 즉 `string`으로 된 python code는 `exec()`를 활용해서 쉽게 내부에서 빌드할 수 있기 때문에, `ipynb`파일에서 내가 원하는 특정 cell의 코드만 찾으면 그를 스트링으로 넘겨서 실행하면 깔끔한 것 같아요. 
- 따라서 `ipynb` 파일을 스트링으로 읽어들이면 끝나는 것 같습니다. 가능하면, 딕셔너리나, 아무튼 다른 형태로 읽어들이면 더 이쁠것 같긴 한데요. 

## solve it. 

- 그래서 `sample_ipynb_to_import.ipynb`라는 파일을 sample로 만들고, 이를 json로 변환시켰다. 해당 파일 소스는 본 포스트 끝부분에 넣어두었다. 
- 파일 스트림 생성 => json을 활용하여 스트링을 딕셔너리로 변환 => 딕셔너리에서 코드 부분만 읽어서 다시 스트링으로 병합 => `exec`로 빌드 로 진행하면 됩니다. 아래 코드를 보시면 됩니다. 


```python
import json
k = json.load(open("sample_ipynb_to_import.ipynb", 'r', encoding='utf-8'))
all_code_lst =[]
for cell in k['cells']:
    if cell['cell_type']=='code':
        all_code_lst.append("".join(cell['source']))
all_code = "\n".join(all_code_lst)
exec(all_code)
```

- 이렇게 하고 나면 해당 쥬피터 노트북 안에서 다른 ipynb에서 선언된 함수와 변수들을 사용할 수있습니다. 

```python
print(len(test_log))
print(return_unique_activities(test_log))
```
```
7000
['a', 'b', 'e', 'f', 'c', 'd']
```

- 단 magic command 를 썼을 경우에는 코드를 빌드 시킬때 문제가 될 수 있다. 예를 들어서 `%matplotlib inline`와 같은 커맨드가 셀 내부에 있을 경우에는 `syntax error`가 발생한다.

## appendix

### `sample_ipynb_to_import.ipynb`

```
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "log5 = [['a', 'b', 'e', 'f']]*2 + [['a', 'b', 'e', 'c', 'd', 'b', 'f']]*3 + [['a', 'b', 'c', 'e', 'd', 'b', 'f']]*2\n",
    "log5 += [['a', 'b', 'c', 'd', 'e', 'b', 'f']]*4 + [['a', 'e', 'b', 'c', 'd', 'b', 'f']]*3\n",
    "\n",
    "test_log = log5*500\n",
    "\n",
    "def return_unique_activities(input_log):\n",
    "    uniq_act = []\n",
    "    for trace in input_log:\n",
    "        for act in trace:\n",
    "            if act in uniq_act:\n",
    "                continue\n",
    "            else:\n",
    "                uniq_act.append(act)\n",
    "    return uniq_act"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
```

## reference 

- [여기](http://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Importing%20Notebooks.html)서는 저와 다른 방식으로 `ipynb`를 객체로 읽어들여서 모듈로 실행하는 방식으로 진행햇습니다. 약간, 이해가 잘 안되어서 저는 그냥 넘어갔습니다. 나중에 다시 보고 이해되면 추가하겠습니다. 
