class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1

    def age_one_day(self):
        self.age += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    plant = Plant("Rose", 25, 30)
    initial_height = plant.height
    print("=== Day 1 ===")
    plant.get_info()
    for _ in range(6):
        plant.grow()
        plant.age_one_day()
    print("=== Day 7 ===")
    plant.get_info()
    print(f"Growth this week: +{plant.height - initial_height}cm")


if __name__ == "__main__":
    main()
