---
title: Shell - 파일 내에 특정 문자열이 존재하는지 찾기
category: shell
tags: grep shell linux unix
--- 

## Shell - 파일 내에 특정 문자열이 존재하는지 찾기

- shell에서 작업을 하다 보면, 파일 내에 특정한 문자열이 있는지, 있다면 어디에 있는지 검색해야 할 때가 있습니다.
- [stackoverflow - how do i find all files containing specific text on linux](https://stackoverflow.com/questions/16956810/how-do-i-find-all-files-containing-specific-text-on-linux)에 자세한 내용이 나와있는데요. 해당 내용을 정리하면 다음과 같습니다.

## grep - Global search for Regular expression and Print out

- grep 은 file 내에서 정규표현식(Regular expression)에 패턴을 찾느 명령어죠. 다음과 같은 argument들이 있습니다.
  - `-r`: recursive 하게 탐색, 즉 folder 나올 경우 해당 folder 내 모든 file에 대해 동일 명령어를 수행
  - `-n`: 검색 결과 앞에 line number를 함께 표시
  - `-w`: 단어 단위로 매칭합니다. 만약 'a'를 찾을 때 'abc'에서는 'a' 가 단어로 처리되지 않으므로 존재하지 않는 것으로 결과가 나옵니다.
  - `-I`: binary 파일은 검색하지 않음
- 따라서 다음처럼 검색하면 됩니다.

```sh
grep -rn '/path/to/somewhere/' -e 'pattern
```

## Reference

- [stackoverflow - how do i find all files containing specific text on linux](https://stackoverflow.com/questions/16956810/how-do-i-find-all-files-containing-specific-text-on-linux)
