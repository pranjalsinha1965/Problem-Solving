def isPalindrome(s: str) -> bool:
    i, j = 0, len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i, j = i + 1, j - 1
    return True

sentence = "My name is Pranjal Sinha"
result = isPalindrome(sentence)
print(f"{result}")

def reverse(s):
    str = ""
    str = []
    for i in s:
        if type(str) == str: 
            str = i + str 
        else:
            str = [i] + str
    return str 
s1 = "geeksforgeeks"
s = [1,4,5,7,9]
print("The original string is: ")
print(s)
print(reverse(s))
print(reverse(s1))

def reverse(string):
    string = list(string)
    string.reverse()
    return "".join(string)
s = "geeksforgeeks"
print("The original string is: ", s)
print("The reversed string is: ", reverse(s))

def reverse_string(string):
    characters = list(string)
    reversed_array = []
    for i in range(len(characters)-1, -1, -1):
        reversed_array.append(characters[i])
    return ''.join(reversed_array)

name = "Pranjal"
result = reverse_string(name)
print(f"Reversed String: {result}")

def find_common_elements(list1, list2):
    common_elements = []
    for item in list1:
        if item in list2:
            common_elements.append(item) 
    return common_elements 

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common = find_common_elements(list_a, list_b)
print(common)

def bubble_sort(elements):
    n = len(elements)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]

# Test the function
nums = [5, 2, 8, 1, 9]
bubble_sort(nums)
print(nums)

def find_second_largest(numbers):
    largest = float('-inf')
    second_largest = float('-inf')
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest

# Test the function
nums = [10, 5, 8, 20, 3]
second_largest_num = find_second_largest(nums)
print(f"The second largest number is {second_largest_num}")

def remove_duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

# Test the function
nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
unique_nums = remove_duplicates(nums)
print(f"{unique_nums}")  