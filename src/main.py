"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    user_profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.9,
            "likes_acoustic": False,
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.4,
            "likes_acoustic": True,
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.95,
            "likes_acoustic": False,
        },
        "Adversarial Conflict": {
            "genre": "pop",
            "mood": "sad",
            "energy": 0.9,
            "likes_acoustic": False,
        },
    }

    for profile_name, user_prefs in user_profiles.items():
        print(f"\n=== {profile_name} ===")
        recommendations = recommend_songs(user_prefs, songs, k=5)
        for index, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            print(f"{index}. {song['title']} by {song['artist']}")
            print(f"   Score: {score:.2f}")
            print(f"   Reasons: {explanation}")
        print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
