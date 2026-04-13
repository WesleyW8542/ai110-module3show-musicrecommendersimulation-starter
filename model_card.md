# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

**TuneMatch Recommender v1.0**

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

This recommender generates personalized music recommendations based on user preferences for genre, mood, energy level, and acoustic preference. It is designed for music discovery and exploration, assuming users have clear preferences for these musical attributes. This is primarily for classroom exploration and learning about recommendation systems, not for production use with real users.  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The recommender scores songs by comparing them to a user's profile preferences. It looks at the song's genre, mood, energy level, and acoustic qualities. For each song, it calculates a score where higher scores mean better matches to the user's tastes. Songs are then ranked by their scores and the top recommendations are returned.

The scoring considers:
- Genre match: songs in the user's favorite genre get a big boost
- Mood match: songs matching the preferred mood get extra points  
- Energy closeness: songs with energy levels near the user's target get higher scores
- Acoustic preference: if the user likes acoustic music, songs with high acousticness get a bonus

I implemented a weighted scoring system that combines these factors, with genre and mood being the most important factors, followed by energy match, and acoustic preference as a smaller bonus.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The model uses a small catalog of 17 songs loaded from `data/songs.csv`. The catalog includes a mix of genres such as pop, lofi, rock, ambient, jazz, synthwave, indie pop, country, hip-hop, classical, electronic, reggae, blues, and folk. The moods represented include chill, happy, intense, relaxed, moody, focused, energetic, calm, upbeat, sad, and melancholic. 

This dataset is intentionally limited for classroom exploration, so it does not fully cover the diversity of real-world music tastes. For example, there are only one classical track and one blues track, while lofi and pop are better represented. The model also lacks information about lyrics, artist similarity, user listening history, and personal behavior, so it relies solely on song metadata and preferences.

---

## 5. Strengths  

Where your system seems to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system works well for profiles where the user has a clearly defined target energy and prefers a distinct genre. It reliably surfaces songs that are close to the requested energy level and rewards exact genre and mood matches. For example, Chill Lofi users consistently receive calm, low-energy lofi tracks, while High-Energy Pop users get upbeat pop songs with energy near their target.

It is also useful as an educational tool because the scoring logic is transparent and easy to explain. The model clearly shows how genre, mood, energy, and acoustic preference interact, which makes it easier to debug and tune weight changes during experiments.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

This recommender can produce filter bubbles because it over-prioritizes the most common catalog patterns. For example, lofi appears three times and chill mood appears four times in the dataset, so chill/lofi listeners receive stronger matches than rarer tastes like classical, blues, or folk. The energy gap calculation is absolute, so users with high energy preferences can still be served songs that match energy but not mood, which is especially visible with the high-energy/sad adversarial profile. The genre boost is now reduced, so the model is more sensitive to energy and may favor songs that feel right energetically even if the genre is less preferred. The small binary acoustic bonus also fails to capture subtle acoustic nuance, meaning the system can miss richer acoustic recommendations.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

I tested four profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and an adversarial High-Energy Sad profile. I compared the top 5 recommendations for each profile before and after doubling energy importance and halving genre importance. The rankings changed noticeably, with energy-aligned tracks moving higher even when genre or mood matches were weaker. That suggests the change made the system more sensitive to energy, which is useful for energy-driven users, but it did not necessarily make recommendations more accurate for genre-specific or mood-specific listeners.

No need for numeric metrics unless you created some.


---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

The next improvements should focus on broader song coverage and more nuanced personalization. Adding tempo, valence, and user listening history would help the system understand not only energy and genre but also how songs feel emotionally. A better explanation layer could show users why each recommendation was chosen, and a diversity filter could prevent too many songs from the same genre or mood dominating the top results. Finally, supporting more complex profiles like “high-energy but mellow” would require balancing conflicting preferences rather than treating each feature equally.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps

Working through this project showed me that even a small recommender can behave in surprising ways depending on how features are weighted. I learned that genre and energy are easy-to-understand signals, but they can hide the real tradeoffs between mood and user intent. It was interesting to see that a high-energy profile could still end up recommending songs that felt wrong emotionally if the catalog did not include enough mood-matched options. This made me appreciate why real music apps need many data sources and diversity controls rather than relying on just a handful of song attributes.
