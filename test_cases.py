# Unittests are made for number_of_hops up to 6
# Pre-counted the number of solutions for every case.
import unittest
from solution_count import run


class Test_Cases(unittest.TestCase):

    def test_sol_key_0(self):
        results = {1: 1, 2: 2, 3: 6, 4: 12, 5: 32, 6: 64}
        for hops in range(1, 7):
            count_distinct = run(0, hops)
            self.assertEqual(results[hops], count_distinct)

    def test_sol_1(self):
        results = {1: 1, 2: 2, 3: 5, 4: 10, 5: 26, 6: 52}
        for hops in range(1, 7):
            count_distinct = run(1, hops)
            self.assertEqual(results[hops], count_distinct)

    def test_sol_2(self):
        results = {1: 1, 2: 2, 3: 4, 4: 10, 5: 20, 6: 52}
        for hops in range(1, 7):
            count_distinct = run(2, hops)
            self.assertEqual(results[hops], count_distinct)

    def test_sol_3(self):
        results = {1: 1, 2: 2, 3: 5, 4: 10, 5: 26, 6: 52}
        for hops in range(1, 7):
            count_distinct = run(3, hops)
            self.assertEqual(results[hops], count_distinct)

    def test_sol_4(self):
        results = {1: 1, 2: 3, 3: 6, 4: 16, 5: 32, 6: 84}
        for hops in range(1, 7):
            count_distinct = run(4, hops)
            self.assertEqual(results[hops], count_distinct)

    def test_sol_5(self):
        results = {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        for hops in range(1, 7):
            count_distinct = run(5, hops)
            self.assertEqual(results[hops], count_distinct)

    def test_sol_6(self):
        results = {1: 1, 2: 3, 3: 6, 4: 16, 5: 32, 6: 84}
        for hops in range(1, 7):
            count_distinct = run(6, hops)
            self.assertEqual(results[hops], count_distinct)

    def test_sol_7(self):
        results = {1: 1, 2: 2, 3: 5, 4: 10, 5: 26, 6: 52}
        for hops in range(1, 7):
            count_distinct = run(7, hops)
            self.assertEqual(results[hops],  count_distinct)

    def test_sol_8(self):
        results = {1: 1, 2: 2, 3: 4, 4: 10, 5: 20, 6: 52}
        for hops in range(1, 7):
            count_distinct = run(8, hops)
            self.assertEqual(results[hops], count_distinct)

    def test_sol_9(self):
        results = {1: 1, 2: 2, 3: 5, 4: 10, 5: 26, 6: 52}
        for hops in range(1, 7):
            count_distinct = run(9, hops)
            self.assertEqual(results[hops], count_distinct)


if __name__ == '__main__':
    unittest.main()
