---
title: conda - enabling tab completion
category: python-libs
tags: python conda anaconda tab_completion antigen zshrc zsh
---

## conda - enabling tab completion

- shell에서 conda 명령어 자동완성이 되지 않아서, 세팅해주려고 합니다.
- [conda - enable tab completion](https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/enable-tab-completion.html) 문서를 확인해 보면, bash shell에서는 conda version 4.3 이하에서만 지원된다고 나와 있습니다.
- 현재 제 conda version을 확인해 보면 4.8.3이기 때문에, 현재 공식 문서에서 알려주는 방법을 사용할 수는 없죠.

```zsh
$ conda --version
conda 4.8.3
```

- 해당 문서를 쭉 읽어 보면 마지막에는 [github - conda zsh completion](https://github.com/esc/conda-zsh-completion)를 사용하는 것을 추천하다고 되어 있기는 합니다. 그러나, 해당 깃헙 repo에 들어가보면 documentation이 매우 부실한 걸 알 수 있습니다. 그래도 찾아보면, [stackoverflow - zsh autocomplete anaconda environment](https://stackoverflow.com/questions/31818491/zsh-autocomplete-anaconda-environments)에 해당 패키지를 설치하는 방법들이 정리되어 있기는 한데, 음, 이렇게 각각 설치해서는 나중에 유지보수가 꽤나 어려워지죠.

## install conda zsh completion by antigen

- [github - angiten](https://github.com/zsh-users/antigen)을 사용해서 zsh 의 plug-in을 설치해보기로 합니다.
- [github - antigen - Installation](https://github.com/zsh-users/antigen/wiki/Installation)을 보면 다양한 설치 방법이 있는데요, 저는 macOS를 사용하기 때문에, brew를 사용해 봅니다. `brew update`도 함께 진행되었어요.

```zsh
$ brew install antigen
```

- 그 다음 설치된 위치를 확인해봅시다. 

```zsh
$ brew --prefix antigen
/usr/local/opt/antigen
```

- 그리고, 해당 경로의 `antigen.zsh`의 파일을 확인해서 `.zshrc`에 추가해줍니다.

```zsh
source /usr/local/opt/antigen/share/antigen/antigen.zsh
```

- 그리고, 아래 `.zshrc`를 다시 설정해주구요.

```zsh
$ source .zshrc
$ vi ~/.antigenrc
```

- antigen의 설정 파일인 `.antigenrc` 파일을 만들어서, 안에 아래 내용을 추가해줍니다.

```plaintext
antigen bundle esc/conda-zsh-completion
```

- `.zshrc`에는 다음 내용을 업데이트해줍니다. 

```zsh
# 20210704: install antigen
source /usr/local/opt/antigen/share/antigen/antigen.zsh
antigen bundle esc/conda-zsh-completion
antigen init ~/.antigenrc
antigen apply
```

- `.zshrc`를 다시 설정해줍니다.

```zsh
$ source .zshrc
```

- 이렇게 세팅해주고 나면, conda 명령어를 이볅할 때, tab을 사용해서 자동완성됩니다. 

## wrap-up

- 다만 좀 걱정스러운 것은, 처음부터 antigen을 사용해서 package들을 다운받은 것이 아니어서, 각 설정 값들이 여러 곳에 나누어져 관리되고 있다는 것이죠. 지금은 딱히 문제되지 않는데, 이후에는 문제가 될 수도 있으니 염두에 두어야 할 것 같아요.

## reference

- [conda - enable tab completion](https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/enable-tab-completion.html)
- [stackoverflow - zsh autocmplete anaconda environment](https://stackoverflow.com/questions/31818491/zsh-autocomplete-anaconda-environments)
- [github - antigen](https://github.com/zsh-users/antigen)
