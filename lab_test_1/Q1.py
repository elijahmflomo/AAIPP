"""
Q1: Demonstrate multiple list-reversal helpers in Python.

Alternative implementations were sourced via an AI-powered web search to comply
with the requirement of using an AI tool for suggestions.
"""

from __future__ import annotations
import statistics
from timeit import repeat
from typing import Callable, Iterable, List, Sequence, TypeVar


T = TypeVar("T")


def reverse_with_slice(values: Iterable[T]) -> List[T]:
    """Return a reversed copy using Python's slicing syntax."""
    return list(values)[::-1]


def reverse_with_reversed(values: Iterable[T]) -> List[T]:
    """Return a reversed copy using the built-in reversed iterator."""
    return list(reversed(list(values)))


def reverse_in_place_two_pointer(values: Sequence[T]) -> List[T]:
    """Return a reversed copy by swapping elements from both ends."""
    result = list(values)
    left, right = 0, len(result) - 1
    while left < right:
        result[left], result[right] = result[right], result[left]
        left += 1
        right -= 1
    return result


def benchmark(functions: Iterable[Callable[[Sequence[int]], List[int]]]) -> None:
    """Print microsecond-per-run timings for each implementation."""
    sizes = [10, 10**2, 10**3, 10**4, 10**5]
    header = "size".ljust(8) + " ".join(f.__name__.ljust(26) for f in functions)
    print("\nBenchmark results (µs/run):")
    print(header)
    print("-" * len(header))
    for size in sizes:
        data = list(range(size))
        number = max(100_000 // max(size, 1), 1)
        row = f"{size:<8}"
        for func in functions:
            times = repeat(
                stmt=lambda f=func, seq=data: f(seq),
                repeat=5,
                number=number,
            )
            mean = statistics.fmean(times) / number * 1_000_000
            row += f"{mean:<26.2f}"
        print(row)


if __name__ == "__main__":
    sample = [1, 2, 3, 4]
    print("slice:", reverse_with_slice(sample))
    print("reversed():", reverse_with_reversed(sample))
    print("two-pointer:", reverse_in_place_two_pointer(sample))

    benchmark(
        [
            reverse_with_slice,
            reverse_with_reversed,
            reverse_in_place_two_pointer,
        ]
    )

