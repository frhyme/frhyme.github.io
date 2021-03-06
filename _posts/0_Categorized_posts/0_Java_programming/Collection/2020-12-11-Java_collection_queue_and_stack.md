---
title: Java - Collection - Queue, Deque
category: java
tags: java programming interface collection Queue Deque Stack
---

## Java - Collection - Queue

- Queue는 우리가 일상에서 흔히 보는 "대기열"이라고 생각하시면 됩니다. 줄이 있으면 보통 맨 뒤에 줄을 서고 가장 먼저 온 사람이 먼저 줄에서 나가게 되죠. 일상 생활에서 가장 많은 형태의 자료구조이며, 이런 행동 패턴을 "먼저 온 사람이 먼저 나간다"는 의미로 First-In-First-Out, FIFO라고 합니다. 즉, 먼저 온 사람에게 우선권주는 형태인 셈이죠.
- 그리고 매우 당연히도 Java에서도 `Queue<T>` Interface가 구현되어 있습니다. `Collection<T>`을 extend하고, 다음의 method들을 새롭게 선언했죠.
  - `boolean offer(T t)`: Queue에 값을 집어넣고, 성공적으로 넣었다면 `true`를 아니라면 `false`를 리턴하죠.
  - `T remove()`: Queue의 Head를 리턴하고, 삭제하고, 비어 있다면 `NoSuchElementException`를 생성합니다.
  - `T poll()`: Queue의 Head를 리턴하고, 삭제하고, 비어 있다면 `null`을 리턴합니다.
  - `T element()`: Queue의 Head를 리턴하고, 삭제하지는 않고, 비어 있다면, `NoSuchElementException`를 생성합니다.
  - `T peek()`: Queue의 Head를 리턴하고, 삭제하지는 않고, 비어 있다면 null을 리턴합니다.
  - `add (T t)`: 값을 집어넣고, 넣을 수 없다면, `IllegalStateException`를 생성합니다.
- 이렇게 쓰고 보면, "야, 이거 Interface라며, 어떻게 method가 구현되어 있냐?"라는 생각이 드실 수 있는데, Queue Interface를 구현한 아이로 `LinkedList<E>`와 `ArrayDeque<E>`가 있습니다. 그리고, `PriorityQueue`도 있는데 얘는 다음에 설명하도록 할게요.
- 그림으로 보면 다음과 같습니다. Iterable(Interface) > Collection(Interface) > Queue(Interface) > Dequeue(Interface) > LinkedList(Class), ArrayDequeue(Class).

    ![Queue_Dequeue_PriorityQyeye](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20200903183026/Queue-Deque-PriorityQueue-In-Java.png)

- 위의 hierarchy에서 보시는 것처럼 ArrayDeque, LinkedList 모두 Deque를 implement합니다. 그냥 Queue의 경우 한쪽으로만 넣고 다른 하쪽으로 빠진다면, Deque는 그냥, 앞으로도 넣을 수도 있고, 뒤로도 넣을 수 있는 자료구조입니다.
- 그리고 보통 ArrayDeque가 LinkedList에 비해서 더 효율적으로 메모리를 사용한다고 알려져 있죠. 

## Dequeue Implementation 

- Deque를 간단하게 구현해 봤습니다.

```java
class Main {
    public static void main(String[] args) throws Exception {
        // Deque이므로 queue도 stack도 될 수 있죠.
        Deque<Integer> DequeueORstack = new ArrayDeque<>();
        // QUEUE method ----------------
        // addLast: element를 뒤에서 넣어줍니다.
        // addFirst: element를 앞에서 넣어줍니다.
        DequeueORstack.addLast(1);
        DequeueORstack.addLast(2);
        DequeueORstack.addFirst(3);
        System.out.println( DequeueORstack ); // [3, 1, 2]

        // peekFirst: 제일 앞에 있는 원소를 값을 확인하고, QUEUE에서 지우지는 않음.
        // peekLast : 제일 뒤에 있는 원소를 값을 확인하고, QUEUE에서 지우지는 않음.
        System.out.println( DequeueORstack.peekFirst() ); // 3
        System.out.println( DequeueORstack.peekLast() ); // 2
        System.out.println( DequeueORstack ); // [3, 1, 2]

        // PollFirst(): 제일 앞에 있는 원소를 리턴하고, QUEUE에서는 지웁니다.
        // PollLast() : 제일 뒤에 있는 원소를 리턴하고, QUEUE에서는 지웁니다.
        System.out.println( DequeueORstack.pollFirst() ); // 3
        System.out.println( DequeueORstack.pollLast() ); // 2
        System.out.println( DequeueORstack ); // [1]
        System.out.println( DequeueORstack.isEmpty() ); // false

        // Stack Method
        // 전통적인 stack method로 사용해도 됩니다.
        // 얘는 LIFO의 형식을 따릅니다.
        // push: 뒤에서 값을 집어넣어줍니다.
        // pop : 뒤에서 값을 줍니다.
        DequeueORstack.push(7);
        System.out.println( DequeueORstack.pop() ); // 7

        /////////////////////////////////////////////
    }
}
```
