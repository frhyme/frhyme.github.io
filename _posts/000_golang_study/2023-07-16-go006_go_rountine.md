---
title: go006 - go rountine
category: golang
tags: go golang routine
---

## go006 go rountine

- in the Go language, utilizing multiple tasks with goroutines is incredibly simple. Unlike other languages like Python, where you would need to import additional libraries like "multiprocessing" to achieve multiprocessing, Go language provides multiple processing as a default feature.
- Each goroutine in Go operates on a single thread, utilizing a dedicated CPU core. This eliminates the need for costly context switching when switching between threads. Since each thread exclusively operates on its assigned CPU core, there is no need to save the context of the existing thread during thread switching. Consequently, in Go language, each thread operates on its respective CPU core, aligning with the concept mentioned earlier. Although it may initially seem complex, in reality, each CPU core corresponds to one thread, and each thread corresponds to one goroutine. If there are two CPU cores, then two threads can simultaneously execute. However, when the number of goroutines exceeds the available CPU cores, the goroutines are switched on the same thread. This type of goroutine switching on the same OS thread is not considered context switching and does not incur significant costs, unlike switching threads on CPU cores. This lightweight nature of goroutines stems from this particular design principle.

### simple use of go routine

- The code provided illustrates the fundamental usage of goroutines. As previously mentioned, leveraging multiprocessing in Go language is incredibly straightforward and user-friendly.

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

### sync with go routine

- In the above code, while utilizing multiprocessing allows us to perform multiple tasks concurrently, it becomes challenging to determine when all the tasks have completed. However, with the inclusion of a WaitGroup object, we can overcome this challenge.

```go
package main

import (
    "sync"
    "fmt"
)
// wg was declared globally
// because wg was called by function sumAtoB
// and also called by main function
var wg sync.WaitGroup

func sumAtoB(a, b int) {
    sum := 0
    for i := a; i <= b; i++ {
        sum += i
    }
    fmt.Printf("Sum from %d to %d: %d \n", a, b, sum)
    // when the routine is over, call the Done method of waitGroup
    wg.Done()
}

func main() {
    // wait for the 10 jobs were done
    // it also means waitGroup is waiting
    // until wg.Done() called 10 times
    wg.Add(10)

    for i := 0; i < 10; i++ {
        go sumAtoB(1, 10000)
    }

    // main routine is not over until 10 job were done
    wg.Wait()

    fmt.Println("== All computations were done")
}
```

## Wrap-up

- While Go language offers convenient features for multiprocessing, it doesn't necessarily guarantee that code containing multiprocessing will be easy to understand. Like in any language, when dealing with multiprocessing, the code can become more complex and harder to comprehend.
- In general, it is preferable to have code that can be read sequentially, line by line. However, when working with multiprocessing in Go, it may require reading and understanding multiple lines of code together to grasp the overall flow. This can give the impression of a "goto" command, where the control jumps between different parts of the code.
- It's important to strike a balance between utilizing the benefits of multiprocessing and maintaining code readability. Organizing the code structure, providing clear comments, and following best practices can help mitigate the complexity and enhance the understandability of multiprocessing code in Go or any other language.
