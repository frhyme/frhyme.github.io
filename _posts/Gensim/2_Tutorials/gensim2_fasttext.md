


## What is FastText? 

## When to use FastText

- fastText의 기본 원리는 단어에 존재하는 "morphological structure"를 활용하여, 단어의 의미 정보를 추출해내는 것입니다. 이는, 전통적인 traditional word embedding 방식인 word vocabulary에 근거한 word embedding 방식에서는 존재하지 않았던 것이죠. 따라서, 기존의 word2vec의 경우에는 word vocabulary에 존재하지 않는 "새로운 단어"에 대해서는 vector로 표현할 수 없었습니다. 

![morphological structure](https://www.cs.bham.ac.uk/~pjh/sem1a5/pt2/pt2_intro_morph_1.gif)

- 하지만, fastText의 경우는 morphological structure에 근거하여 단어의 의미를 추출하기 때문에, 존재하지 않더라도, 의미를 추출할 수 있습니다. 따라서, 형태적으로 어느 정도 비슷한, german, turkish와 같은 단어들에 대해서도 의미를 어느 정도 유추할 수 있다는 강점이 있죠. 
- fastText는 모든 단어들에 대해서 "그 단어를 내부 subword의 조합"으로 생각합니다. 여기서, subword는 character에 대한 ngram이라고 생각할 수도 있겠죠. 그리고, word에 대한 vector는 단순하게, char-ngram 각각의 벡터의 합으로 나타내어지는 것이죠. 따라서, fastText의 경우 vocabulary에 없는 단어들에 대해서도 효과적으로 추론할 수 있습니다. 최소한, 하나의 character라도 vocabulary에 존재한다면 해결된다는 이야기죠.



## reference

- [gensim - tutorials - fasttext](https://radimrehurek.com/gensim/auto_examples/tutorials/run_fasttext.html#sphx-glr-auto-examples-tutorials-run-fasttext-py)