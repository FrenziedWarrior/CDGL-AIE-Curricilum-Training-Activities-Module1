# sum = 1 + 2
# print(sum)

# Function Definition
# def sum(a, b):
#     print("Sum", a + b)

# # Function Call
# sum(23, 58)


# def sum2(a, b):
#     return a + b

# result = sum2(5, 6)
# print("Sum2", result)

sentences = [] # Memory Address

details = dict()

c = 0 # Value
# print(c, type(c))

a = None
s = "Advik" # Array of values

def analyze_sentence():
    sentences.append("Hello")
    sentences[0] = "World"
    sentences = []
    print(sentences, type(sentences))
    print(s, type(s))
    print(a, type(a))
    print(details, type(details))
    print(c)

analyze_sentence()

history = ["Abc", "Def"]

def process_commands(user_input):
    if user_input == "history":
        for i, h in enumerate(history, start=1):
            print(i, h)


user_input = "history"
process_commands(user_input)

from datetime import datetime
now = datetime.now()
print(now)

filename = "Summary" + "_" + str(now) + ".txt"
print(filename)

f = open(filename, "w")
f.write("Positive\n")
f.write("Negative\n")
f.write("Neutral\n")
