def count_words(text):
    words = text.split()
    return len(words)

# Input
user_input = input("Enter your sentence: ")

# Output
print("Word count:", count_words(user_input))
