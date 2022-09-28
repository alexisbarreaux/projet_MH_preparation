from utils import ROOT_PATH

DIR_PATH = ROOT_PATH / "binpacking"


def split_test_file(source_file_path: str) -> None:
    """
    Takes a file containing multiple binpacking
    problems and splits it into separate files.
    """
    with open(source_file_path, "r") as source_file:
        # Get number of problems as header
        number_of_subproblems = int(source_file.readline())

        # For each get its parameters
        for i in range(number_of_subproblems):
            identifier = source_file.readline().strip()
            problems_parameters = source_file.readline().strip().split(" ")
            [bin_capacity, number_of_items, optimal_bin_numbers] = list(
                map(int, problems_parameters)
            )
            # Get the items
            for items in range(number_of_items):
                item_size = int(source_file.readline())
                print(item_size)

    return


if __name__ == "__main__":
    split_test_file(DIR_PATH / "test_files/binpack1.txt")
