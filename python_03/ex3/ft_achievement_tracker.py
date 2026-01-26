def main():
    print("=== Achievement Tracker System ===")
    # set a set using set().
    player = {
        'alice': ['first_blood', 'pixel_perfect',
                  'speed_runner', 'first_blood',
                  'first_blood'],
        'bob': ['level_master', 'boss_hunter',
                'treasure_seeker', 'level_master',
                'level_master', 'first_blood'],
        'charlie': ['treasure_seeker', 'boss_hunter',
                    'combo_king', 'first_blood',
                    'boss_hunter', 'first_blood',
                    'boss_hunter', 'first_blood'],
        'diana': ['first_blood', 'combo_king',
                  'level_master', 'treasure_seeker',
                  'speed_runner', 'combo_king',
                  'combo_king', 'level_master'],
        'eve': ['level_master', 'treasure_seeker',
                'first_blood', 'treasure_seeker',
                'first_blood', 'treasure_seeker'],
        'frank': ['explorer', 'boss_hunter',
                  'first_blood', 'explorer',
                  'first_blood', 'boss_hunter']
    }

    # do a loop in full set to
    # print each player with his achievements.
    for x in player:
        print(f"Player {x} achievements: {set(player[x])}")
    print("\n=== Achievement Analytics ===")
    # storing the achievements without
    # duplicate using union() function in res variable.
    res = set()
    for p in player.values():
        res = res.union(set(p))
    print(f"All unique achievements: {res}")
    # calculate the lenght and print it
    print(f"Total unique achievements: {len(res)}\n")
    # storing the commun achievements
    # using intersection() function in com variable.
    com = set(player["alice"])
    for p in player.values():
        com = com.intersection(set(p))
    print(f"Common to all players: {com}")
    # do loop in all set to compare each
    # achievements to others to find the rare one
    rare = set()
    for a in res:
        count = 0
        for p in player.values():
            if a in p:
                count += 1
        if count == 1:
            rare.add(a)
    print(f"Rare achievements (1 player): {rare}\n")
    # storing the commun achievements
    # using intersection function in comm variable.
    comm = set(player["alice"]).intersection(set(player["bob"]))
    print(f"Alice vs Bob common: {comm}")
    # storing the unique achievements
    # to alice player using difference() fuction in ali_uni variable
    ali_uni = set(player["alice"]).difference(set(player["bob"]))
    print(f"Alice unique: {ali_uni}")
    bob_uni = set(player["bob"]).difference(set(player["alice"]))
    print(f"Bob unique: {bob_uni}")


if __name__ == "__main__":
    main()
