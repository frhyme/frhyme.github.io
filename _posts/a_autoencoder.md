---
title: auto-encoding, decoding
category: machine-learning
tags: python python-lib machine-learning keras 

---

## auto-encoding decoding??

- 최근에 Generative Adversarial Network를 공부했습니다. 슥 만들고 보니까, 예전에 한 번 슬쩍 봤던, Auto encoder/decoder와 유사하다는 생각이 들었습니다. 
    - 제가 이전에 했던 것은 GAN을 이용해서 MNIST 이미지와 비슷한 이미지를 만드는 generator를 만들었습니다. 
    - 뭔가, 예전에도, auto-encoder, decoder를 이용해서, mnist 이미지 샘플을 더 만드는 걸 봤던 것 같아서요. 
- 비슷하다면 무엇이 비슷하고, 다르다면, 무엇이 다른가? 를 정리하면 좋을 것 같아서 여기서 정리합니다. 

## what is encoding and decoding? 

- 간단하게는, 압축/압축풀기 라고 생각하셔도 됩니다. 
    - encoding: 데이터를 중요한 부분만 남기고, 축소하는 것
    - decodoing: encoded 데이터를 다시 원래 데이터로 복구하는 것
- 당연히, encoding 과정에서 일정 이상의 데이터 손실(loss)는 발생하고 되고, 이를 최대한 줄이면서 encoding을 잘하는 것이 목적이겠죠. 

### auto encoding and decoding 

-  여기에 auto를 붙이면, 각각 알아서 잘 줄여주고 알아서 잘 늘려준다는 말이 됩니다. 누가요? 컴퓨터가요 하하하핫. 

### 적용 가능 예  

- "모자이크된 이미지(encoded image)를 확대하는 것"이 가장 먼저 떠오르네요. encoding된 이미지와, 원래 이미지를 넣어서 decoding되었을때 cost를 줄이도록 학습하면 되겠죠. 
    - 원래 이미지 -> encoded image -> decoded image
    - auto encoder와 auto decoder를 함께 넣고, 원래 이미지와 decoded image간의 loss를 제일 줄이는 방식으로 학습을 시킵니다(cross validation도 당연히 진행하구요). 이후에 decoder만 따로 떼어내어서, 이용하면, encoded image를 decoded image로 변환할 수 있습니다. 
- dimensionality reduction: 결국 데이터 압축은, 차원축소와 같은 말이죠. 지나치게 큰 데이터일 경우에 이 데이터를 더 적은 차원으로 줄일 수 있겠죠. 
    - t-SNE가 이러한 방식으로 만들어진 것이라고 하는데, 만약 원래 차원이 100차원이고, 이를 2차원으로 줄인다면, image와 같은 방식으로 original data(100 dim) => encoded data(2 dim) => decoded img(100 dim)으로 auto encoder/decoder로 학습을 시킵니다. 이때 가장 loss가 적은 방향으로 세팅하고, 이 때, encoder만 따로 떼어내어서, dimensionality reduction으로 사용할 수 있습니다. 

## coding auto-encoding and decoding

- coding이 세 개나 붙는 좋은 라이밍이군요 깔깔. 아무튼 직접 코딩을 해서 auto-encoder, decoder를 모두 만들어 봅시다.

### auto encoder/decoder simple 

- 가장 간단한 형태로 만들었습니다. 아주 간단하게 생각하면, encoder는 그저 원래 feature dimension을 줄이는 거고, decoder는 줄여진 feature dimension을 다시 크게 해주는 거죠. 
- 뉴럴넷을 784 -> 36 -> 784으로 생성했습니다. 


```python
#### data reading 
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
x_train, y_train = mnist.train.images, mnist.train.labels
x_test, y_test = mnist.test.images, mnist.test.labels
#############
import numpy as np 
import matplotlib.pyplot as plt

from keras.models import Sequential, Model
from keras.layers import Input, Dense, Activation
from keras.optimizers import Adam, SGD

####################
### autoencoder setting
encoding_dim = 36# 데이터를 몇 차원으로 줄일 것인지
input_img = Input(shape=(784,))
encoded = Dense(encoding_dim, activation='relu')(input_img)
decoded = Dense(784, activation='sigmoid')(encoded)
autoencoder_simple = Model(input_img, decoded) # keras model은 input/output만 집어 넣음 
print("### autoencoder")
autoencoder_simple.summary()
"""
- 일단 autoencoder를 만들었다. 
- autoencoder는 encoder/decoder로 구성되어 있기는 한데, 바로 가져올 수는 없고, input을 새로 만들어서 연결해주어야 함. 
    - 일단 encoder의 경우는 autoencoder와 완전히 동일하므로, 그대로 사용해도 되지만, 헷갈릴 수 있어서 똑같이 만들어줌. 
    - decoder의 경우, 우선 해당 레이어로 바로 들어가는 input이 없으므로 새로운 input을 만들어주고, 
        - 해당 input을 argument로 받아서 해당 레이어를 사용하는 식으로 연결해줌. 
        - layer의 이름이 같은 것을 보면 알 수 있듯이, 그대로 사용하는 것임
- 이렇게 개별 레이어 끝에 argument를 넣어서 가져오는 것 레이어가 callable object이기 때문.
"""
####################
### encoder setting
input_img2 = Input(shape=(784,))
encoder = Model(input_img2, autoencoder_simple.layers[1](input_img2))
# encoder = Model(input_img, encoded) 와 동일 
print("### encoder")
encoder.summary()
####################
### decoder setting
encoded_input = Input(shape=(encoding_dim,))
decoder = Model(encoded_input, autoencoder_simple.layers[2](encoded_input))
print("### decoder")
autoencoder_simple.compile(optimizer='adadelta', loss='binary_crossentropy')
decoder.summary()
```

- 아래에서 보는 것과 같이, encoder, decoder는 autoencoder에서 사용하는 레이어를 그대로 사용합니다. 

```
Extracting MNIST_data/train-images-idx3-ubyte.gz
Extracting MNIST_data/train-labels-idx1-ubyte.gz
Extracting MNIST_data/t10k-images-idx3-ubyte.gz
Extracting MNIST_data/t10k-labels-idx1-ubyte.gz
### autoencoder
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_94 (InputLayer)        (None, 784)               0         
_________________________________________________________________
dense_144 (Dense)            (None, 36)                28260     
_________________________________________________________________
dense_145 (Dense)            (None, 784)               29008     
=================================================================
Total params: 57,268
Trainable params: 57,268
Non-trainable params: 0
_________________________________________________________________
### encoder
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_95 (InputLayer)        (None, 784)               0         
_________________________________________________________________
dense_144 (Dense)            (None, 36)                28260     
=================================================================
Total params: 28,260
Trainable params: 28,260
Non-trainable params: 0
_________________________________________________________________
### decoder
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_96 (InputLayer)        (None, 36)                0         
_________________________________________________________________
dense_145 (Dense)            (None, 784)               29008     
=================================================================
Total params: 29,008
Trainable params: 29,008
Non-trainable params: 0
_________________________________________________________________
```

```python
autoencoder_simple.fit(x_train, x_train, epochs=10, batch_size=500, verbose=1)
############
# plotting encoded and decoded img
def random_img_plotting(autoencoder_input, file_name):
    # random으로 5개만 그려줍니다. 
    sel_idx = [ np.random.randint(0, len(x_train)) for i in range(0, 5)]
    f, axes = plt.subplots(2, len(sel_idx), figsize=(10, 5))
    for i in range(0, len(axes[0])):
        axes[0][i].imshow(x_train[sel_idx[i], :].reshape(28, 28))
        axes[1][i].imshow(autoencoder_simple.predict(x_train[[sel_idx[i]], :]).reshape(28, 28))
    plt.savefig("../../assets/images/markdown_img/"+file_name)
    plt.show()
random_img_plotting(autoencoder_simple, '180625_autoencoder_simple.svg')
```

![](assets/images/markdown_img/180625_autoencoder_simple.svg)

### auto encoder/decoder deep

- deep 하게 만드는 것도 똑같습니다. 
- 하지만, encoder, decoder를 만들 때는 레이어를 여러개 가져와서 연결해줘야 합니다. 

```python
########
## autoencoder deep 
encoding_dims = 36

input_img = Input(shape=(784,))
x = Dense(256, activation='relu')(input_img)
x = Dense(128, activation='relu')(x)
x = Dense(64, activation='relu')(x)
encoded = Dense(encoding_dims, activation='relu')(x)

x = Dense(64, activation='relu')(encoded)
x = Dense(128, activation='relu')(x)
x = Dense(256, activation='relu')(x)
decoded = Dense(784, activation='sigmoid')(x)

autoencoder_deep = Model(input_img, decoded)
autoencoder_deep.compile(optimizer='adadelta', loss='binary_crossentropy')
#########
## encoder
input2 = Input(shape=(784,))
x = autoencoder_deep.layers[1](input2)
x = autoencoder_deep.layers[2](x)
x = autoencoder_deep.layers[3](x)
x = autoencoder_deep.layers[4](x)
encoder_deep = Model(input2, x)

#########
## decoder
encoded_input = Input(shape=(36,))
x = autoencoder_deep.layers[5](encoded_input)
x = autoencoder_deep.layers[6](x)
x = autoencoder_deep.layers[7](x)
x = autoencoder_deep.layers[8](x)
decoder_deep = Model(encoded_input, x)

print('autoencoder_deep')
autoencoder_deep.summary()
print("encoder_deep")
encoder_deep.summary()
print("decoder_deep")
decoder_deep.summary()
```

- 아래를 보시면, auto encoder, encoder, decoder 들이 모두 서로 레이어를 함께 사용하는 것을 알 수 있습니다. 

```
autoencoder_deep
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_107 (InputLayer)       (None, 784)               0         
_________________________________________________________________
dense_178 (Dense)            (None, 256)               200960    
_________________________________________________________________
dense_179 (Dense)            (None, 128)               32896     
_________________________________________________________________
dense_180 (Dense)            (None, 64)                8256      
_________________________________________________________________
dense_181 (Dense)            (None, 36)                2340      
_________________________________________________________________
dense_182 (Dense)            (None, 64)                2368      
_________________________________________________________________
dense_183 (Dense)            (None, 128)               8320      
_________________________________________________________________
dense_184 (Dense)            (None, 256)               33024     
_________________________________________________________________
dense_185 (Dense)            (None, 784)               201488    
=================================================================
Total params: 489,652
Trainable params: 489,652
Non-trainable params: 0
_________________________________________________________________
encoder_deep
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_108 (InputLayer)       (None, 784)               0         
_________________________________________________________________
dense_178 (Dense)            (None, 256)               200960    
_________________________________________________________________
dense_179 (Dense)            (None, 128)               32896     
_________________________________________________________________
dense_180 (Dense)            (None, 64)                8256      
_________________________________________________________________
dense_181 (Dense)            (None, 36)                2340      
=================================================================
Total params: 244,452
Trainable params: 244,452
Non-trainable params: 0
_________________________________________________________________
decoder_deep
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_109 (InputLayer)       (None, 36)                0         
_________________________________________________________________
dense_182 (Dense)            (None, 64)                2368      
_________________________________________________________________
dense_183 (Dense)            (None, 128)               8320      
_________________________________________________________________
dense_184 (Dense)            (None, 256)               33024     
_________________________________________________________________
dense_185 (Dense)            (None, 784)               201488    
=================================================================
Total params: 245,200
Trainable params: 245,200
Non-trainable params: 0
_________________________________________________________________
```

- 학습을 하고, 결과를 보면, 꽤 복구를 잘하는 편인 것을 알 수 있습니다.
- 사람 눈으로는 encoded img가 별 볼일 없었는데, 지금 보니까 매우 잘 되어 있네요 하하핫

```python
autoencoder_deep.fit(x_train, x_train, 
                     epochs=20, batch_size=500, verbose=0, #validation_data=(x_test, x_test)
                    )
### draw original img, encoded img, decoded img
ks = [8, 12, 3]
f, axes = plt.subplots(3, 3, figsize=(9, 9))
for i, k in enumerate(ks):
    axes[i][0].imshow(x_train[[k], :].reshape(28, 28), cmap=plt.cm.gray)
    axes[i][0].set_title('original img')
    axes[i][0].axis('off')
    axes[i][1].imshow(encoder_deep.predict(x_train[[k], :]).reshape(6,6), cmap=plt.cm.gray)
    axes[i][1].set_title('encoded img')
    axes[i][1].axis('off')
    axes[i][2].imshow(decoder_deep.predict(encoder_deep.predict(x_train[[k], :])).reshape(28,28), 
               cmap=plt.cm.gray)
    axes[i][2].set_title('decoded img')
    axes[i][2].axis('off')
plt.savefig('../../assets/images/markdown_img/180625_autoencoder_deep.svg')
plt.show()
```

![](/assets/images/markdown_img/180625_autoencoder_deep.svg)

### auto encoder/decoder convolutional 

- 이제 컨볼루션으로 만들어봅니다. 이제 사실 그놈이 그놈인데, convolutional layer의 경우는 encoding, decoding 시에 새로운 레이어가 하나 들어가게 되거든요. 그래서 집어넣었습니다. 
- 단, 이제부터는 fitting할 때 시간이 아주 많이 걸립니다 하하핫

```python
```


## GAN과의 차이점? 

- 흐음. 조금 미묘하네요. GAN에서 generator는 'noise data'를 인풋으로 받아서, 거기서부터 시작하는 최대한 비슷한 이미지를 만들어줍니다. 따라서 기존에 없던 데이터(그림 같은 것)이라도 원본중에 뭔가 비슷한게 있다면, 새롭게 만들어낼 수 있습니다. 
- 하지만, Auto encoder/decoder는 원래 없던 데이터라면 새롭게 만드는 것을 불가능한 것 같아요. 
- 다시 말하면, GAN은 좀더 창의적인 느낌, auto encoder/decoder는 원래 있던 것을 압축/복구 하는 측면으로만 쓰이지 않나...싶은데...잘 모르겠습니다 하하하핫. 

## wrap-up

- 가장 큰 수확이라면, t-SNE가 일종의 뉴럴넷으로 설계되어있다는 것을 알게 되었다는 것이고, 

## reference

- <https://blog.keras.io/building-autoencoders-in-keras.html>
- <https://www.datacamp.com/community/tutorials/autoencoder-keras-tutorial>
- <https://towardsdatascience.com/applied-deep-learning-part-3-autoencoders-1c083af4d798>


## raw code 

```python

```