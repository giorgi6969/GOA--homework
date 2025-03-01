def list_join(user_list, str_to_join):
    
    joined_string = str_to_join.join(user_list)
    print(joined_string)


list_join(["giorgi", "luka", "gabriel"], ", ")  
list_join(["hello", "goodbye"], " - ")         
list_join(["cat", "dog", "chicken"], " + ") 
