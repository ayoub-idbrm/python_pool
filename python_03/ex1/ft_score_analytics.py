import sys


def main():
    try:
        if (len(sys.argv) == 1):
            print(f"No scores provided. Usage: python3 {sys.argv[0]}"
                  " <score1> <score2> ...")
            return
        print("=== Player Score Analytics ===")
        scores = [int(arg) for arg in sys.argv[1:]]
        print(scores)
        lenght = len(sys.argv) - 1
        print(f"Total players: {lenght}")
        total = sum(scores)
        print(f"Total score: {total}")
        print(f"Averge score: {total / lenght}")
        high = max(scores)
        print(f"High score: {high}")
        low = min(scores)
        print(f"Low score: {low}")
        print(f"Score range: {high - low}")
    except ValueError as e:
        print(f"oh i gooot u : {e}")


if __name__ == "__main__":
    main()
