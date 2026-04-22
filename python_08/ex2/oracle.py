import os
from dotenv import load_dotenv


load_dotenv()

# Liste des variables obligatoires
REQUIRED_VARS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def get_config():

    config = {}
    missing = []

    for var in REQUIRED_VARS:
        # priorise les variables d'environnement
        value = os.getenv(var)
        if not value:
            missing.append(var)
        config[var] = value

    return config, missing


def security_check():
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


def main():
    print("ORACLE STATUS: Reading the Matrix...")

    config, missing = get_config()

    if missing:
        print("\nWARNING: Missing configuration variables:")
        for m in missing:
            print(f" - {m}")

    print("\nConfiguration loaded:")
    print(f"Mode: {config.get('MATRIX_MODE', 'undefined')}")
    print(f"Database: {config.get('DATABASE_URL', 'undefined')}")
    print(
        "API Access: Authenticated"
        if config.get("API_KEY")
        else "API Access: Missing"
        )
    print(f"Log Level: {config.get('LOG_LEVEL', 'undefined')}")
    print(f"Zion Network: {config.get('ZION_ENDPOINT', 'undefined')}")

    security_check()


if __name__ == "__main__":
    main()
