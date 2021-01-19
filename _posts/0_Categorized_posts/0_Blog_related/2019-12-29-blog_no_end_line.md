---
title: No newline at end of file
category: others
tags: blog jekyl EOF
---

## problem definition

- 요즘 블로그를 조금씩 고치고 있습니다. 늘 그렇듯이, 하나씩 고치다보면 다른 문제점들이 새롭게 생겨나고, 결국 전체를 다 뒤엎어 버려야 그나마 정상적으로 굴러가게 됩니다. 네, 저 같은 실력 없는 개발자들이 항상 하는 하게 되는 노가다지요. 
- 아무튼 블로그를 고치는 중에, `_layouts` 폴더의 yml 파일을 고쳐서 커밋 후 깃헙에 푸쉬를 날렸는데 정상적으로 페이지가 만들어지지 않는 것이죠.
- 그리고 에러 메세지는 `No newline at end of file`이었죠. 즉, "파일 끝에 새로운 줄이 없다"라는 말입니다. 

## solve it easily

- 뭐 고치는 건 문제가 아닙니다. 그리고 한 줄이 아니라, 공백이 필요한 경우도 있어서 웬만하면 공백 + 한 줄 이렇게 넣어주면 해결 되긴 합니다. 

## why it matters?

- 문제는, 이게 왜 중요하냐는 것이죠. 왜 이게 필요할까요?. 
- [stackoverflow - Why should text files end with a newline?](https://stackoverflow.com/questions/729692/why-should-text-files-end-with-a-newline/729773#729773)에 따르면, 다음과 같은 이유로 반드시, 새로운 줄이 추가되어야 한다고 합니다. 

- POSIX 표준에서 'line(한 줄)'이라는 것을 '마지막에 newline char를 포함한 문자들의 조합'으로 정의하고 있기 때문이죠.

> 3.206 Line A sequence of zero or more non- newline characters plus a terminating newline character.

- 따라서, 만약 newline 문자로 끝나지 않는 줄들은 실제 라인으로 고려되지 않습니다. 그것이, 몇몇 프로그램들에서 마지막 라인에 개행문자가 없을 때, 에러가 발생하는 원인이기도 하죠. 

- 또한, 일반 프로그램에서보다, 이는 terminal에서 작업을 할 때, 분명히 이점이 되는 표준인데, 가령 n개 이상의 문자열들을 합친다고 하면 다음과 같이 진행됩니다. 즉 파일을 3개 붙인 것이지만, 결과적으로는 파일간의 차이가 명확히 구분되지 못하죠. 

```bash
$ more a.txt
foo
$ more b.txt
bar$ more c.txt
baz
$ cat {a,b,c}.txt
foo
barbaz
```

## wrap-up

- '개행'이라는 말도, 'newline'이라는 말도 사실 좀 낯설게 느껴집니다. 오히려, 과거에 C를 공부할 때 쓰던 **EOF(End Of File)**이 더 분명하게 느껴져요. 즉, 파일들 끝에, 파일이 끝났음을 명확하게 알려주는 표시를 해줘야 한다는 것이죠. 

## reference

- [No Newline at End of File](https://thoughtbot.com/blog/no-newline-at-end-of-file)
- [stackoverflow - No newline at end of file](https://stackoverflow.com/questions/5813311/no-newline-at-end-of-file)
- [stackoverflow - Why should text files end with a newline?](https://stackoverflow.com/questions/729692/why-should-text-files-end-with-a-newline/729773#729773)
