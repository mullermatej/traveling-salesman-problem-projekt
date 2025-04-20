import random


def inversion_mutation(route):
    # Okreće redoslijed, npr. od 1 do 5-1 elementa, uzme segment i invertira ga
    a, b = sorted(random.sample(range(len(route)), 2))
    print(a, b)
    route[a:b] = reversed(route[a:b])
    return route


if __name__ == "__main__":
    # Testna ruta (npr. gradovi 0 do 9)
    ruta = list(range(10))
    print("Originalna ruta:", ruta)
    mutirana = inversion_mutation(ruta.copy())
    print("Mutirana ruta:  ", mutirana)
