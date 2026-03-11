from .elements import create_fire, create_air, create_earth, create_water

def healing_potion():
    return (f"Healing potion brewed with {create_fire()}"
            f" and {create_water()}")

def strength_potion():
    return ("Strength potion brewed with"
            f" {create_earth()} and {create_fire()}")

def invisibility_potion():
    return ("Invisibility potion brewed with"
            f" {create_air} and {create_water}")

def wisdom_potion():
    return ("Wisdom potion brewed with all"
            f" elements: {create_water} {create_fire} {create_air} {create_earth}")