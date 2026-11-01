import random

MIN_NUMBER = 1
MAX_NUMBER = 1000


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if not (MIN_NUMBER <= min <= max <= MAX_NUMBER and 1 <= quantity <= max - min + 1):
        return []

    return sorted(random.sample(range(min, max + 1), quantity))