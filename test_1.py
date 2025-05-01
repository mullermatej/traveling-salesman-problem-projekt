from assets.utils import (generate_cities, calculate_route_distance,
                          create_initial_population, calculate_fitness)
from notebooks.selection import tournament_selection
from notebooks.pmx import pmx_crossover


def test_all_components():
    print("Testiranje komponenti genetskog algoritma za TSP")
    print("=" * 50)

    # Test 1: Generiranje gradova
    print("\nTest 1: Generiranje gradova")
    num_cities = 5
    cities = generate_cities(num_cities)
    print(f"Generirano {len(cities)} gradova")
    print(f"Prvi grad: {cities[0]}")

    # Test 2: Izračun udaljenosti
    print("\nTest 2: Izračun udaljenosti između dva grada")
    distance = cities[0].distance(cities[1])
    print(f"Udaljenost između {cities[0]} i {cities[1]}: {distance:.2f}")

    # Test 3: Kreiranje inicijalne populacije
    print("\nTest 3: Kreiranje inicijalne populacije")
    population_size = 10
    population = create_initial_population(population_size, num_cities)
    print(f"Kreirana populacija od {len(population)} jedinki")
    print(f"Prva jedinka: {population[0]}")

    # Test 4: Izračun rute i fitnessa
    print("\nTest 4: Izračun duljine rute i fitnessa")
    route = population[0]
    distance = calculate_route_distance(route, cities)
    fitness = calculate_fitness(route, cities)
    print(f"Ruta: {route}")
    print(f"Duljina rute: {distance:.2f}")
    print(f"Fitness: {fitness:.4f}")

    # Test 5: Turnirska selekcija
    print("\nTest 5: Turnirska selekcija")
    fitness_values = [calculate_fitness(route, cities) for route in population]
    tournament_size = 3
    selected = tournament_selection(
        population, fitness_values, tournament_size)
    print(f"Odabrana jedinka: {selected}")

    # Test 6: PMX križanje
    print("\nTest 6: PMX križanje")
    parent1 = population[0]
    parent2 = population[1]
    child = pmx_crossover(parent1, parent2)
    print(f"Roditelj 1: {parent1}")
    print(f"Roditelj 2: {parent2}")
    print(f"Dijete: {child}")

    # Provjera validnosti permutacije
    is_valid = len(set(child)) == len(child) and sorted(
        child) == list(range(num_cities))
    print(f"Validnost permutacije djeteta: {is_valid}")

    print("\nSvi testovi završeni!")


if __name__ == "__main__":
    test_all_components()
