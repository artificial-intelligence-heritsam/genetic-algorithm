from population import Population

def main():
    pop = Population()
    best = pop.select_best()
    termination = 1000

    with open('results.txt', 'w') as f:
        print(pop)
        f.write(str(pop) + '\n')
        
        while termination > 0:
            pop.population = pop.generate_next_generation()
            print(pop)
            f.write(str(pop) + '\n')

            if pop.select_best().fitness == best.fitness:
                best = pop.select_best()
                termination -= 1
            else:
                best = pop.select_best()
                termination = 1000

            best = pop.select_best()

        print(pop)
        f.write(str(pop) + '\n')


if __name__ == "__main__":
    main()