import unittest
from random import randint

from graph_20_22_23_24.graph import SimpleGraph, Vertex


Vertex.__repr__ = lambda v: 'V %s hit %d' % (
        v.Value, v.Hit)
SimpleGraph.__repr__ = lambda x: 'G %s/%s' % (
        x.VerticesCount(), x.max_vertex)


# --------------------------- TESTS ---------------------------------

class AddEdgeRemoveTests(unittest.TestCase):

    def test_add_vertex(self):
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

    def test_edge(self):
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

    def test_remove_vertex(self):
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


class EmptyTests(unittest.TestCase):
    g = None

    def setUp(self) -> None:
        self.g = SimpleGraph(0)

    def test_path_search(self):
        dfs_path = self.g.DepthFirstSearch(1, 0)
        bfs_path = self.g.BreadthFirstSearch(1, 0)
        assert dfs_path == bfs_path == []

    def test_weak(self):
        weak_vs = self.g.WeakVertices()
        assert weak_vs == []


class FillAndEmptyTests(unittest.TestCase):

    def _test(self, size: int):
        g = SimpleGraph(size)
        for val in range(g.max_vertex):
            g.AddVertex(val)
        for i in range(g.max_vertex):
            g.AddEdge(i, randint(0, size-1))
        for i in range(g.max_vertex):
            g.RemoveVertex(i)

        for i in range(g.max_vertex):
            assert all(map(lambda x: x == 0, g.m_adjacency[i]))

    def test_5(self):
        self._test(5)

    def test_32(self):
        self._test(32)

    def test_100(self):
        self._test(100)

    def test_1000(self):
        self._test(1000)


class PathSearchTests(unittest.TestCase):
    g = None

    @classmethod
    def setUpClass(cls) -> None:
        """
                      ___
                      \ /
        0 -- 1 -- 2 -- 3 -- 4
                  /         /
                  5 -- 6 -- 7
                      /\
                      --
        """
        g = SimpleGraph(10)
        for val in range(5):
            g.AddVertex(val)
        g.AddEdge(0, 1)
        g.AddEdge(1, 2)
        g.AddEdge(2, 3)
        g.AddEdge(3, 4)

        g.AddVertex(5)
        g.AddEdge(2, 5)
        g.AddVertex(6)
        g.AddEdge(5, 6)
        g.AddVertex(7)
        g.AddEdge(6, 7)
        g.AddEdge(4, 7)

        g.AddEdge(3, 3)
        g.AddEdge(6, 6)
        cls.g = g

    def test_1_0(self):
        dfs_path = self.g.DepthFirstSearch(1, 0)
        bfs_path = self.g.BreadthFirstSearch(1, 0)
        assert dfs_path == bfs_path == [
                self.g.vertex[1], self.g.vertex[0],
            ]

    def test_1_3(self):
        dfs_path = self.g.DepthFirstSearch(1, 3)
        bfs_path = self.g.BreadthFirstSearch(1, 3)
        assert dfs_path == bfs_path == [
                self.g.vertex[1], self.g.vertex[2],
                self.g.vertex[3],
            ]

    def test_4_5(self):
        dfs_path = self.g.DepthFirstSearch(4, 5)
        bfs_path = self.g.BreadthFirstSearch(4, 5)
        assert dfs_path == bfs_path == [
                self.g.vertex[4], self.g.vertex[3],
                self.g.vertex[2], self.g.vertex[5],
            ]

    def test_4_7(self):
        dfs_path = self.g.BreadthFirstSearch(4, 7)
        bfs_path = self.g.BreadthFirstSearch(4, 7)
        assert dfs_path == bfs_path == [
                self.g.vertex[4], self.g.vertex[7],
            ]

    def test_1_7(self):
        dfs_path = self.g.DepthFirstSearch(1, 7)
        bfs_path = self.g.BreadthFirstSearch(1, 7)
        assert dfs_path == bfs_path == [
                self.g.vertex[1], self.g.vertex[2],
                self.g.vertex[3], self.g.vertex[4],
                self.g.vertex[7],
            ]

    def test_6_6(self):
        dfs_path = self.g.DepthFirstSearch(6, 6)
        bfs_path = self.g.BreadthFirstSearch(6, 6)
        assert dfs_path == bfs_path == [
                self.g.vertex[6], self.g.vertex[6],
            ]

    def test_2_4(self):
        dfs_path = self.g.DepthFirstSearch(2, 4)
        bfs_path = self.g.BreadthFirstSearch(2, 4)
        assert dfs_path == bfs_path == [
                self.g.vertex[2], self.g.vertex[3],
                self.g.vertex[4],
            ]

    def test_1_6(self):
        dfs_path = self.g.DepthFirstSearch(1, 6)
        assert dfs_path == [
                self.g.vertex[1], self.g.vertex[2],
                self.g.vertex[3], self.g.vertex[4],
                self.g.vertex[7], self.g.vertex[6],
            ]
        bfs_path = self.g.BreadthFirstSearch(1, 6)
        assert bfs_path == [
                self.g.vertex[1], self.g.vertex[2],
                self.g.vertex[5], self.g.vertex[6],
            ]


class AWeakVerticesTests(unittest.TestCase):
    g = None

    @classmethod
    def setUp(cls) -> None:
        """
            2 - 4
          / |   |
        0 - 3 - 5 - 7 - 8
          \ |   | /
            1   6
        """
        g = SimpleGraph(10)
        for val in range(9):
            g.AddVertex(val)
        g.AddEdge(0, 1)
        g.AddEdge(0, 2)
        g.AddEdge(0, 3)
        g.AddEdge(1, 3)
        g.AddEdge(2, 3)
        g.AddEdge(2, 4)
        g.AddEdge(3, 5)
        g.AddEdge(4, 5)
        g.AddEdge(5, 6)
        g.AddEdge(5, 7)
        g.AddEdge(6, 7)
        g.AddEdge(7, 8)
        cls.g = g

    def test_init(self):
        weak_vs = self.g.WeakVertices()
        assert weak_vs == [
                self.g.vertex[4], self.g.vertex[8],
            ]

    def test_all_strong(self):
        """
            2 - 4 - 8
          / |   | \ |
        0 - 3 - 5 - 7
          \ |   | /
            1   6
        """
        self.g.AddEdge(4, 7)
        self.g.AddEdge(4, 8)

        weak_vs = self.g.WeakVertices()
        assert weak_vs == []

    def test_strong_to_weak(self):
        """
            2 - 4
          /     |
        0 - 3 - 5 - 7 - 8
          \ |   | /
            1   6
        """
        self.test_init()

        self.g.RemoveEdge(2, 3)
        weak_vs = self.g.WeakVertices()
        assert weak_vs == [
                self.g.vertex[2], self.g.vertex[4],
                self.g.vertex[8],
            ]


# --------------------------- MAIN ----------------------------------

if __name__ == '__main__':
    unittest.main()

