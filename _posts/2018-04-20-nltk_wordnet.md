
# nltk - wordnet 사용하기 

## intro

- wordnet은 프린스턴 대학교에서 과거에 영어단어들에 대해서 구축한 일종의 온톨로지로, 단어간에 어떤 관계를 가지고 있는지를 정리한 온톨로지다. 사전처럼 단어별로 개별적인 의미를 정리하는 것보다, 이렇게 단어간의 관계를 중심으로 정리할 경우 그 활용도가 높아질 수 있다. 
- 일반적으로 '온톨로지'는 특정 세계에 대해 잘 구축된 체계 정도로 번역할 수 있다(학술적으로 들어가면 좀 달라진다). 

- 지속적으로 유지보수되어야 하는 문제점이 있기는 하지만, 현재 영단어에 대해서는 가장 잘 정의된 온톨로지 라고 할 수 있다. 
    - 국내에서도 부산대에서 비슷한 작업을 수행한 적이 있으나, 완전히 공개되지 않아서 접근성 등의 문제가 있음
    - wordnet의 경우는 nltk에 통합되어 상대적으로 쉽게 쓸 수 있음 

- 물론 최근에는 word-embedding 등을 사용해서 온톨로지 없이도 온톨로지와 비슷한 효과를 내고 있기 때문에, 이 라이브러리가 반드시 필요한가?에 대해서는 현재는 의문이 있다. 
    - Word-embedding과 wordnet을 활용하면, 좀 더 재미있는 짓을 할 수 있지 않을까? 싶은데, 예를 들어서 1) 빠르게 학습한다거나, 2).....아무튼...

## word relation in wordnet

- wordnet에서 단어 간에 성립할 수 있는 관계는 대략 다음과 같은 정도로 표현된다. 워드넷에서 다음 네 가지를 어떻게 활용하는지 이후에 설명한다. 
    - synonym: 동의어
    - antonym: 반의어
    - hypernym: 상의어
    - hyponym: 하위어

### pos in wn

- wn에서는 총 다섯 가지 종류의 pos 가 존재한다. 
    - n: noun
    - v: verb
    - a: adjective
    - s: adjective satellite
        - antonym이 없는 단어를 의미한다. 특이한 경우인데, wn에서 adjective의 경우는 (adjective, verb, antonym)의 triple의 형태로 관리되는데, anotynym이 없을 경우만 따로 adjective satellite 로 관리한다. 
    - r: adverb


```python
all_pos = set([synset.pos() for synset in  wn.all_synsets()])
print(all_pos)
```

```
    {'n', 'a', 'v', 'r', 's'}
```

### synset

- a set of synonyms that share a common meaning, 간단히, 비슷한 단어묶음을 의미한다. 
- 'car'에는 다양한 의미들이 존재하는데, 'car'가 가진 5 가지 의미에 대해서 각각 synset이 존재한다. 
    - `synset.pos()`: 품사 출력 
    - `synset.example()`: 예제 문장 


```python
import nltk
from nltk.corpus import wordnet as wn

tab = "    "
for synset in wn.synsets('car'):
    print("{}:".format(synset.name()))
    print(tab+"definition: {}".format(synset.definition()))
    print(tab+"pos: {}".format(synset.pos()))
    for e in synset.examples():
        print("    "+"example: {}".format(e))
    print()
```

```
    car.n.01:
        definition: a motor vehicle with four wheels; usually propelled by an internal combustion engine
        pos: n
        example: he needs a car to get to work
    
    car.n.02:
        definition: a wheeled vehicle adapted to the rails of railroad
        pos: n
        example: three cars had jumped the rails
    
    car.n.03:
        definition: the compartment that is suspended from an airship and that carries personnel and the cargo and the power plant
        pos: n
    
    car.n.04:
        definition: where passengers ride up and down
        pos: n
        example: the car was on the top floor
    
    cable_car.n.01:
        definition: a conveyance for passengers or freight on a cable railway
        pos: n
        example: they took a cable car to the top of the mountain
```

#### simple tip 

- 실수를 방지하기 위해서는 `wn.synsets` 에 넣어주는 단어의 품사를 명확하게 해주는 것이 좋다. 
- 아래에서 보는 것과 같이, 'have'와 'having'의 경우, synset의 결과가 다른 것을 알 수 있는데, having의 경우는 품사가 verb인 경우에 대해서만 출력해주는 반면, have의 경우는 verb가 아닌 경우에 대해서도 출력해주기 때문


```python
print( wn.synsets('have') == wn.synsets('having'))

from nltk.stem.wordnet import WordNetLemmatizer
print(wn.synsets('have') == wn.synsets(WordNetLemmatizer().lemmatize('having', 'v')))
```

```
    False
    True
```

### synset and lemmas

- 앞서 말한 바와 같이, synset은, 해당 워드('car')에 대해 관련있는 워드들의 묶음을 말한다. 
    - `synset.lemmas()`: synset에 포함되는 단어 기본형 리스트(lemma는 단어의 기본형태 정도로 표현할 수 있을 것 같다)
        - stemming의 경우, 단어를 기본 형태로 사전에 없는 형태로 단어를 쪼개기도 하고, 품사를 고려하지 않는 반면
        - lemmatized의 경우, 사전에 있는 형태로만 단어를 쪼개고, 품사를 고려한다 라는 차이가 있다. 

### basic lemmatizer

- 아래에서 보는 것처럼 lemmatizer는 품사를 고려하기 때문에, verb로 lemmatize하는 경우와, noun lemmatize하는 경우가 다르다. 
- stemming의 경우 존재하지 않는 단어를 새로 만들어내는 경우도 있으나, lemmatize는 그런 경우가 없다. 


```python
from nltk.stem.wordnet import WordNetLemmatizer

wnl = WordNetLemmatizer()
target_word = 'having'
print("lemmatizing {}:".format(target_word))
print("verb:", wnl.lemmatize(target_word, 'v'))
print("noun:", wnl.lemmatize(target_word, 'n'))
print()

from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
target_word = "fly"
print("stemming {}".format(porter_stemmer.stem(target_word)))
print("lemmatizing {}".format(wnl.lemmatize(target_word)))
```

```
    lemmatizing having:
    verb: have
    noun: having
    
    stemming fli
    lemmatizing fly
```

### synonyms, hypernyms and hyponyms

- `synset.lemmas()`: synset의 동의어들
- `synset.hypernyms()`: synset의 상위어들
    - 단, 상위어가 여러 개 일 수 있다. 
- hyponyms: 하위어, 


```python
for synset in wn.synsets('car'):
    print("{}: {}".format(synset.name(), synset.definition()))
    synonyms = ", ".join([lem.name() for lem in synset.lemmas()])
    print(tab+"synonyms: {}".format(synonyms))
    
    hypernyms = ", ".join([hypernym.name() for hypernym in synset.hypernyms()])
    print(tab+"hypernyms: {}".format(hypernyms))
    print()
```

    car.n.01: a motor vehicle with four wheels; usually propelled by an internal combustion engine
        synonyms: car, auto, automobile, machine, motorcar
        hypernyms: motor_vehicle.n.01
    
    car.n.02: a wheeled vehicle adapted to the rails of railroad
        synonyms: car, railcar, railway_car, railroad_car
        hypernyms: wheeled_vehicle.n.01
    
    car.n.03: the compartment that is suspended from an airship and that carries personnel and the cargo and the power plant
        synonyms: car, gondola
        hypernyms: compartment.n.02
    
    car.n.04: where passengers ride up and down
        synonyms: car, elevator_car
        hypernyms: compartment.n.02
    
    cable_car.n.01: a conveyance for passengers or freight on a cable railway
        synonyms: cable_car, car
        hypernyms: compartment.n.02
    

#### hypernyms and hypernym_paths 

- 특정 워드의 경우는 반드시 상위 단어가 하나가 아닐 수 있다. 우리가 OOP에서 이중 상속을 구현해야 할 일이 있는 것처럼, 두 개 이상의 개체를 상속받고 있는 경우가 있는데, 이 때는 `hypernym_paths`를 활용할 수 있다. 
    - 물론 이정도의 함수는 직접 할 수 있기는 함. 이라고 허세를 부렸으나, 생각보다 오래 걸렸다고 한다ㅠㅠ

```python
target_word = 'dog.n.01'
print( wn.synset(target_word).hypernyms())
print()
for i, path in enumerate(wn.synset(target_word).hypernym_paths()):
    print(path)
    print()
```

```
    [Synset('canine.n.02'), Synset('domestic_animal.n.01')]
    
    [Synset('entity.n.01'), Synset('physical_entity.n.01'), Synset('object.n.01'), Synset('whole.n.02'), Synset('living_thing.n.01'), Synset('organism.n.01'), Synset('animal.n.01'), Synset('chordate.n.01'), Synset('vertebrate.n.01'), Synset('mammal.n.01'), Synset('placental.n.01'), Synset('carnivore.n.01'), Synset('canine.n.02'), Synset('dog.n.01')]
    
    [Synset('entity.n.01'), Synset('physical_entity.n.01'), Synset('object.n.01'), Synset('whole.n.02'), Synset('living_thing.n.01'), Synset('organism.n.01'), Synset('animal.n.01'), Synset('domestic_animal.n.01'), Synset('dog.n.01')]
```


- 아래는 직접 만든 hypernym_path를 출력하는 함수

```python
def find_hypernym_paths(target_word):
    syns = wn.synset(target_word)
    r_paths = []
    def hypernym_paths_helper(input_syns, paths):
        if len(input_syns.hypernyms())==0:
            for path in paths:
                r_paths.append(path)
        else:
            for hypernym in input_syns.hypernyms():
                hypernym_paths_helper(hypernym, [path+[hypernym] for path in paths])
    hypernym_paths_helper(syns, [[]])
    return r_paths
for i, path in enumerate(find_hypernym_paths('dog.n.01')):
    print("path {}: {}".format(i, path))
```

```
    path 0: [Synset('canine.n.02'), Synset('carnivore.n.01'), Synset('placental.n.01'), Synset('mammal.n.01'), Synset('vertebrate.n.01'), Synset('chordate.n.01'), Synset('animal.n.01'), Synset('organism.n.01'), Synset('living_thing.n.01'), Synset('whole.n.02'), Synset('object.n.01'), Synset('physical_entity.n.01'), Synset('entity.n.01')]
    path 1: [Synset('domestic_animal.n.01'), Synset('animal.n.01'), Synset('organism.n.01'), Synset('living_thing.n.01'), Synset('whole.n.02'), Synset('object.n.01'), Synset('physical_entity.n.01'), Synset('entity.n.01')]
```

#### hyponyms

- synset의 하위어를 의미한다. 

```python
print(wn.synset('dog.n.01').hyponyms())

def DeepPrintHyponyms(syns):
    r_paths = []
    def hyponym_paths_helper(input_syns, paths):
        if len(input_syns.hyponyms())==0:
            for path in paths:
                r_paths.append(path)
        else:
            for hyponym in input_syns.hyponyms():
                hyponym_paths_helper(hyponym, [path+[hyponym] for path in paths])
    hyponym_paths_helper(syns, [[]])
    return r_paths
DeepPrintHyponyms(wn.synset('car.n.01'))
```

```
    [Synset('basenji.n.01'), Synset('corgi.n.01'), Synset('cur.n.01'), Synset('dalmatian.n.02'), Synset('great_pyrenees.n.01'), Synset('griffon.n.02'), Synset('hunting_dog.n.01'), Synset('lapdog.n.01'), Synset('leonberg.n.01'), Synset('mexican_hairless.n.01'), Synset('newfoundland.n.01'), Synset('pooch.n.01'), Synset('poodle.n.01'), Synset('pug.n.01'), Synset('puppy.n.01'), Synset('spitz.n.01'), Synset('toy_dog.n.01'), Synset('working_dog.n.01')]





    [[Synset('ambulance.n.01'), Synset('funny_wagon.n.01')],
     [Synset('beach_wagon.n.01'), Synset('shooting_brake.n.01')],
     [Synset('bus.n.04')],
     [Synset('cab.n.03'), Synset('gypsy_cab.n.01')],
     [Synset('cab.n.03'), Synset('minicab.n.01')],
     [Synset('compact.n.03')],
     [Synset('convertible.n.01')],
     [Synset('coupe.n.01')],
     [Synset('cruiser.n.01'), Synset('panda_car.n.01')],
     [Synset('electric.n.01')],
     [Synset('gas_guzzler.n.01')],
     [Synset('hardtop.n.01')],
     [Synset('hatchback.n.01')],
     [Synset('horseless_carriage.n.01')],
     [Synset('hot_rod.n.01')],
     [Synset('jeep.n.01')],
     [Synset('limousine.n.01'), Synset('berlin.n.03')],
     [Synset('loaner.n.02')],
     [Synset('minicar.n.01'), Synset('minicab.n.01')],
     [Synset('minivan.n.01')],
     [Synset('model_t.n.01')],
     [Synset('pace_car.n.01')],
     [Synset('racer.n.02'), Synset('finisher.n.05')],
     [Synset('racer.n.02'), Synset('stock_car.n.02')],
     [Synset('roadster.n.01')],
     [Synset('sedan.n.01'), Synset('brougham.n.02')],
     [Synset('sport_utility.n.01')],
     [Synset('sports_car.n.01')],
     [Synset('stanley_steamer.n.01')],
     [Synset('stock_car.n.01')],
     [Synset('subcompact.n.01')],
     [Synset('touring_car.n.01')],
     [Synset('used-car.n.01')]]

```


### antonyms

- antonyms의 경우 lemma를 써야한다. 이유는 정확하게 모르겠으나. documnet에는 'some relations are defined by WordNet only over Lemmas' 라고 표현되어 있음. 
    - **추후에 보완 하겠당**


```python
wn.synset('good.a.01').lemmas()[0].antonyms()
```

```
    [Lemma('bad.a.01.bad')]
```


```python
wn.synset('beautiful.a.01').lemmas()[0].antonyms()
```

```
    [Lemma('ugly.a.01.ugly')]
```


### holonyms

- is a member of
- `wn.synset('human.n.01').member_holonyms()` => human is a member of something

```python
def all_holonyms(word):
    for holonym in wn.synset(word).member_holonyms():
        print(holonym)
        print('definition:', holonym.definition())
all_holonyms('human.n.01')
```

```
    Synset('genus_homo.n.01')
    definition: type genus of the family Hominidae
```

```python
all_holonyms('dog.n.01')
```

```
    Synset('canis.n.01')
    definition: type genus of the Canidae: domestic and wild dogs; wolves; jackals
    Synset('pack.n.06')
    definition: a group of hunting animals
```


```python
all_holonyms('lion.n.01')
```

```
    Synset('panthera.n.01')
    definition: lions; leopards; snow leopards; jaguars; tigers; cheetahs; saber-toothed tigers
    Synset('pride.n.04')
    definition: a group of lions
```

### meronyms

- `wn.synset('face.n.01').part_meronyms()` => something is part of face

```python
wn.synset('face.n.01').part_meronyms()
```

```
    [Synset('beard.n.01'),
     Synset('brow.n.01'),
     Synset('cheek.n.01'),
     Synset('chin.n.01'),
     Synset('eye.n.01'),
     Synset('eyebrow.n.01'),
     Synset('facial.n.01'),
     Synset('facial_muscle.n.01'),
     Synset('facial_vein.n.01'),
     Synset('feature.n.02'),
     Synset('jaw.n.02'),
     Synset('jowl.n.02'),
     Synset('mouth.n.02'),
     Synset('nose.n.01')]
```

```python
wn.synset('human.n.01').part_meronyms()
```

```
    [Synset('arm.n.01'),
     Synset('body_hair.n.01'),
     Synset('face.n.01'),
     Synset('foot.n.01'),
     Synset('hand.n.01'),
     Synset('human_body.n.01'),
     Synset('human_head.n.01'),
     Synset('loin.n.02'),
     Synset('mane.n.02')]
```


### similarity

- `wn.synset('dog.n.01').lemma_names()` 말고, similarity를 통해서 계산하는 것도 가능 
- 몇 가지 similarity를 계산하는 방법이 있는데 대부분 wordnet 구조를 중심으로, 상위어, 하위어, graph 내에서의 거리 를 중심으로 계산하는 방법이다. 서로 다른 특성이 있으나, 여기서는 그냥 세 가지 방식이 있다는 것만 알고 넘어간당.
    - path_similarity
    - wup_similarity
    - lch_similarity

#### similar_words_between

- word1, word2에 대해서 다양한 similar_func을 적용하고 sim_threshold 보다 높은 것들만 출력해주는 함수를 만들었다. 

```python
def similar_words_between(w1, w2, similar_func, sim_threshold, max_threshold):
    all_combinations = [(synset1, synset2, similar_func(synset1, synset2)) for synset1 in wn.synsets(w1) for synset2 in wn.synsets(w2)
                    if synset1.pos() == synset2.pos()]
    all_combinations = sorted(all_combinations, key=lambda x: x[2], reverse=True)
    for syn1, syn2, sim in all_combinations:
        if sim is not None and syn1!=syn2:
            if sim > sim_threshold and sim<=max_threshold:
                print("similarity of {} and {}:, {}".format(syn1, syn2, sim))
                print("- Definition of {}: {}".format(syn1, syn1.definition()))
                print("- Definition of {}: {}".format(syn2, syn2.definition()))
                print()
```

### wn.path_similarity

- return a core denoting how similar two word senses are, 
    - based on the shortest path that connects the senses in the is-a (hypernym/hypnoym) taxonomy. 
- The score is in the range 0 to 1. 
- By default, there is now a fake root node added to verbs so for cases where previously a path could not be found---and None was returned---it should return a value. The old behavior can be achieved by setting simulate_root to be False. A score of 1 represents identity i.e. comparing a sense with itself will return 1.


```python
similar_words_between("have", "take", wn.path_similarity, 0.4, 1.0)
```

```
    similarity of Synset('have.v.02') and Synset('carry.v.02'):, 0.5
    - Definition of Synset('have.v.02'): have as a feature
    - Definition of Synset('carry.v.02'): have with oneself; have on one's person
    
    similarity of Synset('experience.v.03') and Synset('take.v.15'):, 0.5
    - Definition of Synset('experience.v.03'): go through (mental or physical states or experiences)
    - Definition of Synset('take.v.15'): experience or feel or submit to
    
    similarity of Synset('accept.v.02') and Synset('accept.v.05'):, 0.5
    - Definition of Synset('accept.v.02'): receive willingly something given or offered
    - Definition of Synset('accept.v.05'): admit into a group or community
```

```python
a = wn.path_similarity( wn.synset("dog.n.01"), wn.synset("dog.n.01").hypernyms()[0] )
print(a)
```

```
    0.5
```

### wn.wup_similarity

- Wu-Palmer Similarity: Return a score denoting how similar two word senses are, 
    - based on the depth of the two senses in the taxonomy and that of their Least Common Subsumer (most specific ancestor node). 
- Note that at this time the scores given do _not_ always agree with those given by Pedersen's Perl implementation of Wordnet Similarity.

```python
similar_words_between("car", "auto", wn.wup_similarity, 0.6, 1.0)
```

```
    similarity of Synset('car.n.02') and Synset('car.n.01'):, 0.7272727272727273
    - Definition of Synset('car.n.02'): a wheeled vehicle adapted to the rails of railroad
    - Definition of Synset('car.n.01'): a motor vehicle with four wheels; usually propelled by an internal combustion engine
```

```python
similar_words_between("have", "take", wn.wup_similarity, 0.6, 1.0)
```

```
    similarity of Synset('experience.v.03') and Synset('take.v.15'):, 0.8571428571428571
    - Definition of Synset('experience.v.03'): go through (mental or physical states or experiences)
    - Definition of Synset('take.v.15'): experience or feel or submit to
    
    similarity of Synset('accept.v.02') and Synset('accept.v.05'):, 0.8
    - Definition of Synset('accept.v.02'): receive willingly something given or offered
    - Definition of Synset('accept.v.05'): admit into a group or community
    
    similarity of Synset('suffer.v.02') and Synset('take.v.15'):, 0.75
    - Definition of Synset('suffer.v.02'): undergo (as of injuries and illnesses)
    - Definition of Synset('take.v.15'): experience or feel or submit to
    
    similarity of Synset('have.v.02') and Synset('carry.v.02'):, 0.6666666666666666
    - Definition of Synset('have.v.02'): have as a feature
    - Definition of Synset('carry.v.02'): have with oneself; have on one's person
    
    similarity of Synset('experience.v.03') and Synset('take.v.19'):, 0.6666666666666666
    - Definition of Synset('experience.v.03'): go through (mental or physical states or experiences)
    - Definition of Synset('take.v.19'): accept or undergo, often unwillingly
```


### wn.lch_similarity

- Return a score denoting how similar two word senses are, 
    - based on the shortest path that connects the senses (as above) and the maximum depth of the taxonomy in which the senses occur. 
- The relationship is given as -log(p/2d) where p is the shortest path length and d the taxonomy depth.


```python
similar_words_between("have", "take", wn.lch_similarity, 2.5, 3.258096538021482)
```

```
    similarity of Synset('have.v.02') and Synset('carry.v.02'):, 2.5649493574615367
    - Definition of Synset('have.v.02'): have as a feature
    - Definition of Synset('carry.v.02'): have with oneself; have on one's person
    
    similarity of Synset('experience.v.03') and Synset('take.v.15'):, 2.5649493574615367
    - Definition of Synset('experience.v.03'): go through (mental or physical states or experiences)
    - Definition of Synset('take.v.15'): experience or feel or submit to
    
    similarity of Synset('accept.v.02') and Synset('accept.v.05'):, 2.5649493574615367
    - Definition of Synset('accept.v.02'): receive willingly something given or offered
    - Definition of Synset('accept.v.05'): admit into a group or community
```


## Reference

- https://web.stanford.edu/class/cs124/lec/sem
- https://pythonprogramming.net/wordnet-nltk-tutorial/
