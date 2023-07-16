---
title: go007 go routine with channel
category: golang
tags: go golang routine
---

## go007 - go routine with channel

- go routine with channel

```go
package main
import (
    "fmt"
    "sync"
    "time"
)

func main() {
    var wg sync.WaitGroup
    // 1. make channel
    ch := make(chan int)

    wg.Add(1)

    // 2. create go routine
    go square(&wg, ch)
    // 4. put input in channel
    ch <- 9
    // 5. Waif fot the whole waitGroup are finished
    wg.Wait()
    // 8. main routine done
}

func square(wg *sync.WaitGroup, ch chan int) {
    // 3. there is nothing in channel
    // so waiting for it
    n := <- ch

    // 6. get number from channel
    // and run these code
    time.Sleep(time.Second)
    fmt.Printf("Square: %d\n", n*n)
    // 7. this wait group were done
    wg.Done()
}
```

## deadlock

- By default, channels in Go do not have any buffer, which means that sending a value on a channel will block until another goroutine is ready to receive the value. If there are no goroutines actively attempting to receive from the channel, and the channel has no buffer to temporarily store the value, the main routine or the sending routine will wait indefinitely for a receiver to become available. This situation leads to a deadlock.
- To avoid such deadlocks, it is important to ensure that there is a corresponding receiver for every value being sent on a channel, or utilize buffering in the channel to allow for temporary storage. Deadlocks can be prevented by carefully coordinating the sending and receiving operations on channels, ensuring that both sides are ready and available to proceed.

```go
package main
import (
    "fmt"
)

func main() {
    // 1. make channel with buffer 0
    ch := make(chan int)

    // 2. put value to channel
    ch <- 9
    // channel doesn't have buffer at all
    // main routine stopped and waiting for forever
    // So, deadlock occurred
    fmt.Println("== no go routine takes parameter from channel")
}
```
