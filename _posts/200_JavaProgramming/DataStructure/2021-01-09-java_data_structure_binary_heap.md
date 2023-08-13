---
title: Java - Data Structure - Binary Heap
category: java
tags: java DataStructure programming list class Tree Heap
---

## Java - Data Structure - Binary Heap

- Java로 Binary Heap을 구현했습니다.
- Binary Heap은 다음 조건을 만족하는 자료 구조를 말하죠. Heap은 작을수록 우선순위를 가지는 MinHeap과, 클수록 우선순위를 가지는 MaxHeap으로 나뉘는데, 여기서는 MinHeap을 기준으로 설명하겠습니다.
  - 각 node는 node의 subtree중에서 가장 작다. 즉 parent node는 모든 child node보다 값이 작다.
  - complete tree이거나 almost complete tree이다. 이건 binary tree에 대해서 "parent level이 꽉 채워지지 않은 상태에서 child node가 존재할 수 없다"라고 이해하셔도 됩니다. 대략 그림으로 보시죠. 그림을 보면, 왼쪽부터 node가 순차적으로 채워져 있는 것을 알 수 있죠. 이런 형태를 complete binary tree라고 합니다.

![Complete binary tree](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Complete_binary2.svg/440px-Complete_binary2.svg.png)

- Heap은 보통 정렬(sorting)할 때 자주 사용됩니다. Heap을 이용한 정렬을 "HeapSort"라고 부르죠. 
- 정렬되지 않은 list 등에서 Heap을 만들 때는 `O(n)`의 시간이 소요되고, 값을 빼낼 때는 각각 `O(log n)`이 소요됩니다(모든 원소에 대해서 수행한다면 `n * O(log n)`). 따라서, (대략적인) 총 소요시간은 `O(n) + n * O(log n)`이 소요되죠. 
- 특히, 만약 앞의 `k`개만 필요하다면, `O(n) + k * O(log n)`로 단축되게 되죠. 즉, HeapSort는 처음부터 모든 원소를 정렬해두는 것이 아니라, 필요할 때마다 조금씩, `O(log n)`만큼 더 시간이 소요됩니다. 그러므로, 빈번하게 최소 혹은 최대값을 가져오지 않는 경우, 그리고 몇 개의 최소값만 가져오는 경우에 사용하여 시간을 단축할 수 있죠.\

## Java - Binary Heap Implementation

- java를 사용하여 Binary Heap을 구현하였습니다.

```java
public static class MinBinaryHeap {
    /*
    - Binary Tree에서는 보통 Node를 만들어서 처리하지만 
    Heap은 complete Tree이므로 다음과 같이 그냥 List<Integer>로 만들어서 처리했습니다.
    혹은 그냥 Array를 사용해도 되죠. 
    - binary tree의 원소들이 다음의 index를 가진다고 생각하면 됩니다.
    즉, container.get(0)을 하면 root Node인 가장 작은 Node에 접근할 수 있죠.
    0 
    1 2 
    3 4 5 6 
    7 8 9 10
    */
    private List<Integer> container;

    public MinBinaryHeap() {
        // 생성자입니다.
        this.container = new ArrayList<>();
    }
    public void swapNode(int idx1, int idx2) {
        // this.container에서 idx1에 위치한 원소와 idx2에 위치한 우너소를 변경해줍니다.
        Integer temp = this.container.get(idx1);
        this.container.set(idx1, this.container.get(idx2));
        this.container.set(idx2, temp);
    }
    public void insertNode(Integer newValue) {
        // 끝에 새로운 value를 넣어주고, 그 index를 리턴
        // 그리고 들어온 새로운 원소가 heap의 조건인 "parent node가 child node보다 작아야 한다"는 조건을
        // 만족하지 않을 수도 있으므로 minifyHeapBottomToTop를 사용하여 아래에서 위로 진행하며 swap
        this.container.add(newValue);
        this.minifyHeapBottomToTop();

    }
    public Integer extractMin(){
        /*
        - 가장 작은 원소인 rootNode의 값을 리턴하고 Heap 내에서 삭제해줍니다.
        - Heap에서는 이 메소드를 수행할 때, 다음과 같은 순서로 수행됩니다.
          - 가장 작은 값(rootNode)의 값을 리턴하고
          - this.container의 끝의 원소와 rootNode의 값을 변경한 다음, 
          - this.conateinr의 끝의 원소를 삭제해주고(값을 바꾼 후 삭제했으므로 기존 rootNode의 값을 삭제해준 것임)
          - Heap은 parent node의 값이 항상 child node의 값보다 작아야 하는데, 지금 해당 성질을 만족하지 않으므로 해결해준다
          그리고 이 부분을 해결해주는 메소드가 바로 minifyHeapTopToBottom() 입니다.
        */
        if (this.container.size() == 0) {
            return null;
        } else {
            Integer returnInteger = this.container.get(0);
            swapNode(0, this.container.size() - 1);
            this.container.remove(this.container.size() - 1);
            minifyHeapTopToBottom();
            return returnInteger;
        }
    }
    public List<Integer> getContainer() {
        // 그냥 현재 컨테이너를 리턴하는 메소드
        return this.container;
    }
    public int getParentIndex(int childIndex) {
        // 현재 ArrayList에서 childIndex의 부모 주소를 리턴
        return (childIndex - 1) / 2;
    }
    public int getLeftChildIndex(int currentIndex) {
        // 현재 ArrayList에서 childIndex의 왼쪽 자식 주소를 리턴
        int returnIndex = currentIndex * 2 + 1;
        if (this.container.size() <= returnIndex) {
            return -1;
        } else {
            return returnIndex;
        }
    }
    public int getRightChildIndex(int currentIndex) {
        // 현재 ArrayList에서 childIndex의 오른쪽 자식 주소를 리턴
        int returnIndex = currentIndex * 2 + 2;
        if (this.container.size() <= returnIndex) {
            return -1;
        } else {
            return returnIndex;
        }
    }
    public void minifyHeapBottomToTop() {
        /*
        * MinHeap는 child node가 무조건 parent node보다 커야 하는데
        * 마지막에 들어온 원소가 이를 충족시켜주지 못하므로, 아래에서 위로 내려가면서 
        swap을 통해 해결해줌
        */
        int childNodeIndex = this.container.size() - 1;
        int parentNodeIndex = getParentIndex(childNodeIndex);

        while (true) {
            if (childNodeIndex == parentNodeIndex) {
                break;
            } else {
                Integer childNodeValue = this.container.get(childNodeIndex);
                Integer parentNodeValue = this.container.get(parentNodeIndex);

                if (childNodeValue < parentNodeValue) {
                    swapNode(childNodeIndex, parentNodeIndex);
                    childNodeIndex = parentNodeIndex;
                    parentNodeIndex = getParentIndex(childNodeIndex);
                } else {
                    break;
                }
            }
        }
    }
    public void minifyHeapTopToBottom() {
        /*
        * MinHeap는 child node가 무조건 parent node보다 커야 하는데
        * 마지막에 들어온 원소가 이를 충족시켜주지 못하므로, swap을 통해 해결해줌
        * 위에서 아래로 내려가면서 자식 중 작은 놈과 swap을 진행해줍니다.
        */  
        if (this.container.size() != 0) {
            int currentNodeIndex = 0;
            while (true) {
                int leftChildIndex = getLeftChildIndex(currentNodeIndex);
                int rightChildIndex = getRightChildIndex(currentNodeIndex);
                int childIndex = -1;
                if (leftChildIndex == -1 && rightChildIndex == -1) {
                    break;
                } else if (leftChildIndex != -1 && rightChildIndex != -1) {
                    Integer leftChildValue = this.container.get(leftChildIndex);
                    Integer rightChildValue = this.container.get(rightChildIndex);
                    if ( leftChildValue < rightChildValue) {
                        childIndex = leftChildIndex;
                    } else {
                        childIndex = rightChildIndex;

                    }
                    // find which is max between left and right
                    Integer currentNodeValue = this.container.get(currentNodeIndex);
                    Integer childNodeValue = this.container.get(childIndex);
                    if (currentNodeValue < childNodeValue) {
                        break;
                    } else {
                        swapNode(currentNodeIndex, childIndex);
                    }
                } else {
                    if (leftChildIndex != -1) {
                        childIndex = leftChildIndex;
                    } else {
                        childIndex = rightChildIndex;
                    }
                    Integer currentNodeValue = this.container.get(currentNodeIndex);
                    Integer childNodeValue = this.container.get(childIndex);
                    if (currentNodeValue < childNodeValue) {
                        break;
                    } else {
                        swapNode(currentNodeIndex, childIndex);
                    }
                }
            }
        } else {
            // container has nothing
        }
    }
}
```

- 실제로 다음과 같이 실행해보면 잘 되는 것을 알 수 있습니다.

```java
import java.util.*;

class Main {
  public static class MinBinaryHeap {...}
    public static void main(String[] args) throws Exception {
        MinBinaryHeap mbh = new MinBinaryHeap();
        mbh.insertNode(3);
        mbh.insertNode(2);
        mbh.insertNode(1);

        System.out.printf("Extract MIN: %3d, current Heap: %s \n", mbh.extractMin(), mbh.getContainer());
        // Extract MIN:   1, current Heap: [2, 3] 
        System.out.printf("Extract MIN: %3d, current Heap: %s \n", mbh.extractMin(), mbh.getContainer());
        // Extract MIN:   2, current Heap: [3] 
        System.out.printf("Extract MIN: %3d, current Heap: %s \n", mbh.extractMin(), mbh.getContainer());
        // Extract MIN:   3, current Heap: [] 
    }
}
```
