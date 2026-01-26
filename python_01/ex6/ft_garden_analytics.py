class Plant:

    def __init__(self, name, height, age):

        self.name = name
        self.height = height
        self.initial_height = height
        self.age = age

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):

    def __init__(self, name, height, age, color):

        super().__init__(name, height, age)
        self.color = color
        self.blooming = True


class PrizeFlower(FloweringPlant):
    """Special flowering plant with prize points"""
    def __init__(self, name, height, age, color, points):
        """
        Initialise une fleur de prix.

        Args:
            name (str): Nom de la plante.
            height (int): Hauteur de la plante en cm.
            age (int): Âge de la plante en jours.
            color (str): Couleur des fleurs.
            points (int): Points de prix associés.
        """
        super().__init__(name, height, age, color)
        self.points = points


class GardenManager:
    """Manages multiple gardens and analytics"""
    gardens = []

    class GardenStats:
        """Helper class for garden statistics"""
        @staticmethod
        def total_growth(plants):
            total = 0
            for plant in plants:
                total += 1
            return total

        @staticmethod
        def count_type(plants):
            regular = flowering = prize = 0
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

    def __init__(self, owner):
        """
        Initialise un gestionnaire de jardin.

        Args:
            owner (str): Nom du propriétaire du jardin.
        """
        self.owner = owner
        self.plants = []
        GardenManager.gardens.append(self)

    def add_plant(self, plant):
        if not GardenManager.validate_height(plant.height):
            print(f"{plant.name} has invalid height")
            return
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                print(f"- {plant.name}: {plant.height}cm, "
                      f"{plant.color} flowers (blooming), "
                      f"Prize points: {plant.points}")
            elif isinstance(plant, FloweringPlant):
                print(f"- {plant.name}: {plant.height}cm, "
                      f"{plant.color} flowers (blooming)")
            else:
                print(f"- {plant.name}: {plant.height}cm")
        print()
        growth = GardenManager.GardenStats.total_growth(self.plants)
        regular, flowering, prize = (
            GardenManager.GardenStats.count_type(self.plants))

        print(f"Plants added: {len(self.plants)}, "
              f"Total growth: {growth}cm")
        print(f"Plant types: {regular} regular, {flowering} flowering, "
              f"{prize} prize flowers")

    @staticmethod
    def validate_height(height):
        return height > 0

    @classmethod
    def create_garden_network(cls):
        scores = {}
        for garden in cls.gardens:
            score = 0
            for plant in garden.plants:
                score += plant.height
                score += (plant.height - plant.initial_height) * 10
                if isinstance(plant, PrizeFlower):
                    score += plant.points
            scores[garden.owner] = score
        return scores


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print()
    alice = GardenManager("Alice")
    bob = GardenManager("Bob")

    alice.add_plant(Plant("Oak Tree", 100, 365))
    alice.add_plant(FloweringPlant("Rose", 25, 120, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, 90, "yellow", 10))
    print()

    alice.grow_all()
    print()
    alice.report()
    print()
    print("Height validation test:", GardenManager.validate_height(10))

    bob.plants.append(Plant("Fern", 30, 60))
    bob.plants.append(FloweringPlant("Tulip", 20, 40, "pink"))
    bob.plants.append(PrizeFlower("Orchid", 15, 100, "purple", 27))

    scores = GardenManager.create_garden_network()
    print(f"Garden scores - Alice: {scores['Alice']}, Bob: {scores['Bob']}")
    print("Total gardens managed:", len(GardenManager.gardens))
