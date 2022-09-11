import os
import pickle
from symbolic_src.chromosome import chromosome


INITIAL_ROUNDS = 8  # 8000
PARENT_PATH = "pickle_jar/bestParent.p"


def generate_key_function(data_path: str, rounds: int = INITIAL_ROUNDS):
    # load values from csv file instead of these test values.
    # data = [
    #     (1, 1),
    #     (2, 4),
    #     (3, 9),
    #     (4, 16),
    #     (5, 25),
    #     (6, 36),
    #     (7, 49),
    #     (8, 64),
    #     (9, 81),
    #     (10, 100),
    # ]

    data = load_data_from_csv(data_path)

    optimal_fitness = 0.0
    bestParent = chromosome()
    bestParent.generate_parent_chromosome(10)

    for i in range(0, INITIAL_ROUNDS):
        child = bestParent.clone()
        child.mutate()

        if child.get_fitness(data) > bestParent.get_fitness(data):
            bestParent = child.clone()
            print(
                bestParent.display() + " Fitness: " + str(bestParent.get_fitness(data))
            )

            if optimal_fitness == bestParent.get_fitness(data):
                break

    # pickle the best parent
    pickle.dump(bestParent, open(PARENT_PATH, "wb"))

    return bestParent


def load_data_from_csv(data_path: str):
    """loads the data from the csv file"""
    # check if file exists throw exception if not
    # check if file exists
    if not os.path.isfile(data_path):
        raise FileNotFoundError("File not found")

    data = []

    with open(data_path, "r") as f:
        for line in f:
            data.append(tuple(map(int, line.split(","))))

    return data


def load_key_function() -> chromosome:
    """loads the key function from the file"""
    if not os.path.isfile(PARENT_PATH):
        raise FileNotFoundError("File not found")

    return pickle.load(open(PARENT_PATH, "rb"))
