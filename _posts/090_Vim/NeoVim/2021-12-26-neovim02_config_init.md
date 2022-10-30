---
title: NeoVim - Neovim 설정하고 jedi-vim 설치하기
category: vim
tags: vim vi neovim nvim python jedi programming vundle
---

## NeoVim - Neovim 설정하고 jedi-vim 설치하기

### Neovim설정하기 

- NeoVim은 `~/.config/nvim/init.vim`에서 설정합니다. 없을 경우 폴더를 만들어 주고요. 

```bash
$ cd ~/.config/
mkdir nvim
$ cd ~/.config/nvim
vi init.vim
```

- `init.vim`을 만들어주고 `.vimrc`처럼 파일 내용들을 작성해줍니다.

```bash
syntax on
colorscheme jellybeans
set number
set clipboard=unnamed

set langmenu=en_US.UTF-8
language messages en_US.UTF-8
```

- theme의 경로가 달라졌기 때문에 기존 theme 을 가져와서 복사해줍니다.

```bash
$ cd ~/.vim/colors
$ cp jellybeans.vim ~/.config/nvim/colors/
```

### pkg manager 설치하기 - vim-plug 설치하려다가 Vundle로 돌아감

- 기존 vim에서는 Vundle을 사용했기 때문에, Vundle을 사용하려고 했으나, Neovim에서는 [vim-plug](https://github.com/junegunn/vim-plug)를 사용하는 것으로 보입니다.
- 확인해 보면, 설치가 잘 된 것을 확인할 수 있죠.

```bash
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 82789  100 82789    0     0   171k      0 --:--:-- --:--:-- --:--:--  170k
$ cd .local/share/nvim/site/autoload/
$ ls
plug.vim
```

- 다만 설치 중에 패키지가 끌어와지지 않아서, 그냥 Vundle로 돌아갑니다.

```bash
$ git clone https://github.com/VundleVim/Vundle.vim.git ~/.config/nvim/bundle/Vundle.vim
```

- jedi-vim을 Vundle내에 작성해줍니다. 그리고 `:PluginInstall`을 실행하여, 플러그인들을 설치해줍니다.

```vimrc
set rtp+=~/.config/nvim/bundle/Vundle.vim
call vundle#begin('~/.config/nvim/bundle')
 
Plugin 'VundleVim/Vundle.vim'
Plugin 'davidhalter/jedi-vim'
"Plugin 'Valloric/YouCompleteMe'
 
call vundle#end()
```

- jedi vim을 실행했으나, 다음과 같이 python3가 feature로 설정되어 있지 않아서, 실행이 안됩니다.

```plaintext
Error detected while processing function jedi#init_python[11]..<SNR>27_display_exception:
line   19:
Error: jedi-vim failed to initialize Python: jedi-vim requires Vim with support for Python 3. (in function jedi#init_python[4]..<SNR>27_init_python, line 4)
```

- 현재 vim을 확인해 보면, feature가 설치되어 있지 않은 것을 알 수 있음. 

```plaintext
$ vi --version
NVIM v0.6.0
Build type: Debug
LuaJIT 2.1.0-beta3
...
Features: +acl +iconv +tui
```

- 실제로 nvim에서 `:python a.py`를 실행해 보면 다음과 같은 에러가 발생합니다.

```plaintext
E319: No "python" provider found. Run ":checkhealth provider" 
```

- `:checkhealth provider`를 해봅니다.

```plaintext
## Python 3 provider (optional)
  - WARNING: No Python executable found that can `import neovim`. Using the first available executable for diagnostics.
  - ERROR: Python provider error:
    - ADVICE:
      - provider/pythonx: Could not load Python 3:
  - INFO: Executable: Not found
```

- python module를 사용하려면, `pynvim`이라는 모듈이 필요하다고 합니다. 아래 명령어를 실행해 보죠.

```bash
$ python3 -m pip install --user --upgrade pynvim
Collecting pynvim
  Downloading pynvim-0.4.3.tar.gz (56 kB)
     |████████████████████████████████| 56 kB 5.4 MB/s 
Requirement already satisfied: msgpack>=0.5.0 in ./opt/anaconda3/lib/python3.7/site-packages (from pynvim) (0.6.1)
Requirement already satisfied: greenlet in ./opt/anaconda3/lib/python3.7/site-packages (from pynvim) (0.4.15)
Building wheels for collected packages: pynvim
  Building wheel for pynvim (setup.py) ... done
  Created wheel for pynvim: filename=pynvim-0.4.3-py3-none-any.whl size=41588 sha256=...
Successfully built pynvim
Installing collected packages: pynvim
Successfully installed pynvim-0.4.3
WARNING: You are using pip version 21.1.3; however, version 21.3.1 is available.
```

- 이렇게 하고 나니까, 문제없이 실행되고, jedi-vim도 사용할 수 있끼는 하지만....그냥 vim을 사용할 때보다 오히려 느려진 느낌이 드네요.....실패한 것 같습니다.

## Wrap-up

- 처음에 NeoVim을 설치하기로 한 것은, jedi-vim이 너무 느려서, 혹시 Neovim에서는 Jedi-vim이 빨라질 수 있지 않을까, 하는 기대감 때문이었는데요. 결과적으로는 전혀 빨라지지 않았습니다. 오히려 조금 더 느린 느낌마저 들어요.
- 만약 그러함에도 NeoVim이 가진 분명한 장점이 있따면, 이 아이를 쓰겠지만...글쎄요. 잘 모르겠습니다.
- 따라서, 결국은 원래대로 vim을 사용해 보기로 했습니다.
