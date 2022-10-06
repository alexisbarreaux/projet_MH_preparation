from binpacking.constants import SPLIT_TEST_FILES_DIR
from binpacking.heuristics import naive_base_order, HeuristicRunner
from binpacking.utils import (
    display_optimum_versus_found,
    display_excess_optimum_versus_found,
)


if __name__ == "__main__":
    runner = HeuristicRunner(
        method=naive_base_order,
        test_directory=SPLIT_TEST_FILES_DIR,
        show_solution=True,
        show_runtime=True,
        verbose=True,
    )
    (
        found_solutions,
        known_optimums,
        runtimes,
    ) = runner.run_method_on_whole_directory_saving_results()

    """
    display_optimum_versus_found(
        found_solutions=found_solutions, known_optimums=known_optimums
    )
    """

    display_excess_optimum_versus_found(
        found_solutions=found_solutions,
        known_optimums=known_optimums,
        display_type="percentage",
    )
