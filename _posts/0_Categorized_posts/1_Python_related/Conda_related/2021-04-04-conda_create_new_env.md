---
title: conda - 새로운 environment 만들기
category: python-libs
tags: python conda anaconda
---

## conda - 새로운 environment 만들기

- conda를 사용해서 새로운 python 독립 환경을 만들기 위해서는 다음 커맨드를 사용하면 됩니다.

```bash
conda create -n <new_environment_name>
```

- 전체 command들을 보여드리면 다음과 같습니다.
- `conda env list`: 현재 설치되어 있는 conda environment들과 활성화되어 있는 conda environment를 확인합니다.

```bash
$ conda env list
# conda environments:
#
base                     /Users/.../opt/anaconda3
```

- `conda create -n python_scratch`: 이름이 "python_scratch"인 conda environment를 새로 만들어 줍니다.
  - 기존에 설치되어 있는 `base`와 버전이 다르다고 Warning을 주는데 그냥 무시합니다 호호.

```bash
$ conda create -n python_scratch
Collecting package metadata (current_repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
  current version: 4.8.3
  latest version: 4.9.2

Please update conda by running

    $ conda update -n base -c defaults conda



## Package Plan ##

  environment location: /Users/seunghoonlee/opt/anaconda3/envs/python_scratch



Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate python_scratch
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

- `conda env list`: 잘 설치되어 있는지 확인해 봅니다.

```bash
$ conda env list
# conda environments:
#
base                     /Users/.../opt/anaconda3
python_scratch           /Users/.../opt/anaconda3/envs/python_scratch
```

- `conda activate python_sracth`: 새로 만든 conda environment를 활성화해줍니다.

```bash
$ conda activate python_scratch
$ conda env list
# conda environments:
#
base                     /Users/.../opt/anaconda3
python_scratch        *  /Users/.../opt/anaconda3/envs/python_scratch
```
