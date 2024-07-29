import random
n = 20                # size of individual
m = 200               # size of population
n_generations = 40    # number of generations

fitnesses = []
def compute_fitness(individual):
    return sum(gen for gen in individual)

def create_individual():
    return [random.randint(0,1) for _ in range(n)]

def crossover(individual1, individual2, crossover_rate = 0.9):
    individual1_new = individual1.copy()
    individual2_new = individual2.copy()

    for i in range(n):
        if random.random() < crossover_rate:
            individual1_new[i] = individual2[i]
            individual2_new[i] = individual1[i]
    return individual1_new, individual2_new

def mutate(individual, mutation_rate = 0.05):
    individual_m = individual.copy()
    for i in range(n):
        if random.random() < mutation_rate:
            individual_m[i] = random.randint(0,1)
    
    return individual_m

# population is sorted according to fitness

def selection(sorted_old_population):
    index1 = random.randint(0,m-1)
    index2 = random.randint(0,m-1)

    while index2 == index1:
        index2 = random.randint(0,m-1)
    
    individual_s = sorted_old_population[max(index1, index2)]
    return individual_s

def create_new_population(old_population, gen = 1):
    # step 1: sort population
    sorted_population = sorted(old_population, key = compute_fitness)

    fitnesses.append(compute_fitness(sorted_population[m-1]))
    print("Best :", compute_fitness(sorted_population[m-1]))

    new_population = sorted_population[-1]
    while len(new_population) < m:
        #step 2: selection
        individual_s1 = selection(sorted_population)
        individual_s2 = selection(sorted_population)

        #step 3: crossover
        individual_c1, individual_c2 = crossover(individual_s1, individual_s2)
        
        #step 4: mutation
        individual_m1 = mutate(individual_c1)
        individual_m2 = mutate(individual_c2)

        new_population.append(individual_m1)
        new_population.append(individual_m2)
    return new_population

# create population
population = [create_individual() for _ in range(m)]

#loops
for i in range(n_generations):
    population = create_new_population(population, i)

import matplotlib.pyplot as plt

plt.plot(fitnesses)
plt.xlabel('Generations')
plt.ylabel('Fitness')
plt.show()





