#2)
def sum_of_two_numbers(num1, num2):
    return num1 + num2


result = sum_of_two_numbers(5, 3)
print(result) 
#3)
    if not numbers:  
        return None
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


numbers_list = [10, 5, 20, 15]
max_number = find_maximum(numbers_list)
print(max_number)  

 
