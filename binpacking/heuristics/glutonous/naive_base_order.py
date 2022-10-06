from typing import Tuple

import numpy as np


def naive_base_order(
    bin_capacity: int, number_of_items: int, items_sizes: int
) -> Tuple[int, list]:
    """
    Manage items in the base order they are given,
    for each try to put it in a bin, if none fit add one.

    Complexity is O(n²), for each item i we have at most to check at most i - 1 bins
    used before.
    """
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
    return number_of_bins, items_bin_position


def naive_with_ordered_items(
    bin_capacity: int, number_of_items: int, items_sizes: int
) -> Tuple[int, list]:
    """
    Manage items in the order of descending sizes,
    for each try to put it in a bin, if none fit add one.

    Complexity is O(n²), for each item i we have at most to check at most i - 1 bins
    used before.
    """
    items_bin_position = [-1 for _ in range(number_of_items)]
    bins_left_capacity = []
    max_bin = -1

    ordering = np.argsort(np.array(items_sizes))

    for item_position in ordering:
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
    return number_of_bins, items_bin_position
