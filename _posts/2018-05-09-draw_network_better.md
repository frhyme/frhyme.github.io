---
title: networkx와 matplotlib를 사용하여 graph를 예쁘게 그려 봅시다. 
category: python-lib
tags: python python-lib networkx matplotlib

---

## maplotlib를 사용하는 이유. 

- 이전 포스트에서는 `graphviz`를 사용하겠다고 했었습니다. 물론 이 것의 장점이 있기는 한데, 약간 범용적인 측면에서 생각해보면 결국 matplotlib로 돌아가게 됩니다(물론 process model을 표현하는데는 graphviz가 훨씬 좋습니다만). 
- python에서는 결국 그림을 그릴때 `matplotlib`를 중심으로 생각하게 되고, 특히 documnetation이 훨씬 많으니까요. 따라서, 다시 matplotlib를 활용해서 그림을 그려보려고 합니다. 
- 이후에 `networkx`의 documentation을 다시 보고 그림 그리는 걸 다시 정리해서 올리도록 하겠습니다. 

## just do it

- 아래 코드에서 조금 특이한 부분이라면, `margin`을 넣은 것. 
- 내부에서 scaling을 따로 해준 것 밖에 없습니다. 
- 특히 이 scaling이 은근히 어려운데, 
    - node의 크기 변화는 어떻게 되어야 그 변화 차이가 분명하게 보일까요? 
    - edge의 굵기 또한 어떻게 되어야 그 변화 차이가 분명하게 보일까요? 
    - 이를 위해서 기존의 exponential한 분포를 linear하게, 바꾸고, 여기서 차이를 두었습니다. 
- 그래도 썩 마음에 들지는 않아요. 나중에 좀 더 고민해보아야 할 것 같구요. 

```python
def draw_whole_graph(inputG, outPicName):
    plt.close('all')
    f = plt.figure(figsize=(16, 10))
    plt.margins(x=0.05, y=0.05) # text 가 잘리는 경우가 있어서, margins을 넣음
    pos = nx.spring_layout(inputG)
    """
    한번씩 input_lst가 비어있을때가 있는데 왜 그런지 확인 필요.
    """
    def return_log_scaled_lst(input_lst):
        r_lst = map(np.log, input_lst)
        try:
            max_v = max(map(np.log, input_lst))
            min_v = min(map(np.log, input_lst))
            return map(lambda v: v/max_v, r_lst)
        except: 
            print(input_lst)
    node_weight_lst = return_log_scaled_lst([n[1]['weight'] for n in inputG.nodes(data=True)])
    edge_weight_lst = return_log_scaled_lst([e[2]['weight'] for e in inputG.edges(data=True)])
    nx.draw_networkx_nodes(inputG, pos, 
                           node_size = list(map(lambda x: x*2000, node_weight_lst)),
                     #node_size = [ n[1]['weight']*1000 for n in inputG.nodes(data=True)],
                     alpha=1.0 )
    # label의 경우는 특정 node만 그릴 수 없음. 그리면 모두 그려야함. 
    nx.draw_networkx_labels(inputG, pos, font_weight='bold', 
                            font_family='sans-serif', 
                            font_color='black', font_size=15
                           )
    nx.draw_networkx_edges(inputG, pos, 
                           width = list(map(lambda x: 5**(x+1), edge_weight_lst)), 
                           edge_color='b', alpha=0.5
                          )
    plt.axis('off')
    plt.savefig('../../assets/images/markdown_img/'+outPicName)
    #plt.show()
```