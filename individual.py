import numpy as np
from util import binary_to_decimal, heuristic, P_M


class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calc_fitness()

    def calc_fitness(self):
        return 1 / (heuristic(*self.decode_chromosome()) + 0.0000000001)

    def decode_chromosome(self):
        x = int(self.chromosome[:10])
        y = int(self.chromosome[10:])
        res_x = -5 + ((x - 0) / (9999999999 - 0)) * (5 - (-5))
        res_y = -5 + ((y - 0) / (9999999999 - 0)) * (5 - (-5))

        return res_x, res_y

    def mutate(self, p_m=P_M):
        mutated = [int(x) for x in self.chromosome]

        for i in range(len(mutated)):
            if np.random.random() <= p_m:
                mutated[i] = np.random.randint(0, 10)

        self.chromosome = ''.join(str(x) for x in mutated)
        self.fitness = self.calc_fitness()

    def __str__(self) -> str:
        x, y = self.decode_chromosome()

        return f'{self.chromosome} ({x:.2f}, {y:.2f}) {self.fitness:.2f}'
