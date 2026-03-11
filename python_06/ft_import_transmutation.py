import alchemy.elements
from alchemy.elements import create_water
from alchemy.potions import healing_potion as heal
from alchemy import create_earth, create_fire, strength_potion


def main():
    print("\n=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}\n")

    print("Method 2 - Specific function import:")
    print(f"Create_water(): {create_water()}\n")

    print("Methode 3 - Aliased import:")
    print(f"heal(): {heal()}\n")

    print("Methode 4 - Multiple imports:")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}")

    print("\nAll import transmutation methods mastered!")


if __name__ == "__main__":
    main()
