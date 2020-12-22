---
title: R - ggplot with title
category: R_programming
tags: R R_programming ggplot 
---

## R - ggplot with title

- R에서 ggplot을 이용해서 그림을 그리고 title을 넣어주는 코드입니다.

```R
# Load ggplot
require("ggplot2")


# ggplot으로 그림을 그리려면 data.frame이어야 하죠.
data_df = data.frame(x = c(0, 1, 2), y=c(1, 6, 3))

# ggplot에 data.frame을 넘겨주고요
plt = ggplot(data_df, aes(x=x, y=y))

# scatter plot으로 그릴 것이므로 geom_point()을 추가해주고요
plt = plt + geom_point()

# ggtitle을 넘겨줍니다.
plt = plt + ggtitle("THIS IS TITLE")

# 그리고 title을 어떻게 꾸밀지에 대한 정보는 다음과 같이 넘겨줍니다.
plt_theme = theme(
    # title 요소에 대한 정보
    plot.title=element_text(
        size=15, # 크기 
        color="red", # 색깔
        hjust=0.5 # 정렬 정도( horizontal-justify 가 의미겠죠.)
    )
)

# 그리고 ggplot과 ggtitle을 더해서 넘겨주면 그려집니다 짠하고
plot(
    plt+ plt_theme
)
```

## Wrap-up

- python이랑 R은 그림 그리는 방식이 완전히 달라서 좀 낯설군요 흠.