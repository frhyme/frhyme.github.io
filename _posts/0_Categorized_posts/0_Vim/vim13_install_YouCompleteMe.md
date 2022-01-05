---
title: vim 13 - Install YouCompleteME
category: vim
tags: vi vim python jedi plugin vundle
---

- .vimrc 파일 내에 Vundle에 YouCompleteMe를 등록해준다.

```bash
Plugin 'Valloric/YouCompleteMe'
```

- PluginInstall 을 사용하여 설치가 완료되면 다음과 같이 YouCompleteMe를 Compile해줘야 한다는 메세지가 뜹니다. 지금은 안하고 나중에 할거에요.

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

- 파일을 열 때마다 아래 메세지가 뜨는데 흠 

```
The ycmd server SHUT DOWN (restart with ':YcmRestartServer'). Unexpected exit code -6. Type ':YcmToggleLogs ycmd_63090_stderr_cp3kz28g.log' to check the logs.
```


- 이런 경우 버전의 문제가 있을 수도 있어서, 재설치해주는 게 좋다는 의견이 있어 재설치를 하기로 한다.


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


:PluginClean


- 그래도 계속 안되어서 아래 링크에 있는 내용을 참조하여 진행하기로 했다.
https://github.com/ycm-core/YouCompleteMe/wiki/Troubleshooting-steps-for-ycmd-server-SHUT-DOWN


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

- 직접 ymcd를 띄워보려고 하는데요, 띄워지지 않았음. 위 에러인 `PyMUTEX_LOCK` 문제는, macOS에서 Conda가 실행될 때만 발생하는 문제점이라고 알려져 있씁니다


- 발생한 곳은 다르지만, [[BUG] Fatal Python error: PyMUTEX_LOCK(gil->mutex) failed #3081](https://github.com/pybind/pybind11/issues/3081)를 참고해보면, 다음과 같은 내용이 있습니다.

```
This only seems to appear when using conda's python on Mac OS. I haven't reproduced it elsewhere. Suspect that python is built with clang 10 from conda, while the python package in question is built with clang11, and some incompatibility arises.
```

## 정리

- 현재 제가 사용하고 있는 python의 버전은 3.7.6이고, Clang은 4.0.1 이라고 나옵니다.
- clang은 맥에서 기본으로 사용하고 있는 compiler임. 그리고, Clang은 LLVL의 메인 프론트엔드를 담당하며, 소스 코드(c, c++, python 등)을 LLVM IR(Intermediate Representaion)으로 변환해준다. 즉, 컴파일러라고 생각하면 된다.
- 뮤텍스(MutEx)는 "한 쓰레드에 여러 개의 CPU 연산을 행하다가 내부 데이터가 오염되지 않도록 방지하는 GIL"을 의미하는 것으로 보인다.

## 20220104 

- Anaconda를 업데이트해보자. 현재 버전은 다음과 같고.

```
$ conda --version                                                                                     
conda 4.8.3
$ python --version                                                                                   
Python 3.7.6
$ python3 --version                                                                                  
Python 3.7.6
$ python2 --version                                                                                   
Python 2.7.18
```

- python에서 사용하는 clang은 4.0.1인데, Apple에 설치되어 있는 clang의 버전은 13.0.0이라고 나옵니다. 흠.

```
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


- 흠 잘 모르겠지만 일단 python 버전부터 올려보겠습니다. 아나콘다 버전을 올릴거에요. 다만, 생각을 해보니 conda는 자체 명령어라서 아나콘다를 의미하는 것 같지는 않아요.

```
$ conda --version 
conda 4.8.3
$ conda update conda
```

- 따라서, 아나콘다를 [Anaconda](https://www.anaconda.com/products/individual)에서 직접 다시 다운받아서 설치해보기로 합니다.
- 설치를 하다보니, 이미 설치되어 있다고 아래 커맨드를 사용하라고 하네요.
- 다만 설치에 시간이 꽤 걸립니다. 너무 오래 걸려서....일단 넘어갑니다.

```
$ conda update anaconda
```

- install.py 를 실행해 줍니다. 그래도 안되네요. 

https://johngrib.github.io/wiki/vim-auto-completion/#youcompleteme

```bash
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
$ python install.py --clang-completer 
Generating ycmd build configuration...OK
Compiling ycmd target: ycm_core...OK
Building regex module...OK
Building watchdog module...OK
```

- 이렇게 해도, c를 실행해서 확인해 보면 안되는데 흠....
[github - vim auto completion - YouCompleteMe](https://johngrib.github.io/wiki/vim-auto-completion/#youcompleteme)를 참조하여, .vimrc 파일에 아래 내용을 작성해 줘야 한다는 말이 있어서, 해당 내용을 추가해줍니다.

```bash
let g:ycm_server_python_interpreter = '/usr/local/bin/python3'
```

- 문서 파일을 열었을 때 뜨는 파일이 이전과는 다르긴 합니다.

```plaintext
The ycmd server SHUT DOWN (restart with ':YcmRestartServer'). YCM core library not detected; you need to compile YCM before using it. Follow the instructions in the documentation.
```

- 

## reference

- [github - YouCompleteme - Installation](https://github.com/ycm-core/YouCompleteMe#installation)
- [Vim 에디터 사용법 설명 및 C++/Python 개발환경설정](https://edward0im.github.io/technology/2020/09/17/vim/)
- [[BUG] Fatal Python error: PyMUTEX_LOCK(gil->mutex) failed #3081](https://github.com/pybind/pybind11/issues/3081)
- [github - YouCompleteMe - Troubleshooting](https://github.com/ycm-core/YouCompleteMe/wiki/Troubleshooting-steps-for-ycmd-server-SHUT-DOWN)
- [github - vim auto completion - YouCompleteMe](https://johngrib.github.io/wiki/vim-auto-completion/#youcompleteme)
