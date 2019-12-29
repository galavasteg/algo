"""
TODO: EN doc
"""


class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False


class SimpleGraph:

    class PathStack(list):
        def pop(self, i=-1):
            if self:
                return super().pop(i)

        def push(self, vertex: Vertex):
            vertex.Hit = True
            self.append(vertex)

        def peek(self):
            if self:
                return self[-1]

    def _all_vertices_iter(self):
        for v in filter(None.__ne__, self.vertex):
            yield v

    def _get_free_vertex_ind(self):
        i = next((i for i, v in enumerate(self.vertex)
                  if v is None), None)
        return i

    def _is_vertex(self, i: int) -> bool:
        """
        :param i: index of self.vertex list
        """
        return i < self.max_vertex and None.__ne__(self.vertex[i])

    def _related_vertices_ind_iter(self, vi: int):
        for i, _ in enumerate(self.m_adjacency[vi]):
            if self.IsEdge(vi, i):
                yield i

    def _unvisit_all_vertices(self):
        for v in self._all_vertices_iter():
            v.Hit = False

    def __init__(self, size: int):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None, ] * size

    def VerticesCount(self):
        return len(tuple(self._all_vertices_iter()))

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

    def DepthFirstSearch(self, VFrom: int, VTo: int) -> list:
        """
        0) Очищаем все дополнительные структуры данных:
        делаем стек пустым, а всем вершинам графа ставим
        Hit = False.
        1) Выбираем текущую вершину X. Для начала работы
        это будет исходная вершина VFrom.
        2) X.Hit = True.
        3) Помещаем вершину X в стек.
        4) Ищем среди смежных вершин вершины X целевую
        вершину VTo. Если она найдена, записываем её в стек
        и возвращаем сам стек. Иначе, выбираем среди
        смежных вершин любую с Hit==False. Если такая вершина
        найдена, делаем её текущей X и переходим к п. 2.
        5) Если непосещённых смежных вершин более нету,
        удаляем из стека верхний элемент. Если стек пуст,
        то прекращаем работу и информируем, что путь не
        найден. Иначе, делаем текущей вершиной
        X верхний элемент стека, ставим X.Hit == True,
        и после чего переходим к п. 4.
        """
        if not (0 <= VFrom < self.max_vertex
                and 0 <= VTo < self.max_vertex):
            return []

        A, B = self.vertex[VFrom], self.vertex[VTo]
        if A is None or B is None:
            return []

        # step 0
        path_stack = self.PathStack()
        self._unvisit_all_vertices()

        return list(path_stack)

