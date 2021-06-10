---
title: c - data structure - graph 
category: c_programming 
tags: c_programming c datastructure graph c
---

## C - Data Structure - Graph 

- 간단하게, c로 Graph를 구현해봤습니다. Adjancency Matrix를 사용해서 구현하였습니다.
- 다만, adjancency matrix의 특성상 node size가 커질수록 낭비되는 메모리의 양이 많다는 것이 문제죠. 이걸 해결하려면, linked list로 처리해주면 됩니다만, 그렇게 처리할 경우에는, edge 존재하는지 파악하기 어려워진다는 단점이 있긴 하죠.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct NODE {
    int exist;
    int value;
} NODE;

typedef struct GRAPH {
    NODE* nodes;
    int max_node_size;
    int** edges;
} GRAPH;

GRAPH* init_graph(int max_node_size) {
    GRAPH* temp_graph = (GRAPH*) malloc(sizeof(GRAPH) * 1);
    temp_graph->max_node_size = max_node_size;
    // set node 
    temp_graph->nodes = (NODE*) malloc(sizeof(NODE) * max_node_size);
    for (int i=0; i < max_node_size; i++) {
        temp_graph->nodes[i].exist = 0;
    }
    // set edges
    temp_graph->edges = (int**) malloc(sizeof(int*) * max_node_size);
    for (int i=0; i < max_node_size; i++) {
        temp_graph->edges[i] = (int*) malloc(sizeof(int) * max_node_size);
    }
    for (int i=0; i < max_node_size; i++) {
        for (int j=0; j < max_node_size; j++) {
            temp_graph->edges[i][j] = 0;
        }
    }
    return temp_graph;
}

int copy_graph(GRAPH* src_graph, GRAPH* dest_graph) {
    // copy node
    if (src_graph->max_node_size > dest_graph->max_node_size) {
        printf("dest_graph node size is smaller than src_graph\n");
        return 0;
    } else {
        // set dest_graph node blank
        for (int i=0; i < dest_graph->max_node_size; i++) {
            dest_graph->nodes[i].exist = 0;
        }
        // set dest_graph edges blank
        for (int i=0; i < dest_graph->max_node_size; i++) {
            for (int j=0; j < dest_graph->max_node_size; j++) {
                dest_graph->edges[i][j] = 0;
            }
        }
        // copy nodes
        for (int i=0; i < src_graph->max_node_size;i++) {
            if (src_graph->nodes[i].exist == 1) {
                dest_graph->nodes[i].exist = 1;
                dest_graph->nodes[i].value = src_graph->nodes[i].value;
            }
        } 
        // copy edges
        for(int i=0; i < src_graph->max_node_size; i++) {
            for (int j=0; j < src_graph->max_node_size; j++) {
                dest_graph->edges[i][j] = src_graph->edges[i][j];
            }
        }
        return 1;
    }
}
GRAPH* expand_copy_graph(GRAPH* src_graph) {
    GRAPH* r_graph = init_graph(src_graph->max_node_size * 2);
    copy_graph(src_graph, r_graph);
    return r_graph;
}

void add_node(GRAPH* graph, int nid, int value) {
    // nid에 위치한 node에 value를 집어넣음.
    if (graph->nodes[nid].exist == 1) {
        printf("node %d already exist \n", nid);
    } else {
        graph->nodes[nid].value = value;
        graph->nodes[nid].exist = 1;
    }
}
void delete_node(GRAPH* graph, int nid) {
    graph->nodes[nid].exist = 0;
    for (int i=0; i < graph->max_node_size; i++) {
        graph->edges[nid][i] = 0; 
    }
    for (int i=0; i < graph->max_node_size; i++) {
        graph->edges[i][nid] = 0; 
    }
}

void add_edge(GRAPH* graph, int nid1, int nid2) {
    NODE* node1 = &graph->nodes[nid1];
    NODE* node2 = &graph->nodes[nid2];

    if (node1->exist != 0) {
        if (node2->exist != 0) {
            // both nodes exist
            graph->edges[nid1][nid2] = 1;
            graph->edges[nid2][nid1] = 1;
        } else {
            // node 2 not exist;
            printf("node 2 not exist \n");
        }
    } else {
        if (node2->exist != 0) {
            // node 1 not exist
            printf("node 1 not exist \n");
        } else {
            // botth not exist
            printf("both node not exist \n");
        }
    }
}
void delete_edge(GRAPH* graph, int n1, int n2) {
    printf("== delete edge %d to %d \n", n1, n2);
    graph->edges[n1][n2] = 0;
    graph->edges[n2][n1] = 0;
}

void print_neighbor(GRAPH* graph, int nid) {
    printf("== neighbors: ");
    for (int i=0; i < graph->max_node_size; i++) {
        if (graph->edges[nid][i] == 1) {
            printf("%d ", i);
        }
    }
    printf("\n");
}
void print_nodes(GRAPH* graph) {
    for (int i=0; i < graph->max_node_size; i++) {
        if (graph->nodes[i].exist != 0) {
            printf("node %d exist, value: %d \n", i, graph->nodes[i].value);
        }
    }
}
void print_edges(GRAPH* graph) {
    for (int i=0; i < graph->max_node_size; i++) {
        for (int j = i + 1; j < graph->max_node_size; j++) {
            if (graph->edges[i][j] != 0) {
                printf("edge - node %d to node %d \n", i, j);
            }
        }
    }
}

int main(void) {
    GRAPH* graph = init_graph(2);
    add_node(graph, 0, 1);
    add_node(graph, 1, 3);
    graph = expand_copy_graph(graph);
    print_nodes(graph);
    add_edge(graph, 0, 1);
    print_edges(graph);

    return 0;
}
```
