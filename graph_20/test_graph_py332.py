from graph_20.graph import SimpleGraph


SimpleGraph.__repr__ = lambda x: 'G %s/%s' % (
    x.VerticesCount(), x.max_vertex)


# --------------------------- TESTS ---------------------------------

def test_add_vertex():
    g = SimpleGraph(0)
    assert g.max_vertex == 0
    g.AddVertex(1)
    assert g.VerticesCount() == 0
    assert g.vertex == []
    for i in range(g.max_vertex):
        assert all(map(lambda x: x == 0, g.m_adjacency[i]))

    g = SimpleGraph(3)
    assert g.max_vertex == 3
    g.AddVertex(1)
    assert g.VerticesCount() == 1
    assert g.vertex[0].Value == 1
    for i in range(g.max_vertex):
        assert all(map(lambda x: x == 0, g.m_adjacency[i]))


# --------------------------- MAIN ----------------------------------


