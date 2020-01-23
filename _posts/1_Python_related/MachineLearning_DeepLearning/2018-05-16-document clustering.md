---
title: document를 클러스터링해봅시당
category: python-lib
tags: python-lib nlp python matplotlib tsne nltk clustering

---

## document clustering

- 뭐, 지금까지 간단하게 자연어 전처리 해주는 것들(영어에 대해서만)과 워드임베딩 등을 했습니다. 대략 어떤 메소드들이 있는지에 대해서 아주 간단하게 발을 담궈 보았고, 이제는 이것들을 어떻게 활용할지에 대한 고민을 하고 있습니다. 
- 원래는 **'after word embedding'** 이라는 제목으로 word-embedding을 가지고 뭘할 수 있을지에 대해서 쓰려고 했습니다만, 아직은 잘 모르겠습니다. 워드 임베딩은 결국 개별 단어를 n차원 공간에 뿌려주는 것을 말하는데, 따라서 개별 워드를 벡터로 표현할 수 있게 되는데, 그래서,....그 다음에는 무엇을 할 수 있는걸까요. 일단 알았으니 나중에 잘 쓸 수있지 않을가 하고 생각합니다 하하핫. 

- 아무튼, 그래서 이제 원래 제가 하던 키워드 분석으로 돌아와서, 논문의 초록을 대상으로 클러스터링을 할 수 있지 않을까? 하는 생각이 들었습니다. word-embedding을 이용해서 클러스터링을 하면 재밌을 것 같다는 생각이 들긴 하는데, **개별 단어의 벡터들의 합이 documnet를 정의하는 형태**가 될 것 같기는 한데, 어떻게 합쳐야 하나? 라는 생각이 듭니다. 음..RNN을 이용해서 만들 수 있을 것 같기도 한데, 저는 앞서 말한 것처럼 맥북에어를 씁니다. RNN 학습하려면 터져나가요 뀨뀨뀨. 

- 아무튼 그렇기 때문에, 저는 우선 `TF-IDF` 를 사용해서 문서를 벡터화하고 이 문서들을 클러스터링해보려고 합니다. 이전에는 **키워드의 구조적 성질을 벡터화하여 클러스터링**했습니다만, 문서에는 보다 포괄적인 정보가 담겨있기 때문에, 클러스터링의 결과가 더 잘 나오지 않을까, 라고 낙관적으로 다시 생각해보기로 합니다(낙관적으로!!! 생각하는게 중요합니다 어차피 안될지 몰라도 낙관적으로!!). 
- 그렇게 한 뒤에 적합하지 않은 문서를 모두 걸러내고, 남은 문서들에 대해서 좀 더 깊게 분석하는 것이 좋지 않을까? 라고 생각해봅니당

## preprocessing abstract, 우선 데이터 정리부터!

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

## make tfidf vector

- 그거 뭐 그냥 쉽게 만들면 되는거 아니냐! 라고 말할 수 있습니다만, 변수를 조절하면서 계속 확인해야 합니다. 매우 번거롭죠. 여러분 데이터 분석은 노가다와 같은 말입니다. 뇌를!! 혹사!! 시킨다!!!
- 아무튼 다음 변수들에 따라서 값이 달라집니다. 어떻게 바꾸면 좋을지 참 어려워용. 
    - `ngram_range`: 일반 대화에서는 1-gram으로 충분할지 모르겠지만, 제가 대상으로 하는 데이터는 논문 초록입니다. 이 경우는 (제 편견일 수도 있겟지만) 복합어가 많을 것 같아요. 그래서 이 레인지를 약간 올려서 (2, 4)정도로 해보았습니다. 
    - `min_df`: **document frequency가 최소한 몇 은 되어야 하느냐**, 라는 이야기입니다. 예를 들어 전체 문서에서 딱 한 번 등장하는데, 이 아이까지 벡터의 디멘션으로 고려해야 하느냐? 그럼 shape이 엄청 길어질텐데? 라는 거죠. 정수 값을 넘길 수도 잇지만, float 값을 넘기면 알아서 전체 빈도 중에서 하위 퍼센트를 걸러냅니다. 
    - `max_df`: **document frequency가 최대한 몇이 되면 안된다**, 라는 말입니다. 'is'같은 단어는 아마도 모든 문서에서 등장할거에요. 그렇다면, 이 단어도 고려해야 하나요? 무의미한 값인데? 그래서 제외합니다. 
    - `binary`: 값에 weight를 주느냐 안주느냐 의미인데, 0보다 크면 1 아니면 0으로 변환하는 것을 말합니다. 이건 관점에 대한 이야기인데, document간의 길이 편차가 크다면 이를 binary로 변경하는 것이 더 좋을 수도 있을 것 같습니다. 

### check document frequency dist. 

- 생각해보니까, min_df, max_df를 결정하기 위해서는 **document frequency의 분포를 먼저 확인하는 것이 필요하지 않을까?** 라는 생각이 들었습니다. 그래서, 이 분포를 도출해서 그림으로 그려주는 코드를 만들고, 플로팅해보았습니다. 

```python
"""
make document frequency distribution
"""

import matplotlib.pyplot as plt
from matplotlib import gridspec

def plot_document_frequency_dist(i_S, min_df=2, max_df=10000):
    """
    텍스트 시리즈를 읽어서 워드의 분포를 파악하고, 해당 워드의 document frequency를 고려하여 
    분포를 그려준다. 
    단, 아직 n-gram의 경우는 해결해주지 않음. 
    """
    df_dict = {}
    for s in i_S:
        ws = set(s.split(" "))
        for w in ws:
            if w in df_dict.keys():
                df_dict[w]+=1
            else:
                df_dict[w]=1
    """min_df or max_df 를 float으로 받으면, 전체 문서 대비 비율로 계산한다. 
    """
    vs = sorted(list(df_dict.values()))
    if min_df < 1: # 1보다 작을 경우에는 전체 문서에 등장하는 비율로 계산함
        min_df = round(len(i_S)*min_df)
    if max_df < 1: # 1보다 작을 경우에는 전체 문서에 등장하는 비율로 계산함
        max_df = round(len(i_S)*max_df)
    if min_df > max_df: # min_df 가 max_df보다 작아야 함. 
        print("min_df({}) is bigger than max_df({})".format(min_df, max_df))
        return None
    for k,v in df_dict.copy().items():
        if v<min_df or max_df<v:
            del df_dict[k]
    print("min_df({}), max_df({})".format(min_df, max_df))
    print("length of vocab: {}".format(len(df_dict.values())))
    
    vs = sorted(list(df_dict.values()))
    
    fig = plt.figure(figsize=(15, 3)) 
    gs = gridspec.GridSpec(nrows=1, ncols=2, 
                           height_ratios=[1], width_ratios=[1, 4]
                          )
    # plot sorted list
    ax0 = plt.subplot(gs[0])
    ax0.plot(vs)
    ax0.set_title("sorted plot")

    # box plot
    ax1 = plt.subplot(gs[1])
    ax1.boxplot(vs, vert=False, notch=True, whis=2.0)
    ax1.set_title('box-plot')
    plt.show()
    return fig

fitered_abstract = filtering_abstract(df['Abstract'])

for i in range(0, 6):
    plot_document_frequency_dist(
        fitered_abstract, min_df=1+i*30, max_df=0.999-(i*0.19)
    ).savefig('../../assets/images/markdown_img/entir_box_plot201805161700_{}.svg'.format(i))
```

- 아래의 연속된 그림을 보면 아시겠지만, 처음에 min_df, max_df를 전체로 했을 때는 그 결과가 너무 outlier들에 몰려 있는 것을 알수 있었는데, min_df와 max_df를 조절해서 plotting했을 때 linear하고, boxplot도 예쁘게 그려지는 형태로 만들어집니다. 

![](/assets/images/markdown_img/entir_box_plot201805161700_0.svg)

![](/assets/images/markdown_img/entir_box_plot201805161700_1.svg)

![](/assets/images/markdown_img/entir_box_plot201805161700_2.svg)

![](/assets/images/markdown_img/entir_box_plot201805161700_3.svg)

![](/assets/images/markdown_img/entir_box_plot201805161700_4.svg)

![](/assets/images/markdown_img/entir_box_plot201805161700_5.svg)

- 결과적으로, **min_df=151, max_df=648** 로 했을때 적당히 예쁘게 나온 것 같아서 이걸로 사용해보려고 합니다. 여전히 차원은 1000 정도로 매우 높은 편이구요. 


## 이제 clustering and visualization!!!

- 아 간단하게 하려고 했는데 하다보니 넘나 인생은 힘들고 길군요. 흑흑. 
- 이제 결과를 가지고 클러스터링을 해보려고 합니당. 코드는 아래와 같습니다. min_df, max_df 는 전체 분포를 그림 그려가면서 뽑은 걸로 넣어주었구요. 

```python
from sklearn.feature_extraction.text import TfidfVectorizer
def make_tfidf_df(sent_lst):
    TFIDFmodel = TfidfVectorizer(
        ngram_range=(1,1), # 앞 뒤 window를 고려하여 확장된 형태로 제시해줌. phrase를 뽑아낼 수 있는 강점이 있기는 할듯. 
        min_df = 151, # document freqeuency 가 min_df 이상은 되는 키워드만으로 vocabulary를 구성
        max_df = 648,# document frequency가 max_df 이하인 키워드만으로 vocabulary를 구성 
        binary = False # binary이면 있다 없다 구조로 변경됨
    )
    TFIDFmodel.fit(sent_lst)
    return pd.DataFrame(TFIDFmodel.transform(sent_lst).toarray(),
             columns = [it[0] for it in sorted(TFIDFmodel.vocabulary_.items(), key=lambda x: x[1])])
#print(df['Abstract'].head(10))
abs_series = filtering_abstract(df['Abstract'])
abs_tfidf_df = make_tfidf_df(abs_series)
```

- 그래, 중요한 놈들만으로 정리를 해준 건 알겠고, 이제 클러스터링을 하면 되는데, 클러스터링을 해도 될까? 확인해보려고 합니다. 어떻게 확인하냐면 일단 그림을 그려봅시당. 
- 음, 그런데, 이렇게 중요한 놈들로만 정리를 해주는게 맞는지도 모르겠다. 사실 아, 데이터 분석에서 어려운 게 항상 데이터 필터링이라서, 어디까지가 유의미한 디멘션이고, 어디가 노이즈인지를 구분하는 것이 정말 어려움....


## 뜬금없는 결말. 

- 몇 가지를 해봤는데..
    - 이후에, 현재 결과에 대해서 클러스터링도 해봤는데 ==> 이상하고 
    - 그래서, 그냥 전체 min_df, max_df를 늘리거나, n_gram range를 증가시켜서도 해봤지만 ==> 딱히 유의미하다고 보기 어려움. 
    - 그다음에 각각을 2차원 공간에 전사해서 시각화해봤지만 ==> 명확하게 구별된다고 보기도 어려움
    - 클러스터 별 논문을 확인해봤는데 ==> 확실한 차별적인 특성이 있다고 하기 좀 애매... 

- 결과적으로 문제는, 일반적인 비교사학습이 가지는 문제점, **그래서, 얘가 잘 되었는지를 어떻게 알 수 있는데?**가 되겠죠. '클러스터링, 그냥 하면 됩니다, 코드 몇 줄 그냥 넣으면 되요'. 그런데, 그래서 그게 클러스터가 3개가 최적인지, 4개가 최적인지, 그리고 그 3개가 각각 제대로 되었는지를 어떻게 확인할 수 있죠? 
- 모릅니다. 결국 전문가의 평가가 들어가야 하죠. 대략 뭐 내부의 거리가 외부와의 거리보다 가깝다, 뭐 그렇게 썰은 풀 수 있지만, 그게 **합리적**이고 맞는 길인지가 참 애매한 것 같아요. 

- 그래서 일단 접습니다. 뭐, 지금까지는 일단 공부한 거라고 생각해야 할것 같아요. 후우. 


## reference

- <https://rare-technologies.com/doc2vec-tutorial/>
- <http://www.engear.net/wp/doc2vec-시작하기/>
- <https://www.lucypark.kr/docs/2015-pyconkr/#59>