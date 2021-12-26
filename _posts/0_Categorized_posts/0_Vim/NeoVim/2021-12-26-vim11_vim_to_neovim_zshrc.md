---
title: vim11 - default vi - vim to neovim
category: vim
tags: vim vi neovim nvim zsh zsrhc
---

## vim11 - default vi - vim to neovim

- neovim을 설치하고, default vim을 neovim으로 변경합니다.
- `.zshrc`에 다음 명령어를 설치해줍니다.

```zshrc
alias vi="nvim"
```

- 혹시 `bad assignment` 오류가 뜬다면, 해당 명령어가 제대로 입력되지 않은 겁니다. 만약 `=` 앞뒤에 space(공백)이 있다면 지워주시면 됩니다.

### Why space not allowed between equal sign

- 왜 =(equal sign) 앞 뒤로 space가 허용되지 않는지에 대해서는 [stackexchange - why are space not allowed in some bash commands like alias](https://unix.stackexchange.com/questions/410651/why-are-spaces-not-allowed-in-some-bash-commands-like-alias)를 확인하시면 좋은데요. 대략 내용을 정리하자면 다음과 같습니다.
- `alias`라는 명령어는 `alias a="b"`와 같이 특정 명령어에 특정 값을 설정하기 위해서 사용하기도 하지만, `alias a`와 같이 `a`에 매핑되어 있는 명령어가 무엇인지 검색하기 위해서 사용할 수 있기 때문입니다.
- 아래와 같이 `alias a b`의 형태로 쓸 경우, `a`, `b`에 매핑되어 있는 값을 쿼리하죠. 따라서, `alias a = "b"`를 실행할 경우에는 `a`, `=`, `"b"`에 각각 매핑되어 있는 값들을 쿼리하는 명령어로 인식하게 됩니다. 따라서, 오류가 발생하게 되는 것이죠.

```bashrc
$ alias a="a" b="b"
$ alias a b 
a=a
b=b
$ alias a = "b"
zsh: bad assignment
a=a
```

## Reference

- [stackexchange - why are space not allowed in some bash commands like alias](https://unix.stackexchange.com/questions/410651/why-are-spaces-not-allowed-in-some-bash-commands-like-alias)