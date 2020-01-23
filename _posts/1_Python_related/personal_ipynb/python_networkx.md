<!-- $theme: gaia -->


## Gong4py  - pandas  
## ==+ NetworkX==
## ==+ matplotlib.pyplot==

##### created by [seunghoon lee](frhyme@postech.ac.kr)
---
<!-- page_number: true -->
# What is ==NetworkX==?

<br>
<br>

> NetworkX is a Python language software package for the **creation, manipulation, and study of the structure, dynamics, and function of complex networks**.

---
# What is network

</br>

## **Network**
### = ==**Nodes**==<small>(+node attribute)</small> 
### \+ ==**edges**==<small>(+edge attribute)</small>

---
# What is network in ==python== 

<small>

**==node==**
A node can be any hashable Python object except None.

**==node attribute==**
<span style="background-color:yellow;">G.node[n] attribute dictionary</span> for the specified node n.

**==edge==**
Edges are either two-tuples of nodes (u,v) or three tuples of nodes with an edge attribute dictionary (u,v,dict).

**==edge attribute==** 
<span style="background-color:yellow;">G.edge[u][v] attribute dictionary</span> for the specified edge u-v.

</small>

---
# 4 Graph python classes 
<small> 

==**Graph**== :arrow_right: `G=nx.Graph()`
This class implements an <span style="background-color:yellow;">undirected graph</span>. 
It <span style="background-color:yellow;">ignores multiple edges</span> between two nodes. 
It does <span style="background-color:yellow;">allow self-loop edges</span> between a node and itself.

==**DiGraph**== :arrow_right: `G=nx.DiGraph()`
<span style="background-color:yellow;">Directed graphs</span>, that is, graphs with directed edges. Operations common to directed graphs, (a subclass of Graph).

==**MultiGraph**== :arrow_right: `G=nx.MultiGraph()`
A flexible graph class that <span style="background-color:yellow;">allows multiple undirected edges </span>between pairs of nodes. 

==**MultiGraph**== :arrow_right: `G=nx.MultiDiGraph()`
A directed version of a MultiGraph.

</small> 

---
# Nodes and Edges insertion
```python
import networkx as nx 
G=nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from( [(1,2), (2,3)] )
```

`add_edges_from` 를 사용할 때, `nx.Graph()`에 node가 없을 경우 node를 자동으로 만들어주기 때문에, `add_nodes_from`을 사용하지 않고, `add_edges_from`만 사용해도 됨


```python
G.add_path([1, 2, 3, 4])
```
<small> 
edges (1, 2), (2, 3), (3, 4)를 graph에 insertion
</small>

---
# Weighted Edges insertion 
```python
WG1=nx.Graph()#weighted undirected graph 
WG1.add_weighted_edges_from(
[(1,2,0.125),(1,3,0.75),(2,4,1.2),(3,4,0.375)])
WG2=nx.Graph()
WG2.add_edges_from([
(1,2,{'weight':0.125}), (1,3,{'weight':0.75}), 
(2, 4,{'weight':1.2}), (3, 4, {'weight':0.375}) ])
```

1) `add_weighted_edges_from` with ==(u, v, weight)==
2) `add_edges_from` with ==(u, v, attr_dict)==
> <small> attr_dict에는 weight이외에도 다양한 attribute가 포함될 수 있음</small>
---

# Nodes and Edges removal

```python
G.remove_nodes_from([1, 2])
G.remove_edges_from([(2, 3)])
```
>node를 없애면 node가 속한 edge들도 함께 없어짐
```python
G.clear() #same as G=nx.Graph()
```
모든 node와 edge 삭제

---

---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
# reference 
[NetworkX Documentation](https://networkx.readthedocs.io/en/stable/overview.html#what-next)

---


> In Greek mythology, **Gaia** also spelled **Gaea**, was the personification of the Earth and one of the Greek primordial deities.
>
> <small>-- *[Gaia (mythology) - Wikpedia, the free encyclopedia](https://en.wikipedia.org/wiki/Gaia_%28mythology%29)*</small>

---
<!-- page_number: true -->

# Overview

**Gaia** is the beautiful presentation theme on Marp!

- ==**New features**==
	1. Title Slides
	2. Highlight
	3. Color scheme

---

# How to use

#### From menu

Select menu: *View :arrow_right: Theme :arrow_right: Gaia*

#### Use directive

Set `gaia` theme by `$theme` Global Directive.

```
<!-- $theme: gaia -->
```

---

# Basic example 1

**Lorem ipsum** dolor *sit* amet, ***consectetur*** adipiscing elit, sed do `eiusmod` tempor ==incididunt== ut labore et dolore ~~magna aliqua~~. :smile:

> Stay Hungry. Stay Foolish. <small>_--Steve Jobs (2005)_</small>

- List A
	1. [Sub list](https://yhatt.github.io/marp/)
	1. Sub list
		- _More Sub list_

---

# Basic example 2

```javascript
document.write('Hello, world!');
```

|table|layout|example|
|:--|:-:|--:|
|align to left|align to center|align to right|
|:arrow_left: left|:arrow_left: center :arrow_right:|right :arrow_right:

![70% center](./images/marp.png)

---
<!-- *template: gaia -->

## Introduce new features!!

# ==1.== Title Slides

---

# ==e.g.== This page :yum:

---

## ==Apply centering== to the page<br />that has only headings!

##### Useful to title slide. :laughing:

---

> **==Tips:==**
> Apply vertical centering to quote only page too.

---
<!-- *template: gaia -->

# ==2.== Highlight

---
## Highlight Markup

You can use `==` for ==highlighting blue==.

```markdown
==This is highlight markup.==
```

#### Notice

*Marp would show <span style="background-color:yellow;">yellow marker highlight</span> in Markdown view or default slide theme.*

---
<!-- *template: gaia -->

# ==3.== Color scheme templates
---
# ==Color== scheme templates

Change color scheme *by `template` page directive.*

```
<!-- template: default -->
```

- **Default** :arrow_left: This page
- Invert
- Gaia (Theme color)

---
<!-- *template: invert -->
# ==Color== scheme templates

Change color scheme *by `template` page directive.*

```
<!-- template: invert -->
```

- Default
- **Invert** :arrow_left: This page
- Gaia (Theme color)

---
<!-- *template: gaia -->
# ==Color== scheme templates

Change color scheme *by `template` page directive.*

```
<!-- template: gaia -->
```

- Default
- Invert
- **Gaia** (Theme color) :arrow_left: This page

---
<!-- *template: invert -->

# Templates can use<br />to ==per pages==!

##### with using temporally page directive `<!-- *template: invert -->`

---
<!-- template: gaia -->

# ==That's all!==

## Let's create beautiful slides<br />with ==Marp== + ==Gaia== theme!

---

#### `<!-- $theme: gaia -->` of Marp

###### [![](./images/marp.png)](https://yhatt.github.io/marp)

#### https://yhatt.github.io/marp
