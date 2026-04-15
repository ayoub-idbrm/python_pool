from typing import Tuple, Callable, List


def fireball(target) -> str:
    return f"Fireball hits {target}"


def heal(target) -> str:
    return f"Heals {target}"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args, **kwargs) -> Tuple[str, str]:
        res1 = spell1(*args, **kwargs)
        res2 = spell2(*args, **kwargs)
        return res1, res2

    return combined


def base_spell(target) -> int:
    return 10


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(*args, **kwargs) -> int:
        result = base_spell(*args, **kwargs)
        return result * multiplier

    return amplified


def is_friend(target) -> bool:
    return target == "friend"


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(*args, **kwargs) -> str:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"

    return caster


def spell_sequence(spells: List[Callable]) -> Callable:
    def sequence_func(*args, **kwargs) -> List[str]:
        results = []
        for spell in spells:
            results.append(spell(*args, **kwargs))
        return results

    return sequence_func


def lightning(target) -> str:
    return f"Lightning strikes {target}"


def main() -> None:
    print("Testing spell combiner...")
    combined_spell = spell_combiner(fireball, heal)
    combined_results = combined_spell("Dragon")
    print("Combined spell result: ", end="")
    for res in combined_results:
        print(res, end=" ")
    print()

    mega_fireball = power_amplifier(base_spell, 3)
    print("Amplified spell result:", mega_fireball("target"))

    conditional_heal = conditional_caster(is_friend, heal)
    print("Conditional cast (friend):", conditional_heal("friend"))
    print("Conditional cast (enemy):", conditional_heal("Dragon"))

    print("Testing spell sequence...")
    spells = [fireball, heal, lightning]
    sequence = spell_sequence(spells)
    sequence_results = sequence("Fire Dragon")
    print("Sequence results:", sequence_results)


if __name__ == "__main__":
    main()
