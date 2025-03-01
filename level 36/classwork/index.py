def manual_capitalize(user_str):
    if len(user_str) == 0:  
        return user_str
    
   
    first_char = user_str[0].upper()
    rest_chars = user_str[1:].lower()
    
    return first_char + rest_chars


print(manual_capitalize("hello world"))    
print(manual_capitalize("PYTHON is Awesome"))  
print(manual_capitalize("capitalize"))      
print(manual_capitalize("123abc"))          
print(manual_capitalize(""))                 

