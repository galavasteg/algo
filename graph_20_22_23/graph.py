"""
TODO: EN doc
"""


class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False


class SimpleGraph:

    class __PathStack(list):
        def pop(self, i=-1):
            if self:
                return super().pop(i)

        def push(self, vertex: Vertex):
            self.append(vertex)

        def peek(self):
            if self:
                return self[-1]

    class __PathQueue(list):
        def enqueue(self, vertex: Vertex):
            self.append(vertex)

        def dequeue(self):
            if self:
                return self.pop(0)

    def _all_vertices_iter(self):
        for v in filter(None.__ne__, self.vertex):
            yield v

    def _iter_vertex_indices(self):
        for i, _ in filter(lambda i_v: None.__ne__(i_v[1]),
                           enumerate(self.vertex)):
            yield i

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

    def _is_strong_vertex(self, vi: int) -> bool:
        import itertools
        related_vis = tuple(self._iter_related_vertices_ind(vi))
        check_related_pairs = tuple(
                itertools.permutations(related_vis, 2))
        is_strong = any(map(lambda vis: self.IsEdge(*vis),
                            check_related_pairs))
        return is_strong

    def _is_weak_vertex(self, vi: int) -> bool:
        is_strong = self._is_strong_vertex(vi)
        is_weak = not is_strong
        return is_weak

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
        """TODO: EN doc"""
        if not all(map(self._is_vertex, (VFrom, VTo,))):
            return []

        A, B = self.vertex[VFrom], self.vertex[VTo]

        # step 0
        path_stack = self.__PathStack()
        self._unvisit_all_vertices()

        # step 1
        X = A
        path_stack.push(X)
        X.Hit = True
        while X:
            # step 2
            finish_vertex = self._get_finish_related_v(X, B)
            if finish_vertex:
                path_stack.push(B)
                X.Hit = True
                X = None
            else:
                not_visited_related_v = self._get_not_visited_related_v(X)
                if not_visited_related_v:
                    X = not_visited_related_v
                    path_stack.push(X)
                    X.Hit = True
                else:
                    # step 3
                    _ = path_stack.pop()
                    X = path_stack.peek()

        return list(path_stack)

    def BreadthFirstSearch(self, VFrom: int, VTo: int) -> list:
        """TODO: EN doc"""
        if not all(map(self._is_vertex, (VFrom, VTo,))):
            return []

        A, B = self.vertex[VFrom], self.vertex[VTo]

        # step 0
        related_vertex_queue = self.__PathQueue()
        waypoints_stack = self.__PathStack()
        finish_vertex = None
        self._unvisit_all_vertices()

        # step 1
        X = A
        X.Hit = True
        while X:
            # step 2
            finish_vertex = self._get_finish_related_v(X, B)
            if finish_vertex:
                X = None
            else:
                not_visited_related_v = self._get_not_visited_related_v(X)
                if not_visited_related_v:
                    # step 3
                    not_visited_related_v.Hit = True
                    related_vertex_queue.enqueue(not_visited_related_v)
                else:
                    X = related_vertex_queue.dequeue()
                    if X:
                        # TODO: reduce algorithm complexity
                        Xi = self._get_vertex_ind(X)
                        path_to_X = self.__PathStack(
                                self.BreadthFirstSearch(VFrom, Xi))
                        waypoints_stack = path_to_X[1:]

        return ([A] + list(waypoints_stack) + [B]
                if finish_vertex else [])

    def WeakVertices(self) -> list:
        weak_vis = list(filter(
                self._is_weak_vertex, self._iter_vertex_indices()))
        weak_vs = [self.vertex[vi] for vi in weak_vis]
        return weak_vs

