---
title: julia에서 python을 가져와봅시다. 
category: python-lib
tags: python python-lib julia 
---

## 요즘 julia를 써보고 있습니다. 

- '왜 써야 되냐?'라고 물으면 음, 그냥 취미생활에 가까운 것 같아요. 
- 아무튼 julia를 써보니, 다른 라이브러리를 쓰지 않았을때 pure python과 pure julia는 속도의 차이가 약 100배 정도 납니다. julia가 더 빠르죠. julia는 알아서 매트릭스 연산으로 처리해주는 것 같아요. 아마도. 
- 아무튼, 그래서 julia와 python을 알아서 연동해서 써보면 좋을 것 같다는 생각을 했습니다.

## using python in julia

- 일단 필요한 `PyCall`이라는 라이브러리가 필요합니다. 해당 라이브러리를 `add`하고 이미 있을 경우 `build`합니다. 

```julia
Pkg.build("PyCall")
```

- 우선 `using PyCall`을 하고, `@pyimport numpy`를 사용합니다. 그럼 잘 됩니다만, 그 다음 결과를 보시면 아시겠지만, 속도가 더 느립니다. 
    - 계산시간: pure python with numpy < julia < numpy in julia < python 
- 즉, 그냥 julia를 사용하는 편이 더 좋은 것 같아요. 

```julia
using PyCall ##불러오고 

## python with numpy 속도, 
@pyimport numpy ## 필요한 라이브러리를 가져옴 
@time begin
    function compute_pi(n=10)
        return numpy.sum(numpy.array([ 1/(16^k)*( 4/(8*k+1) - 2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6)) for k in range(0, 10)]))
    end
    compute_pi(20000)
end
## pure julia 속도 
@time begin
    function compute_pi(n=10)
        r = 0
        for k in 0:9
            r+= 1/(16^k)*( 4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6))
        end
        r
    end
    compute_pi(20000)
end 
```

## using julia in python 

- [반대로 python에서도 julia를 쓸 수 있습니다](https://github.com/JuliaPy/pyjulia)만 그럴 필요가 없어서 넘어가려고 했는데, python으로 코드를 쓰다가 필요한 부분은 julia로 작성해서 julia로 결과를 확인하고 뭐 그렇게 쓸 수 있을까? 싶어서 좀 찾아봤씁니다. 

- 설치하고 조금 써보려고 했는데, documentation이 너무 안되어 있어서 사용하실 필요 없을 것 같아요. 혹시 필요하신 분은 [pyjulia](https://github.com/JuliaPy/pyjulia)에 들어가셔서 보시면 될 것 같습니다. 

```bash
pip install julia 
```

## wrap-up

- 문법상 큰 차이가 없고, 필요하면 그냥 julia를 쓰는 편이더 좋은 것 같아요. 좀 다른 라이브러리들을 써야 한다면, python으로 코딩하고, 흠....
- 오히려 python으로 코딩하다가 속도가 느린 부분은 julia로 코딩하여 코드를 넘기면 거기서 알아서 컴파일해서 계산만 돌려주거나 뭐 그렇게 사용하면 좋을 것 같기는 한데요...흠. 아직 이부분은 어떻게 할 수 있을지 잘 모르겠습니다. 좀 나중에 고민해볼게요. 


## reference

- <https://github.com/JuliaPy/pyjulia>
- <https://github.com/JuliaPy/PyCall.jl>