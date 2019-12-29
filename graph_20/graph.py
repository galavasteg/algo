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

    def _get_vertex_ind(self, v: Vertex) -> int:
        return next(filter(lambda i_v: i_v[1] is v,
                           enumerate(self.vertex)))[0]

    def _related_vertices_iter(self, v: Vertex):
        vi = self._get_vertex_ind(v)
        for i in self._related_vertices_ind_iter(vi):
            yield self.vertex[i]

    def _unvisit_all_vertices(self):
        for v in self._all_vertices_iter():
            v.Hit = False

    def _get_finish_related_v(self, v: Vertex, fin_v: Vertex):
        is_finish_v = lambda rv: rv is fin_v
        return next(filter(is_finish_v,
                           self._related_vertices_iter(v)),
                    None)

    def _get_not_visited_related_v(self, v: Vertex):
        is_not_visited_v = lambda rv: not rv.Hit
        return next(filter(is_not_visited_v,
                           self._related_vertices_iter(v)),
                    None)

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
        это будет исходная вершина VFrom. X.Hit = True,
        помещаем вершину X в стек.
        2) Ищем среди смежных вершин вершины X целевую
        вершину VTo. Если она найдена, записываем её в стек
        и возвращаем сам стек. Иначе, выбираем среди
        смежных вершин любую с Hit==False. Если такая вершина
        найдена, делаем её текущей X и переходим к п. 1.
        3) Если непосещённых смежных вершин более нету,
        удаляем из стека верхний элемент. Если стек пуст,
        то прекращаем работу и информируем, что путь не
        найден. Иначе, делаем текущей вершиной
        X верхний элемент стека, ставим X.Hit == True,
        и после чего переходим к п. 2.
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

        # step 1
        X = A
        path_stack.push(X)
        while X:
            # step 2
            finish_vertex_i = self._get_finish_related_v(X, B)
            if finish_vertex_i is not None:
                path_stack.push(B)
                X = None
            else:
                not_visited_related_v = self._get_not_visited_related_v(X)
                if not_visited_related_v is not None:
                    X = not_visited_related_v
                    path_stack.push(X)
                else:
                    # step 3
                    _ = path_stack.pop(-1)
                    X = path_stack.peek()

        return list(path_stack)

