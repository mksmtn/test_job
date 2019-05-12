from typing import Iterable, List, Tuple
import heapq

import matplotlib.pyplot as plt
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
        self._max = (float('-inf'), (0, 0))
        self._min = (float('inf'), (0, 0))
        self._distances = self._calc_all_euclidean_distances_and_set_min_max()

    def max(self) -> Distance:
        """Return maximum Euclidean distance

        :return: biggest distance between vectors
        """
        return self._max

    def min(self) -> Distance:
        """Return minimum Euclidean distance

        :return: smallest distance between vectors
        """
        return self._min

    def histogram(self, file: str) -> List[float]:
        """Draw a histogram to file

        :param file: file name where the result should be saved

        :return: values used in histogram
        """
        bars_count = 21
        names = [str(round(x / 10 - 1, 1)) for x in range(bars_count)]
        values = [0 for _ in range(bars_count)]

        index = 0

        for distance in self._distances:
            distance_value = distance[0]
            threshold = float(names[index])
            while threshold < distance_value and index < bars_count - 1:
                index += 1
                threshold = float(names[index])
            print(threshold)
            print(distance)
            values[index] += 1

        plt.bar(names, values)
        plt.savefig(file, dpi=600)

        return values

    def _calc_all_euclidean_distances_and_set_min_max(self) -> List[Distance]:
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

                    if distance < self._min[0]:
                        self._min = heap_element
                    if distance > self._max[0]:
                        self._max = heap_element

        return distances_heap
