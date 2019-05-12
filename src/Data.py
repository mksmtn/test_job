import numpy as np
import pandas as pd

from src.Config import Config


class Data:
    """Vectors' data from CSV file"""

    _bothProvidedMsg = 'Either `config` or `file` argument should be provided, but not both'
    _noneProvidedMsg = 'Neither `config` nor `file` argument is provided'

    @staticmethod
    def generate_csv(config: Config) -> pd.DataFrame:
        """Generate CSV file with random numbers"""
        array = np.random.rand(config.nrows, config.ncols)
        signs = [-1, 1]

        for row_number in range(config.nrows):
            for col_number in range(config.ncols):
                sign = np.random.choice(signs)
                array[row_number][col_number] = sign * array[row_number][col_number]

        df = pd.DataFrame(array)
        df.to_csv(config.file, header=False, index=False)
        return df

    def __init__(self, config: Config = None, file: str = None):
        """Create or load CSV data

        If `config` is provided, a new CSV file is created.
        If `file` is provided, data gets loaded from that file.
        If both are provided, `TypeError` is thrown.

        :raises TypeError: if given both `config` and `file` arguments, or neither
        """
        if config and file:
            raise TypeError(Data._bothProvidedMsg)

        if not config and not file:
            raise TypeError(Data._noneProvidedMsg)

        if file:
            self._df = pd.read_csv(file, header=None, index_col=False)
        elif config:
            self._df = Data.generate_csv(config)

    @property
    def data_frame(self) -> pd.DataFrame:
        return self._df
