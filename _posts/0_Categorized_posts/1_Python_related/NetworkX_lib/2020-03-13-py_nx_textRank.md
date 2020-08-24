---
title: python에서 textRank 만들기. 
category: python-libs
tags: python python-libs pagerank networkx graph nlp 
---

## 3-line summary 

- textRank는 pagerank를 text에 접목시킨 것이다. 
- 이 때 사용하는 Graph는 word를 node로 하여 문장 내 공동출현 값을 edge의 weight로 주는 경우가 있고 
- 혹은 sentence를 node로 하고 문장 간 유사도를 edge의 weight로 주는 경우가 있다

## TextRank

- textrank는 "text들로부터 network를 만들고 거기에 pagerank를 접목한 것"이 다죠. 여기서 중요한 것은 node, edge가 명확하게 구분되어 있지 않은 text로부터 어떤 것을 node로 설정하고, edge는 어떻게 설정하고 또, 각각의 weight는 어떻게 설정할 것인가? 가에 따라서 결과가 달라지죠. 
- [TextRank 를 이용한 키워드 추출과 핵심 문장 추출 (구현과 실험)](https://lovit.github.io/nlp/2019/04/30/textrank/)를 참고하였으나, 약간 내용이 다릅니다. 저는 `networkx`를 사용하여 pagerank를 계산하였습니다.


## Build Word-Graph and pagerank. 

- 우선 각 문장 내에 등장하는 word(단어)를 node로 설정하고, 문장 내에서 가깝게 위치하면 서로 edge가 있는 것이다, 라고 가정하여 word-graph를 만들어 보겠습니다. 여기서 "가깝다"라는 말이 모호한데, 이는 window라는 변수를 사용하여, "어느정도 간격 사이에 있으면 가깝다"라고 정의하여 사용하게 됩니다. 

### MAKE Node: Scan vocab from sentences

- 가령 "I am a boy"라는 하나의 문장이 있다고 합시다. 이를 word로 변경하면, I, am, a, boy 라는 네 word가 있는 것이죠. 그렇다면 여기서, 이 네 word를 모두 graph의 node로 정의할 수도 있겠죠. 
- 다만, `min_count`라는 parameter를 통해서, "전체 senstence중에서 최소한 `min_count`번 이상 등장한 키워드"만을 vocab라고 정의할 수도 있습니다. 혹은 `stop_words`를 넘겨주어, "`stop_words`에 속하는 word들은 node로 정의하지 않는다"라는 것도 가능하죠. 
- 또한, 아래 코드를 보면, 결과로 다음 두 자료구조를 리턴합니다. 사실, 굳이 할 필요는 없을 수 있지만, `string`의 경우 가급적 `idx`의 형태로 변환하여 관리해주는 것이 좋습니다. 이는 `pandas`나 다른 자료구조에서도 마찬가지인데, `string`을 쓸 경우, 메모리 용량에 부하가 걸릴 수 있고 이는 다시 속도 저하에 영향을 미치게 되니까요. 따라서, 이를 막기 위해 아래 함수에서 vocab을 변환할 수 있는 자료구조를 아래와 같이 각각 리턴하고 있습니다.
    - `vocab_to_idx`: `{vocab: idx}`의 형태의 딕셔너리. 
    - `idx_to_vocab`: `[vocab]`의 리스트, list에 `[idx]`로 접근
- 또한, 아래 함수에서는 매우 간단하게, `" "`로 쪼개서, 모든 것을 word로 두기는 했지만, 다른 방식도 가능합니다. 가령 POS tagging을 통해 noun, verb 등만 따로 추려낸다거나, 하는 것도 가능하지만, 저는 그냥 일단은 그대로 두기로 했습니다.

```python
def scan_vocabulary(sentences, min_count=1, stop_words=set()):
    """
    sentence로부터 vocab를 min_count를 고려하여 vocab를 생성
    * pos를 고려하여, noun, verb, 형용사 만 남기고 다 날려버리는 것이 필요함.
    """
    word_lst = (s.split(" ") for s in sentences)
    word_lst = ([w for w in w_l if w not in stop_words] for w_l in word_lst)
    word_counter = Counter(chain.from_iterable(word_lst))
    word_counter = {w: c for w, c in word_counter.items() if c >= min_count}
    # idx_to_vocab: count가 높을 수록 앞에 등장
    idx_to_vocab = [w for w, c in sorted(
        word_counter.items(), key=lambda x: -x[1])]
    vocab_to_idx = {w: idx for idx, w in enumerate(idx_to_vocab)}
    return idx_to_vocab, vocab_to_idx
```

### MAKE Edge: vocab occurrence

- 이 앞에서, 적합한 node를 모두 만들었습니다. 그렇다면 이제 node와 node간의 연결인 edge가 어떻게 구성되어 있는지를 알아야겠죠. 이 때, edge가 존재하는지 존재하지 않는지를 보통 `window`라는 값으로 조절합니다. 
- 예를 들어보겠습니다. "I am a boy"라는 문장이 있고 여기서 I, am, a, boy라는 4개의 노드를 뽑았다고 할게요. 여기서 I와 am은 1의 window를 가지고, I와 a 는 2의 window(간격)을 가집니다. 만약 우리가 window를 1로 준다면, 바로 옆에 있는 노드들에 대해서만 edge를 생성해줄 것이고, 이를 크게 한다면, 가령 3으로 한다면, 4개의 노드는 모두 서로 연결되어 있게 되죠. 
- 즉, window를 크게 할수록 edge는 매우 많이 생성되게 됩니다(dense). 반대로 적게 하면 매우 적게 생성되게 되죠(sparse).
- 따라서, window를 변경해 가면서 적합한 결과가 나오는지 파악하는 것이 중요하죠. 또한, `min_coocurrence`라는 값을 통해서 "최소한 몇 번 이상 등장한 edge만 유효하다고 한다"와 같은 것을 설정해줄 수도 있죠.

```python
def vocab_cooccurrence(sentences, vocab_to_idx, window=3, min_cooccurrence=1):
    """
    - window의 길이를 고려하여, 한 문장 내 cooccurrence를 고려하여 리턴. 
    - 한 방향으로만 리턴.
    """
    cooccurrence_dict = {}
    for s in sentences:
        tokens = [t.strip() for t in s.split(" ")]
        # vocab에 있는 것들만 남김.
        tokens = [vocab_to_idx[t] for t in tokens if t in vocab_to_idx]
        for i, token1 in enumerate(tokens):
            left_lim_idx = max(0, i-window)
            right_lim_idx = min(len(tokens), i+window)
            for token2 in tokens[left_lim_idx:right_lim_idx]:
                if token1 != token2:
                    key = tuple(sorted([token1, token2]))
                    if key in cooccurrence_dict:
                        cooccurrence_dict[key] += 1
                    else:
                        cooccurrence_dict[key] = 1
    return {k: v for k, v in cooccurrence_dict.items() if v >= min_cooccurrence}
```

### Make word-Graph

- 위에서 정의한 `scan_vocabulary`와 `vocab_cooccurrence`를 사용하여, word-graph를 만듭니다.

```python
def word_graph(sentences, min_count=1, min_cooccurrence=1, window=3, stop_words=set()):
    """
    - scan_vocabulary를 사용해서, min_count를 넘기고, stop_word에 속하지 않는 vocab만 남기고 
    - vocab_cooccurrence에서 window를 고려하여, vocab간의 edge들을 모두 가져오고
    - 이를 Graph로 만들어서 리턴.
    """
    idx_to_vocab, vocab_to_idx = scan_vocabulary(
        sentences, min_count=min_count, stop_words=stop_words)
    coor_dict = vocab_cooccurrence(
        sentences, vocab_to_idx, window=window, min_cooccurrence=min_cooccurrence)
    G = nx.Graph()
    for i, node_name in enumerate(idx_to_vocab):
        G.add_node(i, name=node_name)
    for (n1, n2), coor in coor_dict.items():
        G.add_edge(n1, n2, coor_count=coor)
    return G
```

### CALC pagerank 

- 이렇게 만들어진 word-graph, `G`에 대해서 pagerank 알고리즘을 적용합니다. 만약, edge의 `cooccurrence`를 고려하고 싶다면, `weight` parameter를 넘겨주면 되죠. 

```python
import networkx as nx 

nx.pagerank(G, weight='coor_count')
```


## Build Sentence-Graph and pagerank. 

- 그다음으로 node를 word가 아니라, sentence로 적용할 수도 있겠죠. 
- 이 경우, node는 각 문장(sentence)가 되고, edge는 문장과 문장의 '유사도(similarity)'가 됩니다. 그리고 이 때, sentence의 유사도는 아래와 같은 함수로 계산하게 되죠. 
- 다만, 아래 수식을 보면, 두 문장 `s1`, `s2`가 있다고 할때, 각 문장의 길이의 로그 값을 분모에서 나누게 됩니다. 즉, "문장이 길어지는 것보다, 문장에서 교집합이 커지는 것이 더 영향을 미친다"라고 말할 수 있는 것이죠. 다시 말해서, 이는 해당 수식, 유사도가 문장의 길이가 길수록 높다고 나온다는 것을 이야기하고 있는 것이죠.
- 이는, textRank가 text summarization에서 주로 사용되기 때문이기도 합니다. text를 요약한다고 할때, 한 문장에서 비록 길더라도, 다른 문장들에서 포함될 수 있는 중요한 다른 단어들을 많이 포함하고 있다면, 그 문장이 더 중요하다, 라는 것을 파악하기 위함인 것이죠.
- 식은 간단하며, 여기서는 아래와 같은 방식으로 edge의 weight를 설정했지만 다른 방법도 가능합니다. 가령, sentence를 doc2vec으로 표현한 다음 cosine-similarity를 사용한다거나 하는 다양한 방식이 있을 수 있죠. 즉, 정답은 없고, 본인이 표현하려는 것에 따라서 달라진다는 이야기죠.

```python
def sentence_similarity(word_lst1, word_lst2):
    if len(word_lst1) <= 1 or len(word_lst2)<=1:
        return 0 
    else:
        l1, l2 = len(word_lst1), len(word_lst2)
        common_words = len(set(word_lst1).intersection(set(word_lst2)))
        return common_words/ (np.log(l1)+np.log(l2)
```

- 다른 부분들의 경우는 이전에 말한 것들과 거의 같아서 추가로 작성하지는 않았습니다. sentence를 node로 그리고 edge의 weight를 sentence의 유사도를 측정하여 집어넣고, 그 과정에서 너무 작은 weight는 무시한다거나 하는 식으로 graph를 pruning하여 처리할 수 있겠죠. 
- 그다음 `pagerank`를 사용하여 가장 높은 값을 가지는 node 즉 sentence들을 순서대로 뽑아낸다면 그것들이 대략적인 summarization이 됩니다.

## wrap-up

- 저는 원래 network에 대한 많은 개념들을 알고 있습니다. 자연어처리에 대해서는 잘 알지 못했는데, 파고 들어가다보니, 자연어들도 graph로 표현하여 기법들을 사용할 수 있다는 것을 알게 된 것 같네요. 
- 다만, 저는 항상 "어떻게 graph를 만드는 것이 가장 좋은 graph modeling인가?"라는 생각을 합니다. 결과적으로 몇가지 metric을 사용해서 평가해봤더니 좋아더라, 라는 것도 가능하긴 하지만 이보다, "해당 graph가 어느 정도의 density를 가진다면 일반적으로 graph로 표현이 잘 된 것으로 본다"와 같으, 그런 것들이 있으면 좋을 것 같은데 잘 없는 것 같아요. 


## reference

- [TextRank 를 이용한 키워드 추출과 핵심 문장 추출 (구현과 실험)](https://lovit.github.io/nlp/2019/04/30/textrank/)