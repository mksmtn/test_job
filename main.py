import numpy as np
import pandas as pd


def generate_csv(file: str, nrows: int, ncols: int):
    """Generate CSV file with random numbers

    :param file: Name of CSV file to write numbers
    :param nrows: Number of rows in the generated CSV file
    :param ncols: Number of columns in the generated CSV file
    """

    array = np.random.rand(nrows, ncols)
    df = pd.DataFrame(array)
    df.to_csv(file)


def main():
    # generate_csv()
    # TODO
    pass


if __name__ == '__main__':
    main()
