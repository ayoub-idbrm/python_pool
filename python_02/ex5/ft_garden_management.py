class GardenError(Exception):
    """Base class for all garden-related errors"""
    pass


class PlantError(GardenError):
    """Raised when there is a problem with plant data"""
    pass


class WaterError(GardenError):
    """Raised when there is a watering problem"""
    pass


class GardenManager:
    def __init__(self):
        self.plants = {}   # plant_name -> {"water": int, "sun": int}

    def add_plant(self, plant_name):
        try:
            if not isinstance(plant_name, str) or plant_name.strip() == "":
                raise PlantError("Plant name cannot be empty!")

            if plant_name in self.plants:
                raise PlantError(f"{plant_name} already exists in the garden!")

            # Default health values
            self.plants[plant_name] = {"water": 5, "sun": 8}
            print(f"Added {plant_name} successfully")

        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self):
        print("Opening watering system")
        try:
            if not self.plants:
                raise WaterError("No plants to water!")

            for plant in self.plants:
                print(f"Watering {plant} - success")

        except WaterError as e:
            print(f"Caught WaterError: {e}")

        finally:
            # Cleanup always happens
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name, water_level, sunlight_hours):
        try:
            if plant_name not in self.plants:
                raise PlantError(f"{plant_name} does not exist!")

            if not (1 <= water_level <= 10):
                raise ValueError(f"Water level {water_level}"
                                 " is invalid (1–10)")

            if not (2 <= sunlight_hours <= 12):
                raise ValueError(f"Sunlight hours {sunlight_hours}"
                                 " are invalid (2–12)")

            print(
                f"{plant_name}: healthy "
                f"(water: {water_level}, sun: {sunlight_hours})"
            )

        except (PlantError, ValueError) as e:
            print(f"Error checking {plant_name}: {e}")


def test_garden_management():
    print("=== Garden Management System ===")

    garden = GardenManager()

    print("\nAdding plants to garden...")
    garden.add_plant("tomato")
    garden.add_plant("lettuce")
    garden.add_plant("")          # invalid
    garden.add_plant("tomato")    # duplicate

    print("\nWatering plants...")
    garden.water_plants()

    print("\nChecking plant health...")
    garden.check_plant_health("tomato", 5, 8)
    garden.check_plant_health("lettuce", 15, 6)   # bad water level
    garden.check_plant_health("carrot", 4, 6)     # plant does not exist

    print("\nTesting error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
