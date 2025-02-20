def sentence_to_words(sentence):
    words = []
    word = ""
    
    for char in sentence:
        if char != " ":  # If the character is not a space, add it to the current word
            word += char
        else:
            if word:  # If a word exists, add it to the list
                words.append(word)
                word = ""  # Reset word

    if word:  # Add the last word if there is one
        words.append(word)
    
    return words

# Example usage
print(sentence_to_words("Hello world, how are you?"))  
# Output: ['Hello', 'world,', 'how', 'are', 'you?']

# Prompting user for input
user_sentence = input("Enter a sentence: ")
print("List of words:", sentence_to_words(user_sentence))
