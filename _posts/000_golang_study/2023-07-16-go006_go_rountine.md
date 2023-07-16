---
title: go006 - go rountine
category: golang
tags: go golang routine
---

## go006 go rountine

- in the Go language, utilizing multiple tasks with goroutines is incredibly simple. Unlike other languages like Python, where you would need to import additional libraries like "multiprocessing" to achieve multiprocessing, Go language provides multiple processing as a default feature.
- Each goroutine in Go operates on a single thread, utilizing a dedicated CPU core. This eliminates the need for costly context switching when switching between threads. Since each thread exclusively operates on its assigned CPU core, there is no need to save the context of the existing thread during thread switching. Consequently, in Go language, each thread operates on its respective CPU core, aligning with the concept mentioned earlier. Although it may initially seem complex, in reality, each CPU core corresponds to one thread, and each thread corresponds to one goroutine. If there are two CPU cores, then two threads can simultaneously execute. However, when the number of goroutines exceeds the available CPU cores, the goroutines are switched on the same thread. This type of goroutine switching on the same OS thread is not considered context switching and does not incur significant costs, unlike switching threads on CPU cores. This lightweight nature of goroutines stems from this particular design principle.

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
