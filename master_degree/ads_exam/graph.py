import heapq
from collections import defaultdict


def build_graph(cities, roads):
    """
    Строит неориентированный граф:
    graph[id] = [(neighbor_id, distance, time, cost), ...]
    а также отображение имя_города -> id.
    """
    graph = defaultdict(list)
    city_ids = {name: id for id, name in cities.items()}

    # т.к. дороги двусторонние, добавляем две записи с противоположным начало и концом дороги
    for id1, id2, distance, time, cost in roads:
        graph[id1].append((id2, distance, time, cost))
        graph[id2].append((id1, distance, time, cost))

    return graph, city_ids


def dikstra(graph, start, end, weight_index):
    """
    Классический алгоритм Дейкстры по одному критерию.

    weight_index:
    - 0: использовать длину
    - 1: использовать время
    - 2: использовать стоимость

    Возвращает:
    - path: список ID вершин от start до end
    - total_weight: суммарный вес по выбранному критерию
    или (None, None), если пути нет.
    """
    queue = [(0, start)]
    dist = {start: 0}
    parent = {start: None}

    while queue:
        vertex_cost, vertex = heapq.heappop(queue)
        if vertex == end:
            break
        if vertex_cost > dist.get(vertex, float("inf")):
            continue

        for to, distance, time, cost in graph[vertex]:
            weight = [distance, time, cost][weight_index]
            new_cost = vertex_cost + weight
            if new_cost < dist.get(to, float("inf")):
                dist[to] = new_cost
                parent[to] = vertex
                heapq.heappush(queue, (new_cost, to))

    if end not in dist:
        return None, None

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent.get(current)
    path.reverse()

    return path, dist[end]
