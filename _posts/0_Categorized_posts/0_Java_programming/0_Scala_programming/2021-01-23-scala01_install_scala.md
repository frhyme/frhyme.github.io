---
title: Scala - Install scala
category: scala
tags: scala programming install brew intellij REPL
---

## Scala - Install scala

- 그냥 `brew install scala`를 사용해서 설치하면 됩니다.

```plaintext
$ brew install scala
Updating Homebrew...
==> Auto-updated Homebrew!
Updated 2 taps (homebrew/core and homebrew/cask).
==> New Formulae
aliddns                                            crane                                              ko                                                 luv
==> Updated Formulae
Updated 143 formulae.
==> New Casks
aegisub                                  kieler                                   prezi-video                              spotter                                  the-unofficial-homestuck-collection
==> Updated Casks
Updated 175 casks.
==> Deleted Casks
evom                              irip                              ringtones                         ripit                             tagalicious                       teamspeak-client

==> Downloading https://downloads.lightbend.com/scala/2.13.4/scala-2.13.4.tgz
######################################################################## 100.0%
==> Caveats
To use with IntelliJ, set the Scala home to:
  /usr/local/opt/scala/idea
==> Summary
🍺  /usr/local/Cellar/scala/2.13.4: 42 files, 23.4MB, built in 8 seconds
```

- scala을 설치하고 난 다음 terminal에 `scala`를 치면 다음처럼 REPL로 scala를 실행할 수 있습니다.

```plaintext
$ scala
Welcome to Scala 2.13.4 (OpenJDK 64-Bit Server VM, Java 15.0.1).
Type in expressions for evaluation. Or try :help.

scala> var a = 10
var a: Int = 10

scala> 
```

## Run Scala in Intellij

- IntelliJ에서 scala를 실행하기 위해서, scala 프로젝트를 만들어줍니다.
- `Scala > IDEA` 를 선택하여, "IDEA-based Scala project"로 설정해줍니다. 
- 이때 기 설치된 scala sdk도 선택해줍니다. 
- 그리고 `src > main.scala`를 만들고 다음 코드를 작성해줍니다. 가끔 아래 코드에서 오류가 나는 경우가 있는데, 그때는 다시 scala sdk를 설정해주면 됩니다.

```scala
// main.scala
object HelloWorld {
  def main(args: Array[String]) {
    println("Hello, Scala World!")
  }
}
```

```plaintext
Hello, world!

Process finished with exit code 0
```
