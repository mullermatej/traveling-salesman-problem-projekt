import random


def tournament_selection(population, fitness_values, tournament_size):
    if tournament_size <= 0 or tournament_size > len(population):
        raise ValueError(
            "Tournament veličina mora biti pozitivna i manja od populacije")

    tournament_indices = random.sample(range(len(population)), tournament_size)

    best_index = tournament_indices[0]
    best_fitness = fitness_values[best_index]

    for idx in tournament_indices[1:]:
        if fitness_values[idx] > best_fitness:
            best_index = idx
            best_fitness = fitness_values[idx]

    return population[best_index]
