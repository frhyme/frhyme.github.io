---
title: Google Analytics 결과 분석하기 
category: others
tags: analytics google DNS 
---

## GA 결과는 각각 어떤 의미를 가질까요? 

- 예전에 Google Analytics를 블로그에 연결했습니다. 사실 그냥 들어오는 사람들이 얼마나 될까 뭐 그거만 보려고 했는데, 요즘 은근히 보는 사람이 늘어났어요. 감사합니다. 
- 보는 사람들이 늘어나니까, 왜 이 블로그에 들어오게 될까 좀 더 자세하게 알고 싶어졌어요. 그래서 google analytics에서 제가 모르는 것들을 정리해보기로 했어요. 

## 유입 경로 

- 유입 경로는 총 세 가지로 나뉩니다. 
    - Direct: 블로그에 직접 들어오는 경우, 브라우저 밖(ppt 등)을 통해 링크로 들어오는 경우 
    - Organic: 구글/네이버 등의 검색엔진을 통해 들어오는 경우 
    - Referal: 다른 사이트에서 이 블로그가 링크되어 있을 때, 그 블로그로부터 들어오는 경우 

- 저의 경우는 대부분이 organic이고요, direct의 경우는 아마도 제가 들어간게 아닐까...싶고요...
- referal의 경우는 몇 개가 있는데 왜 있는지 모르겠군요. referal로 들어오는 경우가 많아야 제 블로그의 가치가 있어진다 라고 생각되기도 해요. 그런데, 그런것에 비해서는 제가 너무 막 정리를 해놓기는 했죠...


## keyword 

### (not provided )

- keyword에 (not provided)라고 표시되어 있는 것을 볼 수 있습니다. 내 블로그를 어떤 키워드로 검색해서 들어왔는지를 정확하게 알고 싶은데 (not provided) 라고 검색되어 있는 것을 보면 약간 허탈합니다. 
- 이는 [2011년 10월 구글이 사용자 정보를 보호하기 위해서 모든 키워드를 암호화하여 처리하였기 때문](https://googleblog.blogspot.com/2011/10/making-search-more-secure.html)에 발생한 일입니다. 
- 즉, Google에서 검색하여 들어온 경우 모두 키워드에 (not provided) 로 표시되는 것이라고 할 수 있습니다. 
- 네이버에서 유입된 키워드는 잘 표시됩니다 하하하. 

### (not set)

- 이는 일단 organic search(검색 엔진을 통해 유입된 경우)를 제외하고 direct/referal로 들어온 경우를 말합니다. 키워드로 검색해서 들어온 것이 아니므로 keyword 자체가 없고 따라서 (not set) 이 됩니다. 
- 다른 경우에도, (not set)은 딱히 값을 표시할 것이 없다. 즉 Null과 같은 값이 되겠네요. 

## service provider 

- internet service provider는 말 그대로 인터넷 서비스를 공급해주는 업체를 말합니다. kt, skt, samsung sds 등 네트워크를 설치하고 관리해주는 아주 많은 업체들이 여기에 포함되겠죠. 
- 뒤에서 설명할 network domain의 경우는 unknown.unknown 이나 (not set)으로 명확하게 되어 있지 않은 경우들이 있지만, 서비스 프로바이더의 경우는 대부분이 채워져 있습니다(약 1%의 (not set)이 존재하는데, 이정도는 무시해도 될것 같아요). 

## network domain

- 자 이제 network domain이 문제입니다. network domain은 약 60% 이상이 unknown.unknown으로 구성되고, 3%가 (not set)으로 되어 있습니다. 그 외에는 ac.kr, samsung.co.kr 등 일반적인 네트워크 도메인들이 표시되어 있구요. 

### DNS(Domain Name System)

- 사실 주소창에 ip를 쳐도 문제없이 개별 사이트에 들어갈 수 있습니다. 하지만 ip를 외우는 것이 매우 어려우니까 해당 ip에 할당된 domain name이 존재하고, domain name을 주소창에 치면 해당 ip로 연결되는 시스템을 가지고 있죠. 이러한 것을 Domain Name System이라고 부릅니다. 
- foward zone(domain name ==> ip), reverse zone(ip ==> domain name)이 각각 존재합니다. 이를 통해 변환해주는 것이죠. 

### unknown.unknown

- 고정 ip이고, DNS에서 ip를 domain name으로 변환할 수 있는 경우에는 google analytics에서 알아서 인식하고 값을 저장해 줄 수 있습니다. 
- 그러나 유동 ip일 경우에는 해당 ip에 적합한 domain name을 찾을 수가 없습니다. DNS에 업데이트되어 있지 않음은 물론, 특정 유동 ip에 대해서 domain name을 설정해버리면 이후 ip가 다른 곳에 할당되었을 때 문제가 발생할 수 있거든요. 
- 일반적인 가정집이 모두 해당 isp에서 할당받은 유동 ip를 사용할 것이며 이들이 아마도 unknown.unknown으로 인식되는 것이 아닐까 싶습니다. 
- LTE 등으로 들어오는 경우도 아마 포함될 것 같아요. 

### (not set)

- 아마도 이 경우는 ip는 고정 ip인데 아직 DNS에서 ip를 domain name으로 변환할 수 없는 경우, 를 말하는 것이 아닐까 싶습니다. 

## bounce rate(이탈률)

- 이탈률은 "이탈수 / 전체 방문자 수"를 의미합니다(이탈수: landing page와 exit page가 같은 경우). 즉 사이트에 들어온 page가 A이고 A만 보고 사이트를 나간 비율을 의미합니다. 
- 만약 일반적인 서비스 사이트라면, main page에서 bounce rate가 매우 높을 경우 문제가 될 수 있지만, 일반 블로그에서는 큰 문제가 된다고 생각하지는 않아요. 제 개인 블로그의 메인 페이지는 구글 혹은 네이버이고 여기서 검색해서 제가 쓴 포스트가 클린된다면, 그 때 그 포스트를 누른 사용자는 그 포스트에만 관심있을 확률이 높다고 생각해요. 
    - 그리고 개별 포스트 맨 아래에서 관련 포스트를 추천해주는 엔진이 영 엉망이거든요. 관련 검색어 등으로 잘 찾아서 추천해주는 방식으로 세팅한다면 좀 나아질 수 있겠네요. 이 부분은 차후에 개선하겠습니다.