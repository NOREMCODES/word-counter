def count_words(text):
    words = text.split()
    return len(words)

# Example usage
sample_text = "NoremCodes is building automation tools for businesses."
word_count = count_words(sample_text)
print(f"Word count: {word_count}")
