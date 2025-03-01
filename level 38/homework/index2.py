# 4) 
user_string = input("Enter a string: ")
print(user_string.isupper())  

# 5) 
def is_all_uppercase(s):
    return s.isupper()

# 5)
print(is_all_uppercase("HELLO"))  
print(is_all_uppercase("Hello"))  
print(is_all_uppercase("123ABC"))  

# 6) 
if user_string.isupper():
    print("The string is entirely in uppercase.")
else:
    print("The string is not fully uppercase.")

