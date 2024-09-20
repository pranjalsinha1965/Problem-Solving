def find_common_elements(list1, list2):
    common_elements = []
    for item in list1: 
        if item in list2: 
            common_elements.append(item)
    return common_elements 

list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]
common = find_common_elements(list_a, list_b)
print(common)
