---
title: Java - Data Structure - Tree
category: java
tags: java DataStructure programming list class Tree
---

## Java - Data Structure - Tree

- java를 사용해서 tree를 만들어봤습니다. childNode의 개수에는 제한이 없고, 다음 method를 구현하였습니다.
  - `addChildNode`: 자식 Node를 집어넣는다.
  - `findNode`: Node가 존재하는지 찾는다.
  - `getHeight`: tree의 길이를 계산한다.
  - `getSize`: tree의 Node의 개수를 센다.

```java
import java.util.*;

class Main {
    public static class TreeNode<ValueType> {
        public ValueType value;
        public TreeNode<ValueType> parentNode;
        public List<TreeNode<ValueType>> childrenNodes;

        public TreeNode(ValueType value) {
            this.value = value;
            this.parentNode = null;
            this.childrenNodes = new ArrayList<>();
        }
        public TreeNode<ValueType> addChildNode(ValueType value) {
            TreeNode<ValueType> newNode = new TreeNode<>(value);
            this.childrenNodes.add(newNode);
            newNode.parentNode = this;
            return newNode;
        }
        public TreeNode<ValueType> findNode(ValueType value) {
            // from root
            if (this.value == value) {
                return this;
            } else {
                TreeNode<ValueType> returnNode = null;
                for (TreeNode<ValueType> childNode : this.childrenNodes) {
                    TreeNode<ValueType> tempNode = childNode.findNode(value);
                    if ( tempNode != null) {
                        returnNode = tempNode;
                        break;
                    } else {
                        continue;
                    }
                }
                return returnNode;
            }
        }
        public int getHeight() {
            if (this == null) {
                return 0;
            } else {
                int maxHeight=0;
                for (TreeNode<ValueType> node : this.childrenNodes) {
                    int tempHeight = node.getHeight();
                    if (maxHeight <= tempHeight) {
                        maxHeight = tempHeight;
                    }
                }
                return maxHeight + 1;
            }
        }
        public int getSize() {
            if (this == null) {
                return 0;
            } else {
                int r = 1;
                for (TreeNode<ValueType> eachChildNode : this.childrenNodes) {
                    r += eachChildNode.getSize();
                }
                return r;
            }
        }
        public boolean isFullBinary() {
            if (this.childrenNodes.size()==2) {
                TreeNode<ValueType> leftNode  = this.childrenNodes.get(0);
                TreeNode<ValueType> rightNode = this.childrenNodes.get(1);
                if (leftNode.getSize() == rightNode.getSize()) {
                    if (isPowerOfTwo(leftNode.getSize() + 1)) {
                        return leftNode.isFullBinary() & rightNode.isFullBinary();
                    } else {
                        return false;
                    }
                } else {
                    return false;
                }
            } else if (this.childrenNodes.size()==0) {
                return true;
            } else {
                return false;
            }
        }
        public List<ValueType> leafNodes() {
            List<ValueType> returnedValueLst = new ArrayList<>();
            if (this.childrenNodes.size()==0) {
                returnedValueLst.add(this.value);
            } else {
                for (TreeNode<ValueType> node: this.childrenNodes) {
                    returnedValueLst.addAll(node.leafNodes());
                }
            }
            return returnedValueLst;
        }
    }
    public static void main(String[] args) throws Exception {
        TreeNode<Integer> rootNode = new TreeNode<Integer>(0);

        rootNode.addChildNode(1);
        rootNode.addChildNode(2);
        rootNode.addChildNode(3);
        rootNode.childrenNodes.get(0).addChildNode(4);
        rootNode.findNode(2).addChildNode(5);

        System.out.println(rootNode.getSize()); // 6
        System.out.println(rootNode.getHeight()); // 3

    }
}
```
