from tree_diet_cpp import bag
from tree_diet_cpp import tree_diet as cpp_tree_diet
from graph_classes import recurse_print

def tree_diet(R, adj, target_width, important_edges, tags=None):

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
