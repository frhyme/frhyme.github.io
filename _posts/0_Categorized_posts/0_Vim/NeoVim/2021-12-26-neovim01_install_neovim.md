---
title: NeoVim - Install Neovim 
category: vim
tags: vim vi neovim nvim 
---

## NeoVim - Install Neovim 

### Intro 

- 기존 vim을 사용하다가 jedi-vim의 실행 속도가 매우 느려서 혹시 default vim을 사용하는 것이 문제인가 싶어서, NeoVim을 설치해봤습니다.
- 결론부터 말하자면, NeoVim을 설치한다고 해서 jedi-vim이 빨라지지는 않습니다. 

### Install Vim 

- 일단 neovim을 가져와서, 직접 source에서 설치를 해보려고 했으나 make에서 오류가 발생합니다.
- 사실, `brew install neovim`를 사용해서 직접 설치해도 되지만, 그래도 가져온 소스에서 직접 설치해보기로 합니다.

```bash
$ git clone https://github.com/neovim/neovim
$ cd neovim
# stable branch로 전환해줍니다.
$ git checkout stable
$ make

$ sudo make install 
$ cd .deps && cmake -G 'Unix Makefiles' 
/bin/sh: cmake: command not found
make: *** [build/.ran-third-party-cmake] Error 127
```

- cmake에서 문제가 발생하는 것이므로, cmake를 설치하면 되겠죠.

```bash
brew install cmake
```

- 설치해 보면, 이번에는 `unibilium`이 없다고 합니다. 얘는 glibtool에 속하는 아이로 보이므로, 또 설치를 해봅니다.

```bash 
$ sudo make install
mkdir -p build
touch build/.ran-third-party-cmake
/Applications/Xcode.app/Contents/Developer/usr/bin/make -C .deps
[  1%] Performing build step for 'unibilium'
make[4]: glibtool: No such file or directory
make[4]: *** [unibilium.lo] Error 1
make[3]: *** [build/src/unibilium-stamp/unibilium-build] Error 2
make[2]: *** [CMakeFiles/unibilium.dir/all] Error 2
make[1]: *** [all] Error 2
make: *** [deps] Error 2
$ brew install libtool
```

- 이번에는 aclocal이 없다고 하니, `automake`라는 아이를 설치해봅니다.
- automake를 설치하고 나면, 이제 neovim을 설치할 수 있습니다. 조금 오래 걸리기는 합니다.

```bash
line 44: aclocal: command not found
make[3]: *** [build/src/libuv-stamp/libuv-configure] Error 127
make[2]: *** [CMakeFiles/libuv.dir/all] Error 2
make[1]: *** [all] Error 2
make: *** [deps] Error 2
$ brew install automake
$ sudo make install
```

- 이제 command line에서 `nvim`을 실행해 보면 실행됩니다. 설치된 경로는 `usr/local/share/nvim`입니다.
- default로 `vi`를 `nvim`으로 설정하려면, `.bashrc` 혹은 `.zshrc`에 다음 내용을 집어넣으면 됩니다.

```zsh
alias vi='nvim'
```

## wrap-up

- NeoVim을 사용해 봤지만, jedi-vim을 사용한다고 더 빨라지지 않고, 기존 vim에 비해서 좋은 점이 있는지도 잘 모르겠네요.
- 일단 지우지는 않고 좀 더 파악해봐야할것 같아요.

## reference 

- [github - jedi vim](https://github.com/davidhalter/jedi-vim)
- [vim 빌드해보자](https://ujuc.github.io/2017/01/28/vim_bir-deu-hae-bo-ja/)
- [neovim1](https://neovim.io/)
- [neovim - wiki](https://github.com/neovim/neovim/wiki/Building-Neovim)
