from typing import Iterable, List, Tuple
import heapq

import numpy as np

from src.Data import Data


# Type aliases

Value = float
Coordinates = Tuple[int, int]
Distance = Tuple[Value, Coordinates]

# End Type aliases


class EuclideanDistance:
    """Tools for working with Euclidean distances

    After instantiation stores all Euclidean distances in a priority queue
    (min heap).
    """

    @staticmethod
    def calc_euclidean_distance(vector_0: Iterable[float], vector_1: Iterable[float]) -> float:
        array_0 = np.array(vector_0)
        array_1 = np.array(vector_1)
        return np.linalg.norm(array_0 - array_1)

    def __init__(self, data: Data):
        self._data = data
        self._distances = self._calc_all_euclidean_distances()

    def max(self) -> Distance:
        """Return maximum Euclidean distance

        Calculate Euclidean distances between vectors in the current DataFrame
        and return the biggest distance

        :return: biggest distance between vectors
        """
        return self._distances[-1]

    def min(self) -> Distance:
        """Return minimum Euclidean distance

        Calculate Euclidean distances between vectors in the current DataFrame
        and return the smallest distance

        :return: smallest distance between vectors
        """
        return self._distances[0]

    def histogram(self, file: str):
        """Draw a histogram to file

        :param file: file name where the result should be saved
        """
        pass

    def _calc_all_euclidean_distances(self) -> List[Distance]:
        distances_heap = []

        outer_counter = -1

        for row_tuple_0 in self._data.data_frame.itertuples(index=False):
            inner_counter = -1
            outer_counter += 1

            for row_tuple_1 in self._data.data_frame.itertuples(index=False):
                inner_counter += 1

                same_vector = outer_counter == inner_counter
                already_calculated = outer_counter > inner_counter
                are_pair_good = not same_vector and not already_calculated

                if are_pair_good:
                    distance = EuclideanDistance.calc_euclidean_distance(row_tuple_0, row_tuple_1)
                    coordinates = (outer_counter, inner_counter)
                    heap_element = (distance, coordinates)
                    heapq.heappush(distances_heap, heap_element)

        return distances_heap
