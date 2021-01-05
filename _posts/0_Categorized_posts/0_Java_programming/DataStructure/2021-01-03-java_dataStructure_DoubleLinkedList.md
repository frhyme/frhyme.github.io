---
title: Java - Data Structure - Double Linked List 
category: java
tags: java DataStructure programming list class 
---

## Java - Data Structure - Double Linked List 

- Java에서 Linked List를 만들었습니다.

### Node for DoubleLinkedList

- 우선 `Node`를 아래와 같이 설계했습니다. 
- 얘를 외부에 따로 만들어줘도 문제가 없기는 한데, 저는 `DoubleLinkedList` 내에 `static`으로 만들 겁니다.

```java
public static class Node<ValueType> {
    /*
    * @ValueType은 Node에 담겨야 하는 타입을 말합니다. 가령 Integer, Double, String*/
    private ValueType value;
    private Node<ValueType> nextNode;
    private Node<ValueType> prevNode;

    Node(ValueType value, Node<ValueType> prevNode, Node<ValueType> nextNode) {
        this.value = value;
        this.prevNode = prevNode;
        this.nextNode = nextNode;
    }
    // Access Node Neighbour
    ValueType getValue() {
        return this.value;
    }
    Node<ValueType> getPrevNode() {
        return this.prevNode;
    }
    Node<ValueType> getNextNode() {
        return this.nextNode;
    }
    // Check Node Existence
    boolean hasNextNode() {
        if (this.nextNode != null) {
            return true;
        } else {
            return false;
        }
    }
    boolean hasPrevNode() {
        if (this.prevNode != null) {
            return true;
        } else {
            return false;
        }
    }
}
```

### Java - DoubleLinkedList

- 아래와 같이 DoubleLinkedList를 만들어줍니다.

```java
package com.company;

public class DoubleLinkedList<ValueType> {
    public static class Node<ValueType> {...}

    private Node<ValueType> head;
    private Node<ValueType> tail;
    private int size;

    public DoubleLinkedList() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    // Access Head, Tail
    public Node<ValueType> getHead() {
        return this.head;
    }
    public Node<ValueType> getTail() {
        return this.tail;
    }
    // Check DoubleLinkedList size;
    public int size() {
        return this.size;
    }
    public boolean isEmpty() {
        return this.size == 0;
    }
    public String toString() {
        Node<ValueType> pointer = this.head;
        String resultStr = "";

        while (true) {
            resultStr += pointer.value;
            resultStr += " ";
            if (pointer.hasNextNode()) {
                pointer = pointer.nextNode;
            } else {
                break;
            }
        }
        return resultStr;
    }

    // Add new Node
    public void addHead(ValueType newValue) {
        // 앞으로 집어넣기
        Node<ValueType> pointer = new Node<>(newValue,null, this.head);

        if (this.head != null) {
            this.head.prevNode = pointer;
        }
        this.head = pointer;

        if (this.tail == null) {
            this.tail = pointer;
        }
        this.size += 1;
    }

    public void addTail(ValueType newValue) {
        // 뒤로 집어넣기
        Node<ValueType> pointer = new Node<>(newValue, tail, null);

        if (this.tail != null) {
            this.tail.nextNode = pointer;
        }
        this.tail = pointer;

        if (this.head == null) {
            this.head = pointer;
        }
        this.size += 1;
    }

    // Remove node
    public void removeHead() {
        if (this.size != 0) {
            this.head = this.head.nextNode;
            this.head.prevNode = null;
            this.size -= 1;
        } else {
        }
    }
    public void removeTail() {
        if (this.size != 0) {
            this.tail = this.tail.prevNode;
            this.tail.nextNode = null;
            this.size -= 1;
        } else {
        }
    }
}
```

- 아래와 같이 간단하게 테스트를 해보면 잘 되는 것을 알 수 있죠.

```java
import java.util.*;
import com.company.DoubleLinkedList;

class Main {
    public static void main(String[] args) throws Exception {
        DoubleLinkedList<Integer> doubleLinkedList = new DoubleLinkedList<>();

        doubleLinkedList.addHead(1);
        doubleLinkedList.addHead(2);
        doubleLinkedList.addHead(3);
        doubleLinkedList.addHead(4);
        doubleLinkedList.addTail(5);
        System.out.println(doubleLinkedList.toString());
        doubleLinkedList.removeHead();
        System.out.println(doubleLinkedList.toString());
        doubleLinkedList.removeTail();
        System.out.println(doubleLinkedList.toString());
    }
}
```

## Raw Code

```java
public class DoubleLinkedList<ValueType> {
    public static class Node<ValueType> {
        /*
        * @ValueType은 Node에 담겨야 하는 타입을 말합니다. 가령 Integer, Double, String*/
        private ValueType value;
        private Node<ValueType> nextNode;
        private Node<ValueType> prevNode;

        Node(ValueType value, Node<ValueType> prevNode, Node<ValueType> nextNode) {
            this.value = value;
            this.prevNode = prevNode;
            this.nextNode = nextNode;
        }
        // Access Node Neighbour
        ValueType getValue() {
            return this.value;
        }
        Node<ValueType> getPrevNode() {
            return this.prevNode;
        }
        Node<ValueType> getNextNode() {
            return this.nextNode;
        }
        // Check Node Existence
        boolean hasNextNode() {
            if (this.nextNode != null) {
                return true;
            } else {
                return false;
            }
        }
        boolean hasPrevNode() {
            if (this.prevNode != null) {
                return true;
            } else {
                return false;
            }
        }
    }

    private Node<ValueType> head;
    private Node<ValueType> tail;
    private int size;

    public DoubleLinkedList() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    // Access Head, Tail
    public Node<ValueType> getHead() {
        return this.head;
    }
    public Node<ValueType> getTail() {
        return this.tail;
    }
    // Check DoubleLinkedList size;
    public int size() {
        return this.size;
    }
    public boolean isEmpty() {
        return this.size == 0;
    }
    public String toString() {
        Node<ValueType> pointer = this.head;
        String resultStr = "";

        while (true) {
            resultStr += pointer.value;
            resultStr += " ";
            if (pointer.hasNextNode()) {
                pointer = pointer.nextNode;
            } else {
                break;
            }
        }
        return resultStr;
    }

    // Add new Node
    public void addHead(ValueType newValue) {
        // 앞으로 집어넣기
        Node<ValueType> pointer = new Node<>(newValue,null, this.head);

        if (this.head != null) {
            this.head.prevNode = pointer;
        }
        this.head = pointer;

        if (this.tail == null) {
            this.tail = pointer;
        }
        this.size += 1;
    }

    public void addTail(ValueType newValue) {
        // 뒤로 집어넣기
        Node<ValueType> pointer = new Node<>(newValue, tail, null);

        if (this.tail != null) {
            this.tail.nextNode = pointer;
        }
        this.tail = pointer;

        if (this.head == null) {
            this.head = pointer;
        }
        this.size += 1;
    }

    // Remove node
    public void removeHead() {
        if (this.size != 0) {
            this.head = this.head.nextNode;
            this.head.prevNode = null;
            this.size -= 1;
        } else {
        }
    }
    public void removeTail() {
        if (this.size != 0) {
            this.tail = this.tail.prevNode;
            this.tail.nextNode = null;
            this.size -= 1;
        } else {
        }
    }
}
```
