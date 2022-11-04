import numpy as np
from individual import Individual
from util import random_genes, POP_SIZE, P_C


class Population:
    def __init__(self, size=POP_SIZE):
        self.population = self.generate_population(size)
        self.generations = 0

    def generate_population(self, size):
        population = []

        for _ in range(size):
            population.append(Individual(random_genes(20)))

        return population

    def generate_mating_pool(self):
        mating_pool = []

        for _ in range(len(self.population)):
            mating_pool.append(self.roulette_wheel_selection())

        return mating_pool

    def roulette_wheel_selection(self):
        population_fitness = sum(
            [chromosome.fitness for chromosome in self.population])

        chromosome_probabilities = [
            chromosome.fitness/population_fitness for chromosome in self.population]

        return np.random.choice(self.population, p=chromosome_probabilities)

    def generate_next_generation(self):
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
        return max(self.population, key=lambda x: x.fitness)

    def __str__(self) -> str:
        return f'Generation: {self.generations}\n' + '\n'.join(str(x) for x in self.population) + '\n'
