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


def generate_csv(config: Config):
    """Generate CSV file with random numbers"""
    array = np.random.rand(config.nrows, config.ncols)
    df = pd.DataFrame(array)
    df.to_csv(config.file)


def main(config: Config):
    generate_csv(config)
    # TODO
    pass


if __name__ == '__main__':
    config = Config(
        file='vectors.csv',
        nrows=501,
        ncols=11,
    )
    main(config)
