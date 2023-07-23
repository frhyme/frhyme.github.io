---
title: Mermaid - Flow Chart를 그려보자.
category: mermaid
tags: mermaid jekyll github diagram javascript
---

## Mermaid - 다양한 diagram을 그려보자

- 저는 블로그에서 [mermaid-js](https://mermaid-js.github.io/mermaid/#/)을 CDN을 사용해 include하고, post에서 다음의 방식을 통해 Diagram이 그려지도록 설정한 상황입니다.
- 본 포스팅에서는 Flow Chart를 그리는 방법을 정리합니다.

```plaintext
<div class="mermaid"> 
    graph LR;
        A --> B;
        A --> C;
        B --> D;
        C --> D;
</div>
```

<div class="mermaid"> 
    graph LR;
        A --> B;
        A --> C;
        B --> D;
        C --> D;
</div>

## Mermaid - Flow Chart

- [Mermaid - flow chart](https://mermaid-js.github.io/mermaid/#/flowchart?id=flowcharts-basic-syntax)의 내용을 정리하였습니다.

### Flow Chart Orientation

- 그림이 그려지는 방향은 다음과 같은 4가지 방식이 있습니다.
  - `TD`: Top to Down(or `TB`)
  - `LR`: Left to Right
  - `BT`: Bottom to Top
  - `RL`: Right to Left

### Node and Shape

- `nodeID[text]`: `nodeID`를 ID로 가지고 `text`를 표시해주는 직사각형 node를 만듭니다.
- `nodeID(text)`: 코너가 둥그런 직사각형 node를 만듭니다.
- `nodeID[(text)]`: 원통형 node를 만듭니다. Database로 표시해주기에 좋겠죠.
- `nodeID((text))`: 원 모양의 node를 만듭니다.
- `nodeID{text}`: 마름모 모양의 node를 만듭니다.

### Edge 

- `nodeID1 --> nodeID2`: `nodeID1`와 `nodeID2`를 화살표로 연결합니다.
- `nodeID1 --- nodeID2`: `nodeID1`와 `nodeID2`를 직선으로 연결합니다.
- `nodeID1 ---|Text| nodeID2`: `nodeID1`와 `nodeID2`를 **직선으로** 텍스트와 함께 연결합니다.
- `nodeID1 -->|Text| nodeID2`: `nodeID1`와 `nodeID2`를 **화살표로** 텍스트와 함께 연결합니다.
- `nodeID1 -.-> nodeID2`: `nodeID1`와 `nodeID2`를 **점선 화살표로** 텍스트와 함께 연결합니다.
- `nodeID1 ==> nodeID2`: `nodeID1`와 `nodeID2`를 **두꺼운 화살표로** 텍스트와 함께 연결합니다.
- 그리고 화살표 모양을 길게 하면 실제로 길어집니다. 가령 `==>`보다 `=====>`로 하면 훨씬 길게 그려지죠.

### Example Node and Edge 

- 앞에서 배운 node, edge를 사용해서 다음과 같은 간단한 예제를 만들어 봤습니다.

```html
<div class="mermaid"> 
    graph LR
        nID1;
        nID2[text of nID1];
        nID3[(Database)];
        nID4((Circle));
        nID5{rhombus};
        nID6(rounded shape);
        nID1 --> nID2;
        nID3 --- nID4;
        nid4 ==> nID3;
        nID3 -->|Text| nID5;
        nID5 -.-> nID6;
</div>
```

<div class="mermaid"> 
    graph LR
        nID1;
        nID2[text of nID1];
        nID3[(Database)];
        nID4((Circle));
        nID5{rhombus};
        nID6(rounded shape);
        nID1 --> nID2;
        nID3 --- nID4;
        nid4 ==> nID3;
        nID3 -->|Text| nID5;
        nID5 -.-> nID6;
</div>

---

### Subgraph 

- graph를 구분하여 만들 수도 있습니다.

```html
<div class="mermaid"> 
flowchart LR
    subgraph subG1 
        a1 --> a2;
    end
    subgraph subG2
        b1 ==> b2;
    end
    a1 -.-> b1;
</div>
```

<div class="mermaid"> 
    flowchart LR
        subgraph subG1 
            a1 --> a2;
        end
        subgraph subG2
            b1 ==> b2;
        end
        a1 -.-> b1;
</div>

## Wrap-up

- 그 외에도 다양한 styling이 있지만 귀찮으니 더 정리하지 않도록 합니다 호호호.

## Reference

- [mermaid-js](https://mermaid-js.github.io/mermaid/#/)
