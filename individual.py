import numpy as np
import pandas as pd

from util import CHROMOSOME_SIZE, binary_to_decimal, heuristic, P_M


class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calc_fitness()

    def calc_fitness(self):
        """Calculates the fitness of the individual"""
        return 1 / (heuristic(*self.decode_chromosome()) + 0.0000000001)

    def decode_chromosome(self):
        """Decodes the chromosome into a tuple of x and y"""
        cut_point = CHROMOSOME_SIZE // 2
        max_val = '9' * cut_point
        x = int(self.chromosome[:cut_point])
        y = int(self.chromosome[cut_point:])
        res_x = -5 + ((x - 0) / (int(max_val) - 0)) * (5 - (-5))
        res_y = -5 + ((y - 0) / (int(max_val) - 0)) * (5 - (-5))

        return res_x, res_y

    def mutate(self):
        """Mutates the individual"""
        mutated = [int(x) for x in self.chromosome]

        for i in range(len(mutated)):
            if np.random.random() <= P_M:
                mutated[i] = np.random.randint(0, 10)

        self.chromosome = ''.join(str(x) for x in mutated)
        self.fitness = self.calc_fitness()

    def __str__(self) -> str:
        ind = pd.Series()
        ind['Chromosome'] = self.chromosome
        ind['X'] = self.decode_chromosome()[0]
        ind['Y'] = self.decode_chromosome()[1]
        ind['Fitness'] = self.fitness

        return str(ind)
