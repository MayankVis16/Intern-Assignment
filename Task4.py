def process_sentence(sentence):
    # Split sentence into words
    words = sentence.split()
    
    # Count the number of words
    word_count = len(words)
    
    # Reverse the order of words
    reversed_sentence = " ".join(reversed(words))
    
    # Replace spaces with hyphens
    modified_sentence = sentence.replace(" ", "-")
    
    return word_count, reversed_sentence, modified_sentence

# Prompt user for input
user_input = input("Enter a sentence: ")

# Process the sentence
word_count, reversed_sentence, modified_sentence = process_sentence(user_input)

# Display results
print(f"Number of words: {word_count}")
print(f"Reversed sentence: {reversed_sentence}")
print(f"Modified sentence: {modified_sentence}")