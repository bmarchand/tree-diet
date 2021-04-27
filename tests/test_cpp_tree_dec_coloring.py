from graph_cpp_routines import optim_num_real_edges, bag, tree_diet
from graph_pylib import Graph, py_bag, py2cpp

def test_grid():

    G = Graph(9)

    G.add_edge(0,1)
    G.add_edge(1,2)

    G.add_edge(0,3)
    G.add_edge(1,4)
    G.add_edge(2,5)

    G.add_edge(3,4)
    G.add_edge(4,5)

    G.add_edge(3,6)
    G.add_edge(4,7)
    G.add_edge(5,8)

    G.add_edge(6,7)
    G.add_edge(7,8)

    R0 = bag([], 0)
    R = bag([0,1,2,3], 1)
    B1 = bag([1,2,3,4], 2)
    B2 = bag([2,3,4,5], 3)
    B3 = bag([3,4,5,6], 4)
    B4 = bag([4,5,6,7], 5)
    B5 = bag([5,6,7,8], 6)

    R0.add_child(R)
    R.add_child(B1)
    B1.add_child(B2)
    B2.add_child(B3)
    B3.add_child(B4)
    B4.add_child(B5)
    
    num_real, list_edges = tree_diet(R0, G.adj, 2, [])
    print(num_real)
    assert(num_real==10)

def test_clique():

    R = bag([], 0)

    L = bag([0,1,2,3,4], 1)

    R.add_child(L)

    G = Graph(5)

    for u in range(5):
        for v in range(5):
            G.add_edge(u,v)

    c = {}
   
     
    ans = optim_num_real_edges(R, {}, 4, c, G.adj, [],0)
    num_real = ans
    
    print("table ", c)

    assert(num_real == 10)

    num_real, list_edges = tree_diet(R, G.adj, 3, [])
    assert(num_real == 6)
    assert(num_real == len(list_edges))    

    num_real, list_edges = tree_diet(R, G.adj, 2, [])
    assert(num_real == 3)
    assert(num_real == len(list_edges))    

def test_clique_niceTD():

    R = bag([], 0)
    
    G = Graph(5)

    for u in range(5):
        for v in range(5):
            G.add_edge(u,v)

    B1 = bag([0,1,2,3,4], 1)
    B2 = bag([0,1,2,3], 2)
    B3 = bag([0,1,2], 3)
    B4 = bag([0,1], 4)
    B5 = bag([1], 5)

    R.add_child(B1)
    B1.add_child(B2)
    B2.add_child(B3)
    B3.add_child(B4)
    B4.add_child(B5)

    num_real, list_edges = tree_diet(R, G.adj, 4, [])
    assert(num_real == 10)
    assert(num_real == len(list_edges))    

    num_real, list_edges = tree_diet(R, G.adj, 3, [])
    assert(num_real == 9)
    assert(num_real == len(list_edges))    
    
    num_real, list_edges = tree_diet(R, G.adj, 2, [])
    assert(num_real == 7)
    assert(num_real == len(list_edges))    

def test_small_branching():

    G = Graph(6)

    G.add_edge(0, 1)
    G.add_edge(1, 2)
    G.add_edge(0, 3)
    G.add_edge(1, 3)
    G.add_edge(1, 4)
    G.add_edge(2, 4)
    G.add_edge(3, 4)
    G.add_edge(3, 5) 
    G.add_edge(4, 5) 

    R = bag([], 0)

    B1 = bag([1,3,4], 1)
    B2 = bag([0,1,3], 2)
    B3 = bag([1,2,4], 3)
    B4 = bag([3,4,5], 4)

    R.add_child(B1) 
    B1.add_child(B2)
    B1.add_child(B3)
    B1.add_child(B4)

    ans = tree_diet(R, G.adj, 2, [])
    print(ans)
    num_real, list_edges = ans
    assert(num_real == len(list_edges))    

    assert(num_real == 9)

def test_py2cpp():

    R = py_bag([])

    B1 = py_bag([1,3,4])
    B2 = py_bag([0,1,3])
    B3 = py_bag([1,2,4])
    B4 = py_bag([3,4,5])

    R.add_child(B1) 
    B1.add_child(B2)
    B1.add_child(B3)
    B1.add_child(B4)
   
    d = py2cpp(R) 
    new_R = d[R]

    assert(len(new_R.children)==1)
    assert(len(new_R.children[0].children)==3)

if __name__=='__main__':

    test_grid()
