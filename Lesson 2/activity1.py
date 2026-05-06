# Importing required packages
import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initializing colorama to use it in the script
colorama.init()

print(f"{Fore.CYAN}🕵️   Welcome to Sentiment Detective!   🕵️{Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA}Please enter your name:{Style.RESET_ALL} ").strip()

if not user_name:
    user_name = "Dark Knight" # What if user does not provide a name

conversation_history = []

print(f"\n{Fore.CYAN}Hello, Detective {user_name}!")

print(f"Type a sentence and I will analyze your sentences with TextBlob and show you the sentiment. I will also save your history of analyses.")

print(f"Type {Fore.YELLOW}'clear'{Fore.CYAN},{Fore.YELLOW}'history'{Fore.CYAN}, or {Fore.YELLOW}'quit'{Fore.CYAN} to quit.{Style.RESET_ALL}\n")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue

    if user_input.lower() == "quit":
        print(f"\n{Fore.BLUE} Quitting Sentiment Detective. Farewell, Agent {user_name}!{Style.RESET_ALL}")
        break
    elif user_input.lower() == "clear":
        conversation_history.clear()
        print(f"{Fore.CYAN} All conversation history cleared!{Style.RESET_ALL}")
        continue
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN} Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😞"
                else:
                    color = Fore.LIGHTBLUE_EX
                    emoji = "😭"

                print(f"{idx}. {color}{emoji} {text} "
                      f"(Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")
        continue
    
    # Let's analyze the sentiment
    polarity = TextBlob(user_input).sentiment.polarity

    # Check the polarity and decide what kind of sentiment it is
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😊"
    else:
        sentiment_type = "Neutral"
        color = Fore.LIGHTBLUE_EX
        emoji = "😭"

    # Save in the history array
    conversation_history.append((user_input, polarity, sentiment_type))

    print(f"{color}{emoji} {sentiment_type} sentiment detected! "
          f"(Polarity: {polarity:.2f})")