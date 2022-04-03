---
title: Vim 27 - vimrc version control by Git
category: vim
tags: vi vim git vimrc
---

## Vim 27 - vimrc version control by Git

- 저는 주 IDE로 vim을 사용합니다. 초기에는 VScode를 사용했으나 소소한 기능들이 '실제로 어떻게 흘러가는지' 코드를 뜯어볼 수 없다는 점에서 에러가 발생했을 때 대응이 어려운 경우들이 있더라구요. 그리고 점차 마우스 사용보다 키보드 사용을 늘려나가는 과정에서 모든 것을 터미널에서 처리해 버리면 마우스를 쓸 일이 줄어들기도 해서, 현재는 Vim만을 쓰고 있습니다.
- 이 배경에서 vim을 사용하다가 소소한 기능 추가 혹은 변경이 필요할 경우 `~/.vimrc` file을 수정하게 됩니다.
- 다만, `.vimrc` file의 경우 home directory에 위치해 있고, 그냥 file하나로만 존재하기 때문에 변경 이력이 관리되지 않습니다. 해당 파일의 내용이 바뀔 경우 그 영향도가 매우 큼에도 불구하고, 변경 이력이 관리되지 않을 경우 실수로 잘못 변경했을 때 복구하는 것이 몹시 힘들어집니다.
- 따라서, `.vimrc` file을 관리할 수 있는 방법을 고민하다가 찾아봤습니다. [stackoverflow - adding your vim vimrc to github aka dot files](https://stackoverflow.com/questions/18197705/adding-your-vim-vimrc-to-github-aka-dot-files)를 참고했고, 대략 다음과 같은 내용들이 있을 것 같아요.

1. home directory(`~/`)를 git으로 관리하고, `.gitignore` file에서 `.vimrc` file만을 관리하도록 설정함.
1. `~/vim_config`과 같은 folder를 만들고, `.vimrc` file을 여기로 옮기고, `~/`에는 soft link를 생성한다.
1. `~/vim_config`과 같은 folder를 만들고, `.vimrc` file에 대한 hard link file을 만든다.

- 1번은 어쨋든 home directory를 git의 관리하에 둬야 합니다. 물론 `.gitignore`을 설정하면 문제가 없기는 하지만, 저는 그래도 좀 위험하다고 느껴지는 부분이 있어요.
- 2, 3번은 사실 link를 사용한다는 점에서 동일한데요. soft link의 경우는 원본 파일을 git folder로 옮기고, home directory에는 soft link file을 위치시킵니다. 이 경우 혹시라도, git 관리 폴더를 삭제했을 경우 원본 파일에 접근할 수 없게 됩니다. soft link니까요. 다만 hard link는 완전히 동일한 inode 값을 가지기 때문에 home directory의 file이 삭제되어도 혹은 git 폴더의 파일이 삭제되어도 문제가 없습니다.
- 따라서, 저는 우선 hard link를 생성하기로 결정했습니다. 이후 folder에 대해서도 관리가 필요할 경우에는 soft link를 만들어야겠으나 우선 오늘은 `.vimrc` file만 관리할 목적이므로 hard link로 관리하겠습니다.

## Do it

- github에 [frhyme - vim_config](https://github.com/frhyme/vim_config) repo를 만들었습니다.

```sh
git clone https://github.com/frhyme/vim_config.git
cd vim_config
ln ~/.vimrc ./.vimrc
```

## Wrap-up

- ".vimrc file에 대해서 version control하고 싶다"라는 생각이 떠올랐을 때, 본능적으로 바로 google에 "vimrc git"과 같은 키워드를 검색하게 됩니다.
- 저는 이미 link, git 도 모두 알고 있는 상황이었는데요, stackoverflow 에서 답변을 검색해서 보니, "이미 내가 알고 있던 것을 조합한 것"이더라고요. 다르게 말하면 내가 검색을 하기 전에 스스로 해결해보려는 고민을 조금 해봤다면 달라졌을 거라는 얘기죠.
- 다음부터는 구글에 검색하기 전에 잠깐이라도 해당 문제를 스스로 풀 수 있는지 고민해 봐야 할 것 같습니다.

## Reference

- [stackoverflow - adding your vim vimrc to github aka dot files](https://stackoverflow.com/questions/18197705/adding-your-vim-vimrc-to-github-aka-dot-files)
