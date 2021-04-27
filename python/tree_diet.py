from graph_cpp_routines import bag



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

    new_R = cpp_equiv[R]
    return cpp_equiv
