---
title: go006 - go rountine
category: golang
tags: go golang routine
---

## go006 go rountine

- in go language, it is so easy to use mutliple tasking by using go routine. simple code is like below. On other language like python, if I want to use multiple processing, I have to import other libraries like `multiprocessing`, but, on go language multiple processing is default provided.
- each go rountine operates on single thread, and each thread use each CPU core. It means that go rountine doesn't require context switching cost on switching thread. When switching thread, CPU keep the context of existing thread, but if each thread only operates on each CPU(forever), they don't need to save existing context of thread. Therefore, In go lang, like what I said before, each thread is operated on each CPU Core. Maybe it sounds like a little difficult, in detail, One CPU core has one thread, one thread has one go routine. If there are two CPU Core, just two threads could be operating at same time. When there are more go rountine than the number of CPU core, go routine is changed on same thread. Switching go routine on same OS thread is not context switching and it doesn't require lots of cost like switching thread on CPU core. Because of that reason, go routine is more light weight than thread.

```go
package main

import "fmt"
import "time"

func PrintNumbers() {
    for i :=1; i <= 5; i++ {
        time.Sleep(400 * time.Millisecond)
        fmt.Printf("%d ", i)
    }
}

func PrintAlphabet() {
    alphabets := []rune{'a', 'b', 'c', 'd', 'e', 'f'}
    for _, each_alphabet := range alphabets {
        time.Sleep(300 * time.Millisecond)
        fmt.Printf("%c ", each_alphabet)
    }
}

func main() {
    /*
    To run this code
    go build this_file.go
    ./this_file
    */
    fmt.Printf("== go rountine\n")
    go PrintNumbers()
    go PrintAlphabet()

    // time.Sleep(3 * time.Second) 부분이 없을 경우
    // 위의 go rountine 이 종료되기 전에 먼저 main rountine이 종료됩니다.
    // 따라서, sub routine들인 PrintNumbers(), PrintAlphabet() 가 실행되도록
    // 하려면 main routine을 종료시키지 않고 있어야 하죠
    time.Sleep(3 * time.Second)

    fmt.Printf("== go rountine finished\n")
}
```
