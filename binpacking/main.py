from binpacking.constants import SPLIT_TEST_FILES_DIR
from binpacking.heuristics import naive_base_order, HeuristicRunner


if __name__ == "__main__":
    runner = HeuristicRunner(
        method=naive_base_order,
        test_directory=SPLIT_TEST_FILES_DIR,
        show_solution=True,
        show_runtime=True,
        verbose=True,
    )
    runner.run_method_on_whole_directory()
