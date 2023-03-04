from ga_tsp import Genetic
from aco_tsp import AntColony
import time
import numpy as np
from utils_tsp import generate_cities, make_mat, change_mat_diag_elem
from visualize import plot_statistics

NUMBER_OF_TEST = 30  # 30
NUMBER_OF_CITIES = 50  # 25, 50, 100, 300


def main():
    elapsed_times_GA = []
    elapsed_times_ACO = []
    best_dists_GA = []
    best_dists_ACO = []

    for i in range(1, NUMBER_OF_TEST+1):
        # Inizializzazione random della matrice delle distanze tra
        # una città x e una città y
        city_coordinates = generate_cities(NUMBER_OF_CITIES)
        adjacency_mat = make_mat(city_coordinates)
        adjacency_mat = change_mat_diag_elem(adjacency_mat, np.inf)

        tsp_ga = Genetic(distances=adjacency_mat, pop_size=100,
                         elite_size=1, max_generation=90, mutation_rate=0.1)  # max_generation = 50,100,150

        tsp_aco = AntColony(adjacency_mat, n_ants=int((NUMBER_OF_CITIES*2)/5),
                            n_best=1, n_iterations=90, decay=0.9, alpha=1, beta=5)  # n_iterations = 50,100,150

        # GA-TSP
        print("GA run test number:{}".format(i))
        st = time.time()
        best_dists_GA.append(tsp_ga.geneticAlgorithm().fitness)
        et = time.time()
        elapsed_times_GA.append(et-st)

        # ACO-TSP
        print("ACO run test number:{}".format(i))
        st = time.time()
        best_dists_ACO.append(tsp_aco.run()[1])
        et = time.time()
        elapsed_times_ACO.append(et-st)

    plot_statistics(NUMBER_OF_TEST, elapsed_times_GA, elapsed_times_ACO,
                    best_dists_GA, best_dists_ACO)


if __name__ == "__main__":
    main()
