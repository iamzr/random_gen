# Random Number Generator

`RandomGen` is a Python class for generating random numbers based on specified probabilities. This class allows you to define a set of random numbers and their associated probabilities, and then retrieve a random number based on those probabilities.

## Features

- Initialize a list of random numbers with corresponding probabilities.
- Automatically normalizes probabilities that do not sum to 1.
- Generates random numbers according to the specified probabilities.

## Installation

This project requires Python 3.12 and above. There are no external dependencies required.

## Usage

### Initialization

To create an instance of `RandomGen`, you need to provide a list of random numbers and their corresponding probabilities.

```python
from random_gen import RandomGen 

random_numbers = [1, 2, 3]
probabilities = [0.2, 0.3, 0.5]

gen = RandomGen(random_numbers, probabilities)
```
### Generate Random Numbers
You can generate a random number using the `next_num` method:

```python
random_number = gen.next_num()

print(random_number)  # Outputs one of the random numbers based on the defined probabilities
```

## Example
Here's a complete example of how to use the RandomGen class:

```python
from random_gen import RandomGen

# Define random numbers and their corresponding probabilities
random_numbers = [10, 20, 30]
probabilities = [0.1, 0.3, 0.6]

# Create an instance of RandomGen
gen = RandomGen(random_numbers, probabilities)

# Generate and print random numbers based on the specified probabilities
for _ in range(10):
    print(gen.next_num())
```

## Error Handling
The RandomGen class raises the following exceptions:

- `ValueError`: If the lengths of random_numbers and probabilities do not match.
- `ValueError`: If any probability is negative or if the sum of probabilities is zero.

## Testing

Unit tests are available to ensure the correct functionality of the `RandomGen` class. You can use the `pytest` framework to run the tests.

### Running Tests

To run the tests, make sure you have `pytest` installed. If you haven't installed it yet, you can do so using pip:

```bash
pip install pytest
```

Once pytest is installed, you can run the tests with the following command:

```commandline
pytest
```