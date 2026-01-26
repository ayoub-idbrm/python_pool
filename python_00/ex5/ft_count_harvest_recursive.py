def recursion(n):
    if n == 0:
        return
    recursion(n - 1)
    print(f"Day {n}")


def ft_count_harvest_recursive():
    recursion(int(input("Days until harvest: ")))
    print("Harvest time!")
