from graph_pylib import Graph
from graph_cpp_routines import tree_diet, bag

def test_buggy():

    
    G = Graph(9)

    G.add_edge(1,2)
    G.add_edge(2,3)

    G.add_edge(2,5)

    R = bag([], 0)

    B1 = bag([7,8], 1)
    B2 = bag([6,7,8], 2)
    B3 = bag([4,6,7,8], 3)
    B4 = bag([3,4,6,7,8], 4)
    B5 = bag([0,3,4,6,7,8], 5)
    B6 = bag([0,3,4,5,6], 6)
    B7 = bag([0,1,2,3,5], 7)

    R.add_child(B1)
    B1.add_child(B2)
    B2.add_child(B3)
    B3.add_child(B4)
    B4.add_child(B5)
    B5.add_child(B6)
    B6.add_child(B7)

    must_have_edges = [(1,2),(2,3)]

    num_real, list_edges = tree_diet(R, G.adj, 2, must_have_edges)

    for e in must_have_edges:
        assert(e in list_edges)
   
    assert(len(list_edges)==2) 

if __name__=='__main__':
    test_buggy()
