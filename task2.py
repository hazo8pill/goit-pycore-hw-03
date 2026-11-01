"""Task 2: generate a sorted set of unique lottery numbers."""

import random

# Allowed bounds for any ticket number.
MIN_NUMBER = 1
MAX_NUMBER = 1000


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """Return `quantity` unique random numbers from [min, max], sorted ascending.

    Parameter names shadow the builtins `min`/`max` because the assignment
    specifies this signature.

    Args:
        min: Smallest allowed number, at least MIN_NUMBER (1).
        max: Largest allowed number (inclusive), at most MAX_NUMBER (1000).
        quantity: How many numbers to draw; 1..(max - min + 1).

    Returns:
        Sorted list of unique numbers, or [] if any parameter is out of range.

    Examples:
        >>> ticket = get_numbers_ticket(1, 49, 6)
        >>> len(ticket), len(set(ticket)), ticket == sorted(ticket)
        (6, 6, True)
        >>> get_numbers_ticket(1, 5, 6)  # can't draw 6 unique from 5
        []
    """

    if not (MIN_NUMBER <= min <= max <= MAX_NUMBER and 1 <= quantity <= max - min + 1):
        return []

    return sorted(random.sample(range(min, max + 1), quantity))
