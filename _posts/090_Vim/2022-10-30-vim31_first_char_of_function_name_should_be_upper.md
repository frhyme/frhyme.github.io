---
title: vim31 - first char of function name should be upper
category: vim
tags: vim function vi
---

## vim31 - first char of function name should be upper

- vim에서 function을 정의할 때, function name의 첫번째 글자는 대문자(Upper letter)가 되어야 합니다.

```vim
function FunctionName()
endfunction
```

- `:help user-function`를 통해 이유를 확인해 보면 대략 "builtin function 과의 name confusion을 막기 위해서 user defined function의 경우는 upper case를 쓰도록 한다"인 것 같네요.

> The function name must start with an uppercase letter, to avoid confusion with builtin functions.  To prevent from using the same name in different scripts avoid obvious, short names.  A good habit is to start the function name with the name of the script, e.g., "HTMLcolor()".

## Reference

- [stackexchange - do vimscript functions have to start with a capital letter and if so why](https://vi.stackexchange.com/questions/2659/do-vimscript-functions-have-to-start-with-a-capital-letter-and-if-so-why)
