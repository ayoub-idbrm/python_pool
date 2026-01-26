def garden_operations():
    print("=== Garden Error Types Demo ===\n")
    """
    testing the first case value error
    """
    print("Testing ValueError...")
    try:
        age = int("abc")
        print(f"{age}")
    except ValueError as ve:
        print(f"Caught ValueError: {ve}\n")
    """
    testing the second case divide by zero
    """
    print("Testing ZeroDivisionError...")
    try:
        res = 100 / 0
        print(f"{res}")
    except ZeroDivisionError as z:
        print(f"Caught ZeroDivisionError: {z}\n")
    """
    testing the third case file not found
    """
    print("Testing FileNotFoundError...")
    try:
        with open("missing.txt", "r") as f:
            _ = f.read()
    except FileNotFoundError as f:
        print(f"Caught FileNotFoundError: {f}\n")
    """
    testing the fourth case keyerror
    """
    print("Testing KeyError...")
    try:
        garden_plants = {"rose": 30, "oak": 20}
        print(garden_plants["banana"])
    except KeyError as d:
        print(f"Caught KeyError: {d}\n")
    """
    testing the last case multiple errors
    """
    print("Testing multiple errors together...")
    try:
        var = int("ayoub")
        res = 100 / 0
        print(f"{var} and {res}")
    except (ValueError, ZeroDivisionError):
        print("caughtt an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    garden_operations()
