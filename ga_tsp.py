import numpy as np
import random


class Chromosome():
    def __init__(self):
        self.genes = []
        self.fitness = np.inf


class Genetic(object):
    def __init__(self, distances, pop_size=100, elite_size=10, max_generation=100,
                 mutation_rate=0.03):
        self.distances = distances
        self.pop_size = pop_size
        self.max_generation = max_generation
        self.mutation_rate = mutation_rate
        self.elite_size = elite_size

    def createNewPopulation(self, size):
        population = []
        for x in range(size):
            newChromosome = Chromosome()
            # Inzializza random gli indici delle città per ogni cromosoma
            newChromosome.genes = random.sample(
                range(1, len(self.distances)), len(self.distances)-1)
            # Aggiunge uno zero all'inizio
            newChromosome.genes.insert(0, 0)
            # Aggiunge uno zero alla fine
            newChromosome.genes.append(0)
            # Calcola il funzionale del cromosoma
            newChromosome.fitness = self.fitness(newChromosome.genes)
            # Aggiunge il cromosoma alla popolaziones
            population.append(newChromosome)
        return population

    # Calcola la fitness: totale delle distanze

    def fitness(self, genes):
        return sum(
            [self.distances[genes[i], genes[i + 1]]
                for i in range(len(genes) - 1)]
        )

    # Restituisce il cromosoma con il funzionale più piccolo

    def findBestChromosome(self, population):
        allFitness = [i.fitness for i in population]
        bestFitness = min(allFitness)
        return population[allFitness.index(bestFitness)]

    # In K-Way tournament selection, we select K individuals
    # from the population at random and select the best out
    # of these to become a parent. The same process is repeated
    # for selecting the next parent.

    def tournamentSelection(self, population, k=4):
        # Seleziona random k individui
        selected = [population[random.randrange(
            0, len(population))] for i in range(k)]
        # Prende il migliore tra i k individui selezionati
        bestChromosome = self.findBestChromosome(selected)
        return bestChromosome

    # Restituisce un cromosoma figlio

    def reproduction(self, population):
        parent1 = self.tournamentSelection(population, 10).genes
        parent2 = self.tournamentSelection(population, 6).genes
        while parent1 == parent2:
            parent2 = self.tournamentSelection(population, 6).genes

        return self.orderOneCrossover(parent1, parent2)

    def orderOneCrossover(self, parent1, parent2):

        child = [-1] * len(parent1)
        child[0], child[len(parent1) - 1] = 0, 0

        point1 = random.randint(0, len(parent1)-2)
        point2 = random.randint(0, len(parent1)-2)

        # Mi assicuro che point1 sia minore di point2
        if point1 > point2:
            point1, point2 = point2, point1

        child[point1:point2 + 1] = parent1[point1:point2 + 1]

        i = point2+1  # indice per il figlio
        j = point1  # indice per il parent2
        while child[i] in [-1, 0]:
            if child[i] != 0:
                if parent2[j] not in child:
                    child[i] = parent2[j]
                    i += 1
                    if i == len(parent1):
                        i = 0
                else:
                    j += 1
                    if j == len(parent1):
                        j = 0
            else:
                i += 1
                if i == len(parent1):
                    i = 0

        # Effettua una mutazione del figlio ottenuto,
        # con un tasso di mutazione pari a MUTATION_RATE
        if random.random() <= self.mutation_rate:
            child = self.swapMutation(child)

        # Create new chromosome for child
        newChromosome = Chromosome()
        newChromosome.genes = child
        newChromosome.fitness = self.fitness(child)
        return newChromosome

    # Sample:
    # Chromosomes =         [0, 3, 8, 5, 1, 7, 12, 6, 4, 10, 11, 9, 2, 0]
    # Mutated chromosomes = [0, 11, 8, 5, 1, 7, 12, 6, 4, 10, 3, 9, 2, 0]

    def swapMutation(self, chromo):
        p1, p2 = [random.randrange(1, len(chromo) - 1) for i in range(2)]
        while p1 == p2:
            p2 = random.randrange(1, len(chromo) - 1)
        temp = chromo[p1]
        chromo[p1] = chromo[p2]
        chromo[p2] = temp
        return chromo

    def geneticAlgorithm(self):
        #allBestFitness = []
        population = self.createNewPopulation(self.pop_size)
        generation = 0
        # Ciclo principale
        while generation < self.max_generation:
            generation += 1

            offsprings = []
            elite_population = sorted(population, key=lambda i: i.fitness)[
                :self.elite_size]

           # Incrocio
            for i in range(self.elite_size, self.pop_size):
                # Select parent, make crossover and
                # after, append in population a new child
                offsprings.append(self.reproduction(population))

            population = offsprings + elite_population
            random.shuffle(population)

            # Fitness media della popolazione
            ''' averageFitness = round(
                np.sum([genom.fitness for genom in population]) / len(population), 2) '''
            # Prende il miglior cromosoma
            bestChromosome = self.findBestChromosome(population)
            print("\n" * 5)
            print("Generation: {0}\nPopulation Size: {1}\nBest Fitness(distance): {2}"
                  .format(generation, len(population),  # averageFitness,
                          bestChromosome.fitness))

            # Tiene traccia di tutte le migliori fitness di ogni generazione per poi
            # tracciare la curva
            # allBestFitness.append(bestChromosome.fitness)

        return bestChromosome
        # Visualize
        # plot(generation, allBestFitness, bestChromosome, cityCoordinates)
