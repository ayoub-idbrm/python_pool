def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        f = open("ancient_fragment.txt", "r")
        print("connection established...\n")
        print("RECOVERED DATA:")
        print(f.read())
        f.close()
    except FileNotFoundError:
        print("Error: Storage vault not found. Run data generator first.")
    finally:
        print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
