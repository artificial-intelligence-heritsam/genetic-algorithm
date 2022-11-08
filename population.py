import numpy as np
from individual import Individual
from util import random_genes, POP_SIZE, P_C


class Population:
    def __init__(self, size=POP_SIZE):
        self.population = self.generate_population(size)
        self.generations = 0

    def generate_population(self, size):
        """Generates a population of individuals"""
        population = []

        for _ in range(size):
            population.append(Individual(random_genes()))

        return population

    def generate_mating_pool(self):
        """Generates a mating pool"""
        mating_pool = []

        for _ in range(len(self.population)):
            mating_pool.append(self.roulette_wheel_selection())

        return mating_pool

    def roulette_wheel_selection(self):
        """Performs roulette wheel selection"""
        population_fitness = sum(
            [chromosome.fitness for chromosome in self.population])

        r = np.random.uniform()
        i = 0
        while r > 0:
            r -= self.population[i].fitness / population_fitness
            i += 1
            if i == len(self.population):
                i -= 1
                break
        
        return self.population[i]

    def generate_next_generation(self):
        """Generates the next generation"""
        mating_pool = self.generate_mating_pool()
        new_pop = []

        for i in range(len(mating_pool) // 2):
            parent1 = mating_pool[i]
            parent2 = mating_pool[(i + 1)]
            child, child2 = self.crossover(parent1, parent2)
            child.mutate()
            child2.mutate()
            new_pop.append(child)
            new_pop.append(child2)

        new_pop.sort(key=lambda x: x.fitness, reverse=True)
        self.population.sort(key=lambda x: x.fitness, reverse=True)

        new_pop = new_pop[:-2] + self.population[:2]
        self.generations += 1

        return new_pop


    def crossover(self, parent1, parent2, p_c=P_C):
        """Performs crossover"""
        if np.random.random() <= p_c:
            crossover_point = np.random.randint(1, len(parent1.chromosome) - 1)
            child_chromosome = parent1.chromosome[:crossover_point] + \
                parent2.chromosome[crossover_point:]
            child2_chromosome = parent2.chromosome[:crossover_point] + \
                parent1.chromosome[crossover_point:]
        else:
            child_chromosome = parent1.chromosome
            child2_chromosome = parent2.chromosome

        return Individual(child_chromosome), Individual(child2_chromosome)

    def select_best(self):
        """Selects the best individual"""
        return max(self.population, key=lambda x: x.fitness)

    def __str__(self) -> str:
        return f'Generation: {self.generations}\n' + '\n'.join(str(x) for x in self.population) + '\n'
