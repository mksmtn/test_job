from sys import argv
from decimal import Decimal

from src.Config import Config
from src.Data import Data
from src.Math import EuclideanDistance


def main(args):
    file = 'examples/vectors.csv'
    if args[1] == 'g':
        if len(args) == 4:
            nrows = int(args[2])
            ncols = int(args[3])
        else:
            nrows = 501
            ncols = 11
        config = Config(
            file=file,
            nrows=nrows,
            ncols=ncols,
        )
        Data(config)
    elif args[1] == 'a':
        data = Data(file=file)
        ed = EuclideanDistance(data)
        with open('examples/summary.txt', 'w+') as handle:
            handle.write('min:' + str(ed.min) + '\n')
            handle.write('max:' + str(ed.max) + '\n')
            handle.write('xlabels: ' + str(ed._get_xlabels(Decimal('0.1'))) + '\n')
        ed.histogram('examples/hist.png')


if __name__ == '__main__':
    main(argv)
