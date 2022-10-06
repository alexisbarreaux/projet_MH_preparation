from global_constants import DISPLAY_STYLES

import matplotlib.pyplot as plt
import numpy as np


def display_optimum_versus_found(optimums: list, found_solutions: dict) -> None:
    """
    Takes list of optimums and solutions as a dict where keys are the used methods
    and values are the solutions found for each method.
    """
    plt.clf()

    methods = list(found_solutions.keys())
    abscisses = np.arange(len(found_solutions[methods[0]]))

    # Plot methods
    for i in range(len(methods)):
        method = methods[i]
        plt.plot(abscisses, found_solutions[method], DISPLAY_STYLES[i], label=method)

    # Also plot optimums
    plt.plot(abscisses, optimums, DISPLAY_STYLES[-1], label="optimums")

    plt.legend(loc="lower right")
    plt.show()
    return


def display_excess_optimum_versus_found(
    optimums: list, found_solutions: dict, display_type: str = "raw"
) -> None:
    plt.clf()

    methods = list(found_solutions.keys())
    abscisses = np.arange(len(found_solutions[methods[0]]))
    array_optimums = np.array(optimums)

    # Plot methods
    for i in range(len(methods)):
        method = methods[i]
        solutions = found_solutions[method]
        array_solutions = np.array(solutions)

        excess = array_solutions - array_optimums
        if display_type == "percentage":
            excess = 100 * np.divide(excess, array_optimums)

        plt.plot(abscisses, excess, DISPLAY_STYLES[i], label=method)

    plt.legend(loc="lower right")
    plt.show()
    return


def display_runtimes(runtimes: dict) -> None:
    """
    Takes runtime as a dict where keys are the used method and
    value are the runtimes for said method.
    """
    plt.clf()

    methods = list(runtimes.keys())
    abscisses = np.arange(len(runtimes[methods[0]]))

    for i in range(len(methods)):
        method = methods[i]
        plt.plot(abscisses, runtimes[method], DISPLAY_STYLES[i], label=method)

    plt.legend(loc="lower right")
    plt.show()
    return
