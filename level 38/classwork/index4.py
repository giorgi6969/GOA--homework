def element_remover(user_list, index_to_remove):
    try:
        removed_element = user_list.pop(index_to_remove)  
        print(f'deleted element: {removed_element}')
        print(f'new list: {user_list}')
    except IndexError:
        print("seen index dosent exist in the list")

element_remover(["cow", "cat", "dog", "amazing"], 1)  
element_remover(["pants", "clothes", "leaf"], 0)      
element_remover(["pizza", "pasta", "salad"], 2)             
