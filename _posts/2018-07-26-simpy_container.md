---
title: simpy Container 사용하기 - gas fueling 모델링하기 
category: python-lib
tags: python python-lib simuation simpy numpy generator
---

## covers

- 여기서는 resource 중에서 container를 활용해봅니다. 

### simpy.container?

> Resource for sharing homogeneous matter between processes, either continuous (like water) or discrete (like apples).

- simpy.container는 간단하게 주유소 탱크라고 생각하시면 됩니다. homogeneour한 값을 가진(물만, 석유만 등) 큰 탱크를 모델링한 것이죠. 사실 반드시 써야 하는 요소는 아닙니다. 간단하게 `level`, `get`, `put`만 있는 객체인데, 현재 값을 확인하고, 넣거나, 빼거나 하는 것이 다라서요. 
    - 그냥 임의의 값을 만들어두고 그 값에서 빼고 더하고, 하는 식으로 관리해도 문제가 없지만, 이렇게 쓰는 것이 좀 더 기억하기 편하잖아요. 
- container에서 바로 resource랑 연결해서 쓸 수있으면 좋은데 그렇지는 않은 것 같아요. 즉, 컨테이너를 사용할 때는 리소스도 개별적으로 만들어서 해당 리소스에 리퀘스트를 날리고, 리퀘스트가 허용되었을 때 컨테이너에서 값을 빼는 식으로 사용합니다. 
    - 필요하다면, container와 resource를 하나의 클래스안에 집어넣고 사용해도 괜찮을 것 같네요. 

## water pump, water container

- 랜덤한 시간으로 사람이 물을 사용하는 구조를 만들어 봅시다. 

### people modeling 

- 일단 사람을 모델링할게요 
    - `water_pump` 리소스에 일단 사용요청을 하고
    - 사용이 되면, 현재 `water_container`에 양이 충분히 있는지 파악하고 
    - 양이 충분히 있을 경우, 물을 사용하고
    - 없을 경우 재충전을 하지 못했다고 하고 떠납니다. 

```python
def people(env, p_num, water_pump, water_container):
    with water_pump.request() as req:
        yield req
        required_water = np.random.uniform(10, 100)
        if water_container.level >= required_water:
            water_container.get(required_water)
            yield env.timeout(required_water/10)
            print("people {:2d} used {:6.2f} fuel".format(p_num, required_water))
        else: 
            print("water container can't refuel it")
        print("{:6.2f}: water {:8.2f} remained".format(env.now, water_container.level))
```

### people_arrival modeling

- 어떤 주기로 사람이 오는지 모델링하고, 그 시간에 맞춰서 새로운 사람 프로세스를 env에 넘겨줍니다. 

```python
def people_arrival(env,water_pump, water_container):
    for p_num in (i for i in range(0, 1000)):
        arrival_time = np.random.triangular(left=1, right=5, mode=1)
        print("{:6.2f}: people {:2d} arrived".format(env.now, p_num))
        yield env.timeout(arrival_time)
        env.process(people(env, p_num, water_pump, water_container))
```

### water refueling modeling

- 5초에 한번씩 현재 물의 양을 체크하고, 일정 수준보다 작게 있을 경우 `put`메소드로 값을 넣어줍니다. 
- 단 한번에 다 넣는다는 것은 말이 안되기 때문에, 그 시점에서 필요했던 양을 초별로 나누어서 넣습니다. 

```python
def water_refueling(env, water_container):
    while True:
        if (water_container.level / water_container.capacity) <= 0.1:
            refuel_amount = water_container.capacity - water_container.level 
            ## 1초에 50씩 넣음.
            for i in range(0, int(refuel_amount//50)):
                yield env.timeout(1)
                water_container.put(50)
            yield env.timeout(1)
            water_container.put(refuel_amount%50)
            print("{:6.2f}: water_contaienr refueled".format(env.now))
        ## 5 초에 한번씩 현재 물 양을 체크함
        yield env.timeout(5)
```

- 시뮬레이션을 돌립니다. 

```python
env = simpy.Environment()
water_pump = simpy.Resource(env, capacity=1)
water_reservoir = simpy.Container(env, capacity = 500, init=10)

env.process( people_arrival(env, water_pump, water_reservoir) )
env.process(water_refueling(env, water_reservoir))

env.run(until=20)
```

- 시뮬레이션 결과는 대략 다음과 같습니다. 잘 되네요.

```
  0.00: people  0 arrived
  1.84: people  1 arrived
water container can't refuel it
  1.84: water    60.00 remained
  5.95: people  2 arrived
people  1 used  24.04 fuel
  8.35: water   385.96 remained
  8.41: people  3 arrived
  9.74: people  4 arrived
people  2 used  15.23 fuel
  9.94: water   420.73 remained
 10.00: water_contaienr refueled
 13.28: people  5 arrived
 16.12: people  6 arrived
people  3 used  64.10 fuel
 16.35: water   396.63 remained
 17.16: people  7 arrived
```

## gas refueling

- 자 이제 simpy documentation에 있는 [gas refueling](http://simpy.readthedocs.io/en/latest/examples/gas_station_refuel.html)을 모델링해봅시다. 

- gas station을 클래스로 만들고 내부에 container, resource와 필요한 프로세스들을 모두 집어넣을 계획입니다. 
    - gas_fueling: 차에 가스 주입 
    - gas_refueling: 가스 재충전
    - gas_checking: 주기적으로 가스 양이 충분한지 확인

```python
class Gas_Station(object):
    def __init__(self, env):
        ## 환경 세팅, 리소스/컨테이너 생성, 함께 시작되어야 하는 프로세스 추가 
        self.env = env
        self.gas_pump = simpy.Resource(self.env, capacity=2)
        self.gas_container = simpy.Container(self.env, capacity=500, init=10)
        self.env.process(self.gas_checking())
        self.is_refueling = False
    
    def gas_fueling(self, c_num, required_amount):
        ## 차가 오면 가스를 채워주는 프로세스 
        with self.gas_pump.request() as req:
            yield req
            if required_amount > self.gas_container.level:
                ## 가스를 채우려고 보니 가스가 없음
                print("{:8.2f}: {:6.2f} fuel remained".format(self.env.now, self.gas_container.level))
                print("{:8.2f}: car{:2d} leaved".format(self.env.now,c_num))
                self.is_refueling = True
                yield self.env.process(self.gas_refueling())
                self.is_refueling = False
            else:
                ## 가스가 있음.
                self.gas_container.get(required_amount)
                yield self.env.timeout(required_amount/10)
                print("{:8.2f}: car{:2d} used {:6.2f} fuel".format(self.env.now, c_num, required_amount))
                print("{:8.2f}: {:6.2f} fuel remained".format(self.env.now, self.gas_container.level))
    
    def gas_refueling(self):
        ## 가스가 없을때 가스를 채우는 프로세스 
        refuel_amount = self.gas_container.capacity - self.gas_container.level
        print("{:8.2f}: gas_container refuel start".format(self.env.now))
        for i in range(0, int(refuel_amount//50)):
            yield self.env.timeout(1)
            self.gas_container.put(50)
        print("{:8.2f}: gas_container refueled".format(self.env.now))
        
    def gas_checking(self):
        ## 가스가 일정 값 이상으로 떨어지지 않았는지 확인하는 프로세스 
        while True:
            if self.gas_container.level/ self.gas_container.capacity <= 0.1:
                ## 차가 왔을 때 이미 가스가 부족한 상황이면, 위쪽에서 이 프로세스를 돌리고 있을 수 있음. 
                ## 따라서 self.is_refueling등으로 제어하지 않으면 동시에 프로세스가 돌아가고 있을 수 있으므로
                ## 이미 실행중일 때는 실행되지 않도록 제어한다. 
                if self.is_refueling != True:
                    yield self.env.process(self.gas_refueling())
            yield env.timeout(5)
```

- 주기적으로 차를 만들어서 보내는 제너레이터를 만듭니다. 

```python
def car_generator(env, gas_station):
    ## 일정 시간 별로 차에 가스 채우는 프로세스를 수행하는 제너레이터 
    for i in range(0, 1000):
        arrival_time = np.random.exponential(5)
        required_amount = np.random.uniform(10, 100)
        yield env.timeout(arrival_time)
        print("{:8.2f}: car{:2d} arrived".format(env.now, i))
        env.process(gas_station.gas_fueling(i, required_amount))
        
env = simpy.Environment()

gas_station = Gas_Station(env)
env.process(car_generator(env, gas_station))

env.run(until=50)
```

- 결과는 다음과 같습니다. 

```
    0.00: gas_container refuel start
    2.35: car 0 arrived
    8.93: car 1 arrived
    9.00: gas_container refueled
    9.78: car 2 arrived
   10.08: car 3 arrived
   11.90: car 0 used  95.56 fuel
   11.90: 300.56 fuel remained
   14.31: car 2 used  24.04 fuel
   14.31: 276.52 fuel remained
   14.67: car 4 arrived
   14.78: car 5 arrived
   15.32: car 1 used  63.88 fuel
   15.32: 188.56 fuel remained
   22.69: car 4 used  73.73 fuel
   22.69: 114.83 fuel remained
   23.10: car 3 used  87.96 fuel
   23.10:  17.54 fuel remained
   23.71: car 6 arrived
   23.71:  17.54 fuel remained
   23.71: car 6 leaved
   23.71: gas_container refuel start
   24.71: car 7 arrived
   26.53: car 8 arrived
   29.35: car 9 arrived
   32.42: car 5 used  97.29 fuel
   32.42: 417.54 fuel remained
   32.71: gas_container refueled
   34.09: car10 arrived
   35.07: car 7 used  26.51 fuel
   35.07: 383.81 fuel remained
   35.81: car11 arrived
   38.43: car 8 used  57.23 fuel
   38.43: 347.60 fuel remained
   38.69: car 9 used  36.21 fuel
   38.69: 325.04 fuel remained
   38.86: car12 arrived
   39.97: car13 arrived
   40.69: car10 used  22.55 fuel
   40.69: 282.07 fuel remained
   42.99: car11 used  42.97 fuel
   42.99: 201.40 fuel remained
   44.46: car14 arrived
   48.62: car13 used  56.28 fuel
   48.62: 145.12 fuel remained
   48.75: car12 used  80.67 fuel
   48.75: 130.94 fuel remained
   49.14: car15 arrived
   49.47: car16 arrived
```

## raw code

### water contaienr: raw code 

```python
import simpy 
import numpy as np 

np.random.seed(42)

def people(env, p_num, water_pump, water_container):
    with water_pump.request() as req:
        yield req
        required_water = np.random.uniform(10, 100)
        if water_container.level >= required_water:
            water_container.get(required_water)
            yield env.timeout(required_water/10)
            print("people {:2d} used {:6.2f} fuel".format(p_num, required_water))
        else: 
            print("water container can't refuel it")
        print("{:6.2f}: water {:8.2f} remained".format(env.now, water_container.level))
    
def people_arrival(env,water_pump, water_container):
    for p_num in (i for i in range(0, 1000)):
        arrival_time = np.random.triangular(left=1, right=5, mode=1)
        print("{:6.2f}: people {:2d} arrived".format(env.now, p_num))
        yield env.timeout(arrival_time)
        env.process(people(env, p_num, water_pump, water_container))
        
def water_refueling(env, water_container):
    while True:
        if (water_container.level / water_container.capacity) <= 0.1:
            refuel_amount = water_container.capacity - water_container.level 
            ## 1초에 50씩 넣음.
            for i in range(0, int(refuel_amount//50)):
                yield env.timeout(1)
                water_container.put(50)
            yield env.timeout(1)
            water_container.put(refuel_amount%50)
            print("{:6.2f}: water_contaienr refueled".format(env.now))
        ## 5 초에 한번씩 현재 물 양을 체크함
        yield env.timeout(5)
            
        
env = simpy.Environment()
water_pump = simpy.Resource(env, capacity=1)
water_reservoir = simpy.Container(env, capacity = 500, init=10)

env.process( people_arrival(env, water_pump, water_reservoir) )
env.process(water_refueling(env, water_reservoir))

env.run(until=20)
```

### gas refueling: raw code 

```python
import simpy 
import numpy as np 

np.random.seed(42)

class Gas_Station(object):
    def __init__(self, env):
        ## 환경 세팅, 리소스/컨테이너 생성, 함께 시작되어야 하는 프로세스 추가 
        self.env = env
        self.gas_pump = simpy.Resource(self.env, capacity=2)
        self.gas_container = simpy.Container(self.env, capacity=500, init=10)
        self.env.process(self.gas_checking())
        self.is_refueling = False
    
    def gas_fueling(self, c_num, required_amount):
        ## 차가 오면 가스를 채워주는 프로세스 
        with self.gas_pump.request() as req:
            yield req
            if required_amount > self.gas_container.level:
                ## 가스를 채우려고 보니 가스가 없음
                print("{:8.2f}: {:6.2f} fuel remained".format(self.env.now, self.gas_container.level))
                print("{:8.2f}: car{:2d} leaved".format(self.env.now,c_num))
                self.is_refueling = True
                yield self.env.process(self.gas_refueling())
                self.is_refueling = False
            else:
                ## 가스가 있음.
                self.gas_container.get(required_amount)
                yield self.env.timeout(required_amount/10)
                print("{:8.2f}: car{:2d} used {:6.2f} fuel".format(self.env.now, c_num, required_amount))
                print("{:8.2f}: {:6.2f} fuel remained".format(self.env.now, self.gas_container.level))
    
    def gas_refueling(self):
        ## 가스가 없을때 가스를 채우는 프로세스 
        refuel_amount = self.gas_container.capacity - self.gas_container.level
        print("{:8.2f}: gas_container refuel start".format(self.env.now))
        for i in range(0, int(refuel_amount//50)):
            yield self.env.timeout(1)
            self.gas_container.put(50)
        print("{:8.2f}: gas_container refueled".format(self.env.now))
        
    def gas_checking(self):
        ## 가스가 일정 값 이상으로 떨어지지 않았는지 확인하는 프로세스 
        while True:
            if self.gas_container.level/ self.gas_container.capacity <= 0.1:
                ## 차가 왔을 때 이미 가스가 부족한 상황이면, 위쪽에서 이 프로세스를 돌리고 있을 수 있음. 
                ## 따라서 self.is_refueling등으로 제어하지 않으면 동시에 프로세스가 돌아가고 있을 수 있으므로
                ## 이미 실행중일 때는 실행되지 않도록 제어한다. 
                if self.is_refueling != True:
                    yield self.env.process(self.gas_refueling())
            yield env.timeout(5)

def car_generator(env, gas_station):
    ## 일정 시간 별로 차에 가스 채우는 프로세스를 수행하는 제너레이터 
    for i in range(0, 1000):
        arrival_time = np.random.exponential(5)
        required_amount = np.random.uniform(10, 100)
        yield env.timeout(arrival_time)
        print("{:8.2f}: car{:2d} arrived".format(env.now, i))
        env.process(gas_station.gas_fueling(i, required_amount))
        
env = simpy.Environment()

gas_station = Gas_Station(env)
env.process(car_generator(env, gas_station))

env.run(until=50)
```


