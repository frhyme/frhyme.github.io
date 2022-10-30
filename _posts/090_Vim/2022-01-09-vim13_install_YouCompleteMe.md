---
title: vim 13 - Install YouCompleteME - 실패기
category: vim
tags: vi vim python jedi plugin vundle YCM YouCompleteMe
---

## vim 13 - Install YouCompleteME - 실패기

- Vim에서 프로그래밍을 하기 위해, AutoComplete Plugin 인 [github - YouCompleteme - Installation](https://github.com/ycm-core/YouCompleteMe#installation)를 설치하려고 하였으나, 결국은 되지 않아서 그 실패기를 정리합니다.
- macOS Monterey(12.1)에 설치를 시도했으며, 결국은 되지 않았습니다. 해당 이슈는 맥북에서만 빈번하게 등장하는 이슈인 것으로 보이기는 하는데요.

### Install YouCompleteMe - Try

- Vundle을 이용해서 설치하기 위해 `.vimrc` 파일 내에 아래와 같이 YouCompleteMe를 등록해줍니다.

```bash
Plugin 'Valloric/YouCompleteMe'
```

- 그리고, `:PluginInstall`을 사용하여 설칙를 완료하면, 다음과 같이 YouCompleteMe를 Compile해줘야 한다는 메세지가 뜹니다. 지금은 안하고, 나중에 할거에요.

```bash
The ycmd server SHUT DOWN (restart with ':YcmRestartServer'). YCM core library not detected; you need to compile YCM before using it. Follow the instructions in the documentation.
```

- python, vim, cmake를 설치하라고 하는데, 이미 다 설치되어 있습니다. 그리고, 설치하라는 말은 없지만, 명령어에는 go, nodejs까지 모두 설치하라고 되어 있는데, 뭐 하는 김애 다 설치해보기로 합니다. 그리고, vim은 mac에 기본으로 설치되어 있는 vim을 사용해서는 안됩니다. 이는 해당 vim --verion을 실행해보면 확인할 수 있는데요, 초기에 mac에 그대로 설치되어 있는 vim에는 python이 포함되어 있지 않아서 그렇습니다. 뭐 추가를 해주면 됩니다만.

```bash
$ brew install go 
$ brew install nodejs
```

- 둘다 설치 완료했구요.
- mono라고 하는, .NET Framework 도 설치하라는데...얘는 맥 인텔 칩이냐, M1 칩이냐 에 따라서 조금 다른 것 같기는 합니다. 아무튼, 뭐 얘도 설치해보겠습니다.

```bash
$ brew install mono
```

- java의 지원을 받으려면 아래도 사용하라고 하는데요.
- linux command `ln`은 "link"의 약자이며, 일종의 "바로가기"를 만드는 커맨드라고 생각하시면 됩니다. "hard link"와 "soft link"로 구분될 수 있는데요, "hard link"는 원본을 그대로 복사하는 것(hard copy), "soft link"는 원복을 가리키는 포인터를 만드는 것(soft copy) 라고 일단은 생각하시면 될 것 같습니다. 아래 command에서는 `s`를 argument로 넘겨서 soft link로 처리해줍니다.
- `ln -s source link`의 형태로 표현됩니다. 즉, `source`에 대한 soft link를 `link`라는 파일에 연결해주겠다, 라는 말이 되죠.
- `f` argument는 `force`를 의미하구요.
- 실행 후에 해당 경로로 가서 link가 잘 생성되었는지 확인해 봅니다.

```bash
$ brew install java
$ sudo ln -sfn /usr/local/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk
$ cd /Library/Java/JavaVirtualMachines/
$ ls 
```

- YouCompleteMe 를 Compile해봅시다. 끝에 argument `--all`을 설정해준 것은 모든 언어들에 대해서 지원하도록 하겠다는 이야기죠.

```bash
cd ~/.vim/bundle/YouCompleteMe
python3 install.py --all
```

- 설치되었다면, 아래 명령어를 통해 `.ycm_extra_conf.py` 파일을 옮겨줍니다.

```bash
cp  ~/.vim/bundle/youcompleteme/third_party/ycmd/.ycm_extra_conf.py  ~/.vim/
```

- 복사된 파일을 열어보면 아래와 같은 경고 메세지가 뜨는 것을 확인할 수 있습니다.

```bash
$ cd ~/.vim
$ vi .ycm_extra_conf.py
# The ycmd server SHUT DOWN (restart with ':YcmRestartServer'). Unexpected exit code -6. Type ':YcmToggleLogs ycmd_63006_stderr_hdwr32nn.log' to check the logs.
```

- 이런 경우 버전의 문제가 있을 수도 있어서, 재설치해주는 게 좋다는 의견이 있어 재설치를 하기로 합니다.

```bash
$ cd ~/.vim/bundle/YouCompleteMe
$ git pull --recurse-submodules origin master

From https://github.com/Valloric/YouCompleteMe
 * branch              master     -> FETCH_HEAD
Fetching submodule third_party/ycmd
Fetching submodule third_party/ycmd/third_party/bottle
Fetching submodule third_party/ycmd/third_party/jedi_deps/jedi
Fetching submodule third_party/ycmd/third_party/jedi_deps/jedi/jedi/third_party/django-stubs
Fetching submodule third_party/ycmd/third_party/jedi_deps/jedi/jedi/third_party/typeshed
Fetching submodule third_party/ycmd/third_party/jedi_deps/numpydoc
Fetching submodule third_party/ycmd/third_party/jedi_deps/numpydoc/doc/scipy-sphinx-theme
Fetching submodule third_party/ycmd/third_party/jedi_deps/parso
Fetching submodule third_party/ycmd/third_party/mrab-regex
Fetching submodule third_party/ycmd/third_party/watchdog_deps/watchdog
Already up to date.
$ ./install.py
```

- PluginClean을 해보기도 하였지만, 잘 안됩니다.

```vim
:PluginClean
```

### YMCD Start Manually - Failed

- 그래도 계속 안되어서 [github - YouCompleteMe - Wiki - Troubleshooting steps for ycmd server shut down](https://github.com/ycm-core/YouCompleteMe/wiki/Troubleshooting-steps-for-ycmd-server-SHUT-DOWN)을 참고해서 진행해 봅니다.
- ycmd 서버를 직접 구동해보려고 하는 것인데요, 아래의 오류와 함께 진행되지 않습니다. `PyMUTEX_LOCK`에서 오류가 발생하였는데요.

```bash
$ cd /path/to/YouCompleteMe/third_party/ycmd/
$ cat PYTHON_USED_DURING_BUILDING
/some/path/to/python3
$ cp ycmd/default_settings.json .
$ /some/path/to/python3 ycmd --options_file=default_settings.json
serving on http://localhost:<some port>

Fatal Python error: PyMUTEX_LOCK(_PyRuntime.ceval.gil.mutex) failed

[1]    73254 abort      python3 ycmd --options_file=default_settings.json
```

- 직접 ymcd를 띄워보려고 하는데요, 띄워지지 않았습니다. 위 에러인 `PyMUTEX_LOCK` 문제는, macOS에서 Conda가 실행될 때만 발생하는 문제점이라고 알려져 있씁니다.
- 발생한 곳은 다르지만, [[BUG] Fatal Python error: PyMUTEX_LOCK(gil->mutex) failed #3081](https://github.com/pybind/pybind11/issues/3081)를 참고해보면, 다음과 같이, macOS에서 conde python으로 돌릴 때 발생하는 문제, 라는 말이 있죠.
- conda에서 사용하는 clang은 버전10인데 반해, 설치된 python의 경우 clang11을 사용하여 발생한다는 말인 것 같습니다.

```plaintext
This only seems to appear when using conda's python on Mac OS. I haven't reproduced it elsewhere. Suspect that python is built with clang 10 from conda, while the python package in question is built with clang11, and some incompatibility arises.
```

- MUTEX는 MUTually EXclusive의 약자로, 병렬 처리시 발생하는 문제를 막기 위해서 두 쓰레드(혹은 프로세스)가 동시에 접근하지 못하도록 처리하는 메커니즘이라고 보시면 됩니다. Python의 경우는 하나의 프로세스 내에서 단 1개의 Thread에서만 Interpreter를 사용할 수 있습니다. 이걸 GIL(Global Interpreter Lock)이라고 하며, Python에서 사용하는 MUTEX 메커니즘인 것으로 파악되네요.
- 모든 python implementation(구현체)에서 GIL이 존재하는 것은 아니고, CPython에서만 GIL이 존재하는 것으로 알고 있습니다.
- guswo 

### Python, Clang Version 

- clang은 맥에서 기본으로 사용하고 있는 compiler이며, LLVM의 메인 프론트엔드를 담당합니다. 소스 코드(c, c++, python 등)을 LLVM IR(Intermediate Representaion)으로 변환해 주죠. 
- Anaconda를 사용하여 설치한, python에서 사용하는 clang은 4.0.1인데, Apple에 설치되어 있는 clang의 버전은 13.0.0이라고 나옵니다. 어쩌면, 이 둘간의 차이로 인해 발생하는 문제가 아닐까 싶습니다.

```bash 
$ python
Python 3.7.6 (default, Jan  8 2020, 13:42:34) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.

$ clang --version
Apple clang version 13.0.0 (clang-1300.0.29.30)
Target: x86_64-apple-darwin21.2.0
Thread model: posix
InstalledDir: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin
```

- Anaconda를 직접 업데이트하면 Clang의 버전이 올라가면서 문제가 해결될까? 라는 생각을 하였는데, 아래 명령어로는 업데이트가 되지 않는 것 같아서, 여기서 홀드하였습니다.

```bash
$ conda update anaconda
```

### Install by python

- [Vim 자동 완성 사용하기](https://johngrib.github.io/wiki/vim/auto-completion/)를 참조하여, 이번에는 `install.py`를 직접 설치해보기로 합니다.

```bash
$ cd ~/.vim/bundle/YouCompleteMe
# 언어 옵션들을 확인해 봅니다.
$ python install.py --help    
usage: build.py [-h] [--clang-completer] [--clangd-completer] [--cs-completer]
                [--go-completer] [--rust-completer] [--java-completer]
                [--ts-completer] [--system-libclang] [--msvc {15,16,17}]
                [--ninja] [--all] [--enable-coverage] [--enable-debug]
                [--build-dir BUILD_DIR] [--quiet] [--verbose] [--skip-build]
                [--valgrind] [--clang-tidy] [--core-tests [CORE_TESTS]]
                [--cmake-path CMAKE_PATH] [--force-sudo]

optional arguments:
  -h, --help            show this help message and exit
  --clang-completer     Enable C-family semantic completion engine through
                        libclang.
  --clangd-completer    Enable C-family semantic completion engine through
                        clangd lsp server.(EXPERIMENTAL)
  --cs-completer        Enable C# semantic completion engine.
  --go-completer        Enable Go semantic completion engine.
  --rust-completer      Enable Rust semantic completion engine.
  --java-completer      Enable Java semantic completion engine.
  --ts-completer        Enable JavaScript and TypeScript semantic completion
                        engine.
  --system-libclang     Use system libclang instead of downloading one from
                        llvm.org. NOT RECOMMENDED OR SUPPORTED!
  --msvc {15,16,17}     Choose the Microsoft Visual Studio version (default:
                        16).
  --ninja               Use Ninja build system.
  --all                 Enable all supported completers
  --enable-coverage     For developers: Enable gcov coverage for the c++
                        module
  --enable-debug        For developers: build ycm_core library with debug
                        symbols
  --build-dir BUILD_DIR
                        For developers: perform the build in the specified
                        directory, and do not delete the build output. This is
                        useful for incremental builds, and required for
                        coverage data
  --quiet               Quiet installation mode. Just print overall progress
                        and errors. This is the default, so this flag is
                        actually ignored. Ues --verbose to see more output.
  --verbose             Verbose installation mode; prints output from build
                        operations. Useful for debugging build failures.
  --skip-build          Don't build ycm_core lib, just install deps
  --valgrind            For developers: Run core tests inside valgrind.
  --clang-tidy          For developers: Run clang-tidy static analysis on the
                        ycm_core code itself.
  --core-tests [CORE_TESTS]
                        Run core tests and optionally filter them.
  --cmake-path CMAKE_PATH
                        For developers: specify the cmake executable. Useful
                        for testing with specific versions, or if the system
                        is unable to find cmake.
  --force-sudo          Compiling with sudo causes problems. If you know what
                        you are doing, proceed.
$ python install.py --clang-complete --go-completer                    
Generating ycmd build configuration...OK
Compiling ycmd target: ycm_core...OK
Building regex module...OK
Building watchdog module...OK
```

- 이렇게 처리한 다음, `.vimrc` 파일 내에 python의 실행 경로를 추가해줍니다. python 실행 경로는 command line 에서 `which python3`를 통해 확인할 수 있습니다.

```bash
" YMC - YouCompleteMe
let g:ycm_server_python_interpreter = '/Users/seunghoonlee/opt/anaconda3/bin/python3'
```

- 이렇게 처리한 다음, vim을 사용해 문서 파일을 열어 봄변, ycmd가 여전히 안되는 것은 마찬가지입니다.
- 혹시나 싶어, python3로 변경하여 처리해봤지만, 여전히 안되고요.

## Wrap-up

- YouCompleteMe를 설치하려고 여러 방면에서 시도를 해보았으나, 잘 되지 않아서 그냥 포기하기로 했습니다. 대충 원인은 mac에서 사용하는 Clang과 anaconda를 통해 설치한 Clang의 버전이 달라지면서, 뭔가 문제가 생긴 것은 아닐까 싶지만, 일단은 이게 중요하지 않으니 넘어가기로 합니다.
- 뭐...그래도 좋은 시도였다고 봅니다. 결국 원인은 Clang 그리고 GIL 때문인 것으로 파악되는데요, 나중에 시간이 생기면, 해당 모듈 코드를 뜯어보면서 어디가 원인인지 파악해 보면 재미있을 것 같아요.
- [github - neoclide - coc.nvim](https://github.com/neoclide/coc.nvim)이 더 좋다고 해서, 다음에는 얘로 설치해보려고 합니다.

## Uninstall Plugin

- `.vimrc` 파일을 열어서, 불필요한 Plugin 부분을 지워주고, 아래를 순서대로 입력해줍니다.

```bash
:PluginInstall
:PluginClean
```

- `PluginClean`중에 오류가 발생하여, 확인해보니, 아래 경로의 폴더가 지워지지 않은 것 같습니다. log를 뜯어 보면 대충 "Permission Denied"가 뜨던데요, 걍 해당 경로로 가서 바로 지워버립겠습니다.

```bash 
$ cd ~/.vim/bundle/YouCompleteMe
$ sudo rm -rf third_party
$ cd ..
$ rmdir YouCompleteMe
```

## reference

- [github - YouCompleteme - Installation](https://github.com/ycm-core/YouCompleteMe#installation)
- [Vim 에디터 사용법 설명 및 C++/Python 개발환경설정](https://edward0im.github.io/technology/2020/09/17/vim/)
- [[BUG] Fatal Python error: PyMUTEX_LOCK(gil->mutex) failed #3081](https://github.com/pybind/pybind11/issues/3081)
- [github - YouCompleteMe - Troubleshooting](https://github.com/ycm-core/YouCompleteMe/wiki/Troubleshooting-steps-for-ycmd-server-SHUT-DOWN)
- [github - vim auto completion - YouCompleteMe](https://johngrib.github.io/wiki/vim-auto-completion/#youcompleteme)
