files = [
    "lost_archive.txt",
    "classified_vault.txt",
    "standard_archive.txt"
]

print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")


def main(filename: str) -> None:
    try:
        if filename == "standard_archive.txt":
            print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
            with open(filename, "r") as g:
                print("SUCCESS: Archive recovered - ``" + g.read() + "``")
                print("STATUS: Normal operations resumed\n")
        else:
            print(f"CRISIS ALERT: Attempting access to '{filename}'...")
            with open(filename, "r") as f:
                f.read()

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")


for file in files:
    main(file)

print("All crisis scenarios handled successfully. Archives secure.")
