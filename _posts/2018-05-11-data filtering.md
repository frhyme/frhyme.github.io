---
title: 데이터를 필터링합시다. 
category: project
tags: python difflib nltk networkx keyword-network python-lib not-yet
---

## 작업일지

- 제가 궁극적으로 하려는 것은 '저자 키워드'를 필터링 하려는 것입니다. 'small and medium enterprise' 와 'sme'는 같은 의미를 가집니다. 그렇다면 이 두 가지가 모두 표현될 필요는 없겠죠. 따라서 이를 변환하고 싶습니다. 
    - 형태에 따른 분석: 공백, 특수문자 를 삭제하거나, 캐릭터 순서에 따라서 비슷한 경우에 이 유사도를 적용하여 변형합니다. 
    - 의미에 따른 분석: 'small and medium enterprise'와 'medium enterprise'의 경우는 의미적으로 유사하다고도 할 수 있습니다. 음, 이보다는 오히려 'dissimilarity'와 'distance'도 경우에 따라서는 의미적으로 비슷하게 읽힐 수 있습니다. 보통 이러한 작업을 키워드 의미 정제 정도로 표현하는데, 이를 네트워크 분석이나, word-embedding으로 처리할 수 있지 않을까? 하는 것이 제 생각입니다. 
- 따라서 abstract를 이용하면 각 단어들(혹은 단어 구, phrase)을 벡터의 형태로 표현할 수 있으며 이를 이용해 유사도를 평가할 수 있지 않을까? 하는 것이 제 생각입니다. 

### 형태적인 유사도 측정 

- `edit_distance`: w1, w2가 있을때, w1이 w2가 되려면 몇 번 바뀌어야 하는가? 를 카운트한 값, 그러나 word에서는 순서가 매우 중요한데 char간의 순서를 고려하지 않는 다는 단점이 있다. 대신 굉장히 직관적입니다. 
- `SequenceMatcher`: 순서를 고려하여 체크하는 경우, 자세한 건 귀찮아서 적지 않습니다. 
- 코드는 다음과 같습니다. 간단하죠. 

```python
import nltk
import difflib
w1 = "small and medium enterprise"
w2 = "small and medium enterprise sme"
print(nltk.edit_distance(w1, w2))

seq = difflib.SequenceMatcher(None,w1, w2)
print(seq.ratio()) 
seq = difflib.SequenceMatcher(None,'ab', 'abc')
print(seq.ratio()) 
```
```
4
0.9310344827586207
0.8
```

- 이러한 식으로 author keywords를 변환해줍니다. 어느 정도의 threshold로 정하는 것이 적합한지 의문이 들기는 합니다. 대략 보면 0.95 정도면 굉장히 robust한 수준에서 사람이 봐도, '그래, 이건 변경이 되어야지' 정도인데, 0.95라는 값은 십진법을 쓰는 우리에게는 적합한 값이겠지만, 저 분포 상에서 이것이 가장 최적의 값인가?라는 의문은 듭니다. 0.93이거나 뭐 아무튼 그 언저리가 될 수도 있지 않을까 라는 생각이 들긴 하지만, 일단은 그냥 이걸로 하겠습니다. 
    - '형태에 따른 비교 분석'의 경우는 어느 정도 보면서 변경하는 것이 적합한지 확인하는 것이 필요합니다. 
- 또한 변환 dictionary에 transive 관계가 있을 수 있다. 예를 들어서, 
    - a ==> b, b ==> c 인 경우는 a ==> c, b ==> c 인 딕셔너리로 변환을 해야 훨씬 효율적이다. 따라서 해당 코드에서는 이런 부분을 반영하여 transitive한 관계는 무시해주었다.

```python
def make_kwd_change_dict(l_of_l, non_app_keys):
    kwd_counter = itertools.chain.from_iterable(list(auth_kwd_df['Author Keywords']))
    kwd_counter = Counter(total_c).most_common()
    kwd_counter = {w:c for w, c in kwd_counter}

    kwd_changed_dict = {}
    for w1 in sorted(kwd_counter.keys()):
        for w2 in sorted(kwd_counter.keys()):
            if w1 < w2:# 중복으로 계산하는 것을 피하기 위함
                sim_v = difflib.SequenceMatcher(None,w1, w2).ratio()
                if sim_v >= 0.90:
                    if kwd_counter[w1] >= kwd_counter[w2]:
                        kwd_changed_dict[w2]=w1
                        #print("{} ==> {}".format(w2, w1))
                    else:
                        #print("{} ==> {}".format(w1, w2))
                        kwd_changed_dict[w1]=w2
    """
    적합하지 않은 key는 제외함
    """
    new_kwd_changed_dict = filter(lambda k: True if k[0] not in non_app_keys else False, kwd_changed_dict.items())
    new_kwd_changed_dict = {k:v for k, v in new_kwd_changed_dict}
    """
    아래와 같은 상황이 발생할 수 있다. 결국 D 또한 B로 변환되면 되는데, 변환되기 위해서는 
    D ==> C, C==>A, A==B 의 세번 의 과정을 거쳐야 하는 것. 이러한 transivity를 dictionary에서 제외해준다. 

    A: small medium enterprise
    B: small and medium enterprise
    C: small medium enterprise sme
    D: small medium enterprises sme

    A ==> B
    C ==> A
    D ==> C
    """
    non_transvitiy_kwd_dict = {}
    for k, v in new_kwd_changed_dict.items():
        while v in new_kwd_changed_dict.keys():
            v = new_kwd_changed_dict[v]
        non_transvitiy_kwd_dict[k] = v

    for k, v in non_transvitiy_kwd_dict.items():
        print("{} ==> {}".format(k, v))
    return non_transvitiy_kwd_dict
make_kwd_change_dict(list(auth_kwd_df['Author Keywords']), non_app_keys=['lean production', 'coopetition'])
```


## 단어 간의 유사성을 의미론적으로 사용하기

- structural equivalence 를 사용할 수도 있고, word-embedding을 사용할 수도 있을 것 같습니다. 

### structural equivalence 이용하기 

### word-embedding을 함께 이용하기 

- 일단 abstract를 문장으로 나눕니다. `split`만으로는 좀 지저분하게 나와서, 문장으로 나누고, 이를 중심으로 학습시킵니다. 
- 단 개별 element를 공백으로 쪼개서 나눌 것인지, 아니면 'phrase`로 나누어서 학습시킬지는 조금 고민이 필요할 것 같습니다. 

## 최종 코드 

```python
from inflection import singularize 
import nltk
import difflib
from collections import Counter
import itertools 

def total_count(input_df, column_name='Author Keywords'):
    # 'Author Keywords' or 'Noun Phrases'
    r = itertools.chain.from_iterable(input_df[column_name])
    r = Counter(r).most_common()
    return pd.DataFrame(r, columns=[column_name, 'count'])
def make_kwd_change_dict(l_of_l, non_app_keys):
    kwd_counter = itertools.chain.from_iterable(list(auth_kwd_df['Author Keywords']))
    kwd_counter = Counter(total_c).most_common()
    kwd_counter = {w:c for w, c in kwd_counter}

    kwd_changed_dict = {}
    for w1 in sorted(kwd_counter.keys()):
        for w2 in sorted(kwd_counter.keys()):
            if w1 < w2:# 중복으로 계산하는 것을 피하기 위함
                sim_v = difflib.SequenceMatcher(None,w1, w2).ratio()
                if sim_v >= 0.90:
                    if kwd_counter[w1] >= kwd_counter[w2]:
                        kwd_changed_dict[w2]=w1
                        #print("{} ==> {}".format(w2, w1))
                    else:
                        #print("{} ==> {}".format(w1, w2))
                        kwd_changed_dict[w1]=w2
    """
    적합하지 않은 key는 제외함
    """
    new_kwd_changed_dict = filter(lambda k: True if k[0] not in non_app_keys else False, kwd_changed_dict.items())
    new_kwd_changed_dict = {k:v for k, v in new_kwd_changed_dict}
    """
    아래와 같은 상황이 발생할 수 있다. 결국 D 또한 B로 변환되면 되는데, 변환되기 위해서는 
    D ==> C, C==>A, A==B 의 세번 의 과정을 거쳐야 하는 것. 이러한 transivity를 dictionary에서 제외해준다. 

    A: small medium enterprise
    B: small and medium enterprise
    C: small medium enterprise sme
    D: small medium enterprises sme

    A ==> B
    C ==> A
    D ==> C
    """
    non_transvitiy_kwd_dict = {}
    for k, v in new_kwd_changed_dict.items():
        while v in new_kwd_changed_dict.keys():
            v = new_kwd_changed_dict[v]
        non_transvitiy_kwd_dict[k] = v
    return non_transvitiy_kwd_dict
def filtering_auth_kwds(input_df,column_name='Author Keywords', above_n=3):
    print("original unique keyword len: {}".format(
        len(set(itertools.chain.from_iterable(list(input_df[column_name]))))
    ))
    input_df[column_name] = input_df[column_name].apply(lambda ks: [k.strip().lower() for k in ks])
    # edge를 만들때 중복을 방지하기 위해서 sorting해둔다. 
    input_df[column_name] = input_df[column_name].apply(lambda l: sorted(list(set(l))))
    """
    특수문자 삭제: 0-9 이거나, 'a' - 'z'가 아니면 다 삭제. 
    """
    def replace_sp_chr(input_s):
        return "".join(map(lambda c: c if 'a'<=c and c<='z' else c if '0'<=c and c<='9'else " ", input_s)).strip()
    def remove_double_space(input_s):
        while "  " in input_s:
            input_s = input_s.replace("  ", " ")
        return input_s
    input_df[column_name] = input_df[column_name].apply(
        lambda ks: list(map(
            lambda k: remove_double_space(replace_sp_chr(k)), ks)))
    """
    단수 복수 처리: singularized 가 이미 키워드 세트에 포함되어 있을때에만 변형
    """
    all_kwd_set = set(itertools.chain.from_iterable(list(input_df[column_name])))
    to_singular_dict = {}
    for kwd in all_kwd_set:
        singularized_kwd = singularize(kwd)
        if singularized_kwd !=kwd and singularized_kwd in all_kwd_set:
            to_singular_dict[kwd] = singularized_kwd
    input_df[column_name] = input_df[column_name].apply(
        lambda ks: list(map(
            lambda k: to_singular_dict[k] if k in to_singular_dict.keys() else k, ks
        ))
    )
    """
    형태에 따른 키워드 유사도를 평가하여 변환한다. 
    적합하지 않은 키워드는 아래에서 직접 넣어주는 것이 필요함
    """
    non_app_keys = ['lean production', 'coopetition'] ## 여기에 직접 넣어줌.
    kwd_change_dict = make_kwd_change_dict(list(input_df[column_name]), non_app_keys)
    input_df[column_name] = input_df[column_name].apply(
        lambda ks: list(map(
            lambda k: kwd_change_dict[k] if k in kwd_change_dict.keys() else k, ks
        ))
    )
    """
    개별 node가 전체에서 1번 밖에 등장하지 않는 경우도 많은데, 이를 모두 고려해서 분석을 하면, 효율적이지 못한 계산이 된다. 
    따라서, 빈도가 일정 이상을 넘는 경우에 대해서만 고려하여 df를 수정하는 것이 필요하다. 
    """
    filtered_kwds = total_count(input_df, column_name=column_name)
    filtered_kwds = set(filtered_kwds[filtered_kwds['count']>=above_n][column_name])
    input_df[column_name] = input_df[column_name].apply(lambda ks: list(filter(lambda k: True if k in filtered_kwds else False, ks)))
    """
    word embedding 등 다른 데이터 전처리가 필요하다면 여기서 처리하는 것이 좋음. 
    """
    """
    리스트 내부 중복 삭제
    """
    input_df[column_name] = input_df[column_name].apply(
        lambda ks: list(set(ks))
    )
    """
    검색 키워드의 중심에서 거리상으로 측정했을때, 가장 먼 shortest path를 제외하는 등으로의 방식으로도 수행할 수 있지 않을까? 
    """
    print("after filtering, unique keyword len: {}".format(
        len(set(itertools.chain.from_iterable(list(input_df[column_name]))))
    ))
    #print(input_df.head())
    return input_df# 사실 굳이 return을 쓸 필요가 없음. 이미 내부에서 다 바꿔줌. 
auth_kwd_lst = list(df['Author Keywords'].dropna().apply(lambda s: s.strip().split(";")))
auth_kwd_lst = map(lambda ks: [k.strip().lower() for k in ks], auth_kwd_lst)
auth_kwd_lst = list(auth_kwd_lst)
auth_kwd_df = pd.DataFrame({'Author Keywords':auth_kwd_lst})
print(auth_kwd_df.head())
auth_kwd_df = filtering_auth_kwds(auth_kwd_df, column_name='Author Keywords', above_n=5)
```
