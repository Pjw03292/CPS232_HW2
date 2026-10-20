"""Check both algorithms against Python membership on exhaustive small inputs."""
from itertools import combinations_with_replacement
import unittest
from part1 import binary, prepare
from part2 import search


class SearchTests(unittest.TestCase):
    def test_exhaustive_sorted_lists(self):
        for size in range(8):
            for values in combinations_with_replacement(range(-2, 4), size):
                for target in range(-3, 5):
                    with self.subTest(values=values, target=target):
                        self.assertEqual(binary(values, target), target in values)
                        index = search(values, target)
                        self.assertEqual(index != -1, target in values)
                        if index != -1:
                            self.assertEqual(values[index], target)

    def test_arbitrary_input_preprocessing(self):
        values = [33, 3, 40, 11, 21, 9, 16]
        prepared = prepare(values)
        self.assertEqual(values, [33, 3, 40, 11, 21, 9, 16])
        for target in range(42):
            self.assertEqual(binary(prepared, target), target in values)

    def test_large_bounds_and_missing_targets(self):
        values = list(range(0, 20000, 2))
        for target in [-1, 0, 1, 8, 8192, 19998, 19999, 20000]:
            index = search(values, target)
            self.assertEqual(index != -1, target in values)
            if index != -1:
                self.assertEqual(values[index], target)


if __name__ == "__main__":
    unittest.main()
