"""
TODO: EN doc
"""


class Vertex:

    def __init__(self, val):
        self.Value = val


class SimpleGraph:

    def __init__(self, size: int):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None, ] * size

    def VerticesCount(self):
        return sum(map(None.__ne__, self.vertex))

    def _get_free_vertex_ind(self):
        i = next((i for i, v in enumerate(self.vertex)
                  if v is None), None)
        return i

    def _is_vertex(self, i: int) -> bool:
        """
        :param i: index of self.vertex list
        """
        return i < self.max_vertex and None.__ne__(self.vertex[i])

    def _related_vertices_ind_iter(self, v: int):
        for i, _ in enumerate(self.m_adjacency[v]):
            if self.IsEdge(v, i):
                yield i

    def AddVertex(self, v: int):
        i = self._get_free_vertex_ind()
        if None.__ne__(i):
            new_vertex = Vertex(val=v)
            self.vertex[i] = new_vertex

    def RemoveVertex(self, v: int):
        if self._is_vertex(v):
            for related_v in self._related_vertices_ind_iter(v):
                self.RemoveEdge(v, related_v)
            self.vertex[v] = None

    def IsEdge(self, v1: int, v2: int) -> bool:
        return (all(map(self._is_vertex, (v1, v2,)))
                and self.m_adjacency[v1][v2] == self.m_adjacency[v2][v1] == 1)

    def AddEdge(self, v1: int, v2: int):
        if all(map(self._is_vertex, (v1, v2,))):
            self.m_adjacency[v1][v2] = self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1: int, v2: int):
        if all(map(self._is_vertex, (v1, v2,))):
            self.m_adjacency[v1][v2] = self.m_adjacency[v2][v1] = 0

