def bubble_sort(elements): 
    n = len(elements)
    for i in range(n - 1):
        for j in range(n-i-1): 
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]

nums = [5, 2, 8, 1, 9]
bubble_sort(nums)
print(nums)

def find_second_largest(numbers): 
    largest = float('-inf')
    second_largest = float('-inf')
    for num in numbers: 
        if num > largest: 
            largest = num 
        elif num > second_largest and num != largest: 
            second_largest = num 
    return second_largest 

numbers = [5, 2, 8, 1, 9]
result = find_second_largest(numbers)
print(f"{result}")

def find_common_elements(list1, list2): 
    common_elements = []
    for item in list1: 
        if item in list2: 
            common_elements.append(item)
    return common_elements

num1 = [1, 2, 3, 4, 5]
num2 = [3, 4, 5, 6, 7]
result = find_common_elements(num1, num2)
print(f"{result}")

def remove_duplicates(numbers): 
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers: 
            unique_numbers.append(num)
    return unique_numbers

nums = [1, 2, 3, 2, 1, 4, 5, 4]
result = remove_duplicates(nums)
print(f"{result}")

