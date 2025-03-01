# 7) 
sample_string = "Hello World!"
swapped_string = sample_string.swapcase()
print(swapped_string)  # Output: hELLO wORLD!

# 8)
def swap_case(sentence):
    return sentence.swapcase()

# Testing the function
print(swap_case("Python is FUN!"))  
print(swap_case("123abcDEF")) 

user_input = input("Enter a sentence: ")
print("Swapped case:", swap_case(user_input))
