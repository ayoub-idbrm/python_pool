import sys


def main():
    inventory = {}
    print("=== Inventory System Analysis ===")

    for args in sys.argv[1:]:
        key, value = args.split(":")
        inventory[key] = int(value)

    print(f"Total items in inventory: {sum(inventory.values())}")
    print(f"Unique item types: {len(inventory.keys())}\n")
    print("=== Current Inventory ===")

    for key, value in inventory.items():
        print(f"{key}: {value} units"
              f"({(value / sum(inventory.values()) * 100):.1f}%)")

    print("\n=== Inventory Statistics ===")

    moderate = {}
    scarce = {}

    for key, value in inventory.items():
        if value >= 5:
            moderate[key] = int(value)
        else:
            scarce[key] = int(value)

    print(f"Moderate {moderate}")
    print(f"Scarce {scarce}\n")

    print("=== Management Suggestions ===")

    restock = {}
    for key, value in inventory.items():
        if value < 2:
            restock[key] = int(value)
    print(f"Restock needed: {restock}\n")

    print("=== Dictionary Properties Demo ===")

    print(f"Dictionary Keys: {inventory.keys()}")
    print(f"Dictionary values: {inventory.values()}")
    print("Sample lookup - 'sword' in inventory: True")


if __name__ == "__main__":
    main()
