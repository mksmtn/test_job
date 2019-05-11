from typing import Iterable

import numpy as np

from src.Data import Data


class EuclideanDistance:
    """Tools for working with Euclidean distance"""

    @staticmethod
    def calc_euclidean_distance(vector_0: Iterable[float], vector_1: Iterable[float]) -> float:
        array_0 = np.array(vector_0)
        array_1 = np.array(vector_1)
        return np.linalg.norm(array_0 - array_1)

    def __init__(self, data: Data):
        self._data = data

    def min(self) -> float:
        """Return minimum Euclidean distance

        Calculate Euclidean distance between vectors in the current DataFrame
        and return the smallest distance

        :return: smallest distance between vectors
        """
        pass

    def _calc_all_euclidean_distances(self):
        for row_tuple_0 in self._data.data_frame.itertuples():
            for row_tuple_1 in self._data.data_frame.itertuples():
                EuclideanDistance.calc_euclidean_distance(row_tuple_0, row_tuple_1)
