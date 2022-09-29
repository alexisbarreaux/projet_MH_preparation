from binpacking.constants import SPLIT_TEST_FILES_DIR
from binpacking.heuristics import naive_base_order
from binpacking.utils import (
    read_single_problem_from_path,
    check_solution_validity,
    write_solution_to_file,
)

if __name__ == "__main__":
    (
        identifier,
        bin_capacity,
        number_of_items,
        optimal_bin_number,
        items_sizes,
    ) = read_single_problem_from_path(SPLIT_TEST_FILES_DIR / "u120_00.txt")
    (number_of_bins, items_sizes, items_bin_position) = naive_base_order(
        bin_capacity, number_of_items, items_sizes
    )

    assert check_solution_validity(
        bin_capacity, number_of_bins, number_of_items, items_sizes, items_bin_position
    )

    write_solution_to_file(
        "naive_base_order",
        identifier,
        bin_capacity,
        number_of_items,
        optimal_bin_number,
        number_of_bins,
        items_sizes,
        items_bin_position,
    )
    print(number_of_bins, items_sizes, items_bin_position)
