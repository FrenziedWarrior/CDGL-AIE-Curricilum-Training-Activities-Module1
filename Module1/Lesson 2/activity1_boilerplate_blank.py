# TODO: Importing required packages

# Initializing colorama
colorama.init(autoreset=True)

print(f"{Fore.CYAN}🕵️   Welcome to Sentiment Detective!   🕵️")

user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip()

# TODO: What if user does not provide a name? - Use a default name

# TODO: Store conversation history as a list of tuples: (text, polarity, sentiment_type)
conversation_history = []

print(f"\n{Fore.CYAN}Hello, Detective {user_name}!")

print(f"{Fore.CYAN}Type a sentence and I will analyze your sentences with TextBlob and show you the sentiment. I will also save your history of analyses.")

print(f"{Fore.CYAN}Type {Fore.YELLOW}'clear'{Fore.CYAN},{Fore.YELLOW}'history'{Fore.CYAN}, or {Fore.YELLOW}'quit'{Fore.CYAN} to quit.\n")


# TODO: The main loop - should run forever until "quit" command is typed

    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    # Check if user did not input anything
    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.")
        continue

    # Check for commands
    if user_input.lower() == "quit":
        print(f"\n{Fore.BLUE} Quitting Sentiment Detective. Farewell, Agent {user_name}!")
        # TODO: How to quit a loop?
    elif user_input.lower() == "clear":
        # TODO: Empty the conversation_history list
        # TODO: Go back to loop start
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.")
        else:
            print(f"{Fore.CYAN} Conversation History:")
            # TODO: Iterate over the history and print every user-provided sentence with sentiment analysis result

                # TODO: Based on sentiment_type, assign color & emoji

                print(f"{idx}. {color}{emoji} {text} (Polarity: {polarity}, {sentiment_type})")

        # TODO: Go back to loop start
    
    # TODO: Let's analyze the sentiment

    # TODO: Check the polarity. Based on it, assign the appropriate sentiment_type, color, and emoji
    # EMOJIS: 😊  😭  😑

    # TODO: After analyzing each sentence, save in the history

    # TODO: Print result with color, emojis, and polarity
    # FORMAT: 😊 Positive sentiment detected (Polarity: 0.50)