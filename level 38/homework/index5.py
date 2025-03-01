def sentence_to_words(sentence):
    words = []
    word = ""
    
    for char in sentence:
        if char != " ":  
            word += char
        else:
            if word:  
                words.append(word)
                word = ""  

    if word:  
        words.append(word)
    
    return words


print(sentence_to_words("Hello world, how are you?"))  



user_sentence = input("Enter a sentence: ")
print("List of words:", sentence_to_words(user_sentence))
