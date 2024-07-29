# Statement: We have n = 12 items with given values and weights.
# We need to put these n items into a bag with a maximum capacity of max_weight = 70kg
# such that the total value in the bag is maximized.

import random

n = 12   # number of items
m = 360  # number of individuals in the population
n_generations = 200 # number of generations
fitnesses = []  # for plotting fitnesses
max_weight = 70 # maximum weight the bag can hold

# given data
weights = [1, 2, 5, 7, 10, 12, 15, 23, 32, 33, 35, 37]  # weights of the items
prices =  [1, 3, 6, 7, 12, 15, 25, 32, 44, 45, 47, 50]  # values of the items respectively

# generate random gene value
def generate_random_value():  
    return random.randint(0, 1)   

# create chromosome
def create_individual():
    return [generate_random_value() for _ in range(n)]

# calculate fitness
def compute_fitness(individual):
    fitness = sum(c*x for c, x in zip(individual, prices))

    # check if the individual exceeds the weight limit
    if compute_weight(individual) > max_weight:
        # penalty
        fitness = 0
    
    return fitness

# calculate weight
def compute_weight(individual):
    sum_weight = sum(c*x for c, x in zip(individual, weights))
    return sum_weight

# selection
def selection(sorted_population):
    index1 = random.randint(0, m-1)
    while True:
        index2 = random.randint(0, m-1)
        if index2 != index1:
            break
    individual = sorted_population[index1]
    if index1 < index2:
        individual = sorted_population[index2]
    return individual

# crossover
def crossover(individual1, individual2, crossover_rate = 0.9):
    individual_c1 = individual1.copy()
    individual_c2 = individual2.copy()
    if random.random() < crossover_rate:
        index = random.randint(1, n - 2)
        for i in range(index):
            individual_c1[i] = individual2[i]
            individual_c2[i] = individual1[i]
    return individual_c1, individual_c2

# mutation
def mutate(individual, mutation_rate = 0.05):
    individual_new = individual.copy()
    if random.random() < mutation_rate:
        index = random.randint(0, n-1)
        individual_new[index] = generate_random_value()
    return individual_new

# create new population
def create_new_population(old_population):
    sorted_old_population = sorted(old_population, key = compute_fitness)
    fitnesses.append(compute_fitness(sorted_old_population[-1]))
    #print('fitness', fitnesses[-1])

    new_population = []
    while len(new_population) < m - 2:
        # selection
        individual1 = selection(sorted_old_population)
        individual2 = selection(sorted_old_population)

        # crossover
        individual_c1, individual_c2 = crossover(individual1, individual2)

        # mutation
        individual_m1 = mutate(individual_c1)
        individual_m2 = mutate(individual_c2)

        # add to new population
        new_population.append(individual_m1)
        new_population.append(individual_m2)
        
    new_population.append(sorted_old_population[-1])
    new_population.append(sorted_old_population[-2])

    return new_population

# create initial population
population = [create_individual() for _ in range(m)]

for i in range(n_generations):
    population = create_new_population(population)
    
    # for debug
    if (i%1 == 0):
        sorted_population = sorted(population, key=compute_fitness)
        print('fitness', compute_fitness(sorted_population[-1]))

# get final result
sorted_population = sorted(population, key = compute_fitness)
print('way to put items:', sorted_population[-1])
print('total weight:', compute_weight(sorted_population[-1]))
print('total value:', compute_fitness(sorted_population[-1]))
