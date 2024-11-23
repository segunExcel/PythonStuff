
def return_sublist_from_either_dictionary_or_2D_list(data_table:list |dict, key:str)-> list:
    if isinstance(data_table, dict): # check if the data_table is a dictionary
        return data_table[key]
    elif isinstance(data_table, list): # check if the data_table is a 2D list   
        for row in data_table: # iterate through the rows of the 2D list    
            if row[0] == key: # check if the first element of the row is equal to the key
                return row[1:] # return the rest of the row after the first element
    else:
        raise ValueError("data_table must be a dictionary or a 2D list")
    


# This is another approach to the same problem with a slight tweak
def return_sublist_from_either_dictionary_or_2D_list(data_table:list |dict, key:str)-> list:
    if isinstance(data_table, dict): # check if the data_table is a dictionary
        return data_table[key]
    elif isinstance(data_table, list): # check if the data_table is a 2D list   
        for row in data_table: # iterate through the rows of the 2D list    
            if row[0] == key: # check if the first element of the row is equal to the key
                sublist =[]
                for element in row[1:]: # iterate through the rest of the row after the first element
                    sublist.append(element)
                return sublist
    else:
        raise ValueError("data_table must be a dictionary or a 2D list")
