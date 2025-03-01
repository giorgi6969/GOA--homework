# 1) 
sample_string = "hello world"
print(sample_string.islower())  # Output - true

# 2) 
def is_all_lowercase(s):
    return s.islower()

# 2)
print(is_all_lowercase("hello"))  # True
print(is_all_lowercase("Hello"))  # False

# 3)
user_input = input("Enter a string: ")
if user_input.islower():
    print("The string contains only lowercase letters.")
else:
    print("The string contains uppercase letters or other characters.")
