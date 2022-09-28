from typing import Tuple

from binpacking.utils import read_single_problem_from_path


def naive_base_order(source_file_path: str) -> Tuple[int, list]:
    """
    Manage items in the base order they are given,
    for each try to put it in a bin, if none fit add one.
    """
    (
        _,
        bin_capacity,
        number_of_items,
        _,
        items_sizes,
    ) = read_single_problem_from_path(source_file_path)

    items_bin_position = [-1 for _ in range(number_of_items)]
    bins_left_capacity = []
    max_bin = -1

    for item_position in range(number_of_items):
        current_size = items_sizes[item_position]
        item_already_stored = False

        # Sanity test
        if current_size > bin_capacity:
            raise (Exception("Item is over bin capacity"))

        # Attempt to put in existing bin
        for bin_position in range(len(bins_left_capacity)):
            if bins_left_capacity[bin_position] > current_size:
                bins_left_capacity[bin_position] -= current_size
                items_bin_position[item_position] = bin_position
                item_already_stored = True
                break

        # If not possible add new bin
        if not item_already_stored:
            max_bin += 1
            bins_left_capacity.append(bin_capacity - current_size)
            items_bin_position[item_position] = max_bin

    number_of_bins = len(bins_left_capacity)
    return number_of_bins, items_bin_position, bins_left_capacity
