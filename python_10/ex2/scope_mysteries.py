from typing import Callable, Any


def mage_counter() -> Callable:
    counts = 0

    def clouser() -> int:
        nonlocal counts
        counts += 1
        return counts

    return clouser


def spell_accumulator(initial_power: int) -> Callable:
    y = 0

    def incres(x) -> int:
        nonlocal y
        z = x
        x += initial_power + y
        y = z
        return x

    return incres


def enchantment_factory(enchantment_type: str) -> Callable:
    def creat(items_to_enchant: str) -> str:
        return enchantment_type + " " + items_to_enchant

    return creat


def memory_vault() -> dict[str, Callable]:
    stores = {}

    def store(key, value) -> None:
        stores[key] = value

    def recall(key) -> Any:
        return stores[key] if key in stores else "Memory not found"

    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    count = mage_counter()
    count1 = mage_counter()
    print("counter_a call 1: ", count())
    print("counter_a call 2: ", count())
    print("counter_b call 2: ", count1())
    print()
    print("Testing spell accumulator...")
    Base = 100
    spell_counter = spell_accumulator(Base)
    add = 20
    print(f"Base {Base}, add {add}:", spell_counter(add))
    add = 30
    print(f"Base {Base}, add {add}:", spell_counter(add))
    print()
    print("Testing enchantment factory...")
    enchantment_types = ["Flaming", "Frozen", "Flowing"]
    items_to_enchant = ["Cloak", "Sword", "Amulet", "Shield"]
    fac = enchantment_factory(enchantment_types[0])
    print(fac(items_to_enchant[1]))
    fac1 = enchantment_factory(enchantment_types[1])
    print(fac1(items_to_enchant[-1]))
    print()
    print("Testing memory vault...")
    vualt = memory_vault()
    vualt["store"]("secret", 42)
    print("Store 'secret' = 42")
    print("Recall 'secret' :", vualt["recall"]("secret"))
    print("Recall 'unknown':", vualt["recall"]("unknown"))


if __name__ == "__main__":
    main()
