import json

# Load training data from JSON file
with open("../Data/training_data.json", "r") as file:
    training_data = json.load(file)

print("===================================")
print(" Student Assistant Chatbot Started ")
print(" Type 'bye' to exit")
print("===================================")

while True:
    user = input("You: ").lower().strip()

    if user in training_data:
        print("Bot:", training_data[user])

        if user == "bye":
            print("Chat ended.")
            break
    else:
        print("Bot: Sorry, I don't know that answer.")
