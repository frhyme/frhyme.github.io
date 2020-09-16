---
title: Merssenne Twiste 난수 생성기 python으로 코딩.
category: python-basic
tags: python python-basic hexagonal random numpy 
---

## 3-line summary 

- `numpy`를 비롯하여 최근의 많은 random number 생성은 [Mersenne_Twister](https://en.wikipedia.org/wiki/Mersenne_Twister#Algorithmic_detail)에 기반하고 있다. 
- Mersenne_Twister는 (624개의 모수를 생성) => (각각의 모수로부터 "복잡한 공정"을 통해 새로운 난수를 생성) => (624개를 다 쓰면, 새로운 624개의 모수를 생성) 의 순서에 따라 실행됨. 
- `np.random.seed(0)`으로 초기 seed를 설정하는 것은 여기서 "모수의 첫번째 원소를 설정해주는 것"에 지나지 않음.

## intro: 나는 어쩌다, Mersenne_Twister 까지 왔는가. 

- 궁금증을 가진다는 것은, 사실 매우 번거롭게 힘든 일입니다. 사실은 모를 때 가장 몸이 편하죠. 
- 시작은 매우 간단했습니다. 우리는 보통 `numpy.random.seed(seed=3)`같은 방식으로 `numpy`에서 난수가 생성되는 방식을 제어하죠. 
- 종종, 동일한 random성을 설정하고 코딩해야 할 필요성이 있으니까요. 그런데, 문득 이 `seed`라는 겂이 random성에 어떻게 영향을 미치는지 알고 싶었습니다. 솔직히, 간단할 줄 알았거든요. 
- 하지만, 안타깝게도, 여기서 random number를 만드는 방법은 [Mersenne_Twister](https://en.wikipedia.org/wiki/Mersenne_Twister#Algorithmic_detail)이라고 하는 매우 괴랄한 방식에 기초하고 있었습니다. 제가 넘긴 `seed`는 초기에 세팅되는 많은 모수(population) 중 하나를 설정하는 것 뿐이었던 것이죠. 
- 지금도 몇몇 부분에 대해서는 완벽하게 이해하지는 못했습니다만, 그래도 대략 큰 그림 정도는 알게 된 것 같아요.

## What is Random? 

- 우선은 `random`성이라는 것이 무엇인지 정확하게 알 필요가 있습니다. 냉정히 말해서, 컴퓨터의 세계에서 완전한 random은 보장할 수 없습니다. 물론, 이렇게 말하면 완전한 random성은 무엇이냐? 라는 질문이 나올수 있죠. 생각해보니까, 이 질문은 꽤 철학적인 질문이 되는군요. 흠, 그러게요 완전한 random은 무엇이며, 그것이 완전한 random인지는 어떻게 알 수 있을까요? 
- 다르게 말해 보겠습니다. 실용적인 관점에서, 그것이 "진정한(true) randomness"인지를 반드시 필요하지는 않을 수 있습니다. 가령, "1부터 10까지 중에서 random한 값을 뽑아내야 할때", 이런 문제를 풀 때 우리에게 "완전한 랜덤성"이라는 것이 필요할까요? 오히려, 그냥 "1부터 10까지 통계적으로 uniform한 분포를 가질 수 있도록만 해달라"가 더 적합하겠죠. 즉, 이를 우리는 "통계적 random성"이라고 부르겠습니다. 

### Random Generator with `time`

- 이와 같은 랜덤성을 확보하기 위해서, 당연하지만 매우 다양한 방법들이 있어 왔겠죠. 아주 단순하게는 '시간'을 이용하는 방법이 있을 수 있습니다. 
- 이는, 우리에게 아주 미세한 시간의 단위(나노 세컨드)를 측정할 수 있는 시계가 있을 경우, 그 시간의 단위를 '모수'로 사용하여, random을 확보하겠다, 와 비슷한 말이 됩니다. 
- 다음 코드를 보시면, `time`모듈의 가장 낮은 초 단위를 사용하여, 나쁘지 않은 random성을 보여줍니다. 대충 만든 코드이긴 하지만, 만약 함수 없이, 결과만 보여준다면, "음, 나름 랜덤성이 있군"이라고 말할 수도 있는 셈이죠.

```python
import time 

def very_simple_rand():
    """
    빠르게 변하는 시간 값을 사용하여, 
    이 끝부분만 리턴하는 함수
    """
    a = time.time() 
    a = (float(a) - int(a))*(10**12)
    a = int(str(a)[-3:])
    return a
    
print([very_simple_rand() for i in range(0, 8)])
```

```
[797, 168, 344, 625, 547, 883, 166, 285]
```

- 하지만, 시간에 따라서 커지는 경향성이 있다거나, 아무튼 뭐 다양한 문제점이 있습니다. 
- 따라서, 이를 개선하기 위해 폰 노이만이 [Middle Square Method](https://en.wikipedia.org/wiki/Middle-square_method)와 같은 방법을 제시하기도 하였죠. 

## 본론: Mersenne_Twister

- 아무튼 다시 돌아와서, `numpy`를 비롯하여, 현재 대부분의 random number generator에서 사용하는 방법이 바로 이해하기 매우 어려운 [Mersenne_Twister](https://en.wikipedia.org/wiki/Mersenne_Twister#Algorithmic_detail)입니다. 물론, 위키피디아에 매우 잘 설명되어 있지만, 네, 존나 어렵습니다. 

### BackBone of Mersenne_Twister 

- 우선, 큰 그림에서 보면 다음과 같습니다. 
1) seed를 첫번재 항으로 하여(`MT[0]`) 점화식을 통해 624개의 길이를 가진 배열(`MT`)을 생성합니다. 이 MT가 일종의 모수 세트 라고 생각하면 됩니다.
2) "random number를 만들어달라"라는 요청이 들어오면, 이미 생성된 624개의 배열의 첫번째 항(`MT[0]`)으로부터 값을 마구 변형하여(Black BOX) 난수를 리턴한다(실제로는 Black Box 가 아니지만, 그냥 "복잡한 공정"이라고만 이해하셔도 됩니다)
3) MT의 마지막 모수인 `MT[623]`까지 모두 사용하였으면, `twist`로 새로운 `MT`를 만든다. 즉, 모수 세트가 다시 만들어졌으므로, `MT[0]`로부터 Black BOX를 사용하여 새로운 난수를 생성한다.

### Mersenne_Twister: python implementation

- 즉, python으로 구현한다면 다음과 같이 구현하게 됩니다.
    1) `seed_mt`: seed를 첫번째원소로 가지며, 점화식을 통해 `MT`라고 하는 624개의 모수를 생성함. 
    2) `twist`: 624개의 모수를 다 쓰면 `MT`를 재설정한다.
    3) `extract_number`: 모수가 떨어지면 `twist`, 아니면 blackbox

#### seed_mt: 624개의 모수를 생성한다.

- `MT`라고, 하는 가장 624개의 크기를 가지는 배열을 생성하게 됩니다. 그리고 각각의 원소를 활용하여, 새로운 모수를 생성하게 됩니다. 
- 만약 우리가 seed를 지정하게 되면, seed는 `MT[0]`에 값이 지정됩니다. 그리고 그 값으로부터 `MT`가 차근차근 생성하게 되죠.

```python 
def seed_mt(seed):
    """
    # MT는 624개의 원소를 가지는, 배열입니다. 
    # 그리고, 이 각각의 값들은 이후 extract_number()라는 함수를 통해 
    # 새로운 난수를 생성하는 모수가 되죠. 
    # 즉, 맨 처음에는 MT[0]를 사용해서 난수를 만들고, 
    # 그 다음에는 MT[1]를 사용해서 난수를 만듭니다. 
    # 본 함수, seed_mt(seed) 는 MT를 초기화해주는 함수인 것이죠. 
    # 보통, 우리가 seed를 준다는 것은 그저, 
    # MT의 첫번째 값을 지정해준다는 것과 같습니다. 
    # MT는 일종의 점화식을 통해서 생성되므로, 첫번째 값을 어떻게 지정하느냐에 따라서 
    # 이후의 값이 결정되죠.
    """
    global MT # MT: Mersenne Twister, 624개의 배열.
    global n # n: degree of recurrence, 624.
    global w  # w: word size (in number of bits). 32 bit일 때는 32.
    global LOWER_MASK # 32칸이 모두 1
    # 첫번째 원소를 seed를 통해 변형하고,
    MT[0] = seed
    for i in range(1, n):
        # LOWER_MASK는 이름은 lower지만, 32칸이 모두 1로 구성되어 있음.
        # 이 값으로 temp 와 AND bit operation을 처리할 경우,
        # temp의 마지막 32칸에서 1인 값만 가져오게됨.
        # 다르게 말한다면, 문자열로 끝의 32칸만 읽어서, 가져와도 된다는 이야기임.
        temp = f * (MT[i - 1] ^ (MT[i - 1] >> (w - 2))) + i
        MT[i] = temp & LOWER_MASK
```

#### twist: 624개의 모수를 다 쓰면 `MT`를 재설정한다.

- 앞서 말한 바와 같이, `MT`는 624개의 모수 세트입니다. 
- 외부에서, "난수를 주세요!"라고 한다면, `MT[0]`로부터 "블랙박스를 통해" 새로운 난수를, 그 다음에는 `MT[1]`로부터 "블랙박스를 통해" 새로운 난수를 생성하게 되겠죠. 
- 그런데, 만약 624개의 난수를 다 주었다면, 어떻게 해야 할까요? 다시, `MT[0]`로 돌아갈 수는 없습니다. 그러면, 이전에 624번 전에 준 난수를 그대로 주게 되니까요. 
- 따라서, 이 때는 `MT` 전체를 재설정해주어야 합니다. 이 과정을 `twist`라고 하죠.

```python
def twist():
    """
    # MT는 일종의 모수, population이라고 생각하면 됩니다. 
    # 새로운 random number를 생성할 때, MT의 index번째 원소부터 출발하여, 
    # 그 원소를 bitwise operation를 통해 변형하게 되죠. 
    # MT는 n, 즉 624개의 값을 가지며, 
    # 제가 624개의 random number를 생성해냈다면, 
    # 이미 모수들은 다 사용된 것이므로, 새로운 모수가 필요합니다. 
    # 이 때, 새로운 모수를 만들어내는 과정이 바로, twist()인 셈이죠.
    """
    # m: middle word
    # an offset used in the recurrence relation defining the series x, 1 ≤ m < n
    global m
    # n: degree of recurrence, 624.
    global n
    # a: coefficients of the rational normal form twist matrix
    global a
    # LOWER_MASK: 32칸이 모두 1
    global LOWER_MASK
    # UPPER_MASK: LOWER_MASK의 보수.
    global UPPER_MASK

    for i in range(0, n):
        x = (MT[i] & UPPER_MASK) + (MT[(i + 1) % n] & LOWER_MASK)
        xA = x >> 1
        if (x % 2) != 0:
            # lowest bit of x(가장 오른쪽의 bit가 0이라는 말)
            xA = xA ^ a
        MT[i] = MT[(i + m) % n] ^ xA
```

#### extract_number: 모수가 떨어지면 twist, 아니면 blackbox

- 이 함수가 일종의 main 함수인 셈이죠. 여기서는 `MT`를 이용해서 `blackbox`를 통해 새로운 수를 만들어냅니다. 
- 사실은 `blackbox`가 아니고, bit operation이 막 진행되는데, 뭐, 제가 다 알 필요는 없을 것 같아요. 그냥, "복잡하게 만들어서 랜덤처럼 보이려고 한다" 정도로만 알고 있어도 되지 않을까? 싶어요.

```python
def extract_number():
    """
    # MT는 일종의 모수(population)을 의미합니다. 
    # 이 함수는 모수들로부터 순서대로 하나의 모수를 선택하고, 
    # 아래 정의한 BLACK_BOX()라는 함수에서 값을 변형합니다. 
    # 그리고, 이를 통해 생성된 값이 random number가 되죠. 
    # 따라서, 이미 생성된 MT라는 모수를 한 바퀴 돌면 
    # 다시 twist()를 통해 새로운 모수를 생성하고, 다시 index는 초기화됩니다. 
    """
    def BLACK_BOX():
        """
        MT의 index번째 원소로부터, 
        u, d, t, c, s, b, l 를 사용하여 
        변형합니다. 
        왜 이렇게 해야 하는지는 이해가 안되네요 호호호. 
        """
        global u, d, t, c, s, b, l
        global MT
        global index
        y = MT[index]
        y = y ^ ((y >> u) & d)
        y = y ^ ((y << t) & c)
        y = y ^ ((y << s) & b)
        y = y ^ (y >> l)
    global n
    global index
    global LOWER_MASK
    if index>=n:
        # population을 한바퀴 돌았으므로,
        # 다시 새로운 population을 생성해주고(twist)
        # 다시 index를 초기화.
        twist()
        index = 0
    # MT의 index번째 값을부터 random한 값을 생성함.
    BLACK_BOX()
    index += 1
    return MT[index] & LOWER_MASK
```

### 정리하자면. 

- 헷갈릴 수 있으므로 다시 정리하겠습니다. 
    1) `seed_mt`: 우선, seed로부터 점화식을 통해 624개라는 배열을 만들어줍니다. 이 배열들의 원소들은 점화식을 통해서 나왔으므로, 서로 수학적인 관계에 있지만, 얘네도 이미 난수라고 (어느정도는) 말이 됩니다. 
    2) `extract_number`: `seed_mt`를 통해 생성된 624개의 수를 하나씩 읽어가면서, 각 값으로부터 생성된 새로운 난수를 만듭니다(그냥 난수를 가지고 또 난수를 만든다! 라고 생각하셔도 되죠). 만약 624개를 다 쓰면, 이 다음에 twist를 통해 모수 세트를 변형해줍니다
    3) `twist`: 624개의 모수를 다 쓰면, 이제 바꿔줘야, 진정한 랜덤성이 확보되므로, 모수 자체를 다른 모수들로 변경해줍니다.
- 물론, 이는 결국 큰 그림일 뿐입니다. 큰 그림으로 보면 "그냥 난수에 난수를 섞어서 더 어려운 난수를 만든다는 것 아니야"로 끝나기는 하죠. 다만, 내부의 내용들은 너무 어려워서 솔직히 모르겠어요 호호호호.

## wrap-up 

- 뭐, 아무튼, 대충 무슨 말인지는 이해하였고, python으로도 코딩하였습니다. 사실 `np.random.seed(0)`가 궁금해서 찾아본 것이기는 한데, 나름 재밌있던 것 같네요.

## reference

- [numpy.random.get_state](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.get_state.html)
- [Mersenne_Twister - Algorithm](https://en.wikipedia.org/wiki/Mersenne_Twister#Algorithmic_detail)


## raw-code 

```python
# coefficient.
# w: word size (in number of bits), bit의길이.
w = 32
# n: degree of recurrence
n = 624
# m: middle word, an offset used in the recurrence relation defining the series x, 1 ≤ m < n
m = 397
# r: separation point of one word, or the number of bits of the lower bitmask, 0 ≤ r ≤ w - 1
r = 31

# a: coefficients of the rational normal form twist matrix
a = 0x9908B0DF
# u, d, l: additional Mersenne Twister tempering bit shifts/masks
(u, d) = (11, 0xFFFFFFFF)
l = 18
# s, t: TGFSR(R) tempering bit shifts
# b, c: TGFSR(R) tempering bitmasks
(s, b) = (7, 0x9D2C5680)
(t, c) = (15, 0xEFC60000)

f = 1812433253



# LOWER_MASK: 32칸이 모두 1.
# 2^32 - 1, 0xFFFFFFFF
LOWER_MASK = 0xFFFFFFFF
# complement of LOWER_MASK
UPPER_MASK = ~LOWER_MASK
################################

def seed_mt(seed):
    """
    # MT는 624개의 원소를 가지는, 배열입니다. 
    # 그리고, 이 각각의 값들은 이후 extract_number()라는 함수를 통해 
    # 새로운 난수를 생성하는 모수가 되죠. 
    # 즉, 맨 처음에는 MT[0]를 사용해서 난수를 만들고, 
    # 그 다음에는 MT[1]를 사용해서 난수를 만듭니다. 
    # 본 함수, seed_mt(seed) 는 MT를 초기화해주는 함수인 것이죠. 
    # 보통, 우리가 seed를 준다는 것은 그저, 
    # MT의 첫번째 값을 지정해준다는 것과 같습니다. 
    # MT는 일종의 점화식을 통해서 생성되므로, 첫번째 값을 어떻게 지정하느냐에 따라서 
    # 이후의 값이 결정되죠.
    """
    global MT # MT: Mersenne Twister, 624개의 배열.
    global n # n: degree of recurrence, 624.
    global w  # w: word size (in number of bits). 32 bit일 때는 32.
    global LOWER_MASK # 32칸이 모두 1
    # 첫번째 원소를 seed를 통해 변형하고,
    MT[0] = seed
    for i in range(1, n):
        # LOWER_MASK는 이름은 lower지만, 32칸이 모두 1로 구성되어 있음.
        # 이 값으로 temp 와 AND bit operation을 처리할 경우,
        # temp의 마지막 32칸에서 1인 값만 가져오게됨.
        # 다르게 말한다면, 문자열로 끝의 32칸만 읽어서, 가져와도 된다는 이야기임.
        temp = f * (MT[i - 1] ^ (MT[i - 1] >> (w - 2))) + i
        MT[i] = temp & LOWER_MASK
def twist():
    """
    # MT는 일종의 모수, population이라고 생각하면 됩니다. 
    # 새로운 random number를 생성할 때, MT의 index번째 원소부터 출발하여, 
    # 그 원소를 bitwise operation를 통해 변형하게 되죠. 
    # MT는 n, 즉 624개의 값을 가지며, 
    # 제가 624개의 random number를 생성해냈다면, 
    # 이미 모수들은 다 사용된 것이므로, 새로운 모수가 필요합니다. 
    # 이 때, 새로운 모수를 만들어내는 과정이 바로, twist()인 셈이죠.
    """
    # m: middle word
    # an offset used in the recurrence relation defining the series x, 1 ≤ m < n
    global m
    # n: degree of recurrence, 624.
    global n
    # a: coefficients of the rational normal form twist matrix
    global a
    # LOWER_MASK: 32칸이 모두 1
    global LOWER_MASK
    # UPPER_MASK: LOWER_MASK의 보수.
    global UPPER_MASK

    for i in range(0, n):
        x = (MT[i] & UPPER_MASK) + (MT[(i + 1) % n] & LOWER_MASK)
        xA = x >> 1
        if (x % 2) != 0:
            # lowest bit of x(가장 오른쪽의 bit가 0이라는 말)
            xA = xA ^ a
        MT[i] = MT[(i + m) % n] ^ xA

def extract_number():
    """
    # MT는 일종의 모수(population)을 의미합니다. 
    # 이 함수는 모수들로부터 순서대로 하나의 모수를 선택하고, 
    # 아래 정의한 BLACK_BOX()라는 함수에서 값을 변형합니다. 
    # 그리고, 이를 통해 생성된 값이 random number가 되죠. 
    # 따라서, 이미 생성된 MT라는 모수를 한 바퀴 돌면 
    # 다시 twist()를 통해 새로운 모수를 생성하고, 다시 index는 초기화됩니다. 
    """
    def BLACK_BOX():
        """
        MT의 index번째 원소로부터, 
        u, d, t, c, s, b, l 를 사용하여 
        변형합니다. 
        왜 이렇게 해야 하는지는 이해가 안되네요 호호호. 
        """
        global u, d, t, c, s, b, l
        global MT
        global index
        y = MT[index]
        y = y ^ ((y >> u) & d)
        y = y ^ ((y << t) & c)
        y = y ^ ((y << s) & b)
        y = y ^ (y >> l)
    global n
    global index
    global LOWER_MASK
    if index>=n:
        # population을 한바퀴 돌았으므로,
        # 다시 새로운 population을 생성해주고(twist)
        # 다시 index를 초기화.
        twist()
        index = 0
    # MT의 index번째 값을부터 random한 값을 생성함.
    BLACK_BOX()
    index += 1
    return MT[index] & LOWER_MASK

# MT를 초기화합니다.
# 사실은 초기화라기보다, 그냥 이 배열을 메모리에 저장해주는 것이죠.
MT = [0 for i in range(0, n)]
# 한번 변형해주고, index를 제일 앞으로 돌려줍니다.
seed_mt(10)
index = 0

for i in range(0, 10):
    num = extract_number()
    print(num)


print("--")
```