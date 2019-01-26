---
title: homoiconicity가 무엇인가? 
category: others
tags: homoiconicity programming-language
---

## What is homoiconicity

- 최근에 언어 julia를 좀 파보다가, julia라는 언어가 lisp에서 가져온 homiconicity를 가지고 있다고 하더군요. 공부를 하다보면, 생각보다 훨씬 자주 Lisp라는 언어를 만나고 합니다.
- 아무튼 간에, 그러한 이유로 좀 찾다가 정리를 하고 있습니다. 
- 위키피디아에서 작성된 내용에 의하면 homiconicity는 다음과 같다고 합니다. 

> In homoiconic languages, all code can be accessed and transformed as data, using the same representation. This property is often summarized by saying that the language treats "code as data".

- 한국어로 변환하자면, 모든 코드는 데이터로서 접근 및 변환될 수 있다. 따라서, 간략히 말하자면 homoiconic language에서는 "모든 code는 data다"라고 할 수 있다는 것이죠.
- 조금 더 쉽게 말하면, 모든 코드는 abstract syntax tree의 형태로 표현되고, abstract syntax tree 또한 리스트다, 라고 해석되는 것을 말합니다. 코드를 abstract tree의 형태, 자료 구조의 형태로 저장하고, 이를 필요할 때, 저장해두는 것도 가능하지만, eval해서 실행하는 것도 가능하다는 이야기죠. 
- 즉, 코드가 코드를 데이터로 관리하고, 필요할때만 가져온다 뭐 그런 이야기인데, 아무래도 직접 실행하면서 보면 더 좋을 것 같네요. 

## meta-programming 

- homoiconicity를 이용한 프로그래밍 스킬이 meta-programming이라고 합니다. 

> Metaprogramming is a programming technique in which computer programs have the ability to treat other programs as their data. It means that a program can be designed to read, generate, analyze or transform other programs, and even modify itself while running.

- 위키피디아에 의하면, 다음처럼 프로그램 자체를 데이터로서 인식하고, 프로그램을 읽고, 쓰고, 분석하고, 변환 및 수정하는 것을 심지어 프로그램이 운영되고 있는 상황에서 할 수 있다는 말입니다. 
- 쓰고 보니, homoiconicity와 매우 유사하다고 할 수 있겠네요. 여기서는 code 자체를 first-class data type으로 받아들인다고 합니다. 이 말인즉슨, 모든 것은 코드이자 데이터, 즉 homoiconicity를 적극 반영하고 있는 것이다, 라고 할 수 있는 것이죠. 


### meta-programming in julia 

- lisp는 어떻게 실행해야 하는지 모르겠고, 또 저에게 능숙한 언어가 아니라서, 일단은 Julia에서 meta-programming을 해보기로 했습니다. 
- 찾아보니 이미 [meta-programming in julia](https://docs.julialang.org/en/latest/manual/metaprogramming/)라는 튜토리얼도 있구요. [julia-box](https://www.juliabox.com/)에서 실행하면 좋습니다. 


```julia
prog = "1 + 1" #현재는 스트링, 
println(prog, " ==> ", typeof(prog))
ex1 = Meta.parse(prog)# paring하면 symbolic expression, 혹은 abstract syntax tree가 list의 형태로 수행된다고 생각해도 됨. 
println(ex1, " ==> ", typeof(ex1))
println(ex1.head) ## abstract syntax tree의 꼭대기놈인듯. 
println("----------")
println(ex1.args)## 내부의 값들은 모두 다음 array의 형태로 저장됨 
println(eval(ex1))## 지금은 이 expr을 실행하면 2이지만, 
ex1.args = Any[:-, 1, 1]## 내부의 argument를 바꾸고 
println(eval(ex1))## 실행하면, 0이 됨.
"""
이처럼 code 또한 자료구조의 형태로 관리되기 때문에, 특정한 위치의 값들을 변경해서 사용할 수 있음. 
"""
ex2 = Expr(:call, :-, 1, 1)
println(ex1==ex2)## string으로 넣어서 parsing한 것과, 바로 Expr의 형태로 변환한 것이 동일합니다. 
```

```
1 + 1 ==> String
1 + 1 ==> Expr
call
----------
Any[:+, 1, 1]
2
0
true
```

## Is python homoiconic language?

- python에서도 eval이 있다, 따라서 해당 언어를 homoiconic language라고 할 수 있나? 
    - python에서도 코드를 스트링으로 저장하고, 해당 코드를 실행할 수 있습니다만, 해당 코드는 그냥 string으로 존재할 뿐이지, symbolic expression의 형태로 수행되는 것이 아닙니다. 따라서, 그냥 코드를 인터프리터로 돌려주는 것 뿐, homoiconicity라고 하기에는 어려움이 있습니다. 

## wrap-up

- julia tutorial에 macro등이 쭉 있었는데, 이건 일단 제가 해석하기로는 반복되는 부분을 한번에 변환해주는 뭐 그런겁니다. 이를 통해서 code reuse를 높일 수 있다고 하는데, 이건 솔직히 잘 모르겠네요. 