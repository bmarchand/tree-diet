from tree_diet_cpp import bag
from tree_diet_cpp import tree_diet as cpp_tree_diet
from graph_classes import recurse_print

def tree_diet(R, adj, target_width, important_edges, tags=None):
    """
    Main function for eponym method.

    :param R: Python Bag instance, root of the input tree decomposition. It needs to be **empty**. 
    :type R: Bag
    :param adj: Adjacency dictionary of input graph. Keys are vertices and values lists of neighbors.
    :type adj: **dict**
    :param target_width: Target width value.
    :type target_width: **int** 
    :param important_edges: List of edges that the algorithm will try to keep in priority. Within the dynamic programming scheme, their deletion will have a large (~infinite) negative impact on the cost function, so keeping them, if possible given the width constraint, is highly favored.
    :type important_edges: **list**
    ...
    ...
    :return: **(OPT, real_edges)** : A **tuple** consisting of the optimal number of realizable edges given the target width constraint (OPT), and a list of realizable edges of length OPT.
    :rtype: **tuple**
    """

    cpp_R = py2cpp(R, tags=tags)

    print("cpp tree")
    recurse_print(cpp_R[R], 0)
    print("cpp tree end ")

    result = cpp_tree_diet(cpp_R[R], adj, target_width, important_edges)

    return result

def py2cpp(R, tags=None):

    if not tags:
        number = 0

    queue = [R]

    cpp_equiv = {}

    while len(queue)>0:

        u = queue.pop()

        if not tags:
            cpp_u = bag(u.vertices, number)
            number += 1
        else:
            cpp_u = bag(u.vertices, tags[u])

        cpp_equiv[u] = cpp_u
    
        for c in u.children:
            queue.append(c)

    queue = [R]

    while len(queue) > 0:

        u = queue.pop()

        for c in u.children:

            cpp_equiv[u].add_child(cpp_equiv[c])

            queue.append(c)

    return cpp_equiv
