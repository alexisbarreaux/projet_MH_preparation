import matplotlib.pyplot as plt
import numpy as np


def display_optimum_versus_found(found_solutions: list, known_optimums: list) -> None:
    abscisses = np.arange(len(found_solutions))
    plt.clf()
    plt.plot(abscisses, found_solutions, "r+")
    plt.plot(abscisses, known_optimums, "b^")
    plt.show()
    return


def display_excess_optimum_versus_found(
    found_solutions: list, known_optimums: list, display_type: str = "raw"
) -> None:
    abscisses = np.arange(len(found_solutions))
    array_solutions, array_optimums = np.array(found_solutions), np.array(
        known_optimums
    )
    excess = array_solutions - array_optimums
    if display_type == "percentage":
        excess = 100 * np.divide(excess, array_optimums)
    plt.clf()
    plt.plot(abscisses, excess, "r+")
    plt.show()
    return
