from ex0.CreatureCard import CreatureCard


def main():
    try:
        print("=== DataDeck Card Foundation ===\n")
        print("Testing Abstract Base Class Design:\n")
        # create a creature card
        print("CreatureCard Info:")
        creature = CreatureCard(
            "Fire Dragon",
            5,
            "Legendary",
            7,
            5,
        )
        # calling overrided function get_card_info
        print(creature.get_card_info(), "\n")

        # game state will be passed to play to retrieve mana
        # and check if it bigger than card.cost
        print("Playing Fire Dragon with 6 mana available:")
        game_state = {
            "available_mana": 6,
        }

        print(
            "Playable:",
            creature.is_playable(game_state["available_mana"]),
        )

        game_result = creature.play(game_state)
        print(game_result, "\n")

        print("Fire Dragon attacks Goblin Warrior:")
        print(creature.attack_target("Goblin Warrior"), "\n")
        # testing 3 value for mana to check we can play
        print("Testing insufficient mana (3 available):")
        print("Playable:", creature.is_playable(3), "\n")

        print("Abstract pattern successfully demonstrated!")
    # the block except executed in case of passing health or attack < 0
    except ValueError as e:
        print(e)


main()
