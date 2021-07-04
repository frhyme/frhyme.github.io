---
title: conda, pip - export pkgs
category: python-libs
tags: python conda anaconda pip freeze package 
---

## conda - conda export pkgs

- conda 명령어를 사용하여, 현재 환경에서 설치된 패키지들을 확인하려면 다음 명령어를 사용하면 됩니다.
- `pip list`와 `conda list`는 기본적으로 같다고 생각하시면 됩니다.

```zsh
$ conda list
$ pip list
```

- `pip freeze`를 사용하면, 다음과 같이 깔끔한 형태로 정리해 줍니다.

```zsh
$ pip freeze
alabaster==0.7.12
anaconda-client==1.7.2
anaconda-navigator==1.9.12
anaconda-project==0.8.3
applaunchservices==0.2.1
...
```

- 따라서, 아래 command를 사용해서 `requirement.txt`에 해당 패키지들을 다음처럼 깔끔하게 정리할 수 있죠.
  - `pip freeze`: 현재 python 환경에 설치된 pkg들을 `pkg_name==pkg_version`의 형태로 출력해주는 명령어 
  - `> requirement.txt`: `requirment.txt` 파일을 write mode로 읽어서, 이전에 수행된 명령어의 결과를 집어넣고 출력해줍니다.
- `vi requirement.txt`를 사용해서 값이 잘 저장되었는지를 확인할 수 있죠.

```zsh
$ pip freeze > requirement.txt
$ vi requirement.txt
```

- 만약 다른 환경에서, `requirment.txt`에 저장된 패키지들을 모두 설치해주고 싶다면, 다음 명령어를 사용하면 된다.

```zsh
pip install -r requirement.txt
```

- conda에서도 같은 작업을 수행할 수 있는데요. 명령어는 다음과 같습니다.

```zsh
$ conda list --export > requirement_by_conda.txt                                                                                           
$ vi requirement_by_conda.txt   
```

- 이렇게 생성된 `requirement_by_conda.txt`를 활용해서 새로운 conda 환경을 구축해 주고 싶을 때는, 아래 명령어를 사용하면 됩니다.

```zsh
conda create --name new_conda_env --file requirement_by_conda.txt
```

- 만약, 아래 명령어를 사용했을 때, 진행되다가, 다음과 같은 메세지와 함께 진행이 되지 않는다면, 해당 conda 환경에 설치되어 있는 몇몇 package들이 `conda install`을 통해 설치할 수 없는 패키지들이라는 것을 말합니다.

```zsh
PackagesNotFoundError: The following packages are not available from current channels:

  - requests-oauthlib==1.3.0=pypi_0
...
```

- 따라서, 아예 새로운 conda 환경을 구축해 주고 다시 진행해 보기로 합니다.
  - 새로운 pure한 conda 환경을 만들어주고, 
  - 해당 env를 활성화 해주고 
  - 해당 env에서 새로운 package를 설치해주고
  - 현재 env의 pkg들을 txt 파일로 만들어주고,
  - 만들어준 txt 파일로부터 새로운 conda 환경을 구축해주고
  - 잘 생성되었는지 확인해보고, 지워줍니다.

```zsh
$ conda create --name new_env
$ conda activate new_env
$ conda install networkx
$ conda list --export > requirement_for_test.txt
$ conda create --name new_conda_env --file requirement_for_test.txt
$ conda env list
$ conda env remove -n new_conda_env
$ conda env list
```

## wrap-up

- conda, pip를 사용하여 현재 설치되어 있는 패키지들을 가져와서 동일한 환경을 구축할 수 있는 방법을 정리하였습니다.
