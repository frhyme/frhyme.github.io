---
title: gensim - tutorial - doc2vec
category: python-libs
tags: python python-libs gensim similairty word2vec nlp doc2vec 
---

## 2-line summary 

- Doc2vec는 각 Document를 vector로 표현하는 모델입니다. input을 word2vec으로 넣고, output을 각 document에 대한 vector를 설정하여 꾸준히 parameter를 fitting합니다. 
- 또한, 그 결과로, word2vec오 자연히 학습이 되므로(물론 완전히 동일하지는 않겠지만), 이 둘을 모두 효과적으로 사용할 수 있죠.

## Review: BOW, word2vec

### Bag of word

- Bag-of-word는 "word vocabulary의 문단별 빈도수"를 각 document를 표현하는 베터로 생각하는 것을 말합니다. 사실, 이것만으로도 꽤 의미는 있지만, 이 아이는 word의 순서에 대해서 고려하지 못하죠. 물론, n-gram을 사용하면 어느 정도 되지만, local order밖에 고려하지 못할 뿐만 아니라, 계산에 큰 로드가 걸리게 됩니다. 또한, '의미(semantic)'를 고려하지 못한다는 문제가 있는데요 특히, "거리가 의미의 다름"을 표현하지는 않게 됩니다. 이는 Word2vec에서 해결하였죠. 

### word2vec

- Word2vec은 shallow neural network를 사용해서, "가깝게 위치한 단어들은 비슷한 의미를 가진다"는 가정 하에, 매우 강한 의미적 추론을 진행할 수 있습니다. 그리고 word2vec을 이용해서 doc2vec을 진행할 수 있죠. 
- 하지만, 과연, 'word의 vector을 어떻게 조합해야 doc2vec가 되는걸까요?'

## Doc2vec: Paragraph Vector(PV-DM, PV-DBOW)

- 2014년 발표된 Doc2Vec 알고리즘은 기존의 word2Vec을 사용한 결과보다 훨씬 뛰어났습니다. 기본 아이디어는 "Document 자체를 그냥 word2vec의 word처럼 생각한다. 하지만, 그냥 그것을 우리는 doc2vector로 부른다"라는 것이 다입니다. 다시 말하면, 그냥 "Word"가 들어갈 자리에 Document"가 들어간다는 것만이 다른 것이죠.
- 가령 우리에게 `"I am a boy"`라는 sentence 혹은 document가 있다고 합시다. 다시 말하면, 이 아이는 "I", "am", "a", "boy"라는 4개의 word vector의 조합이죠. 이 4개의 word vector를 input으로 받아들여서, 이 document의 vector를 출력한다면, 즉, 여러 data를 연속적으로 먹여가면서 parameter를 fitting한다면, 이는 결국 해당 document에 대해서 괜찮은 vector를 뽑아주게 되겠죠. 
- 혹은 반대로, document vector를 input으로 두고, word-vector를 추론하도록 parameter를 fitting할 수도 있습니다. 
- 결국, 이 두가지 방식이 각각 PV-DM, PV-DBOW이며, 이는 CBOW, SG와 비슷합니다. 그리고, 몰라도 됩니다. 
- 다만, 이로 인해서 Doc2vec으로 학습을 완료하고 나면, word2vec도 자동으로 학습이 되므로, 이 둘을 모두 이용할 수 있습니다. 다만, 그냥 word2vec으로 학습한 결과와 완전하게 동알하지는 않겠죠.

## Doc2vec: implement model by gensim

- 설명하기 귀찮으니까 그냥 해봅니다. `gensim`을 이용해서 doc2vec model을 만들었습니다. 그리고, doc2vec class 내에는 당연히 word2vec 모델이 존재하죠.

```python
import gensim

sentences = [
    "He is a boy", "He is a man", "She is a girl"
]
sentences = [s.lower().strip().split(" ") for s in sentences]
#----------------------------------------
# Tagging Sentences
# 하나의 paragraph에 대해서 하나의 sentence로 설정해줌.
tagged_documents = []
for i, s in enumerate(sentences):
    tagged_documents.append(
        gensim.models.doc2vec.TaggedDocument(s, [i])
    )
Doc2Vec_model = gensim.models.doc2vec.Doc2Vec(vector_size=50, min_count=1)
#----------------------------------------
# # BUILD word2vec vocab
# Doc2vec은 word2vec에 근거함.
Doc2Vec_model.build_vocab(tagged_documents)
#----------------------------------------
# Train tagged_documents
Doc2Vec_model.train(tagged_documents, total_examples=len(tagged_documents), epochs=300)
#----------------------------------------
# Infer new document vector
# not string, use list of string as input
print("== Document vector")
new_document = "he is a man"
new_doc_vector = Doc2Vec_model.infer_vector(new_document.lower().split(" "))
print(f"Document, '{new_document}' to vector {new_doc_vector[:5]}")
#----------------------------------------
# Use wor2vec similarity 
# Document 전체에 대해서 similarity를 측정하여, 가장 가까운 word-vector를 사용해서 결과를 리턴.
print("== word similarity")
print(Doc2Vec_model.wv.similar_by_vector(new_doc_vector))
#----------------------------------------
# Use Doc2vec similarity
# docvec.most_similar는 word에 대한 vector에 기반해서 처리됨.
print("== document similarity")
doc_sim_lst = Doc2Vec_model.docvecs.most_similar(positive=[new_doc_vector], topn=len(Doc2Vec_model.docvecs))
for doc_id, sim in doc_sim_lst:
    print(f"Document {doc_id} - similarity: {sim:.5f}")
print("== complete")
```

- 결과는 다음과 같습니다.

```
== Document vector
Document, 'he is a man' to vector [-0.01550222  0.00654157  0.00314305  0.02054347  0.00220825]
== word similarity
[('is', 0.25534892082214355), ('man', 0.16589590907096863), ('a', 0.15215086936950684), ('girl', 0.11516174674034119), ('he', 0.09550413489341736), ('she', 0.012047693133354187), ('boy', -0.13721874356269836)]
[('she', 0.22538770735263824), ('man', 0.13674762845039368), ('is', 0.0875273197889328), ('a', 0.043554868549108505), ('boy', -0.0036111846566200256), ('girl', -0.012933444231748581), ('he', -0.2287140041589737)]
== document similarity
Document 1 - similarity: 0.70888
Document 2 - similarity: 0.68156
Document 0 - similarity: 0.60137
== complete
```


## wrap-up

- paragraph는 word의 조합입니다. 그리고 이미 word는 vector와 하는 방법이 알려져 있죠. 
- 모든 paragraph는 unique하고, 이는 내부의 word의 vector를 사용해서 표현할 수 있습니다. 다시 말하면, paragraph의 vector는 내부 word의 vector의 조합으로 표현될 수 있습니다. 그리고 반대로, document의 vector 또한, 내부의 word의 vector로 표현될 수 있어야 겠죠. 
- 따라서, input을 word vector, output을 paragraph으로 설정하고 꾸준히 parameter를 tuning합니다. 그러면 결국 양쪽을 모두 잘 표현할 수 있는 document vector를 생성하는 모델이 세워지죠. 
- 그리고 doc2vec을 만드는 과정에서 word2vec 모델이 필요하므로 필연적으로 word2vec도 생성됩니다. 



## reference

- [gensim - tutorial - doc2vec](https://radimrehurek.com/gensim/auto_examples/tutorials/run_doc2vec_lee.html#sphx-glr-auto-examples-tutorials-run-doc2vec-lee-py)