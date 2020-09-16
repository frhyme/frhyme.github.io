---
title: 자료구조 - trie
category: python-basic
tags: python python-basic trie data-structure
---

## 문자열을 검색할 때

- 알고리즘 문제들을 풀다보면, 문자열 검색을 해야 하는 일들이 종종 생깁니다. 예를 들어서, N개의 문자열 리스트가 있을 때, 내가 원하는 특정 문자가 해당 N개의 문자열에 있는지 파악하는 것 같은 일들이 비일비재하죠. 
- 뇌없이 코딩할 때는 다음처럼 하면 됩니다. 

```python
str_lst = [...] # N개의 string이 들어가 있는 문자열 리스트 
for s in str_lst:
    if s in str_lst:
        print(s)
        break
```

- 그러나, 이렇게 처리할 경우에는, N이 커질수록 검색하는데 비용이 너무 많이 들죠. 
- 따라서, 보통 이럴 때는 trie라는 자료구조를 이용합니다. 

## trie or suffix-tree

- trie라고 보통 한다고 합니다. re**trie**val에서 따온말이라고 하는데, 워드의 문자를 쪼개서, k진트리로 변환하는 것을 말합니다. 
- 그냥 아래처럼 짜면 되는데요.

```python
class Node(object):
    def __init__(self, key, data=None):
        self.key=key # character 
        self.data=data # 기존 방식에서는 True/False로 집어넣지만, 여기서는 string or None을 집어넣음.
        self.children = {} # 해당 char에서 다른 캐릭터로 이어지는 children character(key)들과 각 Node(value)

class Trie(object):
    def __init__(self):
        self.head = Node(key=None, data=None)
    def insert_string(self, input_string):
        # Trie에 input_string을 넣어줌
        cur_node = self.head
        for c in input_string:
            if c not in cur_node.children.keys():
                cur_node.children[c] = Node(key=c)
            cur_node = cur_node.children[c]
        cur_node.data=input_string
    def search(self, input_string):
        # input_string이 현재 trie에 있는지 찾아서 TF를 리턴 
        cur_node = self.head
        for c in input_string:
            if c not in cur_node.children.keys():
                return False
            else:
                cur_node = cur_node.children[c]
        if cur_node.data==input_string:
            return True
        else:
            return False
    def start_with(self, prefix):
        # prefix로 시작하는 모든 워드를 찾아서 리턴합니다. 
        cur_node = self.head
        words = []
        subtrie = None
        for c in prefix:
            if c in cur_node.children.keys():# 있으므로 값을 하나씩 찾으며 내려감. 
                cur_node = cur_node.children[c]
                subtrie = cur_node
            else:# prefix가 현재 trie에 없으므로, 빈 리스트를 리턴 
                return []
        # 이제 prefix가 존재한다는 것을 알았고, subtrie에 있는 모든 워드를 찾아서 리턴하면 됨. 
        cur_nodes = [subtrie]
        next_nodes = []
        while True:
            for c in cur_nodes:
                if c.data!=None:
                    words+=[c.data]
                next_nodes+=list(c.children.values())
            #print("nn", [n.data for n in next_nodes])
            if len(next_nodes)==0:
                break
            else:
                cur_nodes = next_nodes
                next_nodes = []
        return words
##########################################
t = Trie()
t.insert_string("abcd")
t.insert_string("abdc")
t.insert_string("acbd")
t.insert_string("abkd")
t.insert_string("abzzzz")
t.search('abdc')
t.start_with('ab')
```

## reference

- [파이썬에서 Trie 구현하기](https://blog.ilkyu.kr/entry/파이썬에서-Trie-트라이-구현하기)
