---
title: Java - Data Structure - Ternary Tree
category: java
tags: java DataStructure programming list class Tree
---

## Java - Data Structure - Ternary Tree

- Java로 3명의 child를 가지는 Tree를 구현했습니다.

```java
import java.util.*;

class Main {
    public static class TreeNode<ValueType> {
        public ValueType value;
        public TreeNode<ValueType> parentNode;
        public TreeNode<ValueType> leftNode;
        public TreeNode<ValueType> midNode;
        public TreeNode<ValueType> rightNode;

        public TreeNode(ValueType value) {
            this.value = value;
            this.parentNode = null;
            this.leftNode = null;
            this.midNode = null;
            this.rightNode = null;
        }
        public TreeNode<ValueType> addNode(ValueType value, String whichChild) {
            if (whichChild.equals("left")) {
                this.leftNode = new TreeNode<>(value);
                return this.leftNode;
            } else if (whichChild.equals("mid")) {
                this.midNode = new TreeNode<>(value);
                return this.midNode;
            } else if (whichChild.equals("right")) {
                this.rightNode = new TreeNode<>(value);
                return this.rightNode;
            } else {
                return null;
            }
        }
        public TreeNode<ValueType> findRootNode() {
            if (this.parentNode == null) {
                return this;
            } else {
                return this.parentNode.findRootNode();
            }
        }
        public TreeNode<ValueType> setValue(ValueType value) {
            this.value = value;
            return this;
        }
        public int getSize() {
            int r = 1;
            if (this.leftNode != null) {
                r += this.leftNode.getSize();
            }
            if (this.midNode != null) {
                r += this.midNode.getSize();
            }
            if (this.rightNode != null) {
                r += this.rightNode.getSize();
            }
            return r;
        }
    }
    public static TreeNode<Integer> fullTernaryTreeNode(int startX, int depth) {
        TreeNode<Integer> rootNode = new TreeNode<Integer>(startX);
        if (depth==0) {
            return rootNode;
        } else {
            rootNode.leftNode  = fullTernaryTreeNode(startX * 3 + 1, depth - 1);
            rootNode.midNode   = fullTernaryTreeNode(startX * 3 + 2, depth - 1);
            rootNode.rightNode = fullTernaryTreeNode(startX * 3 + 3, depth - 1);
            return rootNode;
        }
    }
    public static void preOrderTraversal(TreeNode<Integer> rootNode) {
        if (rootNode != null) {
            System.out.println(rootNode.value);
            preOrderTraversal(rootNode.leftNode);
            preOrderTraversal(rootNode.midNode);
            preOrderTraversal(rootNode.rightNode);
        } else {
        }
    }

    public static void main(String[] args) throws Exception {
        TreeNode<Integer> rootNode = fullTernaryTreeNode(0, 2);
        preOrderTraversal(rootNode);
    }
}
```
