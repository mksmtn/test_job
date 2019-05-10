from src.Config import Config
from src.Data import Data


def main():
    config = Config(
        file='vectors.csv',
        nrows=501,
        ncols=11,
    )
    data = Data(config)


if __name__ == '__main__':
    main()
