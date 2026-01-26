class Error(Exception):
    def __init__(self, message="a plant error catched"):
        super().__init__(message)


"""
    i use this class to costoum my error
"""


def check_plant_health(plant_name, water_level: int, sunlight_hourse: int):
    if plant_name.strip() == "":
        raise Error("Plant name cannot be empty!")
    if water_level < 1:
        raise Error(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise Error(f"Water level {water_level} is too high (max 10)")
    if sunlight_hourse < 2:
        raise Error(f"Sunlight hours {sunlight_hourse} is too low (min 2)")
    if sunlight_hourse > 12:
        raise Error(f"Sunlight hours {sunlight_hourse} is too high (max 12)")
    return f"Plant '{plant_name}' is healthy!"


"""
    this function check to us the input (name, water_level....ect)
    i use raise to  catch every error for avoiding program crashing
"""


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 8, 7))
        print()
    except Error as d:
        print(f"Error: {d}\n")
    print("Testing empty plant name...")
    try:
        check_plant_health("", 6, 10)
    except Error as f:
        print(f"Error: {f}\n")
    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 10)
    except Error as g:
        print(f"Error: {g}\n")
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 7, 0)
    except Error as h:
        print(f"Error: {h}\n")
    print("All error raising tests completed!")


"""
    this function print to us the output and we use
    try/except to avoid crash the program
"""


if __name__ == "__main__":
    test_plant_checks()
