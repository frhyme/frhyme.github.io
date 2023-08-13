---
title: Java - Data Structure - Binary Search Tree
category: java
tags: java DataStructure programming list class Tree
---

## Java - Data Structure - Binary Search Tree

- Java에서 Binary Search Tree를 구현했습니다.
- `removeNode`가 꽤나 어려웠는데, 지워야 하는 node의 자식 노드가 2개인지 1개인지(왼쪽인지, 오른쪽인지) 없는지에 따라서 과정이 조금씩 달라집니다. 뿐만 아니라, 이 때, 지운 다음 parentNode도 살아남아 있어야 하기 때문에 이게 좀 성가셨죠. 함수 내부에서 값을 `currentNode`, `parentNode`를 2개 return할 수 있으면 해결되는 문제이기는 했는데요, java에서는 이걸 하기가 어려우니까요.
- 그래서, 하나는 reference로 바로 적용해버리고, 하나는 return으로 처리해서 해결했습니다.

```java
public class BinarySearchTree {
    public static class Node {
        public int key;
        public int value;
        public Node left;
        public Node right;

        public Node(int key, int value) {
            this.key = key;
            this.value = value;
            this.left = null;
            this.right = null;
        }
    }
    public Node root;

    public BinarySearchTree() {
        this.root = null;
    }
    public Node findNode(int targetKey) {
        Node pointer = this.root;
        while (true) {
            if (pointer == null) {
                break;
            } else {
                if (targetKey < pointer.key) {
                    pointer = pointer.left;
                } else if (pointer.key < targetKey) {
                    pointer = pointer.right;
                } else {
                    return pointer;
                }
            }
        }
        return null;
    }
    public Node insertNode(int key, int value) {
        Node newNode = new Node(key, value);
        if (this.root == null) {
            this.root = newNode;
            return this.root;
        } else {
            Node pointer = this.root;
            Node parent = null;

            while (true) {
                parent = pointer;
                if (key < pointer.key) {
                    pointer = pointer.left;
                    if (pointer == null) {
                        parent.left = newNode;
                        break;
                    }
                } else if (pointer.key < key) {
                    pointer = pointer.right;
                    if (pointer == null) {
                        parent.right = newNode;
                        break;
                    }
                }
            }
            return newNode;
        }
    }
    public static Node getMinNode(Node node) {
        if (node.left == null) {
            return node;
        } else {
            return getMinNode(node.left);
        }
    }
    public static Node removeNode(Node node, int key) {
        /*
        * recursive하게 node로부터 출발하하여 key를 가진 node를 찾습니다.
        * 결과로 Node를 리턴하게 되는데, 이를 통해
        * 지워야 하는 node의 상위 노드와 지워야 하는 node를 연결합니다.*/
        if (node == null) {
            return null;
        } else {
            if (key < node.key) {
                // node의 leftNode로부터 출발하여 key를 가진 node를 recursive하게 찾습니다.
                // 그리고 node.left에 넣어줌으로써, node는 빼고 위 아래로 연결해주죠.
                node.left = removeNode(node.left, key);
            } else if (node.key < key) {
                // node의 rightNode로부터 출발하여 key를 가진 node를 recursive하게 찾습니다.
                // 그리고 node.right에 넣어줌으로써, node는 빼고 위 아래로 연결해주죠.
                node.right = removeNode(node.right, key);
            } else {
                // node.key == key
                if (node.left != null && node.right != null) {
                    // node가 왼쪽 오른쪽 자식 모두 가지고 있을 때
                    Node minNodeOfRightTree = getMinNode(node.right);
                    // minNodeOfRightTree의 key, value 값을 node에 넣어줍니다(replace)
                    // 그러나, minNodeOfRightTree와 동일한 node가 아직 존재하죠.
                    node.key = minNodeOfRightTree.key;
                    node.value = minNodeOfRightTree.value;
                    // minNodeOfRightTree를 지워줍니다.
                    // 오른쪽 tree에서 지운 놈이므로 node.right로 설정해줘야 하죠.
                    node.right = removeNode(node.right, minNodeOfRightTree.key);
                }
                else if (node.left != null) {
                    // node가 왼쪽 자식만 있을 때,
                    // node의 왼쪽을 연결
                    node = node.left;
                }
                else if (node.right != null) {
                    // node가 오른쪽 자식만 있으면,
                    // node를 지우고 node의 오른쪽 자식을 연결
                    node = node.right;
                }
                else {
                    // 자식이 없을 때는 그냥 지우면 된다.
                    node = null;
                }
            }
            return node;
        }

    }
    public static void preorderTraversal(Node node) {
        if (node != null) {
            System.out.printf("key: %d, value: %d \n", node.key, node.value);
            preorderTraversal(node.left);
            preorderTraversal(node.right);
        }
    }
    public static void inorderTraversal(Node node) {
        if (node != null) {
            preorderTraversal(node.left);
            System.out.printf("key: %d, value: %d \n", node.key, node.value);
            preorderTraversal(node.right);
        }
    }
    public static int getDepth(Node startNode, Node targetNode) {
        // Depth는 root로부터의 길이를 말합니다.
        Node pointer = startNode;
        int r = 0;
        while (true) {
            if (pointer.key < targetNode.key) {
                r += 1;
                pointer = pointer.right;
            } else if (targetNode.key < pointer.key) {
                r += 1;
                pointer = pointer.left;
            } else {
                break;
            }
        }
        return r;
    }
    public static int getHeight(Node node) {
        // 현재 node부터 가장 긴 길이의 node까지의 길이를 찾습니다.
        if (node == null) {
            return 0;
        } else {
            int leftHeight = getHeight(node.left);
            int rightHeight = getHeight(node.right);
            if (leftHeight > rightHeight) {
                return 1 + leftHeight;
            } else {
                return 1 + rightHeight;
            }
        }
    }
}
```
