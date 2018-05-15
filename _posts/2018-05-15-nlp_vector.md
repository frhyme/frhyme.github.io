---
title: natural language processing을 해보장
category: python-lib
tags: python python-lib nltk 
---

## one-hot encoding to word embedding

- 요즘 아무래도 포스팅이 중복되는 느낌들이 있습니다. 제가 이 블로그를 공부하면서 그 과정을 계속 쓰기 때문에 이 포스트 또한 지난 번에 쓴 내용들과 겹치는 부분들이 있을 것 같습니다. 그래도, 계속 합니다. 이게 마음이 이 블로그를 많은 사람들이 봤으면 좋겠어서 신경을 써야하지만 또 나만 편하면 됐지 라고도 생각하게 되는 양면성이 있네요ㅠㅠ
- 아무튼, 제가 word-embedding에 관심을 가지는 이유는 논문의 abstract를 분석하고 싶기 때문인데요, 기존의 author keyword만으로는 효과적인 분석에 제한이 있다고 생각합니다. 따라서 index keyword를 사용하여 bipartite graph를 만들고 거기서 semantically similarity를 사용하여 확장 분석을 수행하였습니다. 
- 자, 그럼 이제 남은 것은 **abstract**입니다. 이걸 이용해서 이상한 짓들을 좀 하고 싶은데, 대략 다음이 될 수 있지 않을까? 싶습니다. 
    - 'author kwd - index kwd'의 관계처럼 author kwd - noun in abstract 의 bipartite graph를 만들어서 author kwd를 벡터로 표현
    - abstract를 자체를 벡터화하여 이를 활용해 abstract간의 클러스터링 혹은 필터링. 
    - abstract의 verb-noun 구조를 활용하여, 뭔가 의미있는 발견???등등
- 이런걸 할 수 있을 것 같은데, 이 모든 것은 nlp 의 영역에 속하는 것 같습니다. 
- 따라서, 비교적 간단하게 nlp를 공부해보려고 합니다. 


## CountVectorizer

- 아주 간단하게, document의 개별 워드를 하나의 디멘션으로 파악하고, 그 갯수(weight)를 해당 dimension의 값으로 한 벡터를 만들어보자. 

```python
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

sent_lst = ["I am a boys, boy", 'You are a girl', "he is the a boy or girl"]

def make_count_vector_df(sent_lst):
    """
    관사 삭제: the a 등은 자동으로 삭제됨
    단수 복수는?: 삭제되지 않는다. 
    비교적 간단하게 여기서 count vector를 만들 수 있기는 한데, 이정도는 나도 금방 코딩해서 만들 수 있는 정도기는 함. 
    뭐 그래도 경우에 
    """
    CV_model = CountVectorizer(
        ngram_range=(1,2), # 앞 뒤 window를 고려하여 확장된 형태로 제시해줌. phrase를 뽑아낼 수 있는 강점이 있기는 할듯. 
        """document frequency(d, t): term이 등장한 document의 갯수
        """
        min_df = 1, # document freqeuency 가 1 이상은 되는 키워드만으로 vocabulary를 구성
        max_df = 2, # document frequency가 2 이하인 키워드만으로 vocabulary를 구성 
        binary = False # binary이면 있다 없다 구조로 변경됨
    )
    cv_result = CV_model.fit_transform(sent_lst)
    # print("CV_model.vocabulary_: {}".format(CV_model.vocabulary_))
    return pd.DataFrame(cv_result.toarray(),
             columns = [it[0] for it in sorted(CV_model.vocabulary_.items(), key=lambda x: x[1])])
print(make_count_vector_df(sent_lst))
```

- `ngram`, `min_df`, `max_df`를 고려하여 벡터로 만들고 그를 `vocabulary_`를 활용하여 `pd.DataFrame`로 변환한 결과

```
   am  am boys  are  are girl  boy  boy or  boys  boys boy  girl  he  he is  \
0   1        1    0         0    1       0     1         1     0   0      0   
1   0        0    1         1    0       0     0         0     1   0      0   
2   0        0    0         0    1       1     0         0     1   1      1   

   is  is the  or  or girl  the  the boy  you  you are  
0   0       0   0        0    0        0    0        0  
1   0       0   0        0    0        0    1        1  
2   1       1   1        1    1        1    0        0 
```


## what is tf-idf

- 뭐, `countvectorizer`의 경우도 나쁘지 않습니다만, 위 결과 테이블을 보시면, 'am', 'are'가 하나의 차원으로 표시되어 있는 것을 알 수 있습니다. 존재하는 모든 sentence에서는 이 단어가 포함되어 있는데, 굳이 이를 표현할 필요가 있을까요? 이는 모든 document의 일반적인 속성에 가깝습니다. 마치 '인간은 눈과 코와 귀가 있다'같은 성질이라서 해당 인간을 표현하는 적합한 특성이 아니라는 말이죠.
    - 음, 그렇게 생각하니까, 개별 워드들에 대해서 clustering해서 대부분의 도큐멘트에 있는 워드들은 제외하는 식으로 필터링을 할 수 있을 것 같기도 하네요. 
- 그래서, 이를 보완하기 위해서 `tf-idf`가 등장했습니다. 

### tf, df and idf and finally tf-idf

- $$term_frequency(document, term)$$: the number of times a term occurs in a given document
- $$document frequency(document, term)$$: the number of documents that contain term t
- $$inverse document frequency(document, term)$$: 실제 계산법에서는 log도 들어가고 하는데, 저는 그냥 직관적으로 $$1/document_frequency$$ 로 생각합니다. 그래도 단순 의미적으로는 아무 문제가 없습니다. 

- `tf-idf` 는 tf*idf or tf/df 라고 해석할 수 있습니다. 따라서 term frequency가 올라갈수록 커지고, document frequency가 커질 수록 작아집니다. 
    - term frequency 가 커질 수록 `tf-idf`는 커진다: 해당 문서에서 해당 term이 많이 나올수록 해당 문서에서 해당 term이 중요하다고 생각되므로 커진다. 
    - document frequency 가 커질 수록 `tf-idf`는 작아진다: 해당 문서에도 해당 term이 많이 나와도, 다른 많은 문서들에서도 해당 term이 등장했다면, `tf-idf`는 작아진다. (여기서 다른 문서들에서 얼마나 등장했는가에 따라서 값을 보정할 수 있을 것 같네요)
- 따라서, tf-idf는 **다른 문서들에서 적게 등장하고, 이 문서에서만 많이 등장하는 유별난 놈에게만 점수를 많이 주는 방법**이라고 말할 수 있을 것 같군용. 이건 일종의 feature extraction이군용

```python
from sklearn.feature_extraction.text import TfidfVectorizer
def make_tfidf_df(sent_lst):
    TFIDFmodel = TfidfVectorizer(
        ngram_range=(1,1), # 앞 뒤 window를 고려하여 확장된 형태로 제시해줌. phrase를 뽑아낼 수 있는 강점이 있기는 할듯. 
        min_df = 1, # document freqeuency 가 1 이상은 되는 키워드만으로 vocabulary를 구성
        max_df = 10, # document frequency가 2 이하인 키워드만으로 vocabulary를 구성 
        binary = False # binary이면 있다 없다 구조로 변경됨
    )
    TFIDFmodel.fit(sent_lst)
    #print(TFIDFmodel.vocabulary_)
    return pd.DataFrame(TFIDFmodel.transform(sent_lst).toarray(),
             columns = [it[0] for it in sorted(TFIDFmodel.vocabulary_.items(), key=lambda x: x[1])])
sent_lst = ["I am a boy", "I am a girl", "I am a dog"]
print( make_tfidf_df(sent_lst) )
```

- 결과를 보면 'am'의 경우는 모든 도큐먼트에 있기 때문에 의미없는 값이 됩니다 하핫. 'boy', 'dog', 'girl'이 더 중요한 feature인 것으로 변환된 것을 알 수 있습니다.

```
         am       boy       dog      girl
0  0.508542  0.861037  0.000000  0.000000
1  0.508542  0.000000  0.000000  0.861037
2  0.508542  0.000000  0.861037  0.000000
```

## 그래서 충분한가요!!

- 이게 최선인가요!, 잘 모르겠군요. 어쨌든 이런 방식으로도, 해당 도큐먼트에 대해서 어느 정도 의미있는 벡터를 표현할 수 있기는 한데, 이게 최고인지는 모르겠어요. 결국 지금까지의 내용은 `document`를 가장 잘 설명하기 위한 방법일 뿐입니다. 다시 말해서, 개별 word를 잘 설명할 수는 없다는 것이죠. 그래서 **word-embedding**이 나왔습니다. 

## 그래서 word-embedding은 무엇이 다른가? 

- word-embedding의 차이점이라면 앞 뒤 문맥을 파악한다는 것이 차이입니다. **비슷한 의미를 가지는 단어는 앞뒤로 비슷한 단어들에 의해 둘러싸여 있다** 가 word-embedding의 핵심인 것 같구요. 이렇게 보면 '네트워크 분석에서 구조적으로 유사한 단어(공유하는 edge가 같거나, weight도 같은 경우)들은 비슷한 역할을 가진다'와 일면 유사하게 느껴지기도 하네요.
    - 음, 저는 네트워크가 익숙하기 때문에 네트워크로 해석을 하면, 개별 단어 뭉텅이(문장을 단어로 쪼갠 형태)에서 네트워크를 생성하고,그 네트워크로부터 `adjacency matrix`를 만들면 그것이 word representation이다 라고 말할 수 있는 것처럼 보이기도 합니다. 화면에 요놈들이 잘 분화되어 있는지는 t-sne로 데이터를 축소한 다음, 뿌려주면 되는 것 같고요. 
    - 하지만, 이렇게 한다고 해도, 해당 단어의 앞 뒤로 몇 개 까지를 edge가 있다고 가정할 것인가, weight를 다르게 둘 것인가 등의 문제들이 발생하기는 합니다. 
- 지난번에도 간단하게 워드 임베딩에 대해서 알아봤습니다. 컴퓨터는 숫자만 이해할 수 있는데 워드는 숫자가 아니다. 따라서 **워드를 숫자로 표현하자**라는 것이 핵심이겠네요. 그런데 어떻게 표현할 수 있는가? 가 중요하겠죠. 

### just do it. 

- 모르겠고, 코드로 해봅시다. 결과를 보면서 역으로 생각하는 게 저한테는 더 잘 맞는 것 같아용. 
- 간단하게 코드를 짜서 넘기면 문제가 생길 때가 있습니다. 보통 이 때 오류는 `RuntimeError: you must first build vocabulary before training the model`인데, gensim의 word2vec는 최소한 5개 이상 되는 워드 들에 대해서만 vocab를 구성합니다. 따라서 너무 작은 sample로만 넘기면 학습이 안되요. 

- sample 수를 늘려가면서, 정말 비슷한 의미를 가지는 워드들이 모이는지 확인해봅니다.
- 굉장히 단순한 데이터를 넘겼습니다. 저 문장들로만 보면, 'boy'와 'girl', 'dog'는 반드시 가깝게 모여야 하는데, 실제로 해보면 점점 가까워 지는 것을 알 수 있습니다. 유의미하다는 생각을 합니다. 

![](/assets/images/markdown_img/word_embedding_subplot_20180515.svg)

```python
from gensim.models.word2vec import Word2Vec
import matplotlib.pyplot as plt

f, axes = plt.subplots(2, 2, sharex=False, sharey=False)
f.set_size_inches((16, 6)) 
for i in range(0, 2):
    for j in range(0, 2):
        sample_n = [1, 1000, 2000, 6000][i*2+j]
        sent_lst = ["I am a boy", "I am a girl", "I am a dog"]*sample_n
        sent_split_lst = map(lambda s: list(s.lower().split(" ")), sent_lst)

        model = Word2Vec(list(sent_split_lst), size=2, window = 3, min_count=1)
        model.init_sims(replace=True)# 학습 완료 후, 필요없는 메모리 삭제 

        for x, y, t in ((model.wv.get_vector(w)[0], model.wv.get_vector(w)[0], w) for w in model.wv.index2entity):
            axes[i][j].scatter(x, y, cmap=plt.cm.rainbow)
            axes[i][j].text(x+0.01, y, t, fontsize=12)
            axes[i][j].set_title("sample size = {}".format(sample_n))
f.tight_layout()# 그냥 이걸로 다 해결되었다.
plt.savefig('../../assets/images/markdown_img/word_embedding_subplot_20180515.svg')
plt.show()
```


## reference
- <https://stackoverflow.com/questions/33989826/python-gensim-runtimeerror-you-must-first-build-vocabulary-before-training-th>
- <https://ratsgo.github.io/natural%20language%20processing/2017/03/08/word2vec/>

