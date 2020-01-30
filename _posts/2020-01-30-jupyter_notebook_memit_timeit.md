---
title: python - jupyter notebook 에서 magic command로 memory, time 성능 체크하기. 
category: python-libs
tags: python python-libs jupyter-notebook performance-checking memit ipython timeit
---

## `timeit`를 `ipython`을 이용한 성능체크. 

- 기본적으로 비슷한 두 코드의 성능을 비교할 때는 '시간'과 '리소스(메모리) 사용량'만 보면 됩니다. 
- 그리고 jupyter notebook에서 이는 magic command 인 `%`를 이용해서, `%timeit`와 `%memit`로 처리할 수 있죠. 
- 또한, `ipython_memory_usage`를 사용하면 cell별로 메모리 사용량을 체크하면서 코드를 진행할 수 있습니다.

## Do it. 

- 첫번째 cell은 다음과 같습니다. 

### Cell 1:

```python
# magic command %memit 를 사용하기 위해 필요한 라이브러리, 
import memory_profiler 
%load_ext memory_profiler
########################
# ipython_memory를 사용하여 cell별로 메모리를 계속 관찰하기 위한 라이브러리. 
import ipython_memory_usage 
import ipython_memory_usage.ipython_memory_usage as imu
%ipython_memory_usage_start


N =10**6

# memory watching start 
imu.start_watching_memory()
```

### Cell 2:

- 두번째 cell에서 다음 코드와 같이, `%timeit` `%memit`를 사용하여, 코드의 성능을 시간과, 메모리 관점에서 체크해줍니다. 두 매직 커맨드를 동시에 사용했기 때문에, `timeit`의 각 시행(여기서는 10번 시행함)마다 `memit`가 돌아가게 되죠.

```python
%timeit %memit test_lst = [i for i in range(0, N)]
print("--")
```

- 가장 메모리를 많이 사용한 순간(peak memory)는 어느 정도인지, 이전 대비 memory의 증분(increment)는 어느정도인지 를 표시해줍니다. 
- 그리고, 가장 마지막의 라인은 앞에서 `imu.start_watching_memory()`를 통해 메모리를 모니러팅하기 시작했기 때문에, 어느 정도의 메모리가 셀별로 쓰이는지를 출력해줍니다.

```
peak memory: 157.66 MiB, increment: 67.21 MiB
peak memory: 158.19 MiB, increment: 28.36 MiB
peak memory: 160.12 MiB, increment: 29.81 MiB
peak memory: 158.91 MiB, increment: 28.10 MiB
peak memory: 158.51 MiB, increment: 27.45 MiB
peak memory: 154.76 MiB, increment: 23.45 MiB
peak memory: 155.00 MiB, increment: 23.45 MiB
peak memory: 155.30 MiB, increment: 23.24 MiB
434 ms ± 28 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
--
In [13] used 0.7734 MiB RAM in 3.54s, peaked 64.66 MiB above current, total RAM usage 91.22 MiB
```

### Cell 3:

- 다른 코드에 대해서도, 여기서는 메모리를 어느 정도 사용하는지를 알 수 있습니다. 
- 그리고, 마지막 줄을 보면 `imu.start_watching_memory()`는 종종 MiB를 음수의 값으로 표시할 때가 있습니다. 이는, 이전 코드 대비 메모리 사용량이 감소했다는 말로, 효율적이라는 말이라고, 일단은 해석해도 되죠.

```python
%timeit %memit test_lst = (i for i in range(0, N))
```

```
peak memory: 90.98 MiB, increment: 0.00 MiB
peak memory: 90.98 MiB, increment: 0.00 MiB
peak memory: 90.98 MiB, increment: 0.00 MiB
peak memory: 90.98 MiB, increment: 0.00 MiB
peak memory: 90.98 MiB, increment: 0.00 MiB
peak memory: 90.98 MiB, increment: 0.00 MiB
peak memory: 90.98 MiB, increment: 0.00 MiB
peak memory: 90.98 MiB, increment: 0.00 MiB
219 ms ± 7.62 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
In [14] used -0.2344 MiB RAM in 1.86s, peaked 0.00 MiB above current, total RAM usage 90.98 MiB
```

- 그리고, 모니터링을 다 했다면 이제 아래의 코드로 멈춰줍니다.

```python
imu.stop_watching_memory()
```

## wrap-up

- 음. 그냥 시간만 고려할 때가 편했습니다. 메모리 사용량까지 고려하는 거는 매우 귀찮네요. 
- [ipython memory usage](https://github.com/ianozsvald/ipython_memory_usage)에 대한 자세한 내용은 링크를 참고하시면 좋습니다