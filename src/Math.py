from decimal import Decimal, ROUND_DOWN, ROUND_UP
from typing import Iterable, List, Tuple

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
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
        self._find_min_max()

    @property
    def max(self) -> Distance:
        """Return maximum Euclidean distance

        :return: biggest distance between vectors
        """
        return self._max

    @property
    def min(self) -> Distance:
        """Return minimum Euclidean distance

        :return: smallest distance between vectors
        """
        return self._min

    def histogram(self, file: str, step: float = 0.1):
        """Draw a histogram to file

        :param file: file name where the result should be saved
        :param step: X-axis step
        """
        xlabels = self._get_xlabels(Decimal(str(step)))
        yvalues = self._get_yvalues(xlabels)

        plt.bar(xlabels, yvalues)
        plt.xlabel('Distance')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(2))
        plt.savefig(file)

    def _distances_generator(self):
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
                    value = EuclideanDistance.calc_euclidean_distance(row_tuple_0, row_tuple_1)
                    coordinates = (outer_counter, inner_counter)
                    distance = (value, coordinates)
                    yield distance

    def _find_min_max(self):
        for distance in self._distances_generator():
            if distance[0] < self._min[0]:
                self._min = distance
            if distance[0] > self._max[0]:
                self._max = distance

    def _get_xlabels(self, step: Decimal) -> List[str]:
        """Return X-axis labels for histogram"""
        xlabels = []
        first_label = Decimal(str(self._min[0])).quantize(step, rounding=ROUND_DOWN)
        last_label = Decimal(str(self._max[0])).quantize(step, rounding=ROUND_UP)

        current_label = first_label
        while current_label <= last_label:
            xlabels.append(str(current_label))
            current_label += step

        assert xlabels[-1] == str(last_label)

        return xlabels

    def _get_yvalues(self, xlabels: List[str]) -> List[float]:
        """Return Y-axis values for histogram"""
        yvalues = [0 for _ in xlabels]
        length = len(xlabels)
        for distance in self._distances_generator():
            for i in range(length - 1):
                min_border = float(xlabels[i])
                max_border = float(xlabels[i+1])
                if min_border <= distance[0] < max_border:
                    yvalues[i] += 1

        return yvalues
