import random


class RandomGen:
    """
    Class for generating random numbers.
    """

    def __init__(self, random_numbers: list[int], probabilities: list[float]) -> None:
        """
        Initializes class with random numbers and their probabilities.

        :param random_numbers: List of random numbers.
        :param probabilities: List of probabilities for each number.
        """
        if len(random_numbers) != len(probabilities):
            raise ValueError("Length of random numbers and probabilities must match.")

        self._random_numbers = random_numbers

        total_probability = sum(probabilities)

        if total_probability == 0.0 or any(p < 0 for p in probabilities):
            raise ValueError(
                "Probabilities must be non-negative and sum to a positive number."
            )

        # Normalize probabilities if the total probability doesn't equal 1
        self._probabilities = (
            probabilities
            if total_probability == 1
            else [p / total_probability for p in probabilities]
        )

        # Create cumulative probabilities
        self._cumulative_prob = []
        cumulative_sum = 0
        for prob in self._probabilities:
            cumulative_sum += prob
            self._cumulative_prob.append(cumulative_sum)

    def next_num(self) -> int:
        """
        Returns one of the random numbers based on initialized probabilities.

        :return: One of the random numbers.
        """
        random_number = random.random()

        for i, cumulative_prob in enumerate(self._cumulative_prob):
            if random_number < cumulative_prob:
                return self._random_numbers[i]
