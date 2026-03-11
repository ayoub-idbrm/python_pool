import alchemy
import alchemy.elements

def main():
    print("=== Sacred Scroll Mastery ===\n")
    
    print("Testing direct module access:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(f"alchemy.elements.create_water(): {alchemy.elements.create_water()}")
    print(f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}")
    print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")
    
    print("\nTesting package-level access (controlled by __init__.py):")
    
    # Test fire - exposed
    try:
        print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    except AttributeError as e:
        print(f"alchemy.create_fire(): AttributeError - {e}")
        
    # Test water - exposed
    try:
        print(f"alchemy.create_water(): {alchemy.create_water()}")
    except AttributeError as e:
        print(f"alchemy.create_water(): AttributeError - {e}")
        
    # Test earth - not exposed
    try:
        print(f"alchemy.create_earth(): {alchemy.create_earth()}")
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")
        
    # Test air - not exposed
    try:
        print(f"alchemy.create_air(): {alchemy.create_air()}")
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")
        
    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")

if __name__ == "__main__":
    main()
