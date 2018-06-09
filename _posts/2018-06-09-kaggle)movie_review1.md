---
title: kaggle) imdb movie review를 분석합니다 - 1편
category: machine-learning
tags: kaggle python python-lib word2vec sklearn random-forest BeautifulSoup numpy pandas nltk 
---

## movie review분석하기!!!

- 요즘은 kaggle에 할만한 컴페티션을 찾아 다닙니다. 찾다가, movie review가 있고, 어떻게 해야 하는지에 대해서도 매우 자세하게 나와 있는 것 같아서, 한번 해보려고 해요!! 뭔가 계속 kaggle만 하니까 약간 잉여처럼 보이는 것 같기도 한데...맞습니다. 

## part 1: using bow(Bag of words)

- 일단은 아주 간단한 방법부터 시작합니다. 문서(라고 하겠습니다. 리뷰든, 무엇이든 하나의 글 집합을 의미합니다)는 문장들로 이루어져 있습니다. 다시 문장은 워드로 구성되어 있죠. 아주 단순하게, 단어에 많이 존재하는 단어들이 해당 문서의 특성을 말해준다고, 말할 수 있습니다. 물론 단어의 문맥도 고려해야겠지만, 데이터가 많다면 이런 단순한 접근만으로도 유의미한 결과를 가져올 수 있지 않을까? 하고 생각합니다. 
- 그래서, 아주 단순하게 진행합니다. 

### 몇 가지. 

- 기본적인 텍스트처리(소문자화, 공백 제거, html tag 제거) + nltk에 있는 stopword 들 삭제 
- count vectorization 
    - 이 때, train_data에 fitting한 vectorizer를 test_data에 tranform해야 함을 명심!, test_data에 새롭게 `fit_transform`을 하면 안된다. 
- random forest 에 fitting and prediction 

### coding 

- 다른 건 별로 수정하지 않고, randomforest의 `n_estimator`만 올리면서 진행했습니다. 
- 이렇게 돌려도, 0.84566 정도의 accuracy가 나오네요 오....

```python
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import re 
from bs4 import BeautifulSoup 
import nltk
from sklearn.feature_extraction.text import CountVectorizer

train_url = '/Users/frhyme/Downloads/labeledTrainData.tsv'
train_df = pd.read_csv(train_url, delimiter='\t', header=0, quoting=3)
#train_df = train_df[:1000] # 생각보다 계산이 오래 걸려서 일단 이걸 넣어줌

def cleaning_each_review(raw_review):
    cleaned_review = BeautifulSoup(raw_review, 'lxml').get_text()# 태그를 없애줍니다. 
    cleaned_review = re.sub("[^a-zA-Z]"," ", cleaned_review ).lower().strip()
    while "  " in cleaned_review: # 공백을 없애줍니다. 
        cleaned_review = cleaned_review.replace("  ", " ")
    words_in_cleaned_review = cleaned_review.split(" ")# 단어를 잘라줍니다. 
    stop_words = nltk.corpus.stopwords.words('english')
    # nltk에 정의된 무의미한 단어를 삭제해줍니다. 
    words_in_cleaned_review = filter(lambda w: True if w not in stop_words else False, words_in_cleaned_review)    
    return " ".join(list(words_in_cleaned_review))
train_df['cleaned_movie_review'] = train_df['review'].apply(cleaning_each_review)
print("----data cleaning complete----")

vectorizer = CountVectorizer(analyzer = "word", tokenizer = None,
                             preprocessor = None, stop_words = None, 
                             max_features = 5000) # max_feature의 술ㄹ 조절하자

# CountVectorizer의 결과는 sparse matrix로 리턴되는데, 따라서 이를 np.array로 변형해주는 것이 필요함. 
train_word_count_df = pd.DataFrame(vectorizer.fit_transform(train_df['cleaned_movie_review']).toarray(), 
                             columns=vectorizer.get_feature_names())
print("----word count vectorization complete----")
"""
값들이 표준화되지도 않았고, n-gram을 사용한 것도 아니고, 
하지만 어쨌든 간에 개별 review에 대해서 feature vector를 만들었습니다. 
이걸 사용해서, 학습을 해보려고 합니다. 믿음의 랜덤포뤠스트!!!
"""
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=100)# n_estimators를 늘리면서 해봐야 할것 같아요. 
rf.fit(train_word_count_df.values, train_df['sentiment'])
print("----fitting complete----")
########

# test_data에 적용해봅니다. 
test_url = '/Users/frhyme/Downloads/testData.tsv'
test_df = pd.read_csv(test_url, delimiter='\t', header=0, quoting=3)
test_df['cleaned_movie_review'] = test_df['review'].apply(cleaning_each_review)

print("----test data count vectorization----")
test_word_count_df = pd.DataFrame(vectorizer.transform(test_df['cleaned_movie_review']).toarray(), 
                             columns=vectorizer.get_feature_names())
output = pd.DataFrame( data={"id":test_df["id"], "sentiment":rf.predict(test_word_count_df.values)} )
# Use pandas to write the comma-separated output file
output.to_csv( "Bag_of_Words_model.csv", index=False, quoting=3 )
print("----all complete upload it on kaggle----")
```


## part 2: word-embedding 

- 여기서부터는 word-embedding을 사용합니다. 텍스트 전처리 과정은 비슷한데, bag of words 때는 필요없다고 판단되는 word들을 모두 지웠는데, 여기서는 어떤 words도 지우지 않습니다. word-embedding은 **개별 단어들이 어디에 위치해 있는가 is 그 단어의 의미**이기 때문에, 모든 단어를 활용해야 합니다. 
- 또한, 그래서, 단어가 아닌 sentence를 활용하는 것이 필요합니다. 정확히는 sentence를 순서대로 word로 쪼개서 만든 word list가 필요하죠. 
- 또한 list of list의 형태로, 넘겨주는 것이 필요합니다. 현재는 paragraph로 있어서, sentence로 잘라주는 것이 필요한데, 다행히도 `nltk`에 문장으로 잘라주는 함수가 있습니다. 
- 또한, BOW에서는 train_data만 이용해 줬지만, 여기서는 train_data와 unlabel_train_data를 모두 이용해줍니다. word-embedding 자체는 unsupervised learning이기 때문에, label이 필요가 없습니다. 단순하게 word를 node로 고려하고 거리를 재는 방법입니다. 
- 이 part2에서는 gensim을 이용한 word-embedding까지만 진행하고, 이후, word-embedding을 이용한, supervised learning은 part3에서 이용합니다. 

### making word semantic vector 

- gensim 라이브러리를 이용해서 word2vec을 이용합니다. 
- 해당 라이브러리를 이용할 때 중요한 주요 parameter들은 대략 다음과 같습니다. 
    - **Architecture**: Architecture options are skip-gram (default) or continuous bag of words. We found that skip-gram was very slightly slower but produced better results.
    - **Training algorithm**: Hierarchical softmax (default) or negative sampling. For us, the default worked well.
    - **Downsampling of frequent words**: The Google documentation recommends values between .00001 and .001. For us, values closer 0.001 seemed to improve the accuracy of the final model.
    - **Word vector dimensionality**: More features result in longer runtimes, and often, but not always, result in better models. Reasonable values can be in the tens to hundreds; we used 300.
    - **Context / window size**: How many words of context should the training algorithm take into account? 10 seems to work well for hierarchical softmax (more is better, up to a point).
    - **Worker threads**: Number of parallel processes to run. This is computer-specific, but between 4 and 6 should work on most systems.
    - **Minimum word count**: This helps limit the size of the vocabulary to meaningful words. Any word that does not occur at least this many times across all documents is ignored. Reasonable values could be between 10 and 100. In this case, since each movie occurs 30 times, we set the minimum word count to 40, to avoid attaching too much importance to individual movie titles. This resulted in an overall vocabulary size of around 15,000 words. Higher values also help limit run time.
- 결과로 나온 sentence의 수가 다른데, 그냥 무시합니다. 뭐 그놈이 그놈이겠져. 
- 그리고 이걸 돌리면 매우 CPU가 혹사당하는데 얼마나 혹사당하는지를 보려면 `top -o cpu`를 터미널에 쳐주면 됩니당


```python

## part 2 
import warnings
warnings.filterwarnings('ignore')
"""
- 여기서는 word-embedding을 이용합니다. 
"""
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import re 
from bs4 import BeautifulSoup 
import nltk
import nltk.data
from sklearn.feature_extraction.text import CountVectorizer

import itertools

train_url = '/Users/frhyme/Downloads/labeledTrainData.tsv'
train_df = pd.read_csv(train_url, delimiter='\t', header=0, quoting=3)

unlabeled_train_url = '/Users/frhyme/Downloads/unlabeledTrainData.tsv'
unlabeled_train_df = pd.read_csv(unlabeled_train_url, delimiter='\t', header=0, quoting=3)

def review_to_wordlist( review, remove_stopwords=False):
    review_text = BeautifulSoup(review).get_text()
    review_text = re.sub("[^a-zA-Z]"," ", review_text)
    words = review_text.lower().split()
    if remove_stopwords:
        stops = set(stopwords.words("english"))
        words = [w for w in words if not w in stops]
    return(words)

def review_to_sentences(review, tokenizer, remove_stopwords=False):
    # sentence tokenizer가 밑에서 선언되는데, 그냥 여기서 디폴트로 만들어주는 게 더 좋을 수 있다. 
    # 흠...이 tokenizer는 점도 없는데 어떻게 이렇게 잘 잘라주는거지. 
    raw_sentences = tokenizer.tokenize(review.strip())
    sentences = []
    for raw_sentence in raw_sentences:
        # If a sentence is empty, skip it
        if len(raw_sentence) > 0:
            # Otherwise, call review_to_wordlist to get a list of words
            sentences.append( review_to_wordlist(raw_sentence) )
    return sentences

sentences = []
for i, r in enumerate(list(train_df['review'])+list(unlabeled_train_df['review'])):
    sentences += review_to_sentences(r, tokenizer=nltk.data.load('tokenizers/punkt/english.pickle'))
    if i % 5000==0:
        print("{} complete".format(i))
"""
- 결과로 나오는 sentence의 수가 kaggle의 수와 다를 수는 있습니다(저의 경우 대략 2000개 차이남). 큰 문제는 아니므로 무시합니다. 
"""

# Import the built-in logging module and configure it so that Word2Vec 
# creates nice output messages
import logging
# logging 귀찮아서안하기로 함. 대충 3-4분 걸림. 
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Initialize and train the model (this will take some time)
from gensim.models import word2vec
print("Training model...")
model = word2vec.Word2Vec(sentences, 
                          workers = 4,# Number of threads to run in parallel
                          size = 300, # Word vector dimensionality                      
                          min_count = 40, # Minimum word count
                          window = 10, # Context window size
                          sample = 1e-3, # Downsample setting for frequent words
                         )
# If you don't plan to train the model any further, calling 
# init_sims will make the model much more memory-efficient.
model.init_sims(replace=True)

# It can be helpful to create a meaningful model name and 
# save the model for later use. You can load it later using Word2Vec.load()
model_name = "300features_40minwords_10context"
model.save(model_name)
print("training complete")
```

- 위 코드를 돌리면, 잘 학습이 됩니다 하하하하하


### exploring model

- 학습한 결과를 간단하게 `doesnt_match`를 활용해 확인해볼 수 있습니다. 해당 method는 공백으로 구분된 문장에서 가장 이질적인 단어 하나를 돌려주는 메소드인데, 대충 보면, 언뜻 봐도 리즈너블한 결과가 나오는 것을 알 수 있습니다. 

```python
doesnt_match_sentences = [
    "man woman child kitchen", 
    "france england germany berlin", 
    "paris berlin london austria",
    'movie actor actress director', 
    'movie actor actress', 
    'movie cinema film art',
    'actor actress director', 
]
for s in doesnt_match_sentences:
    print("{} => {}".format(s, model.doesnt_match(s.split())))
print("---doesnt match over---")
for w in ['man', 'movie', 'soldier']:
    similar_words = ", ".join([s_w[0] for s_w in model.most_similar(w)][:5])
    print("'{}' is most similar with ({})".format(w, similar_words))
print("---most similar over---")
```

```
man woman child kitchen => kitchen
france england germany berlin => berlin
paris berlin london austria => paris
movie actor actress director => movie
movie actor actress => movie
movie cinema film art => art
actor actress director => director
---doesnt match over---
'man' is most similar with (woman, lady, monk, lad, farmer)
'movie' is most similar with (film, flick, movies, it, sequel)
'soldier' is most similar with (army, warrior, navy, marine, dictator)
---most similar over---
```

## part 3: words to paragraph

- word에 대해서 각각 semantic vector를 계산했다면, 이제 이를 이용해서 paragraph에 대한 semantice vector를 구성할 수 있다. 
- 그 두 가지 방법에 대해서 각각 설명한다. 

### word to paragraph: vector averaging

- 그냥 paragraph에 있는 모든 word의 semantic vector의 평균값을 냅니다. 간단하죠. 
- 이렇게 word semantic vector의 평균을 papragraph semantice vector로 생각하고, 바로 random forest에 구겨 넣습니다. 되겠죠 뭐 먼산. 
- `n_estimators`의 수를 10, 50, 100으로 변화시켜가면서 하고 있는데, 생각만큼 잘 되지 않음. BOW를 사용했을때, 0.84정도 나왔는데, 비슷한 수준밖에 되지 않음. `n_estimators`를 500까지도 올려보겠습니다. 
- 답이 읎다. 계속 0.83대에 머무르네요....일단은 word clustering으로 넘어가 보겠습니다. 

```python
## after making train_df and test_df 
def makeFeatureVec(words, model, num_features):
    """
    - word list의 개별 semantic vector의 평균을 계산하여 돌려주는 함수
    - method가 조금 달라서 고쳐준 부분이 있음 
    """
    # Pre-initialize an empty numpy array (for speed)
    featureVec = np.zeros((num_features,),dtype="float32")
    nwords = 0.0
    # the model's vocabulary. Convert it to a set, for speed 
    index2word_set = set(model.wv.index2word)
    for word in words:
        if word in index2word_set: 
            nwords = nwords + 1.0
            featureVec = np.add(featureVec, model[word])
    return np.divide(featureVec,nwords) # Divide the result by the number of words to get the average

def getAvgFeatureVecs(reviews, model, num_features):
    """
    - makeFeatureVec가 개별 word list로부터 semantic vector의 평균을 계산하여 돌려줬다면
    - 이 함수의 경우는 review list로부터 semantice vector의 평균 list를 돌려준다. 
    - 이전에 word2vec 학습할때 num_feature의 경우 300으로 했으므로 아마도 300이어야 할듯
    - 이건 굳이 argument로 넣을 필요 없이, 만든 model의 num_feature를 내부에서 돌리는게 더 효율적이지 않나? 
    """
    # Preallocate a 2D numpy array, for speed
    reviewFeatureVecs = np.zeros((len(reviews),num_features),dtype="float32")
    # Loop through the reviews
    for i, review in enumerate(reviews):
        if i%5000. == 0.:
            print("Review {:.0f} of {:.0f}".format(i, len(reviews)))
        reviewFeatureVecs[i] = makeFeatureVec(review, model, num_features)
    return reviewFeatureVecs

clean_train_reviews = []
for review in train_df["review"]:
    clean_train_reviews.append( review_to_wordlist( review, remove_stopwords=True ))
trainDataVecs = getAvgFeatureVecs( clean_train_reviews, model, num_features=300 )
print("---train data over---")

clean_test_reviews = []
for review in test_df["review"]:
    clean_test_reviews.append( review_to_wordlist( review, remove_stopwords=True ))
testDataVecs = getAvgFeatureVecs( clean_test_reviews, model, num_features=300)
print("---test data over---")

#######
### random forest fitting 
#######
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier( n_estimators = 500)
print("Fitting a random forest to labeled training data...")
rf = rf.fit( trainDataVecs, train_df["sentiment"] )
# Write the test results 
output = pd.DataFrame( data={"id": test_df["id"], "sentiment": rf.predict( testDataVecs )} )
output.to_csv( "Word2Vec_AverageVectors.csv", index=False, quoting=3 )
print('complete')
```

### word to paragraph: using clustering

- paragraph의 word들에 대한 semantic vector를 평균으로 내어 paragraph vector로 고려한 방금의 approach로는 효과적인 결과를 얻지못했습니다. BOW와 큰 차이가 없어요. 
- 그래서 적절하게 clustering을 이용해보려고 합니다. 이전에는 **Bag of Word**를 이용했다면, 여기서는 **Bag of Centroids**
를 이용합니다. 
- 간단하게, review의 word들이 어떤 cluster에 속하는지를 통해 review을 표현하는 거죠. 간단히 어떤 cluster에 속하는지를 count해서 vector로 만듭니다. 
- 문제는 clustering을 할때 시간이 아주 오래 걸립니다. 
- 생각해보면 당연해요. vector의 개수가 250000개이고, vecotr의 크기도 300이니까, 아주 빡십니다. 
- clustering 결과가 딱히 유의미한지는 약간 의문이 들기는 하는데 cluster 10은 좀 유의미하네요. 웨스턴 스파게티, 세리지오 레오네, 장고까지! 의미가 있습니다하하핫. 

```
cluster 0:
['box', 'blockbuster']
-------
cluster 1:
['companion', 'sweetheart', 'muse']
-------
cluster 2:
['alleged', 'accidental', 'untimely']
-------
cluster 3:
['wong', 'antonio', 'chang', 'guild', 'vidor', 'alberto', 'dong', 'ghai']
-------
cluster 4:
['africans', 'mormons']
-------
cluster 5:
['launch', 'overnight', 'mp', 'launching', 'katrina']
-------
cluster 6:
['ground', 'lights', 'walls', 'doors', 'closed', 'buildings', 'rooms', 'dust', 'corpses', 'waves', 'bars', 'windows', 'backs', 'roads', 'boxes', 'blocks', 'corners', 'corridors', 'spaces', 'floors', 'curtains']
-------
cluster 7:
['amusingly']
-------
cluster 8:
['states', 'president', 'united', 'bush', 'coup', 'presidential', 'administration', 'republican', 'elected', 'chavez', 'congress', 'constitution', 'germs']
-------
cluster 9:
['logan', 'bart', 'louie', 'kingpin', 'wolverine', 'johnnie', 'bandit', 'blackie', 'gunman', 'curt', 'coroner', 'trump', 'feinstone', 'paco', 'calvin', 'pickpocket', 'jeb']
-------
cluster 10:
['western', 'spaghetti', 'sergio', 'leone', 'django', 'corbucci', 'sukiyaki']
-------
```

- clustering을 해주는 건, 일종의 feature engineering으로 해석이 됩니다. semantically 비슷한 것끼리 묶어주고, 묶어준 놈들끼리 차이를 두도록 feature를 구성하면 좋겠죠. 
- 다만 그 결과 또한, 그다지 잘 나오는것 같지는 않네요. 

- 아무튼 했으니 코드를 넣어두겠습니다. 

```python
# using clustering after word-embedding 
from sklearn.cluster import KMeans
import time

start = time.time() # Start time
word_vectors = model.wv.syn0
# Initalize a k-means object and use it to extract centroids
kmeans_clustering = KMeans( n_clusters = word_vectors.shape[0]//5 )
idx = kmeans_clustering.fit_predict( word_vectors )
# Get the end time and print how long the process took
print("Time taken for K Means clustering: {} seconds".format(time.time()- start))
##### clustering over 
word_centroid_map = dict(zip(model.wv.index2word, idx))
# cluster를 key로 두고, 포함되는 모든 word를 리스트로 value로 넣은 dict
word_centroid_map_grouped_dict = {cluster: [] for cluster in range(min(word_centroid_map.values()), 
                                                              max(word_centroid_map.values())+1)}
for w, k in word_centroid_map.items():
    word_centroid_map_grouped_dict[k].append(w)

# 상위 10개의 클러스트터를 출력해서 한번 봅닌다. 
for k in word_centroid_map_grouped_dict.keys():
    if k >10:
        break
    else:
        print("cluster {}:".format(k))
        print(word_centroid_map_grouped_dict[k])
        print("-------")
### 
def create_bag_of_centroids( wordlist, word_centroid_map ):
    # Pre-allocate the bag of centroids vector (for speed)
    bag_of_centroids = np.zeros( max( word_centroid_map.values() ) + 1, dtype="float32" )
    # cluster에 속하면 count를 늘림. 단순함. 
    for word in wordlist:
        if word in word_centroid_map.keys():
            bag_of_centroids[word_centroid_map[word]] += 1
    # Return the "bag of centroids"
    return bag_of_centroids
# Pre-allocate an array for the training set bags of centroids (for speed)
train_centroids = np.zeros( (train_df["review"].size, word_vectors.shape[0]//5), dtype="float32" )
for i, review in enumerate(clean_train_reviews):
    train_centroids[i] = create_bag_of_centroids( review, word_centroid_map )
# Repeat for test reviews 
test_centroids = np.zeros(( test_df["review"].size, word_vectors.shape[0]//5), dtype="float32" )
for i, review in enumerate(clean_test_reviews):
    test_centroids[i] = create_bag_of_centroids( review, word_centroid_map )
    
# Fit a random forest and extract predictions 
rf = RandomForestClassifier(n_estimators = 200)
# Fitting the forest may take a few minutes
print("Fitting a random forest to labeled training data...")
rf.fit(train_centroids,train_df["sentiment"])
# Write the test results 
output = pd.DataFrame(data={"id": test_df["id"], "sentiment": rf.predict(test_centroids)})
output.to_csv( "BagOfCentroids.csv", index=False, quoting=3)
print('complete')
```

## part 4: using deep and non-deep 

- 앞서 제가 말한대로, avearage paragraph vector 나, centroids counter vectorizer의 경우 모두 BOW보다 딱히 성능이 좋지 못합니다. 이는 개별 word의 결과를 paragraph로 종합하는 과정에서, 당연하지만 context가 모두 무너지기 때문이죠. 
    - `networkx`를 이용해서 직접 네트워크를 모델링해서 이용해볼 수도 있을 것 같긴 한데, 일단 이건 나중에 하자
- 이를 극복하려면, 다음 몇 가지를 수행하면 좋다고 하는데, 
    - 데이터를 더 모으거나
    - 출판된 논문에서 만든 paragraph vector를 사용해보자

## wrap-up

- 결론적으로, 그냥 알아서 잘해야 합니다 허허허허. 
- 일단 제공된 방법으로는 0.85정도의 정확도밖에 확보를 못했어요. 일단 포스트가 너무 길어지는 것 같으니, 다른 포스트에서 다른 방법들을 좀 더 써보도록 하겠습니다.



## reference

- <https://www.kaggle.com/c/word2vec-nlp-tutorial>