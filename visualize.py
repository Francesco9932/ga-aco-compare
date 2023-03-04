import matplotlib.pyplot as plt
from statistics import mean, stdev


def plot_statistics(nTest, elapsed_times_GA, elapsed_times_ACO, best_dists_GA, best_dists_ACO):
    fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(10, 5))
    ax[0][0].plot(range(1, nTest+1), elapsed_times_GA)
    ax[1][0].plot(range(1, nTest+1), best_dists_GA)
    ax[0][1].plot(range(1, nTest+1), elapsed_times_ACO)
    ax[1][1].plot(range(1, nTest+1), best_dists_ACO)

    # Calcolo della media e della stdev del tempo di esecuzione di GA e ACO
    mean_elapsed_time_GA = mean(elapsed_times_GA)
    mean_elapsed_time_ACO = mean(elapsed_times_ACO)
    stdev_elapsed_time_GA = stdev(elapsed_times_GA)
    stdev_elapsed_time_ACO = stdev(elapsed_times_ACO)
    print("Mean of elapsed time GA: {0:.2f}.\nStdev of elapsed time GA: {1:.2f}.".format(
        mean_elapsed_time_GA, stdev_elapsed_time_GA))
    print("Mean of elapsed time ACO: {0:.2f}.\nStdev of elapsed time ACO: {1:.2f}.".format(
        mean_elapsed_time_ACO, stdev_elapsed_time_ACO))
    # Calcolo della media e della stdev della migliore distanza trovata da GA e ACO
    mean_best_dist_GA = mean(best_dists_GA)
    mean_best_dist_ACO = mean(best_dists_ACO)
    stdev_best_dist_GA = stdev(best_dists_GA)
    stdev_best_dist_ACO = stdev(best_dists_ACO)
    print("Mean of dist found GA: {0:.2f}.\nStdev of dist found GA: {1:.2f}.".format(
        mean_best_dist_GA, stdev_best_dist_GA))
    print("Mean of dist found ACO: {0:.2f}.\nStdev of dist found ACO: {1:.2f}.".format(
        mean_best_dist_ACO, stdev_best_dist_ACO))

    ax[0][0].plot(range(1, nTest+1),
                  [mean_elapsed_time_GA for _ in range(1, nTest+1)])
    ax[1][0].plot(range(1, nTest+1),
                  [mean_best_dist_GA for _ in range(1, nTest+1)])
    ax[0][1].plot(range(1, nTest+1),
                  [mean_elapsed_time_ACO for _ in range(1, nTest+1)])
    ax[1][1].plot(range(1, nTest+1),
                  [mean_best_dist_ACO for _ in range(1, nTest+1)])

    ax[0][0].set_xlabel('Test number')
    ax[1][0].set_xlabel('Test number')
    ax[0][1].set_xlabel('Test number')
    ax[1][1].set_xlabel('Test number')
    ax[0][0].set_ylabel('Time [s]')
    ax[1][0].set_ylabel('Distance')
    ax[0][1].set_ylabel('Time [s]')
    ax[1][1].set_ylabel('Distance')
    ax[0][0].set_title('GA algorithm')
    ax[0][1].set_title('ACO algorithm')

    fig.tight_layout()
    plt.show()
