import sys
import os
import site


env = os.getenv("VIRTUAL_ENV")

if env:
    env_name = os.path.basename(env)

    print("MATRIX STATUS: Welcome to the construct\n")

    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment : {env_name}")
    print(f"Environment Path: {env}\n")

    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")

    site_packages = site.getsitepackages()[0]
    print("Package installation path:")
    print(f"{site_packages}")
else:
    print("MATRIX STATUS: You're still plugged in\n")

    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")

    print("\nTo enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate # On Windows")

    print("\nThen run this program again.")
