---
title: colab에서 python auto-complete가 안됩니다. 
category: python-libs
tags: python python-libs colab auto-complete
---

## intro

- 약 1주일전만 하더라도, colab에서 auto-complete가 잘 되었습니다. 
- auto-complete는 예를 들어서, `nx.G`까지만 치고, tab을 누르면 `nx`내에 있는 `G`로 시작하는 함수들이 포함된 drill-down menu가 생기는 것을 말합니다. 이게 없으면, 제가 모든 명령어를 정확하게 다 외우고 있어야 하죠. 
- 그런데, 갑자기 이게 안됩니다. 정확히는 `nx.G`를 누르고 tab을 누르면, `G`와 상관없이, 그냥 blank에서 탭을 친다고 생각하고, drill-down menu가 생깁니다.

![](/assets/images/markdown_img/190115_colab_autocomplete_problem.png)

## way to solve it. 

### 브라우저의 문제인가? 

- 구글 크롬의 문제인가 싶어서, 파이어폭스에서 colab를 실행해보았습니다만, 파이어폭스에서도 똑같은 문제가 발생합니다. 

### 컴퓨터를 껐다 킨다.

- 컴퓨터를 껐다가 켜도 문제가 달라지지 않습니다. 

### 다른 사람의 colab을 가져와서 한다 

- [다른 사람이 만든 colab](https://colab.research.google.com/drive/1l09j_Yv3H016EqHyrJUe_0mNah1M80qf)을 
복사하여 제 드라이브로 가져와서 실행해봅니다. 
- 그런데, 다른 사람의 colab을 가져와서 실행하니까 문제없이 잘 되네요. 흠...

#### 다른 사람의 colab과의 설정 차이는? 

- 위에 링크한 다른 사람의 colab은 python2입니다. 흠. 저는 python3를 쓰고 있습니다. 
- 링크한 colab을 python3로 변경하니, 여기서도 앞서 말한 것과 같은 문제점이 발생합니다.
- 즉, python3의 특정 버전 혹은 colab에서 가져오는 라이브러리의 특정 버전에서 발생하는 문제로 볼 수 있죠. 

### 비슷한 문제를 겪고 있는 다른 사람들은? 

- [찾아보면, 비슷한 문제를 겪고 있는 사람들이 많이 있습니다.](https://github.com/jupyter/notebook/issues/2435)
- 영어로 되어 있어서, 좀 정리를 해야할 것 같기는 한데, ipython의 버전으로 인해 발생하는 문제로 보입니다. 
- 일단 colab의 개발환경은 다음과 같습니다. 

```python
{'commit_hash': 'b467d487e',
 'commit_source': 'installation',
 'default_encoding': 'UTF-8',
 'ipython_path': '/usr/local/lib/python3.6/dist-packages/IPython',
 'ipython_version': '5.5.0',
 'os_name': 'posix',
 'platform': 'Linux-4.14.79+-x86_64-with-Ubuntu-18.04-bionic',
 'sys_executable': '/usr/bin/python3',
 'sys_platform': 'linux',
 'sys_version': '3.6.7 (default, Oct 22 2018, 11:32:17) \n[GCC 8.2.0]'}
```


### 이것저것 해봤지만. 

- 아직 해결법은 못 찾았습니다. 
- 앞서 비슷한 문제를 겪고 있는 사람들처럼 jedi를 삭제하기도 하고, 다시 깔기도 하고, 몇 가지를 해봤으나 별 차이는 없네요. 
- [일단 그래서 colab에 새로운 이슈를 열었습니다.](https://github.com/googlecolab/colabtools/issues/390)

## 결론. 

- 현재로서는 고쳐진 것으로 보입니다. 