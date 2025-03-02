# 2) 
def greet():
    print("Hello, World!")

# 3)
def add_numbers(a, b):
    print(a + b)

# 4)
def multiply_by_ten(n):
    return n * 10

# 5)
def greet_person(name="Guest"):
    print(f"Hello, {name}!")

# 6) 
def outer_function():
    def inner_function():
        print("Inner function is called!")
    inner_function()

# 7) 
def check_even_odd(numbers):
    for num in numbers:
        print("Even" if num % 2 == 0 else "Odd")

# 8) 
def find_maximum(numbers):
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num

# 9) 
def get_positive_numbers(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    return positive_numbers

# 10) 
def sum_divisible_by_3():
    return sum(num for num in range(1, 101) if num % 3 == 0)

