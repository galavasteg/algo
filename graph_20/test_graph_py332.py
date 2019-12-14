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


def test_edge():
    # add edge
    g = SimpleGraph(3)
    for i in range(g.max_vertex):
        assert all(map(lambda x: x == 0, g.m_adjacency[i]))
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddEdge(0, 1)
    assert g.m_adjacency[0][1] == g.m_adjacency[1][0] == 1
    assert all(map(lambda x: x == 0, g.m_adjacency[2]))
    assert g.IsEdge(0, 1) and g.IsEdge(1, 0)
    assert not g.IsEdge(0, 2) and not g.IsEdge(2, 0)
    assert not g.IsEdge(1, 2) and not g.IsEdge(2, 1)
    assert not g.IsEdge(1, 1000)

    # not add
    g.AddEdge(0, 2)
    assert all(map(lambda x: x == 0, g.m_adjacency[2]))
    g.AddEdge(0, 1000)
    assert all(map(lambda x: x == 0, g.m_adjacency[2]))

    # remove edge
    g.RemoveEdge(0, 1)
    for i in range(g.max_vertex):
        assert all(map(lambda x: x == 0, g.m_adjacency[i]))

    # TODO: lots of vertices test
    g = SimpleGraph(999)
    for i in range(g.max_vertex):
        assert all(map(lambda x: x == 0, g.m_adjacency[i]))
    g.AddVertex(15)
    g.AddVertex(2000)
    g.AddEdge(0, 1)
    assert g.m_adjacency[0][1] == g.m_adjacency[1][0] == 1
    assert all(map(lambda x: x == 0, g.m_adjacency[2]))
    g.RemoveEdge(1, 0)
    for i in range(g.max_vertex):
        assert all(map(lambda x: x == 0, g.m_adjacency[i]))


# --------------------------- MAIN ----------------------------------

if __name__ == '__main__':
    test_add_vertex()
    test_edge()

