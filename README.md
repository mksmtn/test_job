# Generate vectors and show distribution

## Requirements

- Python 3.6+
- Installed requirements (see requirements.txt)

## Generating CSV

File `examples/vectors.csv` will be created

    python main.py g

## Analyzing

Based on file `examples/vectors.csv`, `examples/summary.txt`, `examples/hist.png` will be created

    python main.py a

In `examples/summary.txt`, the result will be in the following format:

    min:(distance, (row, column))
    max:(disatnce, (row, column))

## Running tests

    python -m tests.test_data
    python -m tests.test_math
