import os
from pathlib import Path
from typing import Callable

from binpacking.utils import (
    read_single_problem_from_path,
    check_solution_validity,
    write_solution_to_file,
)


class HeuristicRunner:
    """
    Class to define a method to be used to work on the problem and the test files to use.
    """

    # Init vars
    method: Callable = None
    test_directory: Path = None
    test_file_path: Path = None
    # Problems vars
    identifier: str = None
    bin_capacity: int = None
    number_of_items: int = None
    optimal_bin_number: int = None
    items_sizes: list = None
    # Solution vars
    number_of_bins: int = None
    items_bin_position: list = None

    def __init__(
        self, method: Callable, test_directory: Path = None, test_file_path: Path = None
    ) -> None:
        self.method = method
        self.test_directory = test_directory
        self.test_file_path = test_file_path
        return

    def load_single_file(self) -> None:
        """
        Load specified file in class.
        """
        (
            self.identifier,
            self.bin_capacity,
            self.number_of_items,
            self.optimal_bin_number,
            self.items_sizes,
        ) = read_single_problem_from_path(self.test_file_path)

        return

    def write_current_solution(self) -> None:
        write_solution_to_file(
            self.method.__name__,
            self.identifier,
            self.bin_capacity,
            self.number_of_items,
            self.optimal_bin_number,
            self.number_of_bins,
            self.items_sizes,
            self.items_bin_position,
        )

    def check_current_solution_validity(self) -> None:
        assert check_solution_validity(
            self.bin_capacity,
            self.number_of_bins,
            self.number_of_items,
            self.items_sizes,
            self.items_bin_position,
        )

    def run_method_on_single_file(self) -> None:
        """Run given method on current test file."""
        self.load_single_file()
        (self.number_of_bins, self.items_bin_position) = self.method(
            self.bin_capacity, self.number_of_items, self.items_sizes
        )
        self.check_current_solution_validity()
        return

    def run_method_on_single_file_and_write_solution(self) -> None:
        """Run given method on current test file and store solution."""
        self.run_method_on_single_file()
        self.write_current_solution()
        return

    def get_current_solution(self) -> None:
        """Return solution parameters"""
        return self.number_of_bins, self.items_bin_position

    def run_method_on_whole_directory(self) -> None:
        for test_file in os.listdir(self.test_directory):
            self.test_file_path = self.test_directory / test_file
            self.run_method_on_single_file()

    def run_method_on_whole_directory_and_write_solutions(self) -> None:
        for test_file in os.listdir(self.test_directory):
            self.test_file_path = self.test_directory / test_file
            self.run_method_on_single_file_and_write_solution()