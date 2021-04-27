from graph_pylib import Graph
from graph_cpp_routines import tree_diet, bag

def test_tiny():

    
    G = Graph(4)

    G.add_edge(0,1)
    G.add_edge(1,2)
    G.add_edge(2,3)

    G.add_edge(0,2)
    G.add_edge(1,3)

    R = bag([], 0)

    B1 = bag([0], 1)
    B2 = bag([0,1], 2)
    B3 = bag([0,1,2], 3)
    B4 = bag([1,2,3], 3)

    R.add_child(B1)
    B1.add_child(B2)
    B2.add_child(B3)
    B3.add_child(B4)

    must_have_edges = [(0,1),(1,2),(2,3)]

    num_real, list_edges = tree_diet(R, G.adj, 2, must_have_edges)

    for e in must_have_edges:
        assert(e in list_edges)
   
    assert(len(list_edges)==5) 
