---
title: pandas profiling
category: python-libs
tags: python python-libs pandas conda anaconda pandas-profiling
---

## intro: pandas-profiling

- 탐색적 데이터 분석(Exploratory Data Analysis)이라는 것이 있습니다. 어려워 보이지만, 간단하게 설명하자면, 주어진 데이터의 특성이 무엇인지를 파악하는 것을 말합니다. 
- 우선, 저한테 데이터 세트가 있다고 가정을 해보겠습니다. 대략, 엑셀로 정리된 테이블이 있다고 하죠. 대부분 수치 값이겠죠. 
- 무작정 그냥 모델에 넣어서 돌리면 되는 것 아니야? 라고 말할 수도 있습니다. 하지만, 그렇게 간단하게 그냥 돌려서는 안됩니다. 데이터에는 아주 많은 노이즈들이 존재합니다. 대략 다음으로 정리할 수 있죠. 
- 수치 데이터의 경우 지나치게 큰 값이 있거나, 값이 없거나, 데이터들이 normalization이 되어 있지 않거나, 실측된 값이 있거나 하는 다양한 문제가 있겠죠. 그리고 경우에 따라서는 그 데이터 세트의 실측 값을 채워넣거나, 빼고 계산을 하거나, 데이터세트를 n개로 나누어 처리하거나 하는 다양한 방법이 필요하겠죠.
- 아무튼, 이 방법을 pandas-profiling이라는 패키지로 사용할 수 있다고 합니다.
- 잘 모르니까, 일단 설치를 하면서 해보죠. 


## install pandas-profiling

### ERROR during installing pandas-profiling

- 일단 설치를 합니다.

```
conda install pandas-profiling
```

- 뭔가, 이상한 메세지가 뜨면서 잘 안됩니다. 흠. `conda-build`를 업데이트하라고 하네요.

```
WARNING conda.base.context:use_only_tar_bz2(632): Conda is constrained to only using the old .tar.bz2 file format because you have conda-build installed, and it is <3.18.3.  Update or remove conda-build to get smaller downloads and faster extractions.
```

- 해석을 해보자면, 
> Conda is constrained to only using the old .tar.bz2 file format because you have conda-build installed, and it is <3.18.3
- Conda는 옛날 .tar.bz2 file format을 사용하는 것에 제한되어 있는데, 그건, 니가 conda-build 를 설치했고, 그게 3.18.3보다 낮은 버전이기 때문이지. 

> Update or remove conda-build to get smaller downloads and faster extractions
- 그러니까, 더 작게 다운로드를 받거나 빠른 추출을 위해서는 conda-build 를 업데이트하거나, 지워라. 

- 라고 합니다. 역시 해석을 해도 무슨 말인지 알기 어렵군요. 
- 코딩을 많이 하면서 느낀 교훈은 모르면, 일단 에러 메세지를 그대로 복사해서 검색해보라는 것이죠 호호호. 즉, 위 메세지를 그대로 복사해서, 구글에 검색을 해봅니다. 

### What is the exact problem and why it happened?

- 검색을 해보니, [스택오버플로우에 이미 질문이 하나 올라와 있습니다](https://stackoverflow.com/questions/56765518/anaconda-4-7-5-warning-about-conda-build-3-18-3-and-issues-with-python-packag). 그리고 글을 내리다보면, 이미 이 질문의 저자가, conda 리포지토리에서 관련 글을 작성하고 있는 것을 알 수 있죠. 

- 해당 원 글은 [이 링크에](https://github.com/conda/conda/issues/8842)에 있으며, 이런 문제가 발생한 이유는 다음과 같이 작성되어 있습니다. 원글을 쓰고, 영어로 번역하였습니다.

> anaconda is a meta-package. Each version consists of a set of versions that have all gone through QA together as a set. If you change any version of any package in that collection, you no longer have that metapackage, because you have strayed from that known set. There is a special version of that metapackage, custom, that is meant to handle this relaxation of constraints. The "custom" version depends only on a particular version of python - it removes the constraints on all other packages.
- 아나콘다는 메타 패키지(meta-package)입니다(패키지들의 패키지라는 말이겠죠). 아나콘다의 각 버전은 함께 품질 관리/보증(QA, Quality Assurance)을 통해 모아진 다양한 패키지의 버전 묶음으로 구성됩니다. 만약, 세트에서 어떤 패키지에라도 변화가 발생한다면, 당신은 그 메타 페키지를 사용할 수 없습니다. 해당 패키지로부터 벗어난(Staryed) 것이죠. 만약, 거기에 특별한 버전의 메타패키지(custom)이 있다면, 그것은 이러한 종류의 제한으로부터 어느 정도 자유로워질 수 있다는 것을 의미합니다. 

> conda 4.7 builds up its candidates for addition differently from earlier conda versions. It starts with specs from the history, and tries to constrain things where it can, to speed up the solution. When conda finds the anaconda metapackage with the "custom" version, it keeps it, but all of those other dependencies are now orphaned. This is why conda is removing them - they have no spec in the history that tells conda to keep them.
- conda 4.7은 이전 conda version과 다르게 후보들(candidate)을 저장합니다. 보통, 그건 이전 history의 명세(spec)들로부터 시작하지만, 솔루션 속도를 높이기 위해서, 가능한 모든 것을 제한합니다. conda가 아나콘다 커스톰 메타 패키지를 찾는다면, 유지하지만, 다른 의존들은 모두 분리됩니다(orphaned). 이것이, 콘다가 다른 패키지들을 지운 이유입니다. 그들은 콘다가 그들을 유지해야 할 기록상에서 사양이 없기 때문이죠.

### 뭐라는걸까요. 과연. 

- 대충 정리해보겠습니다. 
- 아나콘다는 '괜찮은 파이썬 패키지들을 QA를 통해 하나로 묶어준 묶음'을 말하죠. 즉, 안드로이드 버전들처럼, '관리되는 명확한 버전'들이 존재합니다. 따라서, 필요에 따라서 각 개인이 해당 묶음에 새로운 라이브러리를 추가하거나 한다면, 그 즉시, 내 로컬에서 관리되는 아나콘다는 그 버전을 벗어나게 됩니다. 그래서, 콘다를 통해서 특정 버전을 다운받게 된다면, 그 외의 모든 라이브러리들은 버전에서 분리되기 때문에, 사용할 수 없을 수도 있다. 뭐 대충 그런 말인것 같군요. 
- 대충 이해했습니다만. 뭐 사실 이게 제가 지금 해결해야 하는 문제와 무슨 관련이 있는지는 잘 모르겠습니다. 네, 제가 늘 그래요. 정신차려보면 이상한 곳에 와 있습니다. 

### back to the problem 

- 다시, 원래 에러 코드로 돌아와서, 보면, 결국 `conda-build`를 업데이트하라는 말이죠. 그런데, 하는 김에 그냥 전체 모든 패키지들을 함께 업데이트를 해봅니다. 

```bash
conda update conda
```

- 설치를 죽 하다가, 아래 에러코드와 함께 롤백되었습니다. 즉, 설치가 안되었다는 말이죠. 그리고, 각 라이브러리들의 버전도 차이가 없습니다. 

```
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
ERROR conda.core.link:_execute(637): An error occurred while uninstalling package 'defaults::numpy-base-1.14.3-py36ha9ae307_0'.
FileNotFoundError(2, 'No such file or directory')
Attempting to roll back.

Rolling back transaction: done
```

- 이번에는 `conda-build`만 업데이트를 해봅니다. 
- 이 경우에도 마찬가지로, 잘 진행되는 것처럼 보이다가, 결국은 roll-back 처리 됩니다. 뭔가 설치될 수 없는 문제가 있는 것처럼 보이네요. 

- 그리고, 혹시나 해서 `conda install pandas`를 터미널에 쳐도 똑같습니다. 맨 처음에 말씀드린 그 오류가 뜬다는 이야기죠. 
- 자, 결과적으로는 conda로 

### detour: bash-profiling으로 돌아가자. 

- 현재 저는 콘다에 작은 문제들이 있습니다. 워닝이니까 무시해도 되지만, conda는 업데이트되지 않고요. 아무튼 자잘자잘한 문제들이 있습니다만, 넘어가서 그냥 다시 bash-profiling으로 돌아갑니다. 아래를 실행하니까, 설치가 되기는 하는군요. 

```
conda install bash-profiling
```

- 그리고, 간단한 코드를 실행해봤는데 안 됩니다. 자세히 보니 이제는 numpy가 문제네요. pandas는 numpy에 의존적이고, pandas를 실행할 때, numpy가 실행됩니다. 아무튼, 그래서 numpy를 설치하려고 보니, 이제 다음과 같은 에러메세지가 뜹니다. 

```bash
pip install numpy install numpy
Requirement already satisfied: numpy in /Users/frhyme/anaconda3/lib/python3.6/site-packages (1.14.3)
ERROR: Could not find a version that satisfies the requirement install (from versions: none)
ERROR: No matching distribution found for install
```

- 이제 슬슬 짜증이 나고 그냥, 콘다를 정상적인 놈으로 다 돌려버리기로 결심합니다. 

```
conda update -n base -c defaults conda-build
```

- 위 명령어를 사용해서 모든 패키지를 디폴트로 변경해버리기로 합니다. 이제 다 귀찮아요. 필요하면 아예 새로 까는게 더 빠를 것 같아요. 
- 그리고 `conda info`를 사용하니까, 다음과 같이 뜹니다. 일단, 이전에 비해서는, 대부분 업데이트가 완료되었습니다. 물론 이제 다 초기화했으니, 이전에 만들어준 다른 코드들에서 문제가 발생할 수 있지만, 그건 나중에 생각해보겠습니다. 

```bash
     active environment : None
       user config file : /Users/frhyme/.condarc
 populated config files : /Users/frhyme/.condarc
          conda version : 4.7.12
    conda-build version : 3.18.11
         python version : 3.6.8.final.0
       virtual packages :
       base environment : /Users/frhyme/anaconda3  (writable)
           channel URLs : https://repo.anaconda.com/pkgs/main/osx-64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/osx-64
                          https://repo.anaconda.com/pkgs/r/noarch
          package cache : /Users/frhyme/anaconda3/pkgs
                          /Users/frhyme/.conda/pkgs
       envs directories : /Users/frhyme/anaconda3/envs
                          /Users/frhyme/.conda/envs
               platform : osx-64
             user-agent : conda/4.7.12 requests/2.22.0 CPython/3.6.8 Darwin/19.0.0 OSX/10.15.1
                UID:GID : 501:20
             netrc file : None
           offline mode : False
```

- 그리고 나서 간단한 코드를 실행해보는데, 이번엔 다음과 같은 에러 코드가 뜹니다. 


```
Traceback (most recent call last):
  File "test.py", line 17, in <module>
    main()
  File "test.py", line 14, in main
    profile = df.profile_report()
  File "/Users/frhyme/anaconda3/lib/python3.6/site-packages/pandas/core/generic.py", line 5067, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'profile_report'
```

- `pd.dataframe`에서 `profile_report`를 실행할 수 없다는 말이죠. 와 진짜 이제 성질이 납니다. 다시 설치해봅니다. 

```
conda install -c conda-forge pandas-profiling
```

## finally 

- 이제 됩니다. 아 너무도 멀고 험한 길을 걸어 왔군요. 
- 간단하게, 데이터프레임을 만들고, html 보고서로 변경해봤습니다. 별거 아니군요. 후후. 
- 원래 오늘 좀 더 복잡하게 어떻게 쓸 수 있는지에 대해서 써보려고 했는데, 그건 다음 포스트에서 좀 더 정리해보겠습니다.

```python
import pandas as pd
import numpy as np 
import pandas_profiling

def main():
    print("Start")

    df = pd.DataFrame(
        np.random.rand(100, 5), 
        columns = ['a', 'b', 'c', 'd', 'e']
    )
    print(df.head())

    # dataframe을 리포트로 만들어주고, 
    profile = df.profile_report()
    # 리포트를 html로 추출합니다. 
    profile.to_file(output_file="output.html")
    
main()
```

## wrap-up: lesson-learned

- 사실, 오늘 쓴 글은 `bash-profiling`에 관계된 것이라기보다는 파이썬 관련 패키지 문제가 컸죠. 
- 오늘 다시 느낀 반성은, ***가능하면, 공식 documentation을 보고 진행하자***는 것이죠. [pandas-profiling-doc](https://pandas-profiling.github.io/pandas-profiling/docs/)이 공식 도큐멘테이션입니다. 여기에 들어가면, 어떻게 설치하는 것이 좋은지, 해당 명령어가 아주 정확하게 작성되어 있는데도 불구하고, 저는 다른 2차 블로그에서 내용을 파악하고 진행했습니다. 만약, 처음부터 저 블로그를 봤다면, 좀 읽어보고 침착하게 진행할 수 있지 않았을까 싶어요. 
- 또한, 옛날 생각을 해보면, 저는 처음 파이썬을 사용할 때는 `pip`를 사용해서 필요한 패키지들을 설치했었습니다만, `pip`로 설치할 경우 각 패키지별로 다른 버전을 설치하게 됩니다. 따라서, 종종 서로 다른 패키지들이 버전간에 사맛디 아니하여 코드가 굴러가지 않는 경우들이 있었죠. 그래서, 이후에는 파이썬을 설치할 때 아예 처음부터 아나콘다를 설치하고, conda를 사용하는 일들이 훨씬 많았습니다. 
- 그래서, `pip`보다는, 가능하면 `conda`를 설치하는 일이 많았죠. 그런데, 여기서 명령어도 잘 모르고 좀 무감각하게 사용하는 일이 많은 것 같아요. 그러다보니, 패키지간에 충돌이 발생하고, 또 발생해도 그게 왜 그런지에 대해서도 잘 모르죠. 
- 좀 더 나아가면, 필요에 따라서 가상환경을 세팅하거나 하는 것이 필요하기도 한데, 저는 그것도 귀찮다는 이유로 잘 하지 않습니다. 뭐 그렇습니다 호호호. 


## reference

- <https://wikidocs.net/47193>
- <https://pandas-profiling.github.io/pandas-profiling/docs/>
