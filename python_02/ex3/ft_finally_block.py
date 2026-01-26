def water_plants(plant_list):
    try:
        print("Opening watering system")
        for plant in plant_list:
            if not isinstance(plant, str) or plant.strip() == "":
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"watering {plant}")
    except ValueError as a:
        print(f"Error: {a}")
    finally:
        print("Closing watering system (cleanup)")


"""
    in this function i loop on every element in the
    list and print watering (it's name)
    and the function isinstance it use to check the element is a string or not.
"""


def test_watering_system():
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    good_plants = ["tomato", "lettuce", "carrots"]
    water_plants(good_plants)
    print("Watering completed successfully!\n")
    print("Testing with error...")
    bad_plants = ["tomato", None, "carrots"]
    water_plants(bad_plants)
    print()
    print("Cleanup always happens, even with errors!")


"""
    in this function i create two list or array to test the two cases
    case 1; I have all are plants.
    case 2: I have two plants and one element is none to
    see how the program will catch the error.
"""


if __name__ == "__main__":
    test_watering_system()
