from random import shuffle, randint

from graph_20_22.graph import SimpleGraph, Vertex


Vertex.__repr__ = lambda v: 'V %s hit %d' % (
        v.Value, v.Hit)
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


def test_remove_vertex():
    g = SimpleGraph(5)
    for val in range(3):
        g.AddVertex(val)
    for i in range(3):
        g.AddEdge(0, i)
    g.AddEdge(1, 2)

    assert g.VerticesCount() == 3
    assert g.m_adjacency[0] == [1, 1, 1, 0, 0]
    assert g.m_adjacency[1] == [1, 0, 1, 0, 0]
    assert g.m_adjacency[2] == [1, 1, 0, 0, 0]

    g.RemoveVertex(0)

    assert g.VerticesCount() == 2
    assert g.m_adjacency[0] == [0, 0, 0, 0, 0]
    assert g.m_adjacency[1] == [0, 0, 1, 0, 0]
    assert g.m_adjacency[2] == [0, 1, 0, 0, 0]
    for i in (3, 4,):
        assert all(map(lambda x: x == 0, g.m_adjacency[i]))


def test_fill_empty_random_graph(size: int):
    g = SimpleGraph(size)
    for val in range(g.max_vertex):
        g.AddVertex(val)
    for i in range(g.max_vertex):
        g.AddEdge(i, randint(0, size-1))
    for i in range(g.max_vertex):
        g.RemoveVertex(i)

    for i in range(g.max_vertex):
        assert all(map(lambda x: x == 0, g.m_adjacency[i]))


def test_dfs():
    g = SimpleGraph(0)
    for val in range(g.max_vertex):
        g.AddVertex(val)
    path = g.DepthFirstSearch(1, 0)
    assert path == []

    g = SimpleGraph(10)
    for val in range(5):
        g.AddVertex(val)

    g.AddEdge(0, 1)
    g.AddEdge(1, 2)
    g.AddEdge(2, 3)
    g.AddEdge(3, 4)
    path = g.DepthFirstSearch(1, 0)
    assert path == [
            g.vertex[1], g.vertex[0],
        ]

    path = g.DepthFirstSearch(1, 3)
    assert path == [
            g.vertex[1], g.vertex[2], g.vertex[3],
        ]

    g.AddVertex(5)
    g.AddEdge(2, 5)
    path = g.DepthFirstSearch(4, 5)
    assert path == [
            g.vertex[4], g.vertex[3], g.vertex[2], g.vertex[5],
        ]

    g.AddVertex(6)
    g.AddEdge(5, 6)
    g.AddVertex(7)
    g.AddEdge(6, 7)
    g.AddEdge(4, 7)
    path = g.DepthFirstSearch(4, 7)
    assert path == [
            g.vertex[4], g.vertex[7],
        ]

    path = g.DepthFirstSearch(1, 7)
    assert path == [
            g.vertex[1], g.vertex[2], g.vertex[3],
            g.vertex[4], g.vertex[7],
        ]

    g.AddEdge(6, 6)
    path = g.DepthFirstSearch(6, 6)
    assert path == [
            g.vertex[6], g.vertex[6],
        ]

    g.AddEdge(3, 3)
    path = g.DepthFirstSearch(2, 4)
    assert path == [
            g.vertex[2], g.vertex[3], g.vertex[4],
        ]


# --------------------------- MAIN ----------------------------------

if __name__ == '__main__':
    test_add_vertex()
    test_edge()
    test_remove_vertex()

    test_dfs()

    for s in 5, 32, 100, 1000:
        test_fill_empty_random_graph(s)
