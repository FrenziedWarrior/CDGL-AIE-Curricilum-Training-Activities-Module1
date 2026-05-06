print("Hi. This is Basic Chatbot belonging to Activity 1 from Lesson 1 in Module 1.")

name = input("What is your name? ").lower()

feeling = input("How are you feeling? ").lower()
if "good" in feeling or "great" in feeling or "excited" in feeling:
    print("I'm glad to hear that!")
elif "sad" in feeling or "sick" in feeling or "depressed" in feeling:
    print("Sorry to hear that. Feel better soon!")
else:
    print("Sometimes it's difficult to put in words!")

print(f"Nice talking to you, {name}. Goodbye!")