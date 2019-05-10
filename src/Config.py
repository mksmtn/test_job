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
