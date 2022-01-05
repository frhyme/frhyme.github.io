- python에서는 tab이 4 space인 반면, c에서는 8 space인 이유는?
- bracket 이 안 먹힘 흠 > vimrc 에 수정하고, nvim으로 확인하니까 고쳐질리가 있냐.
- YouCompleteMe - JediVim 이 느려서, 얘 말고 YouCompleteMe를 설치해보려고 함. 얘는 단지 python뿐만 아니라, 다른 언어들도 처리해주는 것 같은데.
https://github.com/ycm-core/YouCompleteMe#installation


- jedi-vim select by tab not enter ? 
- jedi-vim이 느리기는 한데, 라이브러리에 직접 접근할 때는 느리지만, 한번 로드한 다음부터는 빨라짐.

```python
import networkx as nx

# nx. 로 라이브러리르 직접 로드할 때는 느림.
g = nx.Graph()
# 하지만, 다음처럼 g. 으로 접근하는 경우에는 꽤 빠른 편. 
g.
```