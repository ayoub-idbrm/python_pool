def main():
    print("=== Game Analytics Dashboard ===\n")

    # Game data
    data = {
        'players': {
            'alice': {'level': 41, 'total_score': 2824,
                      'sessions_played': 13, 'favorite_mode': 'ranked',
                      'achievements_count': 5},
            'bob': {'level': 16, 'total_score': 4657,
                    'sessions_played': 27, 'favorite_mode': 'ranked',
                    'achievements_count': 2},
            'charlie': {'level': 44, 'total_score': 9935,
                        'sessions_played': 21, 'favorite_mode': 'ranked',
                        'achievements_count': 7},
            'diana': {'level': 3, 'total_score': 1488,
                      'sessions_played': 21, 'favorite_mode': 'casual',
                      'achievements_count': 4},
            'eve': {'level': 33, 'total_score': 1434,
                    'sessions_played': 81, 'favorite_mode': 'casual',
                    'achievements_count': 7},
            'frank': {'level': 15, 'total_score': 8359,
                      'sessions_played': 85, 'favorite_mode': 'competitive',
                      'achievements_count': 1}
        },
        'sessions': [
            {'player': 'bob', 'duration_minutes': 94,
             'score': 1831, 'mode': 'competitive', 'completed': False},
            {'player': 'bob', 'duration_minutes': 32,
             'score': 1478, 'mode': 'casual', 'completed': True},
            {'player': 'diana', 'duration_minutes': 17,
             'score': 1570, 'mode': 'competitive', 'completed': False},
            {'player': 'alice', 'duration_minutes': 98,
             'score': 1981, 'mode': 'ranked', 'completed': True},
            {'player': 'diana', 'duration_minutes': 15,
             'score': 2361, 'mode': 'competitive', 'completed': False},
            {'player': 'eve', 'duration_minutes': 29,
             'score': 2985, 'mode': 'casual', 'completed': True},
            {'player': 'frank', 'duration_minutes': 34,
             'score': 1285, 'mode': 'casual', 'completed': True},
            {'player': 'alice', 'duration_minutes': 53,
             'score': 1238, 'mode': 'competitive', 'completed': False},
            {'player': 'bob', 'duration_minutes': 52,
             'score': 1555, 'mode': 'casual', 'completed': False},
            {'player': 'frank', 'duration_minutes': 92,
             'score': 2754, 'mode': 'casual', 'completed': True},
            {'player': 'eve', 'duration_minutes': 98,
             'score': 1102, 'mode': 'casual', 'completed': False},
            {'player': 'diana', 'duration_minutes': 39,
             'score': 2721, 'mode': 'ranked', 'completed': True},
            {'player': 'frank', 'duration_minutes': 46,
             'score': 329, 'mode': 'casual', 'completed': True},
            {'player': 'charlie', 'duration_minutes': 56,
             'score': 1196, 'mode': 'casual', 'completed': True},
            {'player': 'eve', 'duration_minutes': 117,
             'score': 1388, 'mode': 'casual', 'completed': False},
            {'player': 'diana', 'duration_minutes': 118,
             'score': 2733, 'mode': 'competitive', 'completed': True},
            {'player': 'charlie', 'duration_minutes': 22,
             'score': 1110, 'mode': 'ranked', 'completed': False},
            {'player': 'frank', 'duration_minutes': 79,
             'score': 1854, 'mode': 'ranked', 'completed': False},
            {'player': 'charlie', 'duration_minutes': 33,
             'score': 666, 'mode': 'ranked', 'completed': False},
            {'player': 'alice', 'duration_minutes': 101,
             'score': 292, 'mode': 'casual', 'completed': True},
            {'player': 'frank', 'duration_minutes': 25,
             'score': 2887, 'mode': 'competitive', 'completed': True},
            {'player': 'diana', 'duration_minutes': 53,
             'score': 2540, 'mode': 'competitive', 'completed': False},
            {'player': 'eve', 'duration_minutes': 115,
             'score': 147, 'mode': 'ranked', 'completed': True},
            {'player': 'frank', 'duration_minutes': 118,
             'score': 2299, 'mode': 'competitive', 'completed': False},
            {'player': 'alice', 'duration_minutes': 42,
             'score': 1880, 'mode': 'casual', 'completed': False},
            {'player': 'alice', 'duration_minutes': 97,
             'score': 1178, 'mode': 'ranked', 'completed': True},
            {'player': 'eve', 'duration_minutes': 18,
             'score': 2661, 'mode': 'competitive', 'completed': True},
            {'player': 'bob', 'duration_minutes': 52,
             'score': 761, 'mode': 'ranked', 'completed': True},
            {'player': 'eve', 'duration_minutes': 46,
             'score': 2101, 'mode': 'casual', 'completed': True},
            {'player': 'charlie', 'duration_minutes': 117,
             'score': 1359, 'mode': 'casual', 'completed': True}
        ],
        'game_modes': ['casual', 'competitive', 'ranked'],
        'achievements': ['first_blood', 'level_master', 'speed_runner',
                         'treasure_seeker', 'boss_hunter', 'pixel_perfect',
                         'combo_king', 'explorer']
    }

    players = data['players']
    sessions = data['sessions']
    achievements = data['achievements']

    print("=== List Comprehension Examples ===")

    high_scorers = [name for name, info in players.items()
                    if info['total_score'] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [s['score'] * 2 for s in sessions[:4]]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [name for name, info in players.items()
                      if info['sessions_played'] > 20]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")

    player_scores = {name: info['total_score']
                     for name, info in players.items()}
    print(f"Player scores: {player_scores}")

    score_categories = {
        'high': len([n for n, i in players.items()
                     if i['total_score'] > 5000]),
        'medium': len([n for n, i in players.items()
                       if 2000 <= i['total_score'] <= 5000]),
        'low': len([n for n, i in players.items()
                    if i['total_score'] < 2000])
    }
    print(f"Score categories: {score_categories}")

    achievement_counts = {name: info['achievements_count']
                          for name, info in players.items()}
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")

    # Get unique players from sessions
    unique_players = {s['player'] for s in sessions}
    print(f"Unique players: {unique_players}")

    unique_achievements = {a for a in achievements}
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {s['mode'] for s in sessions}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")

    total_players = len(players)
    print(f"Total players: {total_players}")

    total_achievements = len(achievements)
    print(f"Total unique achievements: {total_achievements}")

    all_scores = [info['total_score'] for info in players.values()]
    average_score = sum(all_scores) / len(all_scores)
    print(f"Average score: {average_score:.1f}")

    top_player = max(players.items(), key=lambda x: x[1]['total_score'])
    top_name = top_player[0]
    top_score = top_player[1]['total_score']
    top_achievements = top_player[1]['achievements_count']
    print(f"Top performer: {top_name} "
          f"({top_score} points, {top_achievements} achievements)")


if __name__ == "__main__":
    main()
