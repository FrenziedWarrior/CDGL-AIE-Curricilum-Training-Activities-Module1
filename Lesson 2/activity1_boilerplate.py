# TODO: Importing required packages
import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initializing colorama
colorama.init(autoreset=True)

print(f"{Fore.CYAN}🕵️   Welcome to Sentiment Detective!   🕵️")

user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip()

# TODO: What if user does not provide a name? - Use a default name
if not user_name:
    user_name = "Dark Knight"

# TODO: Store conversation history as a list of tuples: (text, polarity, sentiment_type)
conversation_history = []

print(f"\n{Fore.CYAN}Hello, Detective {user_name}!")

print(f"{Fore.CYAN}Type a sentence and I will analyze your sentences with TextBlob and show you the sentiment. I will also save your history of analyses.")

print(f"{Fore.CYAN}Type {Fore.YELLOW}'clear'{Fore.CYAN},{Fore.YELLOW}'history'{Fore.CYAN}, or {Fore.YELLOW}'quit'{Fore.CYAN} to quit.\n")


# TODO: The main loop - should run forever until "quit" command is typed
while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    # Check if user did not input anything
    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.")
        continue

    # Check for commands
    if user_input.lower() == "quit":
        print(f"\n{Fore.BLUE} Quitting Sentiment Detective. Farewell, Agent {user_name}!")
        # TODO: How to quit a loop?
        break
    elif user_input.lower() == "clear":
        # TODO: Empty the conversation_history list
        conversation_history.clear()
        print(f"{Fore.CYAN} All conversation history cleared!")
        continue
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.")
        else:
            print(f"{Fore.CYAN} Conversation History:")
            # TODO: Iterate over the history and print every user-provided sentence with sentiment analysis result
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                # TODO: Based on sentiment_type, assign color & emoji
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😭"
                else:
                    color = Fore.LIGHTBLUE_EX
                    emoji = "😑"

                print(f"{idx}. {color}{emoji} {text} (Polarity: {polarity:.2f}, {sentiment_type})")
        continue
    
    # TODO: Let's analyze the sentiment
    polarity = TextBlob(user_input).sentiment.polarity

    # TODO: Check the polarity. Based on it, assign the appropriate sentiment_type, color, and emoji
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😭"
    else:
        sentiment_type = "Neutral"
        color = Fore.LIGHTBLUE_EX
        emoji = "😑"

    # TODO: After analyzing each sentence, save in the history
    conversation_history.append((user_input, polarity, sentiment_type))

    # TODO: Print result with color, emojis, and polarity
    # FORMAT: 😊 Positive sentiment detected (Polarity: 0.50)
    print(f"{color}{emoji} {sentiment_type} sentiment detected! (Polarity: {polarity:.2f})")