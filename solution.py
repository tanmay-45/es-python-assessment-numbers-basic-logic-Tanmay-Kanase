def even_or_odd(n: int) -> str:
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


def add_all(numbers: list) -> int:
    total = 0

    for number in numbers:
        total = total + number

    return total