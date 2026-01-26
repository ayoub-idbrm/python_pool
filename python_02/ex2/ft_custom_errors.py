class GardenError(Exception):
    def __init__(self,  message="A garden error catched"):
        super().__init__(message)


"""
we inherits from exception just for make our own error (message)
"""


class PlantError(GardenError):
    def __init__(self, message="a plant error catched"):
        super().__init__(message)


"""
i make this class to base on it to built my error using plant_health function
"""


class WaterError(GardenError):
    def __init__(self, message="A water error catched"):
        super().__init__(message)


"""
i make this class to base on it to built my error using check_water function
"""


def plant_health(is_wilting):
    if is_wilting:
        raise PlantError("The tomato plant is wilting!")


"""
this function check the plant and
replace the message on PlantError to  the our error message
"""


def check_water(water_amount):
    if water_amount <= 0:
        raise WaterError("Not enough water in the tank!")


"""
this function check the water amount and
replace the message on WaterError to  the our error message
"""


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        plant_health(True)
    except PlantError as p:
        print(f"Caught WaterError: {p}\n")
    print("Testing WaterError...")
    try:
        check_water(0)
    except WaterError as w:
        print(f"Caught WaterError: {w}\n")
    print("Testing catching all garden errors...")
    try:
        plant_health(True)
    except PlantError as a:
        print(f"Caught a garden error: {a}")
    try:
        check_water(0)
    except WaterError as b:
        print(f"Caught a garden error: {b}\n")
    print("All custom error types  work correctly!")
