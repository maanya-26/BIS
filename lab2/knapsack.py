import random

weights = [2, 5, 7, 3, 8, 6, 4, 9, 5, 7]
values = [10, 20, 15, 7, 25, 18, 12, 30, 14, 22]

capacity = 25
num_items = len(weights)

population_size = 20
generations = 50
mutation_rate = 0.05
crossover_rate = 0.8


def create_chromosome():
    return [random.randint(0, 1) for _ in range(num_items)]


def initialize_population():
    return [
        create_chromosome()
        for _ in range(population_size)
    ]


def gene_expression(chromosome):
    selected_items = []

    for i in range(num_items):
        if chromosome[i] == 1:
            selected_items.append(i)

    return selected_items


def fitness(chromosome):
    selected_items = gene_expression(chromosome)

    total_weight = sum(
        weights[i]
        for i in selected_items
    )

    total_value = sum(
        values[i]
        for i in selected_items
    )

    if total_weight > capacity:
        return 0

    return total_value


def calculate_solution(chromosome):
    selected_items = gene_expression(chromosome)

    total_weight = sum(
        weights[i]
        for i in selected_items
    )

    total_value = sum(
        values[i]
        for i in selected_items
    )

    return total_weight, total_value


def selection(population):
    population.sort(
        key=fitness,
        reverse=True
    )

    selected = population[
        :population_size // 2
    ]

    return selected


def crossover(parent1, parent2):

    if random.random() < crossover_rate:

        point = random.randint(
            1,
            num_items - 1
        )

        child1 = (
            parent1[:point]
            + parent2[point:]
        )

        child2 = (
            parent2[:point]
            + parent1[point:]
        )

        return child1, child2

    return parent1[:], parent2[:]


def mutation(chromosome):

    for i in range(num_items):

        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]

    return chromosome


def gene_expression_algorithm():

    population = initialize_population()

    best_solution = None
    best_fitness = 0

    print("\n========== GEA PROCESS ==========\n")

    for generation in range(generations):

        for chromosome in population:

            current_fitness = fitness(chromosome)

            if current_fitness > best_fitness:
                best_fitness = current_fitness
                best_solution = chromosome[:]

        current_best = max(
            fitness(chromosome)
            for chromosome in population
        )

        print(
            f"Generation {generation + 1:2d}: "
            f"Current Best = {current_best:2d}, "
            f"Global Best = {best_fitness:2d}"
        )

        selected = selection(population)

        new_population = selected[:]

        while len(new_population) < population_size:

            parent1 = random.choice(selected)
            parent2 = random.choice(selected)

            child1, child2 = crossover(
                parent1,
                parent2
            )

            child1 = mutation(child1)
            child2 = mutation(child2)

            new_population.append(child1)

            if len(new_population) < population_size:
                new_population.append(child2)

        population = new_population

    return best_solution, best_fitness


best_solution, best_fitness = gene_expression_algorithm()

total_weight, total_value = calculate_solution(
    best_solution
)

selected_items = gene_expression(
    best_solution
)

print("\n========================================")
print("             FINAL RESULT")
print("========================================")

print(
    "Best Chromosome:",
    best_solution
)

print(
    "Selected Items:",
    [i + 1 for i in selected_items]
)

print(
    "Total Weight:",
    total_weight
)

print(
    "Total Value:",
    total_value
)

print(
    "Maximum Capacity:",
    capacity
)

print(
    "Best Fitness:",
    best_fitness
)

print("========================================")
