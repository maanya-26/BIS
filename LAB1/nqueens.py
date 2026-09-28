import random

# Parameters
N = 8
POPULATION_SIZE = 10
MUTATION_RATE = 0.1
GENERATIONS = 100


# Calculate fitness
def fitness(chromosome):
    non_attacking = 0
    total_pairs = N * (N - 1) // 2

    for i in range(N):
        for j in range(i + 1, N):

            # Check if queens are NOT on same diagonal
            if abs(chromosome[i] - chromosome[j]) != abs(i - j):
                non_attacking += 1

    return non_attacking


# Create initial population
population = []

for _ in range(POPULATION_SIZE):
    chromosome = list(range(N))
    random.shuffle(chromosome)
    population.append(chromosome)


# Genetic Algorithm
for generation in range(GENERATIONS):

    # Calculate fitness
    population.sort(key=fitness, reverse=True)

    # Check for solution
    if fitness(population[0]) == N * (N - 1) // 2:
        break

    # Selection
    parent1 = population[0]
    parent2 = population[1]

    new_population = [parent1, parent2]

    # Create new children
    while len(new_population) < POPULATION_SIZE:

        # Crossover
        point = random.randint(1, N - 1)

        child = parent1[:point] + parent2[point:]

        # Fix duplicate rows
        missing = [x for x in range(N) if x not in child]

        used = set()

        for i in range(N):
            if child[i] in used:
                child[i] = missing.pop(0)
            else:
                used.add(child[i])

        # Mutation
        if random.random() < MUTATION_RATE:
            i, j = random.sample(range(N), 2)
            child[i], child[j] = child[j], child[i]

        new_population.append(child)

    population = new_population


# Best solution
best = max(population, key=fitness)

print("Best solution:", best)
print("Fitness:", fitness(best))

# Display chessboard
print("\nChess Board:")

for row in range(N):
    for col in range(N):
        if best[col] == row:
            print("Q", end=" ")
        else:
            print(".", end=" ")
    print()