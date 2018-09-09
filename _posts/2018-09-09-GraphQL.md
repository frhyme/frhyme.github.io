---
title: GraphQL이 무엇일까요. 
category: others
tags: graphql query database graph
---

## 언제나 의식의 흐름. 

- 사실 지금 저는 휴가중입니다. 그러니까, 여유가 있을때 공부를 하면, 끊임없이 공부할 수 있어요. 공부할 거리들이 계속 생겨나니까요. 
- 아마도 지난주에 저는 [neo4j](https://neo4j.com/)라는 GraphDB를 보고 있었던 것 같습니다. 또 여기서 사용하는 query language인 [Cypher](https://neo4j.com/developer/cypher-query-language/)를 보고 있었던 것 같아요. 둘다 조금 보다가, 일단 내가 처리하는 수준의 그래프들은 networkx로도 대부분 처리할 수 있고, 더 진행할 필요는 없지 않을까 싶어서 멈췄던 것으로 기억하고 있습니다. 
- 그런데, 그다음에 RestFul Arhitecture를 보다가 보니, 이제는 rest도 한물 갈 것이고, [GraphQL](https://en.wikipedia.org/wiki/GraphQL)이라는게 대세가 될 거라고 합니다. GraphQL은 언뜻 보기에는 Cypher와 같은 graph query language같기도 한데, 이건 또 어느 면에서 Rest와 유사한 면이 있는걸까요. 

- 그걸 정리해보도록 하겠습니다 하하핫
- 또한 제 포스트보다는 [GraphQL in Action - REST와 이별할 때 생각해야 하는 것들](https://www.slideshare.net/Kivol/graphql-in-action-rest)을 보시는 편이 훨씬 좋습니다. 

## what is GraphQL

> GraphQL is an open source data query and manipulation language, and a runtime for fulfilling queries with existing data - wikipedia

- [위키피디아]에서는 "실시간으로 존재하는 데이터에 대한 질의(query)에 응답하기 위한 오픈소스 데이터 질의 및 조작 언어"라고 하고 

> A query language for your API - graphql.org

- 공식 문서에서는 API에 사용하기 위한 질의어, 라고 하는군요. 미묘하지만, 공식문서에서 강조하고 있는 **API**와 **Query**가 핵심어라고 생각합니다. 

> a query language and execution engine originally created at Facebook in 2012 for describing the capabilities and requirements of data models for client‐server applications. 

- [facebook github 블로그](http://facebook.github.io/graphql/June2018/)에서는 "clier-server application(사실 이게 API와 비슷하죠)의 요구사항등을 설명하기 위해서 페이스북에서 만든 질의어 및 **실행엔진**"이라고 합니다. 점점 더 헷갈리네요. 저는. 

- 정리하자면, GraphQL은 client-server 사이에서 데이터를 효과적으로 주고받기 위한 프로토콜이라고 하면 될 것 같습니다. 
- SQL이 데이터베이스와 유저 간의 프로토콜을 정의하기 위해서 사용되었다면, GraphQL은 API에 대해서 데이터를 질의하고 가져오기 위해 사용되었다고 할까요. 


## why GraphQL

- 그런데, 사실 아직은 잘 모르겠습니다. 이전에도 json으로 서로 잘 통신했던 것 같은데 굳이 새로운 GraphQL을 정의할 필요성이 있을까요?
- [왜 GraphQL을 써야 하는가?에 대한 답을 이 블로그에서 해주셨습니다](https://velopert.com/2318). 또한 [이 블로그에서도 해주셨구요](https://www.robinwieruch.de/why-graphql-advantages-disadvantages-alternatives/).
- 아래에서는 이 두 블로그의 글들을 제가 소화해서 정리해보도록 하겠습니다. 

### The def of RESTful

> A RESTful API is an application program interface (API) that uses HTTP requests to GET, PUT, POST and DELETE data.

- 기존에는 server와 client간에 데이터를 교환 및 조작할 때, [RESTful](https://en.wikipedia.org/wiki/Representational_state_transfer)하게 처리했습니다. REST에서는 모든 것들이 URL(Uniform Resource Locator)로 정의되고, URL과 HTTP method(GET, POST, DELETE, INSERT)를 이용해서 데이터를 읽고 조작합니다. 
- 또한 [그 결과는 다음과 같이 보통 json으로 돌아오죠](https://www.robinwieruch.de/why-graphql-advantages-disadvantages-alternatives/). 

```json
// a RESTful request
GET https://api.domain.com/authors/7

// the response in JSON
{
  "id": "7",
  "name": "Robin Wieruch",
  "avatarUrl": "https://domain.com/authors/7",
  "firstName": "Robin",
  "lastName": "Wieruch"
}
```

- 실제로 이러한 RESTful request는 오랫동안 '표준'인것처럼 사용되어 왔습니다. 그러나, 다음과 같은 몇가지 문제점들이 있었죠. 

### the disadvantages of RESTful

- 기존의 RESTful API에서는 모든 것을 Resource로 인식하고, 해당 Resource에 http method를 통해 명령이 전달되면, 해당 Resource에서 그 결과를 반영하거나, json으로 결과를 리턴합니다. 
- 여기서 문제는, 다음 두 가지죠. 
    - 결과로 리턴되는 json 파일의 형식을 예측할 수 없다. 
        - 보통 json 파일을 가져온 다음, 해당 json파일을 파싱하는 식으로 처리합니다. 
    - 예측할 수 없을 뿐 아니라, 필요하지 않은 파일까지 모두 한번에 날아올 수 있기 때문에 비효율적이다(ovefetching). 
        - 다양한 상황을 반영할 수 있도록 만들 수도 있지만, 그럴 경우 정의되어야 하는 Resource가 증가하고 endpoint가 많아져서 관리가 어려워질 수 있습니다. 

### GraphQL 

- 이걸 변형해서, client 측에서 알아서 특정 질의어를 보내면, 서버에서 해당 질의어에 해당하는 부분만 전달해주면 훨씬 효율적으로 변하게 됩니다. 따라서 client 측에서 알아서 특정 질의어를 보내면, 서버에서 알아서 해당 질의어에 해당하는 값만 전달해주면 되는 것 아닐까요? 
- 이를 지원하는 것이 바로 GraphQL이고, 대락 다음과 같이, json과 유사한 형태로 질의하고, 그 결과륿 가져옵니다. 

```json
// a GraphQL query
author(id: "7") {
  id
  name
  avatarUrl
  articles(limit: 2) {
    name
    urlSlug
  }
}

// a GraphQL query result
{
  "data": {
    "author": {
      "id": "7",
      "name": "Robin Wieruch",
      "avatarUrl": "https://domain.com/authors/7",
      "articles": [
        {
          "name": "The Road to learn React",
          "urlSlug": "the-road-to-learn-react"
        },
        {
          "name": "React Testing Tutorial",
          "urlSlug": "react-testing-tutorial"
        }
      ]
    }
  }
}
```

## ...대충 무슨 말인지는 알겠는데...

- 대략 무슨 말인지는 알겠습니다...원래는 api간의 데이터를 가져오는 방식이 너무 불편했고, 이걸 GraphQL이 구원하겠다, 대충 그런 말인셈이죠. 
- 됐으나, 한번 간단하게라도 만들어보도록 하겠습니다. 

## 흐음....

- 잘 모를때는 일단 깔고, 한번 사용해보면 좋습니다. 
- [graphene-python](https://docs.graphene-python.org/en/latest/quickstart/)를 설치합니다. 

```bash 
pip install graphene
```

- 설치하고, [tutorial](https://docs.graphene-python.org/en/latest/quickstart/)을 좀 진행해봤습니다만, python에서 사용하기에 tutorial 내용은 너무 빈약한 것 같습니다. 

- 우선, 보통 DB에서 정의되어 있는 data model과 연동되는, schema를 따로 설계하고, 
- 이 schema에 대해서 query를 날리면 어떻게 반응할지를 설계한다. 

- 정도인 것 같은데, 좀 굴리면서 봐야할것 같은데 아무래도 내용이 너무 부족하다고 생각됩니다. 


```python 
import graphene

## Creating a basic Schema
class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, name):
        return 'Hello ' + name

schema = graphene.Schema(query=Query)

## querying 
result = schema.execute('{ hello }')
print(result.data['hello']) # "Hello stranger"
```




## wrap-up

- 저는, 이제서야 웹의 데이터를 효과적으로 관리할 수 있는 질의어가 생겼다고 생각합니다. 이제야 데이터베이스에서의 SQL이 생겨난 것이죠. 
- 다만 그것과 별개로, python에서는 GraphQL을 효과적으로 사용할 수 있도록 지원하는 도큐멘트가 너무 없는 것 같아요. 너무 없습니다. 
- 따라서 때려칩니다 하하하하핫. 

## reference

- [GraphQL in Action - REST와 이별할 때 생각해야 하는 것들](https://www.slideshare.net/Kivol/graphql-in-action-rest)
- <https://graphql.org/>
- <https://velopert.com/2318>
- <https://www.robinwieruch.de/why-graphql-advantages-disadvantages-alternatives/>
