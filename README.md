# tree-diet

Implementation of the tree diet algorithm, reducing the treewidth of a graph through min cardinality edge deletion.
Code used for numerical experiments in companion paper: https://hal.inria.fr/hal-03206132/.
Source code documentation available at: https://bmarchand-perso.gitlab.io/tree-diet/.

## Installation
The package is on pypi: https://pypi.org/project/treediet/0.1.0/
```
pip install treediet
```

## Usage

```python
    from treediet.graph_classes import Graph, Bag
    from treediet.tree_diet import tree_diet
   
    # Graph Definition
    G = Graph()
 
    for i in range(5):
        G.add_vertex(i)
 14 
 15     G.add_edge(0,1)
 16     G.add_edge(0,2)
 17     G.add_edge(0,3)
 18 
 19     G.add_edge(1,2)
 20     G.add_edge(1,3)
 21 
 22     G.add_edge(2,3)
 23 
 24     G.add_edge(1,4)
 25     G.add_edge(2,4)
 26     G.add_edge(3,4)
 27 
 28     # Tree Decomposition construction
 29     R = Bag([])
 30 
 31     B1 = Bag([0])
 32     B2 = Bag([0,1])
 33     B3 = Bag([0,1,2])
 34     B4 = Bag([0,1,2,3])
 35     B5 = Bag([1,2,3,4])
 36 
 37     R.add_child(B1)
 38     B1.add_child(B2)
 39     B2.add_child(B3)
 40     B3.add_child(B4)
 41     B4.add_child(B5)
 42 
 43     # Calling Dynamic Programming tree-diet algorithm
 44     OPT, real_edges, color_dictionary = tree_diet(R, G.adj, 2, [])
 45 
 46     print(OPT,real_edges, color_dictionary)
```
 
## (old) Manual install (Linux, MacOS)

Cloning:

    git clone https://gitlab.inria.fr/amibio/tree-diet.git
    cd tree-diet

Installing dependencies (pybind11, numpy, pytest) and setting up the environment:

    python3 -m pip install -r requirements.txt
    . ./setenv.sh 

Then, if you are on linux: 

    make

If you are on mac:

    make macos

Finally, in either case:

    make check

to launch the tests. If they all pass, you are good to go.

## Source code documentation

A Sphinx-based source code documentation, with minimal execution examples, is
available at: https://bmarchand-perso.gitlab.io/tree-diet/.
