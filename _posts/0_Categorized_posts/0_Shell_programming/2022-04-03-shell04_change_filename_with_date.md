---
title: Shell 04 - Change filename with Date
category: shell
tags: shell date filename
---

## Shell 04 - Change filename with Date

- 저는 jekyll을 이용하여 블로그에 글을 올립니다. 음 정확히 말하면 markdown file을 jekyll을 이용하여 html file로 변환해주고 link를 만들어준다, 정도로 해석하면 될 것 같아요.
- 아무튼, 마크다운 파일이 블로그에 등록되려면 `2022-04-03-title.md`의 형태로 존재해야 합니다.
- 보통 블로그에 글을 올리기 위한 작업 순서는 다음과 같이 진행되는데요.

1. `title.md` file을 만들고 draft로 내용을 막 작성한다.
1. 글이 완료되면, `title.md` file을 `2022-04-03-title.md`와 같은 형태로 filename을 변경해 준다.
1. `git commit`을 한다.

- 이 때, `title.md` file을 `2022-04-03-title.md`와 같은 형태로 filename을 변경해 주는 과정이 꽤나 번거롭습니다. 별거 아닌데 특수 문자가 들어가 있어 오타가 날 때도 있고, 가끔 오늘 날짜가 며칠인지 헷갈려서 다시 쓸 때도 있고요.

## make shell script file

- 이를 해결하기 위해서 아주 간단한 shell script file을 작성했습니다.
- home directory에 `change_filename_with_date.sh` 파일을 만들고 다음 내용을 작성해줍니다.

```sh
# 2022-04-03 (Sun) - sng_hn.lee - Init
mv $1 `date +%F-`$1
```

- command line에서 다음 command를 사용하여 해당 파일의 이름을 변경해줍니다.

```sh
./change_filename_with_date.sh title.md
```
