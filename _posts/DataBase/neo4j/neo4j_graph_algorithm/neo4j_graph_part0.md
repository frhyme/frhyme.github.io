---
title: neo4j - graph algorithm - part 0
category: others
tags: database graphdb neo4j 
---

## intro.

- [neo4j - Applied Graph Algorithm course](https://neo4j.com/graphacademy/online-training/applied-graph-algorithms/part-0/)에 작성된 내용을 공부하며 정리하였습니다.

## neo4j - Applied Graph Algorithm course

- Graph Algorithm은 그래프, 노드, 관계(Relationship, edge) 등을 위한 다양한 지표(metric)들을 계산하기 위해서 사용됩니다. 이들은 Centrality, ranking등의 관점에서 그래프에 대한 insight를 제공하거나, community와 같이 그래프에 내재된 구조들을 community-detection, graph-partitioning, clustering 등을 통해서 도출할 수 있도록 해줍니다.
- 이 코스에서는, neo4j에서 Graph Algorithm을 사용하여, 어떻게 그래프 기반의 어플리케이션을 만들 수 있는지에 대해서 배울 수 있습니다.
- 이를 위해, 여기서는 이미 존재하는 웹 어플리케이션으로부터 시작합니다. 이 어플리케이션은 Reacj.js로 반들어진 business reveiw 웹사이트이며, Yelp에서 공개한 데이터로부터 확장되어 사용됩니다. 즉, 우리는 Neo4j를 사용해서 기존 웹 어플리케이션이 얼마나 더 강화될 수 있는지를 작업하게 됩니다.
- 또한, 만약 웹어플리케이션과 React에 대해서 친숙하지 않더라도 상관없습니다.

## Course Outline

### Setup And Cypher Refresher

- Review of the dataset used in this course.
- Accessing the Yelp Neo4j Sandbox.
- Overview of the CodeSandbox React application used in the course.
- Connecting the React application to your Neo4j Sandbox instance.
Verifying configuration and querying the dataset.
Estimated time: 15 minutes

### Category Hierarchy
Learn about the Overlap Similarity algorithm and how to use it in Neo4j to build a hierarchy of categories.
Enhance our business reviews application using Overlap Similarity to improve business search.
Estimated time: 30 minutes

### Ordering Search Results
Learn about Similarity algorithms in Neo4j.
Use Pearson Similarity to improve search result ordering in our business reviews application.
Estimated time: 30 minutes

### Most Relevant Reviews
Learn about PageRank and Personalized PageRank.
Use Personalized PageRank to find more relevant business reviews for users.
Estimated time: 30 minutes

### Photo Recommendations
Learn more about Similarity algorithms in Neo4j.
Learn about Community Detection and the Label Propagation algorithm.
Use Jaccard Similarity and Label Propagation to build a photo based business recommendation feature.
Estimated time: 30 minutes

### Summary
Quiz results.
Review of graph algorithms in Neo4j.
Overview of resources for learning more and doing more with Graph Algorithms in Neo4j.
Estimated time: 10 minutes

Prerequisites
This course focuses on using graph algorithms with Neo4j in an applied environment to enhance functionality of an application. To be successful you should:

Have completed Introduction to Neo4j course or have equal Cypher proficiency.
Be familiar with Neo4j Browser.
Be familiar with the concepts of a web application.
