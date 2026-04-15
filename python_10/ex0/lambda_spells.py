def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda a: a['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    result = list(map(lambda spell: "* " + spell + " *", spells))
    return result


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda m: m['power'], mages))
    return {
        'max_power': max(powers),
        'min_power': min(powers),
        'avg_power': round(sum(powers) / len(powers), 2)
    }


def main():
    artifacts = [
        {'name': 'Storm Crown', 'power': 97, 'type': 'focus'},
        {'name': 'Crystal Orb', 'power': 99, 'type': 'weapon'},
        {'name': 'Lightning Rod', 'power': 101, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 70, 'type': 'focus'}
    ]

    mages = [
        {'name': 'Alex', 'power': 55, 'element': 'ice'},
        {'name': 'Morgan', 'power': 52, 'element': 'water'},
        {'name': 'Jordan', 'power': 79, 'element': 'light'},
        {'name': 'Riley', 'power': 81, 'element': 'water'},
        {'name': 'Phoenix', 'power': 76, 'element': 'earth'}
    ]

    spells = ['shield', 'freeze', 'blizzard', 'flash']

    art_res = artifact_sorter(artifacts)
    power_filter(mages, 55)
    spe_res = spell_transformer(spells)
    mage_res = mage_stats(mages)

    print("Testing artifact sorter...")
    for index, artifact in enumerate(art_res):
        print(f"{artifact['name']} ({artifact['power']})", end=" ")
        if index != len(art_res) - 1:
            print("comes before", end=" ")

    print()

    print("Testing spell transformer...")
    for spell in spe_res:
        print(spell, end=" ")

    print()
    print("TESTING MAGE STATS....")
    print(mage_res)


if __name__ == "__main__":
    main()
