from graph import build_graph, dikstra
from read_write import read_input
from routes import calculate_route_total_weights, select_route


def main():
    """
    Точка входа:
    1. Читает данные из input.txt.
    2. Строит граф.
    3. Для каждого запроса:
       - находит три маршрута, оптимальные по Д, В, С;
       - выбирает один компромиссный маршрут по приоритетам;
       - формирует строки вывода.
    4. Записывает результат в output.txt.
    """
    cities, roads, requests = read_input("input.txt")
    graph, city_ids = build_graph(cities, roads)

    output_lines = []

    for start_name, end_name, orders in requests:
        start_id = city_ids[start_name]
        end_id = city_ids[end_name]

        routes = {}

        for idx, order in enumerate(["ДЛИНА", "ВРЕМЯ", "СТОИМОСТЬ"]):
            route, _ = dikstra(graph, start_id, end_id, idx)
            if route:
                city_names, dist, time, cost = calculate_route_total_weights(
                    graph, route, cities
                )
                routes[order] = (city_names, dist, time, cost)
                output_lines.append(
                    f"{order}: {' -> '.join(city_names)} | Д={dist}, В={time}, С={cost}"
                )

        _, comp_names, comp_dist, comp_time, comp_cost = select_route(routes, orders)
        output_lines.append(
            f"КОМПРОМИСС: {' -> '.join(comp_names)} | Д={comp_dist}, В={comp_time}, С={comp_cost}"
        )

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))


if __name__ == "__main__":
    main()
