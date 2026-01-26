import sys


def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    idd = input("Input Stream active. Enter archivist ID: ")
    report = input("Input Stream active. Enter status report: ")
    print()

    sys.stdout.write(f"[STANDARD] Archive status from {idd}: {report}\n")
    sys.stderr.write("[ALERT] System diagnostic: "
                     "Communication channels verified\n")

    sys.stdout.write("[STANDARD] Data transmission complete\n")
    print()
    sys.stdout.write("Three-channel communication test successful.\n")


if __name__ == "__main__":
    main()
