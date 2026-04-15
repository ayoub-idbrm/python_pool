from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Callable, Any, List


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min,
    }
    if operation not in operations:
        raise ValueError(f"Invalid operation: {operation}")
    if not spells:
        raise ValueError("Spell list cannot be empty")
    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "v1": partial(base_enchantment, power=50),
        "v2": partial(base_enchantment, power=50),
        "v3": partial(base_enchantment, power=50),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


@singledispatch
def spell_dispatcher(spell: Any) -> str:
    return "Unknown spell type"


@spell_dispatcher.register(int)
def _(spell: int) -> str:
    return f"{spell} damage"


@spell_dispatcher.register(str)
def _(spell: str) -> str:
    return spell


@spell_dispatcher.register(list)
def _(spell: List) -> str:
    return f"{len(spell)} spells"


def main():
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("Testing spell dispatcher...")
    print(f"Damage spell: {spell_dispatcher(42)}")
    print(f"Enchantment: {spell_dispatcher('fireball')}")
    print(f"Multi-cast: {spell_dispatcher([1, 2, 3])}")
    print(spell_dispatcher(3.14))


if __name__ == "__main__":
    main()
