---
title: keras를 이용해서, sequence classification 해보기. 
category: machin-learning
tags: classification python python-lib keras LSTM word-embedding sequence numpy 
---

## sequence classificattion??

- 우선, 이 내용은 [이 포스트](https://machinelearningmastery.com/sequence-classification-lstm-recurrent-neural-networks-python-keras/)를 아주 많이 참고하여 작성되었음을 명확하게 밝힙니다.

- RNN으로 만들 수 있는 다양한 모델이 있습니다. 일반적으로는 RNN은 sequence to sequence(기계 번역 등)에 쓰이거나, time series 예측(many to one)등만 알고 있지만, classification에도 문제없이 쓰일 수 있습니다. 
    - 단, 당연하게도, input data가 sequential 한 데이터여야 겠죠. 
- 여기서는 imdb에 쌓여 있는 movie review 데이터를 대상으로 sentiment analysis를 수행합니다. 
    - 단어를 bow, tfidf 를 사용해서 벡터화하거나, n-gram을 활용해서, 문맥을 파악하는 식으로 벡터화하거나, 아무튼 그렇게 해서 classifier를 만들고 적용하는 방식은 이전에 많이 했습니다. 
- 하지만 여기서는, LSTM을 이용합니다. 뭐, n-gram의 경우처럼 일종의 앞 뒤 문맥을 잘 이용해서 학습한다, 정도로 이해하면 되겠네요. 

- 전체 뉴럴넷의 아키텍쳐는 다음과 같습니다. 
    - embedding => convolution => maxpooling => LSTM => Dense
    - 중간중간에 dropout은 알아서 잘 넣습니다. 

## do it. 

- 데이터를 읽고 padding을 넣어줌 
- 개별 무비리뷰에는 캐릭터나 스트링이 들어가있는 것이 아니라, word vocabulary의 index가 채워져 있음. 

```python
import numpy as np 
from keras.datasets import imdb

from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout, Conv1D, MaxPooling1D
from keras.layers.embeddings import Embedding

from keras.preprocessing import sequence

np.random.seed(7)# fix random seed for reproducibility

"""
개별 movie review에 있는, 모든 단어를 고려하는 것은 무의미하기 때문에 
top_words, 즉 상위 5000개의 단어에 대해서만, 추려냄. 나머지는 필터링
그리고 단어는 index로 표시됨.
"""
max_review_length, top_words = 100, 500 # 원래 500, 5000
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=top_words)
"""
sequence의 길이를 똑같이 맞춤. 모두 0으로 채워넣음 
길이가 500보다 큰 경우에는 그냥 일괄적으로 앞부분을 잘라내버림. 
"""
X_train = sequence.pad_sequences(X_train, maxlen=max_review_length)
X_test = sequence.pad_sequences(X_test, maxlen=max_review_length)
print("reading data complete")

```

- 뉴럴넷 아키텍쳐를 만들고, 예측결과를 확인. 

```python
"""
layer의 구성은 
- Embedding: 단어를 벡터화하고, 이 결과 값을 LSTM에 집어넣어줌. 
    - input_dim에 top_words를 넣어주는데, 아마도 내부에서 자동으로 one-hot vector를 만들어주는 것 같음
    - 현재는 one-hot vector가 아니라, 0, 1, 등 word vocab의 index가 넘어감. 
- Conv1D: 구조적인 특성을 파악하기 위해 여러 filter로 찍어줌.
- MaxPooling1D: convolution으로 찍어낸 정보를 좀 더 특징화함. 
- LSTM: sequential한 정보를 활용
- Dense: classification이므로 output layer을 1칸짜리로 넣어줌. 
"""
embedding_vector_length = 32
model = Sequential([
    Embedding(input_dim=top_words, # 5000
              output_dim=embedding_vector_length, # 32
              input_length=max_review_length), 
    Conv1D(filters=32, kernel_size=5, padding='same', activation='relu'), 
    MaxPooling1D(pool_size=2),
    LSTM(50), # 원래는 100, 
    Dropout(0.2), 
    Dense(25, activation='sigmoid'), 
    Dense(1, activation='sigmoid')
])
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=5, batch_size=64)
print("training complete")
scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: {:.2f}".format(scores[1]*100))
```

- 뉴럴넷 형태와, 스코어링. 

```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
embedding_8 (Embedding)      (None, 100, 32)           16000     
_________________________________________________________________
conv1d_2 (Conv1D)            (None, 100, 32)           5152      
_________________________________________________________________
max_pooling1d_2 (MaxPooling1 (None, 50, 32)            0         
_________________________________________________________________
lstm_6 (LSTM)                (None, 50)                16600     
_________________________________________________________________
dropout_4 (Dropout)          (None, 50)                0         
_________________________________________________________________
dense_8 (Dense)              (None, 25)                1275      
_________________________________________________________________
dense_9 (Dense)              (None, 1)                 26        
=================================================================
Total params: 39,053
Trainable params: 39,053
Non-trainable params: 0
_________________________________________________________________
None
Train on 25000 samples, validate on 25000 samples
Epoch 1/5
25000/25000 [==============================] - 171s - loss: 0.5373 - acc: 0.7154 - val_loss: 0.4850 - val_acc: 0.7600
Epoch 2/5
25000/25000 [==============================] - 163s - loss: 0.4209 - acc: 0.8074 - val_loss: 0.4257 - val_acc: 0.8086
Epoch 3/5
25000/25000 [==============================] - 174s - loss: 0.4004 - acc: 0.8214 - val_loss: 0.4004 - val_acc: 0.8158
Epoch 4/5
25000/25000 [==============================] - 165s - loss: 0.3826 - acc: 0.8292 - val_loss: 0.3879 - val_acc: 0.8248
Epoch 5/5
25000/25000 [==============================] - 173s - loss: 0.3687 - acc: 0.8381 - val_loss: 0.3833 - val_acc: 0.8255
training complete
Accuracy: 82.55
```

## wrap-up

- 오늘 한 것은 sequence classification을 RNN을 사용해서 해결했다는 것입니다. 기존에도 BOW 등의 방식으로 classification을 수행한 적은 있는데, RNN을 사용해서 이전 데이터와의 관련성을 고려하여, 데이터를 벡터화하고, 그를 활용해서, 예측을 했다는 점에서 조금 더 높은 점수를 주고 싶습니다. 
    - 이게 그전의 다른 방식들에 비해서 월등히 뭐가 좋다, 이런게 나오면 좋겠지만, 제 컴퓨터가 그렇게 좋지 못해서, 아직 거기까지 하지는 못했어요. 
- 또한, 원래는 `gensim`을 사용해서 word embedding을 했는데, `keras`에 `embedding`이라는 레이어가 있는 것은 또 몰랐네요. 다음부터는 이걸 바로 이용하는 게 더 좋을 것 같습니다. 
- word-embedding을 한 다음, Convolutional layer를 사용합니다. convolutional layer는 이미지를 분류할 때 사용했던 레이어인데, 이미지로부터 특정한 feature를 뽑아내기 위해서 사용했습니다. 여러 개의 filter를 만들고, 이미지를 필터로 찍어냅니다. 
    - 어떤 filter는 귀를 뽑고 어떠한 filter는 코를 뽑고 이런식으로 전체 이미지에서 filter를 먹여가며 쭉 읽어들입니다.
    - 즉 filter는 해당 이미지의 구조적인 특성(귀, 코 등)을 잡아내는 것이죠. 그렇게 종류의 filter가 여러 가지 있고 이를 Dense layer에 집어넣습니다. 
    - 비슷하게, 우리가 word embedding을 통해서, 단어를 벡터화했고, 문장은 이 벡터의 리스트로 이루어져 있습니다. Convolution layer를 사용하면 바로 앞뒤의 문맥뿐만 아니라 좀 더 구조적인 특징을 뽑아내기 좋겠죠(아마도). 그래서 convolutional layer를 사용하여 문장의 구조적인 특징을 뽑아냅니다. 
    - 물론, 그 다음에 maxpooling을 이용해서, 그 특징들을 더 명확하게 만들구요. 
- 정리하자면, embedding => convolution => maxpooling => LSTM => Dense 입니다. 중간중간에 Dropout은 알아서 잘 넣으면 됩니다. 
- 현재 제가 만든 모델의 정확도는 그렇게 높은 편이 아닌데, 제 컴퓨터가 별로 좋지 못해서, 계산을 돌리는게 쉽지 않네요 하하핫. 

## reference 

- <http://adventuresinmachinelearning.com/keras-lstm-tutorial/>
- <https://machinelearningmastery.com/sequence-classification-lstm-recurrent-neural-networks-python-keras/>

## raw code

```python
import numpy as np 
from keras.datasets import imdb

from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout, Conv1D, MaxPooling1D
from keras.layers.embeddings import Embedding

from keras.preprocessing import sequence
np.random.seed(7)# fix random seed for reproducibility

"""
개별 movie review에 있는, 모든 단어를 고려하는 것은 무의미하기 때문에 
top_words, 즉 상위 5000개의 단어에 대해서만, 추려냄. 나머지는 필터링
그리고 단어는 index로 표시됨 .
"""
max_review_length, top_words = 100, 500 # 원래 500, 5000
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=top_words)
"""
sequence의 길이를 똑같이 맞춤. 
길이가 500보다 큰 경우에는 그냥 일괄적으로 앞부분을 잘라내버림. 
"""
X_train = sequence.pad_sequences(X_train, maxlen=max_review_length)
X_test = sequence.pad_sequences(X_test, maxlen=max_review_length)
print("reading data complete")

"""
layer의 구성은 
- Embedding: 단어를 벡터화하고, 이 결과 값을 LSTM에 집어넣어줌. 
    - input_dim에 top_words를 넣어주는데, 아마도 내부에서 자동으로 one-hot vector를 만들어주는 것 같음
    - 현재는 one-hot vector가 아니라, 0, 1, 등 word vocab의 index가 넘어감. 
- Conv1D: 구조적인 특성을 파악하기 위해 여러 filter로 찍어줌.
- MaxPooling1D: convolution으로 찍어낸 정보를 좀 더 특징화함. 
- LSTM: sequential한 정보를 활용
- Dense: classification이므로 output layer을 1칸짜리로 넣어줌. 
"""
embedding_vector_length = 32
model = Sequential([
    Embedding(input_dim=top_words, # 5000
              output_dim=embedding_vector_length, # 32
              input_length=max_review_length), 
    Conv1D(filters=32, kernel_size=5, padding='same', activation='relu'), 
    MaxPooling1D(pool_size=2),
    LSTM(50), # 원래는 100, 
    Dropout(0.2), 
    Dense(25, activation='sigmoid'), 
    Dense(1, activation='sigmoid')
])
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=5, batch_size=64)
print("training complete")
scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: {:.2f}".format(scores[1]*100))
```