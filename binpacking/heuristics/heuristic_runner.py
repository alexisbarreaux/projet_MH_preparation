import os
from pathlib import Path
from typing import Callable
from time import time

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
    runtime: float = None
    # Runtime actions variables
    show_solution: bool = False
    show_runtime: bool = False
    verbose: bool = False
    write_solution: bool = False

    def __init__(
        self,
        method: Callable,
        test_directory: Path = None,
        test_file_path: Path = None,
        show_solution: bool = False,
        show_runtime: bool = False,
        write_solution: bool = False,
    ) -> None:
        self.method = method
        self.test_directory = test_directory
        self.test_file_path = test_file_path
        self.show_solution = show_solution
        self.show_runtime = show_runtime
        self.write_solution = write_solution
        return

    def build_base_display_message(self) -> str:
        return f"Method {self.method.__name__} ran on {self.identifier}"

    def build_display_message(self) -> str:
        print_message = self.build_base_display_message()

        if self.show_runtime:
            print_message += f" in {self.runtime}s"
        if self.show_solution:
            print_message += f" opt/res {self.optimal_bin_number}/{self.number_of_bins}"
        return print_message

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
        start_time = time()
        self.load_single_file()
        (self.number_of_bins, self.items_bin_position) = self.method(
            self.bin_capacity, self.number_of_items, self.items_sizes
        )
        # Store runtime in scientific mode with 3 digits
        self.runtime = f"{(time() - start_time):.3e}"
        # Check validity
        self.check_current_solution_validity()

        # Print if needed
        if self.show_runtime or self.show_solution:
            print(self.build_display_message())

        # Write if needed
        if self.write_solution:
            self.write_current_solution()
        return

    def get_current_solution(self) -> None:
        """Return solution parameters"""
        return self.number_of_bins, self.items_bin_position

    def run_method_on_whole_directory(self) -> None:
        for test_file in os.listdir(self.test_directory):
            self.test_file_path = self.test_directory / test_file
            self.run_method_on_single_file()
