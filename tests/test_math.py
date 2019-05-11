import unittest

from src.Math import EuclideanDistance


class TestEuclidDistance(unittest.TestCase):
    def test_euclid_distance_calculation(self):
        tuple_0 = (1, 1, 1)
        tuple_1 = (1, 1, 0)
        returned_dist = EuclideanDistance.calc_euclidean_distance(tuple_0, tuple_1)
        expected_dist = 1
        self.assertEqual(returned_dist, expected_dist)

        tuple_0 = (-3, 4)
        tuple_1 = (0, 8)
        returned_dist = EuclideanDistance.calc_euclidean_distance(tuple_0, tuple_1)
        expected_dist = 5
        self.assertEqual(returned_dist, expected_dist)

        tuple_0 = (.45, -0.3, .34)
        tuple_1 = (.43, .09, -0.9)
        returned_dist = EuclideanDistance.calc_euclidean_distance(tuple_0, tuple_1)
        expected_dist = 1.3000384609695206
        self.assertAlmostEqual(returned_dist, expected_dist)


if __name__ == '__main__':
    unittest.main()
