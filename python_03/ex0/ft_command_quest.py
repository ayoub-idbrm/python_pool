import sys


def main():
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {len(sys.argv)}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {len(sys.argv) - 1}")
        i = 1
        j = 1
        while (i < len(sys.argv)):
            print(f"Arguments {j}: {sys.argv[i]}")
            j += 1
            i += 1
        print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
