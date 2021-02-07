---
title: conda env 변경하기
category: others
tags: python conda anaconda
---

## conda env 변경하기

- 우선 `conda env list`를 사용하여 현재 사용가능한 conda environment를 확인해봅시다.
- `*` 표시가 되어 있는 env가 현재 활성화되어 있는 env입니다.

```plaintext
$ conda env list
# conda environments:
#
DjangoEnv                /Users/<user_name>/.conda/envs/DjangoEnv
DjangoProject            /Users/<user_name>/.conda/envs/DjangoProject
pythonProject            /Users/<user_name>/.conda/envs/pythonProject
base                  *  /Users/<user_name>/opt/anaconda3
```

- 저는 `DjangoEnv`로 변경을 해주려고 합니다. 
- 우선 `conda activate DjangoEnv`를 사용해서 conda env를 활성화해줍니다.
- 그 다음 `conda info`를 사용해서 현재 conda 환경을 확인해보면, 바뀌었는지 확인할 수 있습니다.

```plaintext
$ conda activate DjangoEnv
$ conda info
     active environment : DjangoEnv
    active env location : /Users/<user_name>/.conda/envs/DjangoEnv
            shell level : 2
       user config file : /Users/<user_name>/.condarc
 populated config files : 
          conda version : 4.8.3
    conda-build version : 3.18.11
         python version : 3.7.6.final.0
       virtual packages : __osx=10.15.7
       base environment : /Users/<user_name>/opt/anaconda3  (writable)
           channel URLs : https://repo.anaconda.com/pkgs/main/osx-64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/osx-64
                          https://repo.anaconda.com/pkgs/r/noarch
          package cache : /Users/<user_name>/opt/anaconda3/pkgs
                          /Users/<user_name>/.conda/pkgs
       envs directories : /Users/<user_name>/opt/anaconda3/envs
                          /Users/<user_name>/.conda/envs
               platform : osx-64
             user-agent : conda/4.8.3 requests/2.22.0 CPython/3.7.6 Darwin/19.6.0 OSX/10.15.7
                UID:GID : 501:20
             netrc file : None
           offline mode : False
```
