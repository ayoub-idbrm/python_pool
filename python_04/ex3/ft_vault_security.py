def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    print("SECURE EXTRACTION:")

    with open("classified_data.txt", "r") as vault:
        data = vault.read()
        print(data)

    print("\nSECURE PRESERVATION:")

    with open("new_security_protocols.txt", "w") as vault:
        vault.write("[CLASSIFIED] New security protocols archived\n")
        print("[CLASSIFIED] New security protocols archived")

    print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
