import os
import unittest
from random import randint

from src.Config import Config
from src.Data import Data


class TestData(unittest.TestCase):
    r = randint(0, 99999999)
    file = str(r) + '_test.csv'
    nrows = 999
    ncols = 49
    min_border = -1.0
    max_border = 1.0
    config = Config(
        file=file,
        nrows=nrows,
        ncols=ncols,
    )

    @classmethod
    def setUpClass(cls) -> None:
        Data(TestData.config)

    @classmethod
    def tearDownClass(cls) -> None:
        os.remove(TestData.file)

    def test_if_file_is_created(self):
        self.assertTrue(
            os.path.isfile(TestData.file)
        )

    def test_if_numbers_are_valid(self):
        data = Data(TestData.config)
        mn = data.data_frame[data.data_frame.columns].min().min()
        mx = data.data_frame[data.data_frame.columns].max().min()
        self.assertTrue(mn > TestData.min_border and mx < TestData.max_border)


if __name__ == '__main__':
    unittest.main()
