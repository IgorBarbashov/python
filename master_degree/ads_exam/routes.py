def select_route(routes, oder):
    """
    Выбор маршрута по приоритетам.

    routes: dict['ДЛИНА'/'ВРЕМЯ'/'СТОИМОСТЬ'] = (city_names, distance, time, cost)
    oder: list['Д','С','В'].
    order_indexes: вспомогательная структура, обозначающая индексы приоритетов в кортеже (names, distance, time, cost)

    Возвращает (route_key, city_names, distance, time, cost).
    """
    order_indexes = {"Д": 1, "В": 2, "С": 3}

    key, (city_names, distance, time, cost) = sorted(
        routes.items(),
        key=lambda item: (
            item[1][order_indexes[oder[0]]],
            item[1][order_indexes[oder[1]]],
            item[1][order_indexes[oder[2]]],
        ),
    )[0]

    return key, city_names, distance, time, cost


def calculate_route_total_weights(graph, route, cities):
    """
    Считает для маршрута суммарные длину, время, стоимость.
    Возвращает (city_names, total_distance, total_time, total_cost)
    """
    total_distance = 0
    total_time = 0
    total_cost = 0

    for i in range(len(route) - 1):
        current = route[i]
        next = route[i + 1]

        for neighbor, distance, time, cost in graph[current]:
            # Ищем ребро current -> next в списке смежности
            if neighbor == next:
                total_distance += distance
                total_time += time
                total_cost += cost
                break

    city_names = [cities[city_id] for city_id in route]
    return city_names, total_distance, total_time, total_cost
