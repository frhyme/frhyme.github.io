---
title: document를 클러스터링해봅시당
category: python-lib
tags: python-lib nlp python matplotlib tsne nltk

---

## document clustering

- 뭐, 지금까지 간단하게 자연어 전처리 해주는 것들(영어에 대해서만)과 워드임베딩 등을 했습니다. 대략 어떤 메소드들이 있는지에 대해서 아주 간단하게 발을 담궈 보았고, 이제는 이것들을 어떻게 활용할지에 대한 고민을 하고 있습니다. 
- 원래는 **'after word embedding'** 이라는 제목으로 word-embedding을 가지고 뭘할 수 있을지에 대해서 쓰려고 했습니다만, 아직은 잘 모르겠습니다. 워드 임베딩은 결국 개별 단어를 n차원 공간에 뿌려주는 것을 말하는데, 따라서 개별 워드를 벡터로 표현할 수 있게 되는데, 그래서,....그 다음에는 무엇을 할 수 있는걸까요. 일단 알았으니 나중에 잘 쓸 수있지 않을가 하고 생각합니다 하하핫. 

- 아무튼, 그래서 이제 원래 제가 하던 키워드 분석으로 돌아와서, 논문의 초록을 대상으로 클러스터링을 할 수 있지 않을까? 하는 생각이 들었습니다. word-embedding을 이용해서 클러스터링을 하면 재밌을 것 같다는 생각이 들긴 하는데, **개별 단어의 벡터들의 합이 documnet를 정의하는 형태**가 될 것 같기는 한데, 어떻게 합쳐야 하나? 라는 생각이 듭니다. 음..RNN을 이용해서 만들 수 있을 것 같기도 한데, 저는 앞서 말한 것처럼 맥북에어를 씁니다. RNN 학습하려면 터져나가요 뀨뀨뀨. 

- 아무튼 그렇기 때문에, 저는 우선 `TF-IDF` 를 사용해서 문서를 벡터화하고 이 문서들을 클러스터링해보려고 합니다. 이전에는 **키워드의 구조적 성질을 벡터화하여 클러스터링**했습니다만, 문서에는 보다 포괄적인 정보가 담겨있기 때문에, 클러스터링의 결과가 더 잘 나오지 않을까, 라고 낙관적으로 다시 생각해보기로 합니다(낙관적으로!!! 생각하는게 중요합니다 어차피 안될지 몰라도 낙관적으로!!). 
- 그렇게 한 뒤에 적합하지 않은 문서를 모두 걸러내고, 남은 문서들에 대해서 좀 더 깊게 분석하는 것이 좋지 않을까? 라고 생각해봅니당

## 우선 논문 초록들을 전처리합시다. 

### preprocessing abstract

- fillna(): 단 scopus에서 가져온 논문 서지 정보 데이터에서는 빈 초록이 '[No abstract available]'로 작성되어 있습니다. 이 부분을 제외하고, 빈 스트링으로 변경해줍니다. 
- 소문자, 공백, 알파벳이 아닌 모든 캐릭터 삭제: 간단하게 합니다. 
- lemmatizing: 복수를 단수로만 바꾸려고 하다가, 이왕 할 꺼면, 그냥 lemmatizing으로 원형의 형태로 바꿔도 되지 않을까? 싶어서 바꿨습니다(tfidf vectorizing에서 직접 해주는지는 잘 모르겠습니다). 이외에도 `tags`를 이용하여 할 수 있는 것들이 더 있을 것 같기도 한데, 귀찮기 때문에 하지 않겠습니다... 다음에 할게여 헤헤. 

```python
from nltk.stem import WordNetLemmatizer
def filtering_abstract(i_S):
    """lower, strip, lemmatizeing? remove sp char
    """
    def replace_sp_chr(input_s):
        return "".join(map(lambda c: c if c.isalpha() else " ", input_s)).strip()
    def remove_double_space(input_s):
        while "  " in input_s:
            input_s = input_s.replace("  ", " ")
        return input_s.strip()
    r_S = i_S.copy().apply(lambda s: s.lower().strip())
    r_S = r_S.apply(lambda s: "" if s == '[No abstract available]' else s)
    r_S = r_S.apply(lambda s: remove_double_space(replace_sp_chr(s)))
    """singularize??"""
    """lemmatizing"""
    lemmatizer = WordNetLemmatizer()
    r_S = r_S.apply(lambda s: " ".join([lemmatizer.lemmatize(w) for w in s.split(" ")]) )
    return r_S
print(df['Abstract'].head(5))
print(filtering_abstract(df['Abstract']).head(5))
```

- 원래도 개별 값의 타입은 스트링이었고, 이후에도 스트링입니다. `TfidfVectorizer`에는 스트링 리스트를 넘겨주어야 합니다. 

```
0    This research paper is to evaluate and present...
1    According to the application requirements of t...
2    This paper reviews the current status of high ...
3    This study shows a low-priced information coll...
4    The proceedings contain 37 papers. The topics ...
Name: Abstract, dtype: object
0    this research paper is to evaluate and present...
1    according to the application requirement of th...
2    this paper review the current status of high t...
3    this study show a low priced information colle...
4    the proceeding contain paper the topic discuss...
Name: Abstract, dtype: object
```

### make tfidf vector

- 그거 뭐 그냥 쉽게 만들면 되는거 아니냐! 라고 말할 수 있습니다만, 변수를 조절하면서 계속 확인해야 합니다. 매우 번거롭죠. 여러분 데이터 분석은 노가다와 같은 말입니다. 뇌를!! 혹사!! 시킨다!!!
- 아무튼 다음 변수들에 따라서 값이 달라집니다. 어떻게 바꾸면 좋을지 참 어려워용. 
    - `ngram_range`: 일반 대화에서는 1-gram으로 충분할지 모르겠지만, 제가 대상으로 하는 데이터는 논문 초록입니다. 이 경우는 (제 편견일 수도 있겟지만) 복합어가 많을 것 같아요. 그래서 이 레인지를 약간 올려서 (2, 4)정도로 해보았습니다. 
    - `min_df`: **document frequency가 최소한 몇 은 되어야 하느냐**, 라는 이야기입니다. 예를 들어 전체 문서에서 딱 한 번 등장하는데, 이 아이까지 벡터의 디멘션으로 고려해야 하느냐? 그럼 shape이 엄청 길어질텐데? 라는 거죠. 정수 값을 넘길 수도 잇지만, float 값을 넘기면 알아서 전체 빈도 중에서 하위 퍼센트를 걸러냅니다. 
    - `max_df`: **document frequency가 최대한 몇이 되면 안된다**, 라는 말입니다. 'is'같은 단어는 아마도 모든 문서에서 등장할거에요. 그렇다면, 이 단어도 고려해야 하나요? 무의미한 값인데? 그래서 제외합니다. 
    - `binary`: 값에 weight를 주느냐 안주느냐 의미인데, 0보다 크면 1 아니면 0으로 변환하는 것을 말합니다. 이건 관점에 대한 이야기인데, document간의 길이 편차가 크다면 이를 binary로 변경하는 것이 더 좋을 수도 있을 것 같습니다. 
- min_df, max_df를 결정하기 위해서는 **document frequency의 분포를 먼저 확인하는 것이 필요하지 않을까?** 생각해봅니다. 흠.

#### check document frequency dist. 

- 

```python
from sklearn.feature_extraction.text import TfidfVectorizer
def make_tfidf_df(sent_lst):
    TFIDFmodel = TfidfVectorizer(
        ngram_range=(2, 4), # 앞 뒤 window를 고려하여 확장된 형태로 제시해줌. phrase를 뽑아낼 수 있는 강점이 있기는 할듯. 
        min_df = 0.1, # document freqeuency 가 min_df 이상은 되는 키워드만으로 vocabulary를 구성
        max_df = 0.3,# document frequency가 10 이하인 키워드만으로 vocabulary를 구성 
        binary = False # binary이면 있다 없다 구조로 변경됨
    )
    TFIDFmodel.fit(sent_lst)
    return TFIDFmodel.vocabulary_, pd.DataFrame(TFIDFmodel.transform(sent_lst).toarray(),
             columns = [it[0] for it in sorted(TFIDFmodel.vocabulary_.items(), key=lambda x: x[1])])
#print(df['Abstract'].head(10))
abs_series = filtering_abstract(df['Abstract'])
abs_vocab, abs_tfidf_df = make_tfidf_df(abs_series.head(100))
```


---


### 예를 들자면, 

- composite vector: 개별 워드를 벡터화할 수 있다면, composite word나, 문장도 벡터로 표현할 수 있지 않을까? 이는 어떻게 할 수 있을까? 
- clustering: abstract를 BOW 등의 방식, TFIDF 등의 방식으로 필터링하는 것은 비교적 간단한게, 이보다 word-embedding을 이용해서 클러스터링할 수 있지 않을까? 
    - 그래서 찾아보니, `doc2vec`이라는 것도 있으나, 내가 생각한 것처럼 document를 벡터차원에 전사해주는 것이 아닌 것으로 보임.
- keyword analysis after clustering: Doc2Vec를 통하면 더 포괄적인 정보에 대해서 클러스터링이 가능하며 이를 활용해 문서들을 클러스터링하고, 개별 클러스터집단에 대해서 개별적으로 키워드 를 분석하는 것이 더 효과적일 수도 있음. 
    - 흠, `Tf-Idf`를 이용해서 개별 문서를 벡터화하고, 클러스터링하면 문서들을 비교적 간단하게 클러스터링할 수 있지 않을까? 
    - 

## reference

- <https://rare-technologies.com/doc2vec-tutorial/>
- <http://www.engear.net/wp/doc2vec-시작하기/>
- <https://www.lucypark.kr/docs/2015-pyconkr/#59>