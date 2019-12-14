from graph_20.graph import SimpleGraph


SimpleGraph.__repr__ = lambda x: 'G %s/%s' % (
    x.VerticesCount(), x.max_vertex)


# --------------------------- TESTS ---------------------------------


# --------------------------- MAIN ----------------------------------


