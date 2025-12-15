def add_city(cities, line):
    """
    Парсит и добавляет в список информацию по городу
    """
    city_id, city_name = line.split(": ", 1)
    cities[int(city_id)] = city_name


def add_road(roads, line):
    """
    Парсит и добавляет в список информацию по дороге
    """
    city_ids, weights = line.split(": ", 1)
    city_from_id, city_to_id = city_ids.split(" - ")
    distance, time, cost = weights.split(", ")
    roads.append(
        (
            int(city_from_id),
            int(city_to_id),
            int(distance),
            int(time),
            int(cost),
        )
    )


def add_request(requests, line):
    """
    Парсит и добавляет в список информацию по запросу
    """
    route_points, route_orders = line.split(" | ")
    city_from_name, city_to_name = route_points.split(" -> ")
    clear_route_orders = route_orders.strip()[1:-1]
    orders = [order.strip() for order in clear_route_orders.split(",")]
    requests.append((city_from_name, city_to_name, orders))


def read_input(filename: str):
    """
    Читает данные из файла input.txt и возвращает:
    - cities: dict[id -> name]
    - roads: список (id1, id2, distance, time, cost)
    - requests: список (city_from_name, city_to_name, orders)
    """
    cities = {}
    roads = []
    requests = []

    sections = ["[CITIES]", "[ROADS]", "[REQUESTS]"]
    section = None

    config = {
        "[CITIES]": {"data": cities, "modifier": add_city},
        "[ROADS]": {"data": roads, "modifier": add_road},
        "[REQUESTS]": {"data": requests, "modifier": add_request},
    }

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line in sections:
            section = line
            continue

        modifier = config[section]["modifier"]
        data = config[section]["data"]
        modifier(data, line)

    return cities, roads, requests
