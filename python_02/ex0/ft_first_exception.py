def check_temperature(temp_str):
    try:
        tmp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return
    if (tmp >= 0 and tmp <= 40):
        print(f"Temperature {tmp}°C is perfect for plants!\n")
    elif (tmp < 0):
        print(f"Error: {tmp}°C is too cold for plants (min 0°C)\n")
    elif (tmp > 40):
        print(f"Error: {tmp}°C is too hot for plants (max 40°C)\n")
    """
    this function check to us every input is it more that 40 or less than 0
    then it print for each case his output.
    """


def main() -> None:
    print("=== Garden Temperature Checker ===\n")
    check_temperature(input("Testing temperature: "))
    check_temperature(input("Testing temperature: "))
    check_temperature(input("Testing temperature: "))
    check_temperature(input("Testing temperature: "))
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
