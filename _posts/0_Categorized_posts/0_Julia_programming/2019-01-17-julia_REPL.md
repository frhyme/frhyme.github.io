---
title: What is REPL?
category: others
tags: REPL programming
---

## REPL??

- julia에 관한 책들을 요즘 시간 날때 종종 보고 있습니다. 그런데 REPL이라는 말이 나오는데, python에서도 유사한 개념을 봤었는데, 대충 넘어갔던 것 같아서, 이번에 REPL이 무엇을 지칭하는지 명확하게 정리해두려고 합니다. 

- [위키피디아에서는 다음처럼 정리되어 있습니다.](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop). interactive toplevel과 동일한 말인데(그냥 쥬피터 노트북, ipython 같은 거라고 생각하시면 되는 것 같습니다). single user input을 받고, evaluation하고, 그 결과를 돌려주고, 이를 다시 반복할 수 있도록 하는 것을 REPL이라고 하는 것 같습니다. 

> A read–eval–print loop (REPL), also termed an interactive toplevel or language shell, is a simple, interactive computer programming environment that takes single user inputs (i.e., single expressions), evaluates them, and returns the result to the user; a program written in a REPL environment is executed piecewise. 

- 다시 정리해보면, 다음과 같겠네요. 
    - Read: 유저가 전달한 커맨드를 읽고
    - Evaluate: 커맨드를 실행하고 
    - Print: 결과를 보여주고 
    - Loop: 다시 처음으로 돌아감. 

## explorative programming

- 이와 같은 REPL은 [explorative programming](https://en.wikipedia.org/wiki/Exploratory_programming)에 유용하다고 합니다. 
- explorative programming은 해당 도메인을 정확하게 이해하고 있지 못할 때 진행하는 software engineering 방법 중 하나를 말합니다. 비슷하게 edit-compile-run-debug의 시스템이라고 할 수 있겠네요. 
- 기존의 전통적인 소프트웨어 시스템에서는 요구사항을 명확하게 정의하고, 그이후에 하나씩 프로그램을 개발하는 형태로 개발되었다면, explorative programming의 경우는 그 반대로, 일단 실행하면서, 요구사항을 계속 새롭게 정의하면서 진행하는 소프트웨어 엔지니어링 방식인 것으로 보입니다. 물론 둘 중에 무엇이 더 좋다, 라는 말은 할 수 없고, 차이가 있는 것일 뿐이죠.