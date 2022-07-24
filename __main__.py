from symbolic_src.chromosome import chromosome


INITIAL_ROUNDS = 100000

def main():
    # load values from csv file instead of these test values.
    data = [
        (1, 1),
        (2, 4),
        (3, 9),
        (4, 16),
        (5, 25),
        (6, 36),
        (7, 49),
        (8, 64),
        (9, 81),
        (10, 100),
    ]

    optimal_fitness = 0.0
    bestParent = chromosome()
    bestParent.generate_parent_chromosome(10)

    for i in range(0, INITIAL_ROUNDS):
        child = bestParent.clone()
        child.mutate()

        if child.get_fitness(data) > bestParent.get_fitness(data):
            bestParent = child.clone()
            print(bestParent.display() + " Fitness: " + str(bestParent.get_fitness(data)))

            if optimal_fitness == bestParent.get_fitness(data):
                break


if __name__ == '__main__':
    main()