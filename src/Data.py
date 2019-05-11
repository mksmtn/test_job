from os import path

import numpy as np
import pandas as pd

from src.Config import Config


class Data:
    """Creates or loads CSV data"""
    def __init__(self, config: Config):
        self._config = config

        if path.isfile(config.file):
            self._df = pd.read_csv(config.file)
        else:
            self._df = self._generate_csv()

    @property
    def data_frame(self) -> pd.DataFrame:
        return self._df

    def _generate_csv(self) -> pd.DataFrame:
        """Generate CSV file with random numbers"""
        array = np.random.rand(self._config.nrows, self._config.ncols)
        signs = [-1, 1]

        for row_number in range(self._config.nrows):
            for col_number in range(self._config.ncols):
                sign = np.random.choice(signs)
                array[row_number][col_number] = sign * array[row_number][col_number]

        df = pd.DataFrame(array)
        df.to_csv(self._config.file)
        return df
