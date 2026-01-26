import math
import random


def coordinates(x, y, z):
    return tuple((x, y, z))


def distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


def parse_coordinates(coord_string):
    try:
        parts = coord_string.split(",")
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        return tuple((x, y, z))
    except Exception as e:
        raise e


def main():
    print("=== Game Coordinate System ===\n")

    coordinates_list = [(31, -36, -24), (44, -15, -10), (-22, -33, 22),
                        (-37, 36, 22), (19, -39, 12), (4, -46, -24),
                        (-39, -23, -11), (14, 27, -24)]

    # Pick two random different coordinates
    origin, position1 = random.sample(coordinates_list, 2)

    print("Position created", position1)
    print("Origin:", origin)
    dis = distance(origin, position1)
    print("Distance betweeen", origin, "and", position1, ": ", f"{dis:.2f}\n")
    print('Parsing coordinates: "3,4,0"')
    try:
        parse = parse_coordinates("3,4,0")
        print("Parsed position:", parse)
        diss = distance(origin, parse)
        print(f"Distance between: {origin} and {parse}: {diss}\n")
    except Exception as e:
        print(f"Error parsing cordinates: {e}")
    print('Parsing invalid coordinates: "abc,def,ghi"')
    try:
        parse_coordinates("abc,def,ghi")
    except Exception as e:
        print("Error parsing coordinates:", e)
        print(f'Error details - Type: ValueError, Args: ("{e}")')
    print("\nUnpacking demonstration:")
    x, y, z = position1
    print("Player at x=", x, ", y=", y, ", z=", z)
    print("Coordinates: X=", x, ", Y=", y, ", Z=", z)


if __name__ == "__main__":
    main()
