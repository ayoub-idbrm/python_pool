def ft_garden_intro() -> None:
    """
    stock our plantes on variables.
    """
    plant = "Rose"
    Height = 25
    Age = 30
    """
    print each variable.
    """
    print(f"Plant : {plant}")
    print(f"Height : {Height}cm")
    print(f"Age : {Age} days")


def main() -> None:
    print("=== Welcome to My Garden ===")
    ft_garden_intro()
    print()
    print("=== End of Program ===")


"""
protect our file for not executing the program when we call it on other file.
"""
if __name__ == "__main__":
    main()
