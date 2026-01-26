class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self, shade_area):
        print(f"{self.name} provides {shade_area} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


def main() -> None:
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin c")
    print("=== Garden Plant Types ===")
    print()
    print(f"{rose.name} (Flower): {rose.height}cm, "
          f"{rose.age} days, {rose.color} color")
    rose.bloom()
    print()
    print(f"{oak.name} (Tree): {oak.height}cm, "
          f"{oak.age} days, {oak.trunk_diameter}cm diameter")
    oak.produce_shade(75)
    print()
    print(f"{tomato.name} (Vegetable): {tomato.height}cm, "
          f"{tomato.age} days, {tomato.harvest_season} harvest")
    print(f"{tomato.name} is rich in {tomato.nutritional_value}")


if __name__ == "__main__":
    main()
