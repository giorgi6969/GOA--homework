def find_min(lst):
  
    min_value1 = min(lst)

  
    min_value2 = lst[0] 
    for num in lst:
        if num < min_value2:
            min_value2 = num

    return min_value1, min_value2  


numbers = [4, 7, 1, 9, -3, 5]
result = find_min(numbers)
print("min() using function:", result[0])
print("using cicle:", result[1])

