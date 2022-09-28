from binpacking.constants import SPLIT_TEST_FILES_DIR
from binpacking.heuristics import naive_base_order


if __name__ == "__main__":
    print(naive_base_order(SPLIT_TEST_FILES_DIR / "u120_00.txt"))
