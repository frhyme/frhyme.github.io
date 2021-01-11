---
title: Java - Class - nested Class
category: java
tags: java programming class OOP inheritance polymorphism
---

## Java - Class - nested Class

- 당연하지만, java의 class 내에도 class를 정의할 수 있습니다. static nested class, local inner class로 정의할 수 있죠.
  - static nested class
  - local inner class 

## Java - nested class - static nested class

- static nested class는 class 내에 static하게 정의된 class죠. 보통 OuterClass에서 사용될 수 있는 InnerClass를 정의할 때 사용되는데요. 가령, Tree, Graph등을 정의할 때 각 Node에 대해서도 정의를 해야겠죠. 이런 경우를 Node를 내부에 static inner class로 만들어서 정의합니다.
- 다음에서 `Tree`라는 class를 만들고 내부에 static inner class인 `Node`를 만들었습니다.

```java
public class Tree {
    public static class Node {
        /*
       Node가 바로 static inner class죠.
        */
        public Integer value;
        public Node(Integer value) {
            this.value = value;
        }
    }
    public Node rootNode;
    public Tree(Node rootNode) {
        this.rootNode = rootNode;
    }
}
```

- 그리고, `main`에서 다음처럼 사용할 수 있죠.

```java
import com.company.Tree;

class Main {
    public static void main(String[] args) throws Exception {
        Tree.Node rootNode = new Tree.Node(1);
        Tree tree = new Tree(rootNode);
    }
}
```

## Java - nested class - local inner class

- Local Inner Class는 그냥, method 내에서 직접 정의해서 만드는 class를 말합니다. 이 메소드 내에서만 유효하죠. 메소드를 벗어나면 class를 사용할 수 없습니다.

```java
class Main {
    public static void main(String[] args) throws Exception {
        /*
        Local Inner Class는 
        아래처럼 method 내에 class를 직접 만드는 경우를 말합니다.
        */
        class LocalInnerClass {
            String name = null;
            public LocalInnerClass(String name) {
                this.name = name;
            }
            public void printName() {
                System.out.println("----------------------------");
                String result = String.format("LocalInnerClass: %s", this.name);
                System.out.println(result);
                System.out.println("----------------------------");
            }
        }
        // 이렇게 정의한 클래스를 직접 생성해서 사용할 수도 있죠.
        LocalInnerClass b = new LocalInnerClass("b");
        b.printName();
        // ----------------------------
        // LocalInnerClass: b
        // ----------------------------
    }
}
```
