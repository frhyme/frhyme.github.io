---
title: 간단하게 folium을 이용하여 지도에 그림 그리기 
category: python-lib
tags: python python-lib map open-street-map 
---

## 간단하게 지도에 내 위치를 표시해봅시다. 

- 간단하게, 지도에 위치를 표시해보려고 합니다. 
- `folium`이라는 라이브러리는 Open Street Map을 이용해서 지도를 활용할 수 있게 해줍니다. 
    - 그냥 오픈소스로 된 지도라고 생각해도 상관없습니다. 
- 단 결과를 html문서로 저장할 수 있습니다. svg, png 형태로는 일단 안되는 것 같네요. 

```python
import folium

my_pos = [36.012827, 129.321488]
## open street map 
map_osm = folium.Map(
    location= my_pos,
    zoom_start=17
)
folium.Marker(my_pos, popup='my current position').add_to(map_osm)
map_osm.save('../../assets/images/markdown_img/2018_0711_map.html')
map_osm
```

[html 문서](/assets/images/markdown_img/2018_0711_map.html)


## wrap-up

- 사람들의 참여가 적어서 Open Street Map보다는 네이버나 다른 지도를 쓰는게 더 좋을 수도 있는데, 일단 이건 무료니까요 하하핫

## reference 

- <http://folium.readthedocs.io/en/latest/quickstart.html>