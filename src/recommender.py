import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numeric fields."""
    songs: List[Dict] = []
    print(f"Loading songs from {csv_path}...")

    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against user preferences and return the score plus reasons."""
    score = 0.0
    reasons: List[str] = []

    if song.get("genre") == user_prefs.get("genre"):
        score += 1.0
        reasons.append("genre match (+1.0)")

    if song.get("mood") == user_prefs.get("mood"):
        score += 1.0
        reasons.append("mood match (+1.0)")

    target_energy = float(user_prefs.get("energy", 0.0))
    energy_diff = abs(song.get("energy", 0.0) - target_energy)
    energy_score = max(0.0, 4.0 - energy_diff * 4)
    score += energy_score
    reasons.append(f"energy closeness (+{energy_score:.2f})")

    if "likes_acoustic" in user_prefs:
        wants_acoustic = bool(user_prefs["likes_acoustic"])
        is_acoustic = song.get("acousticness", 0.0) > 0.5
        if wants_acoustic == is_acoustic:
            score += 0.5
            reasons.append("acoustic preference match (+0.5)")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank songs by score and return the top k recommendation tuples."""
    scored_songs: List[Tuple[Dict, float, str]] = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored_songs.append((song, score, explanation))

    ranked = sorted(scored_songs, key=lambda item: item[1], reverse=True)
    return ranked[:k]
