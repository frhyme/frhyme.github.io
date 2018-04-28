---
title: jupyter notebook에서  import ipynb
category: other
tags: jupyter-notebook python 

---

## does it possible to import .ipynb 

- 일반적으로는 `.py`파일을 다른 `.py` 파일에서 `import` 하는 것은 매우 쉽고 간단하다. 그냥 파일 내부에서 경로만 제대로 하여 `import filename` 해주면 끝임. 만약 사람들이 대부분 `.py` 파일을 만든다면 아무 문제가 없으나, 여기서 문제는 많은 사람들이 `jupyter notebook`으로 작업을 하기 때문에, `.py` 파일이 아니라 .ipynb 파일이 남는다는데 문제가 있다. 
    - 물론 .ipynb 파일을 .py 파일로 변경하는 것은 어렵지 않음. 그러나 매번 변경은 ipynb에서 하는데 할때마다 다시 converting하여 저장하는 식으로 하면 version control 이 어려워질 수 있음
- 따라서 여기서는 다른 `.ipynb`, `.py` 파일에서 `.ipynb`파일을 import 하는 방법을 알아보려고 합니다

## `.ipynb`의 구조 

- 먼저, `.ipynb`의 구조를 파악하는 것이 중요하지 않을까 싶어요. 
- 해당 파일은 딕셔너리의 형태로 구성되어 있습니다(혹은 json). 대략 다음의 형태이며, 코드만 가져오고 싶다면, "cell_type"이 "code"인 부분만 가져오면 됩니다. 다만, 내부는 줄별로 줄바꿈이 되어 있으므로 이를 고려해서 합치면 될것 같네요. 음 `ipynb`파일을 `.py`파일로 바꾸는 건 그렇게 어려운 문제가 아닐것 같아요. 일단 제 생각에는 그렇습니다
- 음 갑자기 든 궁금증인데, 파일이 아닌, 스트링 형태로 코드를 가져와서 돌릴 수 있을까요? 그렇다면, 무의미한 파일이 만들어지는 것이 아니라, `.ipynb`파일와의 동기화를 일정하게 유지할 수 있을 것 같은데요.

```
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
```
- http://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Importing%20Notebooks.html