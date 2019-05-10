import os

import numpy as np
import pandas as pd


class Config:
    """Holds some project-related variables"""

    def __init__(self, file: str, nrows: int, ncols: int):
        """

        :param file: Name of CSV file to write numbers
        :param nrows: Number of rows in the generated CSV file
        :param ncols: Number of columns in the generated CSV file
        """
        self._file = file
        self._nrows = nrows
        self._ncols = ncols

    @property
    def file(self) -> str:
        return self._file

    @property
    def nrows(self) -> int:
        return self._nrows

    @property
    def ncols(self) -> int:
        return self._ncols


class Data:
    """Creates or loads CSV data"""
    def __init__(self, config: Config):
        self._config = config

        if os.path.isfile(config.file):
            self._df = pd.read_csv(config.file)
        else:
            self._df = self._generate_csv()

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


def main():
    config = Config(
        file='vectors.csv',
        nrows=501,
        ncols=11,
    )
    data = Data(config)


if __name__ == '__main__':
    main()