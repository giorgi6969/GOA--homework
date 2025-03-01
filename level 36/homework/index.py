
# 2)
sentence = "Hello world, how are you?"
print(sentence.upper())  # 

# 3) 
user_name = input("Enter your name: ")
print(user_name.upper())

# 4) 
def convert_list_to_uppercase(lowercase_list):
    return [s.upper() for s in lowercase_list]

print(convert_list_to_uppercase(["hello", "world", "python"]))  


# 5)
print(sentence.lower())  
# 6) 
user_email = input("Enter your email address: ").lower()
print(user_email)

# 7) 
def to_lowercase(mixed_case_str):
    return mixed_case_str.lower()

print(to_lowercase("Python is FUN!"))  


# 
# 8)
user_sentence = input("Enter a sentence: ")
print(user_sentence[0].upper() + user_sentence[1:].lower() if user_sentence else "")  

# 9)
def capitalize_list(lowercase_list):
    return [s.capitalize() for s in lowercase_list]

print(capitalize_list(["hello", "world", "python"]))  
# 10)
def capitalize_first_letter(s):
    return s[0].upper() + s[1:].lower() if s else ""

print(capitalize_first_letter("hello world"))  


# 11) 
print(sentence.find("Python"))  

# 12) 
user_substring = input("Enter a substring to search for: ")
print(sentence.find(user_substring))  

# 13) 
def find_character_index(s, char):
    return s.find(char)

print(find_character_index("Hello", "e")) 



# 14) 
user_string = input("Enter a string: ")
print(len(user_string))

# 15) 
def get_lengths(string_list):
    return [len(s) for s in string_list]

print(get_lengths(["hello", "world", "python"]))  



# 16) 
paragraph = "The quick brown fox jumps over the lazy dog. The dog was not amused."
print(paragraph.lower().count("the"))  

# 17) Ask
user_char = input("Enter a character to count: ")
print(user_string.count(user_char))

# 18) 
def count_word_occurrences(text, word):
    return text.lower().split().count(word.lower())

print(count_word_occurrences(paragraph, "the"))  
