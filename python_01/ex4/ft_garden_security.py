class secureplant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = 0
        self._age = 0
        print("=== Garden Security System ===")
        print(f"Plant created: {name}")
        self.set_height(height)
        self.set_age(age)
        print()

    def set_height(self, height):
        if (height < 0):
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age):
        if (age < 0):
            print(f"Invalid operation attempted: height {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def __str__(self):
        return (f"{self.name} ({self._height}cm, {self._age} days)")


if __name__ == "__main__":
    plant = secureplant("Rose", 25, 30)
    plant.set_height(-5)
    print()
    print(f"Current plant: {plant}")
