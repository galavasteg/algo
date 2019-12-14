"""
TODO: EN doc
"""


class Vertex:
    """Каждая вершина будет экземпляром класса Vertex, хранящим
    некоторое абстрактное значение."""

    def __init__(self, val):
        self.Value = val


class SimpleGraph:

    def __init__(self, size: int):
        """Каждая вершина однозначно идентифицируется своим индексом в
        списке vertex, который (индекс) также определяет связи через
        матрицу смежности."""
        self.max_vertex = size
        # матрица смежности, где 0 означает отсутствие
        # ребра между i-й вершиной (первое измерение) и j-й вершиной
        # (второе измерение), а 1 означает наличие ребра;
        self.m_adjacency = [[0] * size for _ in range(size)]
        # список vertex, хранящий вершины.
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

    def AddVertex(self, v: int):
        """добавление новой вершины, которая ни с какими другими
        вершинами не связана; получает параметром целое число,
        которое внутри метода надо преобразовать в объект типа
        Vertex. (тест: вершина имеется, связи с ней отсутствуют);"""
        i = self._get_free_vertex_ind()
        if None.__ne__(i):
            new_vertex = Vertex(val=v)
            self.vertex[i] = new_vertex

    # здесь и далее, параметры v -- индекс вершины в списке vertex
    def RemoveVertex(self, v: int):
        """удаление вершины со всеми её рёбрами, получает индекс
        удаляемой вершины. (тест: до удаления
        некоторые вершины имеют связи с удаляемой вершиной, после
        удаления этих связей нету)."""
        pass

    def IsEdge(self, v1: int, v2: int) -> bool:
        """проверка наличия ребра между вершинами;"""
        return False

    def AddEdge(self, v1: int, v2: int):
        """добавление ребра между двумя заданными вершинами (тест:
        до добавления связи между вершинами не было, после
        добавления появилась);"""
        pass

    def RemoveEdge(self, v1: int, v2: int):
        """удаление ребра между двумя заданными вершинами (тест:
        до удаления связь между вершинами была, после удаления
        отсутствует);"""
        pass

