from binpacking.constants import SPLIT_TEST_FILES_DIR
from binpacking.heuristics import (
    naive_base_order,
    naive_with_ordered_items,
    HeuristicRunner,
)
from binpacking.utils import (
    display_optimum_versus_found,
    display_excess_optimum_versus_found,
    display_runtimes,
)


if __name__ == "__main__":

    # First run with naive
    runner = HeuristicRunner(
        method=naive_base_order,
        test_directory=SPLIT_TEST_FILES_DIR,
        # show_solution=True,
        # show_runtime=True,
        # verbose=True,
    )
    (
        unordered_found_solutions,
        known_optimums,
        unordered_runtimes,
    ) = runner.run_method_on_whole_directory_saving_results()

    # Then run with ordering
    runner.method = naive_with_ordered_items
    (
        ordered_found_solutions,
        _,
        ordered_runtimes,
    ) = runner.run_method_on_whole_directory_saving_results()

    """
    display_runtimes(
        runtimes={
            "naive_base_order": unordered_runtimes,
            "naive_with_ordered_items": ordered_runtimes,
        }
    )
    
    display_optimum_versus_found(
        optimums=known_optimums,
        found_solutions={
            "naive_base_order": unordered_found_solutions,
            "naive_with_ordered_items": ordered_found_solutions,
        },
    )
    """
    display_excess_optimum_versus_found(
        optimums=known_optimums,
        found_solutions={
            "naive_base_order": unordered_found_solutions,
            "naive_with_ordered_items": ordered_found_solutions,
        },
        display_type="percentage",
    )
