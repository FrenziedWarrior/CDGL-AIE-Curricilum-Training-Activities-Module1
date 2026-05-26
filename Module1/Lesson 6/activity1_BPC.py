import time, pandas as pd
from textblob import TextBlob
from colorama import init, Fore
init(autoreset=True)

# TODO: Load the data from the CSV dataset
def load_data(file_path='imdb_top_1000.csv'):
    pass

movies_df = load_data()

# Get a sorted list of unique genres in the whole dataset
# genres = 

# Filters movies by genre and rating, checks overview sentiment, and returns up to n recommendations
def recommend(genre=None, mood=None, rating=None, n=5):
    pass

# Get the sentiment category from TextBlob polarity
def get_sentiment(p):
    return "Positive" if p > 0 else "Negative" if p < 0 else "Neutral"


def show(recs, name):
    print(Fore.YELLOW + f"\n AI-Analyzed Movie Recommendations for {name}:")
    for i, (t,p) in enumerate(recs, 1):
        print(f"{Fore.CYAN}{i}. {t} (Polarity: {p:.2f}, {get_sentiment(p)})")


def dots():
    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)


# Show a list of genres and get input from the user
def get_genre():
    pass


# Get input for the IMDB rating
def get_rating():
    while True:
        x = input(Fore.YELLOW + "Enter minimum IMDB rating (7.6 - 9.3) or 'skip': ").strip()
        if x.lower() == "skip":
            return None
        try:
            r = float(x)
            if 7.6 <= r <= 9.3:
                return r
            print(Fore.RED + "Rating out of range. Try again.\n")
        except ValueError:
            print(Fore.RED + "Invalid input. Try again!\n")


# Welcome message
print(Fore.BLUE + "Welcome to your Personal Movie Recommendation Assistant! \n")
name = input(Fore.YELLOW + "What's your name? ").strip()
print(f"\n{Fore.GREEN}Great to meet you, {name}!\n")
print(Fore.BLUE + "\nLet's find the perfect movie for you!\n")

# Get genre input
genre = get_genre()


# TODO: Get mood input
mood = input(Fore.YELLOW + "How do you feel today? (Describe your mood): ").strip()
print(Fore.BLUE + "\nAnalyzing mood", end="", flush=True)
dots()
# TODO: Get mood polarity


# Get rating input
rating = get_rating()
print(f"{Fore.BLUE}\nFinding movies for {name}", end="", flush=True)
dots()


# TODO: SHOW RECOMMENDATIONS


# TODO: REQUEST FOR MORE RECOMMENDATIONS