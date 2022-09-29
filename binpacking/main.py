from binpacking.constants import SPLIT_TEST_FILES_DIR
from binpacking.heuristics import naive_base_order, HeuristicRunner


if __name__ == "__main__":
    runner = HeuristicRunner(
        method=naive_base_order, test_directory=SPLIT_TEST_FILES_DIR
    )
    runner.run_method_on_whole_directory_and_write_solutions()
