# ex2/main.py
from ex2.EliteCard import EliteCard


def main():
    print("=== DataDeck Ability System ===")

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    elite = EliteCard(
        "Arcane Warrior",
        cost=2,
        rarity="epic",
        attack_power=5,
        health=10)

    print("Playing Arcane Warrior (Elite Card):")

    print("Combat phase:")
    attack_result = elite.attack("Enemy")
    print(f"Attack result: {attack_result}")

    defend_result = elite.defend(2)
    print(f"Defense result: {defend_result}")

    print("Magic phase:")
    elite.channel_mana(8)  # Add 8 mana to cast spells
    spell_result = elite.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f"Spell cast: {spell_result}")

    mana_result = elite.channel_mana(3)
    print(f"Mana channel: {mana_result}")

    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
