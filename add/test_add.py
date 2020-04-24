""" Tests for add. """
from copy import deepcopy
import unittest

from add import add


class AddTests(unittest.TestCase):

    """ Tests for add. """

    def test_single_items(self):
        """ Tests for single items """
        self.assertEqual(add([[5]], [[-2]]), [[3]])

    def test_two_by_two_matrixes(self):
        """ Tests for two by two matrixes """
        matrix_1 = [[6, 6], [3, 1]]
        matrix_2 = [[1, 2], [3, 4]]
        matrix_3 = [[7, 8], [6, 5]]
        self.assertEqual(add(matrix_1, matrix_2), matrix_3)

    def test_two_by_three_matrixes(self):
        """ Tests for two by three matrixes """
        matrix_1 = [[1, 2, 3], [4, 5, 6]]
        matrix_2 = [[-1, -2, -3], [-4, -5, -6]]
        matrix_3 = [[0, 0, 0], [0, 0, 0]]
        self.assertEqual(add(matrix_1, matrix_2), matrix_3)

    def test_input_unchanged(self):
        """ Tests for input unchanged """
        matrix_1 = [[6, 6], [3, 1]]
        matrix_2 = [[1, 2], [3, 4]]
        matrix_1_original = deepcopy(matrix_1)
        matrix_2_original = deepcopy(matrix_2)
        add(matrix_1, matrix_2)
        self.assertEqual(matrix_1, matrix_1_original)
        self.assertEqual(matrix_2, matrix_2_original)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_any_number_of_matrixes(self):
        """ Tests for any number of matrixes """
        matrix_1 = [[6, 6], [3, 1]]
        matrix_2 = [[1, 2], [3, 4]]
        matrix_3 = [[2, 1], [3, 4]]
        matrix_4 = [[9, 9], [9, 9]]
        matrix_5 = [[31, 32], [27, 24]]
        self.assertEqual(add(matrix_1, matrix_2, matrix_3), matrix_4)
        self.assertEqual(
            add(
                matrix_2,
                matrix_3,
                matrix_1,
                matrix_1,
                matrix_2,
                matrix_4,
                matrix_1,
            ),
            matrix_5,
        )

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_different_matrix_size(self):
        """ Tests for different matrix size """
        matrix_1 = [[6, 6], [3, 1]]
        matrix_2 = [[1, 2], [3, 4], [5, 6]]
        matrix_3 = [[6, 6], [3, 1, 2]]
        with self.assertRaises(ValueError):
            add(matrix_1, matrix_2)
        with self.assertRaises(ValueError):
            add(matrix_1, matrix_3)
        with self.assertRaises(ValueError):
            add(matrix_1, matrix_1, matrix_1, matrix_3, matrix_1, matrix_1)
        with self.assertRaises(ValueError):
            add(matrix_1, matrix_1, matrix_1, matrix_2, matrix_1, matrix_1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
