---
title: gensim - reproducible traing - fix seed
category: python-libs
tags: python python-libs gensim word2vec random seed hash
---

## 2-line summary 

- gensim은 word vector를 초기화할 때, seed 값을 이용하며, 하나의 코드 실행 내에서 seed륿 변경하지 않는 한, 값은 동일하게 설정된다. 
- 하지만, 서로 다른 코드 실행에서는 초기 값이 달라질 수 있으며, 이를 조절하기 위해서는 커맨드라인에서 `PYTHONHASHSEED=123 python gensim_reproducible.py`로 코드를 실행해주는 것이 필요하다.

## reproducible gensim. 

- reproducibility를 한국말로 바꾼다면 "재생산성"이 되겠죠. 머신러닝 모델을 만들 때 가장 많이 하게되는 것은 아무래도 parameter tuning이죠. 모델을 만들고 가령 window를 바꾼다거나, epoch을 수정한다거나 하는 식으로 조금씩 변형을 계속 가하면서 어떤 결과가 발생하는지를 알아야 합니다. 

### default seed 

- 다음과 같은 간단한 word2vec 모델을 만들어서 결과를 보겠습니다. 

```python
import gensim

sentences = [
    "He is a boy", "He is a man", "She is a girl"
]*10
sentences = [s.lower().strip().split(" ") for s in sentences]
#----------------------------------------
# BUILD word2vec vocab and TRAIN
for i in range(0, 3):
    WVmodel = gensim.models.word2vec.Word2Vec(size=50, min_count=1)
    WVmodel.build_vocab(sentences)
    WVmodel.train(sentences, total_examples=len(sentences), epochs=30)
    print(WVmodel.wv['boy'][:5])
```

- 결과를 보시면, 따로 seed 값을 지정하지 않았는데도 불구하고, 한 코드안에서는 같은 결과가 생성되는 것을 알 수 있습니다. 
- 이는 seed의 default값이 1이기 때문인 것이죠. 

```python
[ 0.00499384 -0.0028784   0.00208957 -0.00174666  0.0063178 ]
[ 0.00499384 -0.0028784   0.00208957 -0.00174666  0.0063178 ]
[ 0.00499384 -0.0028784   0.00208957 -0.00174666  0.0063178 ]
```

- 다음처럼 `seed`를 변경해주면 값이 매번 다르게 나오게 됩니다. 그리고, 코드 내에서 seed가 변하지 않도록 default값을 지정해준 것은 매우 바람직하고, 타당한 결정이죠.

```python
for i in range(0, 3):
    WVmodel = gensim.models.word2vec.Word2Vec(size=50, min_count=1, seed=i)
    WVmodel.build_vocab(sentences)
    WVmodel.train(sentences, total_examples=len(sentences), epochs=30)
    print(WVmodel.wv['boy'][:5])
```

- 다만, 흥미로운 것은 이전의 실행에서도 `seed=1`이었고, 그 다음의 실행에서도 첫번째는 `seed=1`이었는데, 결과가 다릅니다.

```python
[ 0.00598792 -0.00473597  0.0073735  -0.00795636  0.00356294]
[-0.00351215 -0.00233458  0.00936766 -0.00995884 -0.00403269]
[0.00913222 0.00193524 0.00175384 0.00874679 0.00710758]
```

### Different weight on different code execution 

- 결론적으로, 서로 다른 코드 실행에서는 서로 다르게 weight가 초기화됩니다.
- 물론 seed라는 것이 있지만, 이 아이는 한 코드 실행에서만 동일하게 유지해주는 것 뿐이고, 다른 코드 실행에서는 다른 결과를 만들어냅니다. 
- 따라서, 어떤 코드 실행에서도 동일한 결과를 만들어내려면, 코드 내부에서 무엇을 건드리는 것이 아니라, 아래와 같이 커맨드 라인에서 값을 하나 넘겨줘야 합니다. 
- `PYTHONHASHSEED=123`라는 값을 넘겨주며 전체 python의 동작을 제어해야 한다는 것이죠.

```bash
PYTHONHASHSEED=123 python gensim_reproducible.py
```

## WHY? 

- [gensim - models - word2vec](https://github.com/RaRe-Technologies/gensim/blob/master/gensim/models/word2vec.py#L457)부분에서 `seed`에 대한 설명 부분은 다음과 같습니다. 

> Seed for the random number generator. Initial vectors for each word are seeded with a hash of the concatenation of word + `str(seed)`. Note that for a fully deterministically-reproducible run you must also limit the model to a single worker thread (`workers=1`), to eliminate ordering jitter from OS thread scheduling. (In Python 3, reproducibility between interpreter launches also requires use of the `PYTHONHASHSEED` environment variable to control hash randomization).

- 해석을 하자면 "word에 대한 초기 vector는 word와 str(seed)를 합친 string에 대해서 `__hash__`를 적용하여 표현된다. 모델에 대해서 deterministically-reproducible을 적용하려면 `seed`를 고정하고, `workers`를 1로 설정하면 된다.
- 하지만, 서로 다른 실행에 대해서도 적용하기 위해서는 hash randomization을 조절하기 위해서 환경 변수인 `PYTHONHASHSEED`에 대한 값을 함께 넘겨주는 것이 필요하다. 라는 말이죠. 

### hashing. 

- 즉 gensim에서 각 word의 초기 값은 대충 다음과 같이 설정된다는 이야기죠. 그리고, 이 `__hash__`는 gensim이 python에 의존하고 있는 부분이기 때문에, 이 부분까지 확정적으로 진행하려면 `PYTHONHASHSEED`를 특정한 값으로 넘겨주는 것이 필요하다는 이야기가 됩니다.

```python
def init_vector(word="str", seed=1):
    return (word+str(seed)).__hash__()
```


## wrap-up

- 대부분의 코드들에서는 코드 내부에서 `np.random.seed(0)`으로 코드 실행과 상관없이 동일하게 랜덤성을 유지할 수 있습니다. 
- 하지만, 흥미롭게도, `gensim`은 python의 함수인 `__hash__`를 사용하여 랜덤화하기 때문에, 만약 모든 코드 실행에 대해서 동일한 결과를 만들려면 `__hash__`에 영향을 미치는 변수인, `PYTHONHASHSEED`를 커맨드라인에서 설정해줘야 하죠. 

## reference

- [gensims - models - word2vec](https://radimrehurek.com/gensim/models/word2vec.html)
- [stackoverflow: ensure the gensim generate the same word2vec model for different runs](https://stackoverflow.com/questions/34831551/ensure-the-gensim-generate-the-same-word2vec-model-for-different-runs-on-the-sam)