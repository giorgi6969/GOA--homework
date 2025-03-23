def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # ახალ სიმბოლოს წინ ვამატებთ
    return reversed_str
