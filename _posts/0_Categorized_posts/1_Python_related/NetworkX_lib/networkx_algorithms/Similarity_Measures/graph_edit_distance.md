

I have been conducting a experiment for computing graph similarity.  
I have a question about `nx.optimal_edit_paths(G1, G2)`.
In the [documentation of it](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.similarity.optimal_edit_paths.html), it is written that this function **Returns all minimum-cost edit paths transforming G1 to G2**. 

I use the function in my code and I run it. my code is below. 
Even though `G1` and `G2` are exactly same graph and their graph_edit_cost is 0, 
there a a lot of optimal_edit_paths. 

```python
N = 3
G1 = nx.complete_graph(N)
G2 = nx.complete_graph(N)

edit_path, graph_edit_cost = nx.optimal_edit_paths(G1, G2)
print(f"graph edit cost: {graph_edit_cost}")
for p in edit_path:
    node_edit, edge_edit = p
    print(f"node_edit: {node_edit}")
    print(f"edge_edit: {edge_edit}")
    print("--"*30)
```

the output is below. 
As I said it before, graph_edit_cost is zero because `G1` and `G2` are exactly same graphs. 
but there are lots of optimal path when paths was derived by `nx.optimal_edit_paths(G1, G2)`. 
I don't know why this happend. It doesn't look like 'optimal' because they don't have same edit cost. 

```
graph edit cost: 0.0
node_edit: [(0, 0), (1, 1), (2, 2)]
edge_edit: [((0, 1), (0, 1)), ((0, 2), (0, 2)), ((1, 2), (1, 2))]
------------------------------------------------------------
node_edit: [(0, 0), (2, 1), (1, 2)]
edge_edit: [((0, 2), (0, 1)), ((0, 1), (0, 2)), ((1, 2), (1, 2))]
------------------------------------------------------------
node_edit: [(1, 0), (0, 1), (2, 2)]
edge_edit: [((0, 1), (0, 1)), ((0, 2), (1, 2)), ((1, 2), (0, 2))]
------------------------------------------------------------
node_edit: [(1, 0), (2, 1), (0, 2)]
edge_edit: [((1, 2), (0, 1)), ((0, 1), (0, 2)), ((0, 2), (1, 2))]
------------------------------------------------------------
node_edit: [(2, 0), (0, 1), (1, 2)]
edge_edit: [((0, 2), (0, 1)), ((0, 1), (1, 2)), ((1, 2), (0, 2))]
------------------------------------------------------------
node_edit: [(2, 0), (1, 1), (0, 2)]
edge_edit: [((1, 2), (0, 1)), ((0, 1), (1, 2)), ((0, 2), (0, 2))]
------------------------------------------------------------
```

And also, if the function is correct, How can I transform `G1` to `G2` base on that operations(node_edit, edge_edit)? I don't know how those operations have to be applied to `G2` to make `G2`. 


I always appreciate your help in this library. 
becasue of that, I've learned a lot about network science. 

If you feel my text is rude or not polite, it is because of my lack of english. 
sorry about that. 