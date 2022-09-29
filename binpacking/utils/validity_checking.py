def check_solution_validity(
    bin_capacity: int,
    number_of_bins: int,
    number_of_items: int,
    items_sizes: list,
    items_positions: list,
):
    """
    Assert than a given solution is indeed feasible. Here no bin should be
    overpacked.
    """
    bins_left_capacity = [bin_capacity for _ in range(number_of_bins)]
    for i in range(number_of_items):
        bins_left_capacity[items_positions[i]] -= items_sizes[i]

    return not any(bin_capacity < 0 for bin_capacity in bins_left_capacity)
