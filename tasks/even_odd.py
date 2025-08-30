__all__ = ("even_odd",)


def even_odd(numbers: list[int]) -> float:
    """Определяет отношение суммы четных элементов списка
    к сумме нечетных.

    Example:
        >> even_odd([1, 2, 3, 4, 5])
        0.6667
    """
    sum_of_not_evens =  sum([i for i in numbers if i % 2 == 1])
    return sum([i for i in numbers if i % 2 == 0]) / sum_of_not_evens \
        if sum_of_not_evens != 0 \
        else 0
