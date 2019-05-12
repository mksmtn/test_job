from decimal import Decimal
from typing import List
import math
import unittest

from src.Data import Data
from src.Math import EuclideanDistance


class TestEuclideanDistance(unittest.TestCase):

    def setUp(self) -> None:
        self._data = Data(file='tests/test_vectors.csv')
        self._euclidean_distance = EuclideanDistance(self._data)

    def test_euclidean_distance_calculation(self):
        tuple_0 = (1, 1, 1)
        tuple_1 = (1, 1, 0)
        returned_dist = EuclideanDistance.calc_euclidean_distance(tuple_0, tuple_1)
        expected_dist = 1
        self.assertEqual(returned_dist, expected_dist)

        tuple_0 = (-3, 4, 0)
        tuple_1 = (0, 8, 0)
        returned_dist = EuclideanDistance.calc_euclidean_distance(tuple_0, tuple_1)
        expected_dist = 5
        self.assertEqual(returned_dist, expected_dist)

        tuple_0 = (.45, -0.3, .34)
        tuple_1 = (.43, .09, -0.9)
        returned_dist = EuclideanDistance.calc_euclidean_distance(tuple_0, tuple_1)
        expected_dist = 1.3000384609695206
        self.assertAlmostEqual(returned_dist, expected_dist)

    def test_min_distance(self):
        returned_min_dist = self._euclidean_distance.min
        expected_min_dist = (1, (0, 1))
        self.assertEqual(returned_min_dist, expected_min_dist)

    def test_max_distance(self):
        returned_max_dist = self._euclidean_distance.max
        expected_max_dist = (math.sqrt(51), (0, 3))
        self.assertEqual(returned_max_dist, expected_max_dist)

    def test_number_of_calculated_distances(self):
        returned_number = len(list(
            self._euclidean_distance._distances_generator()
        ))
        expected_number = 6
        self.assertEqual(returned_number, expected_number)

    def test_xlabels(self):
        expected_lables = ['1', '2', '3', '4', '5', '6', '7', '8']
        returned_labels = self._get_xlabels()
        self.assertListEqual(returned_labels, expected_lables)

    def test_yvalues(self):
        xlabels = self._get_xlabels()
        expected_values = [1, 0, 0, 0, 3, 0, 2, 0]
        returned_values = self._euclidean_distance._get_yvalues(xlabels)
        self.assertListEqual(returned_values, expected_values)

    def _get_xlabels(self) -> List[str]:
        return self._euclidean_distance._get_xlabels(Decimal('1'))


if __name__ == '__main__':
    unittest.main()
