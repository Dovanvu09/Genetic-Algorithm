import random

n = 2                  # size of individual
m = 200                # size of population 
n_generations = 100    # number of loops range
losses = []

def generate_random_value():
    return (random.random()*2-1)*100

def compute_loss(individual):
    return sum(gen*gen  for gen in individual)

def create_individual():
    return [generate_random_value() for _ in range(n)]

def crossover(individual1, individual2, crossover_rate = 0.9):
    individual1_new = individual1.copy()
    individual2_new = individual2.copy()

    for i in range(n):
        if random.random() < crossover_rate:
            individual1_new[i] = individual2[i]
            individual2_new[i] = individual1[i]
    return individual1_new, individual2_new

def mutate(individual, mutate_rate = 0.05):
    individual_m = individual.copy()
    for i in range(n):
        if random.random() < mutate_rate:
            individual_m[i] = generate_random_value()
    return individual_m 

def selection(sorted_population):
    index_1= random.randint(0,m-1)
    index_2= random.randint(0,m-1)

    while index_1 == index_2:
        index_2 = random.randint(0,m-1)
    individual_s = sorted_population[min(index_1, index_2)]
    return individual_s

def create_new_population(old_population, gen = 1):
    # step 1: sort population
    sorted_population = sorted(old_population, key = compute_loss)

    losses.append(compute_loss(sorted_population[0]))
    print("Best loss:", compute_loss(sorted_population[0]))

    new_population = sorted_population[:2]
    while len(new_population) < m:
        #step 2: selection 
        individual_s1 = selection(sorted_population)
        individual_s2 = selection(sorted_population)

        #step 3: crossover 
        individual_c1, individual_c2 = crossover(individual_s1, individual_s2)

        #step 4: Mutation
        individual_m1 = mutate(individual_c1)
        individual_m2 = mutate(individual_c2)

        new_population.append(individual_m1)
        new_population.append(individual_m2) 
    return new_population

population = [create_individual() for _ in range(m)]


for i in range(n_generations):
    population = create_new_population(population, i)

import matplotlib.pyplot as plt
plt.plot(losses)
plt.xlabel('Generation')
plt.ylabel('Loss')
plt.show()

