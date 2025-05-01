import random


def pmx_crossover(parent1, parent2):
    size = len(parent1)

    if len(parent2) != size:
        raise ValueError("Roditelji moraju biti iste duljine")

    point1 = random.randint(0, size - 2)
    point2 = random.randint(point1 + 1, size - 1)

    child = [-1] * size

    for i in range(point1, point2 + 1):
        child[i] = parent1[i]

    mapping = {}
    for i in range(point1, point2 + 1):
        if parent2[i] != parent1[i]:
            mapping[parent2[i]] = parent1[i]
            mapping[parent1[i]] = parent2[i]

    for i in range(size):
        if i < point1 or i > point2:
            current_gene = parent2[i]

            while current_gene in child[point1:point2+1]:
                current_gene = mapping.get(current_gene, current_gene)

            child[i] = current_gene

    return child
