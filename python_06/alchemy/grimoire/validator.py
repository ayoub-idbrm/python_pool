def validate_ingredients(ingredients: str) -> str:
    valid_elements = ["fire", "water", "earth", "air"]
    is_valid = any(element in ingredients.lower() for element in valid_elements)
    
    if is_valid:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
