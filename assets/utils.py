import random
from typing import List

from city import City


def generate_cities(num_cities: int, min_coord: float = 0, max_coord: float = 100) -> List[City]:
    return [City(x=random.uniform(min_coord, max_coord),
                 y=random.uniform(min_coord, max_coord))
            for _ in range(num_cities)]


def calculate_route_distance(route: List[int], cities: List[City]) -> float:
    total_distance = 0
    route_length = len(route)

    for i in range(route_length):
        from_idx = route[i]
        to_idx = route[(i + 1) % route_length]

        from_city = cities[from_idx]
        to_city = cities[to_idx]

        total_distance += from_city.distance(to_city)

    return total_distance


def create_initial_population(population_size: int, num_cities: int) -> List[List[int]]:
    population = []
    city_indices = list(range(num_cities))

    for _ in range(population_size):
        route = city_indices.copy()
        random.shuffle(route)
        population.append(route)

    return population


def calculate_fitness(route: List[int], cities: List[City]) -> float:
    distance = calculate_route_distance(route, cities)
    return 1.0 / (distance + 1e-10)


def create_initial_population(population_size, num_cities):
    population = []
    city_indices = list(range(num_cities))

    for _ in range(population_size):
        route = city_indices.copy()
        random.shuffle(route)
        population.append(route)

    return population


def calculate_fitness(route, cities):
    distance = calculate_route_distance(route, cities)
    return 1.0 / (distance + 1e-10)
