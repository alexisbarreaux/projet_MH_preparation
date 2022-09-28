from typing import Tuple, List

from binpacking.constants import BASE_TEST_FILES_DIR, SPLIT_TEST_FILES_DIR


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
    [bin_capacity, number_of_items, optimal_bin_numbers] = list(
        map(int, problems_parameters)
    )
    # Get the items
    items = [int(source_file.readline()) for j in range(number_of_items)]

    return (
        identifier,
        bin_capacity,
        number_of_items,
        optimal_bin_numbers,
        items,
    )


def write_test_file_from_parameters(
    identifier: str,
    bin_capacity: int,
    number_of_items: int,
    optimal_bin_numbers: int,
    items: List[int],
    destination_path: str = SPLIT_TEST_FILES_DIR,
) -> None:
    """
    Creates a test file from the parameters of a problem.
    """
    with open(destination_path / (identifier + ".txt"), "w") as destination_file:
        destination_file.write(identifier)
        destination_file.write(
            "\n" + f"{bin_capacity} {number_of_items} {optimal_bin_numbers}"
        )
        for i in range(number_of_items):
            destination_file.write("\n" + str(items[i]))
    return


if __name__ == "__main__":
    split_test_file(BASE_TEST_FILES_DIR / "binpack1.txt")
