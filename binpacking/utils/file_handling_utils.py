import os
from typing import Tuple, List

from binpacking.constants import (
    BASE_TEST_FILES_DIR,
    SPLIT_TEST_FILES_DIR,
    SOLUTION_FILES_DIR,
)


def split_test_file(source_file_path: str) -> None:
    """
    Takes a file containing multiple binpacking
    problems and splits it into separate files.
    """
    with open(source_file_path, "r") as source_file:
        # Get number of problems as header
        number_of_subproblems = int(source_file.readline())

        # For each get its parameters
        for _ in range(number_of_subproblems):
            write_test_file_from_parameters(*read_single_problem_from_file(source_file))
    return


def split_test_folder(source_directory: str) -> None:
    """
    Takes a folder containing multiple files with binpacking
    problems and splits it into separate files.
    """
    for test_file in os.listdir(source_directory):
        split_test_file(source_directory / test_file)
    return


def read_single_problem_from_path(
    source_file_path: str,
) -> Tuple[str, int, int, int, List[int]]:
    """
    Used to read a file containing a unique problem
    or the next problem of a file when file path is given.
    """
    with open(source_file_path, "r") as source_file:
        return read_single_problem_from_file(source_file)


def read_single_problem_from_file(
    source_file,
) -> Tuple[str, int, int, int, List[int]]:
    """
    Used to read a file containing a unique problem
    or the next problem of a file when file is given.
    """
    identifier = source_file.readline().strip()
    problems_parameters = source_file.readline().strip().split(" ")
    [bin_capacity, number_of_items, optimal_bin_number] = list(
        map(int, problems_parameters)
    )
    # Get the items
    items = [int(source_file.readline()) for j in range(number_of_items)]

    return (
        identifier,
        bin_capacity,
        number_of_items,
        optimal_bin_number,
        items,
    )


def write_test_file_from_parameters(
    identifier: str,
    bin_capacity: int,
    number_of_items: int,
    optimal_bin_number: int,
    items: List[int],
    destination_path: str = SPLIT_TEST_FILES_DIR,
) -> None:
    """
    Creates a test file from the parameters of a problem.
    """
    with open(destination_path / (identifier + ".txt"), "w") as destination_file:
        destination_file.write(identifier)
        destination_file.write(
            f"\n{bin_capacity} {number_of_items} {optimal_bin_number}"
        )
        for i in range(number_of_items):
            destination_file.write(f"\n{items[i]}")
    return


def write_solution_to_file(
    method_used: str,
    identifier: str,
    bin_capacity: int,
    number_of_items: int,
    optimal_bin_number: int,
    found_bin_number: int,
    items_sizes: List[int],
    items_positions: List[int],
    destination_main_folder: str = SOLUTION_FILES_DIR,
) -> None:
    """
    Creates a file from the solution to a problem.
    """
    # Build path and eventually the needed folder
    destination_path = destination_main_folder / method_used
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    with open(destination_path / (identifier + ".txt"), "w") as destination_file:
        destination_file.write(identifier)
        destination_file.write(
            f"\n{bin_capacity} {number_of_items} {optimal_bin_number} {found_bin_number}"
        )
        for i in range(number_of_items):
            destination_file.write(f"\n{items_sizes[i]} {items_positions[i]}")
    return


if __name__ == "__main__":
    split_test_folder(BASE_TEST_FILES_DIR)
