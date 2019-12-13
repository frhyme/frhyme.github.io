---
title: Polyglot persistence
category: others
tags: database nosql polyglot
---

## (번역) polyglot persistence

> Polyglot persistence is the concept of using different data storage technologies to handle different data storage needs within a given software application. Polyglot programming, a term coined by Neal Ford in 2006, expresses the idea that computer applications should be written in a mix of different programming languages, in order to take advantage of the fact that different languages are suitable for tackling different problems. 
- Polyglot persistence(다양한 언어에 대한 고집)은 주어진 소프트웨어 어플리케이션 에서 다양한 데이터 저장소에 대한 필요를 컨트롤하기 위해서, 다양한 저장 기술을 사용하는 것을 말합니다. 
- polyglot programming은 Neal Ford가 2006년에 다양한 문제별로 잘 작동하는 언어들이 다르기 때문에, 이를 효과적으로 이용하기 위해, 컴퓨터 응용 프로그램이 다양한 프로그래밍 언어의 조합으로 쓰여지는 것이 필요하다는 것을 말합니다.

> Complex applications combine different types of problems, so picking the right language for each job may be more productive than trying to solve all aspects of the problem using a single language. This same concept can be applied to databases, that an application can communicate with different databases, using each for what it is best at to achieve an end goal, hence the term polyglot persistence.
- 복잡한 프로그램(application)은 다양한 유형의 문제들이 혼합되어 있습니다. 그래서, 필요에 따라, 각 문제별로 적합한 언어를 선정하는 것이, 모든 문제를 하나의 언어로 푸는 것보다 훨씬 효과적입니다. 
- 이러한 개념은 언어뿐만 아니라, database에도 같은 방식으로 적용될 수 있으며, 어플리케이션이 서로 다른 데이터베이스와 통신함으로 인해, 우리의 최종 목표를 성취하기에 가장 적합하게 하는 것, 이것이 바로 polyglot persistenc입니다.

> There are numerous databases available to solve different problems. Using a single database to satisfy all of a program's requirements can result in a non-performant, "jack of all trades, master of none" solution. Relational databases, for example, are good at enforcing relationships that exist between various data tables. To discover a relationship or to find data from different tables that belong to the same object, an SQL join operation can be used. 

- 이미, 다양한 문제들에 적용할 수 있는 database가 존재한다. 모든 프로그램의 요구사항을 만족하기 위한 하나의 데이터베이스를 사용하는 것은, 성능기준에 맞지 않습니다. "모든 것을 잘하면, 잘하는 것은 없다(jack of all trades, master of none)". 관계형 디비의 경우, 예를 들면, 다양한 데이터 테이블 사이에 존재하는 관계를 제한하는 것에 대해서는 매우 효과적입니다. 하나의 개체(object)에 대한 서로 다른 테이블에 존재하는 데이터를 찾거나, 관계를 발견하기 위해서는, SQL join이 사용될 수도 있죠.

> This might work when the data is smaller in size, but becomes problematic when the data involved grows larger. A graph database might solve the problem of relationships in case of Big Data, but it might not solve the problem of database transactions, which are provided by RDBM systems. Instead, a NoSQL document database might be used to store unstructured data for that particular part of the problem. Thus different problems are solved by different database systems, all within the same application.
- 이것은 데이터가 작을 때는 문제가 없습니다. 그러나, 데이터가 커질 수록 점차 문제가 생겨나기 시작하죠. graph db의 경우 대용량 데이터에 대해서, 관계간에 발생하는 문제들을 해결할 수 있습니다. 하지만, 이는 또한, database transaction에서 발생하는 문제점들을 해결할 수 없죠. 이는 RDBMS에서 처리됩니다. 대신에, NoSQL document dtabase의 경우 특정 분야의 비구조적인 데이터(Unstructured data)를 저정하는 것에 유용합니다. 따라서, 하나의 어플리케이션이라도, 서로다른 문제들이 서로 다른 시스템에 의해서 처리될 수 있다는 것이죠.


## wrap-up

- 저의 주요 언어는 python입니다. 그리고 javascript와 몇 개의 관련 라이브러리들을 사용할 수 있죠. 대학원 졸업시에 필요해서, python으로 백엔드에서 돌아가는 시뮬레이션 프로그램을 만들고, javascript를 사용해서(chart.js, d3.js), 웹 상에서 뿌려지는 시각화를 만들었죠. 
- 사실 인터넷이라는 것이 결국 기본적으로 텍스트를 주고 받는 것이라고 봤을 때(웹브라우저는 텍스트를 받아서, 그림을 그려주는 것이니까요), 파이썬만으로 모든 텍스트를 다 만들어서 제어할 수도 있기는 합니다. 실제로 제가 만든 프로그램에서도, 초기에는 좀 더 많은 문자열을 백엔드에서 만들어 넘겼다면, 이후, 점차 자바 스크립트에 익숙해짐에 따라서, 최소한의 데이터를 넘기고, 자바스크립트에서 직접 더 직관적으로 코딩하기도 했죠. 
- 물론, 지금 제가 말한 것은 그냥 poly-glot programming일 뿐입니다만, 데이터베이스의 경우에도 결국 마찬가지인 것 같습니다. 사람들이 NoSQL이 나오고, 마치 관계형 DB는 필요없다는 식으로 매도를 당하기도 했지만, 각각의 성질은 다르죠. 그래서 필요한 곳에 필요한 것을 쓰는 것이 필요합니다. 
- 다만, 사실 이게 제일 어렵죠. 어떤 문제가 주어졌을 때, 이 문제를 정말 정확하게 이해하고, 그 문제들 세부 서브 문제로 쪼개고, 그리고 그 서브 문제를 풀기에 가장 적합한 것은 무엇인지, 정확하게 매핑을 해야합니다. 아니, 이게 말이 되나요. 관계형DB를 잘 아는 것도 어려운데, 그렇지 않은 것도 다 알라니요 흐흐흐흐흑
- 뭐, 그래도, 결국 여기서 말하고 있는 것은 하나의 언어, 하나의 학문에 대한 아집을 버리는 것이 필요하다, 정도인 것 같습니다.