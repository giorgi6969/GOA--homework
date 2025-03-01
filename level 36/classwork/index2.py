
def big_sentence(name, surname, age, academy, role):
    sentence = "Hello, my name is {}, my surname is {}. I am {} years old. I study at {}, my role is {}."
    formatted_sentence = sentence.format(name, surname, age, academy, role)
    print(formatted_sentence)


big_sentence("giorgi", "sulaqvelidze", 9, "school", "student")

