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
            i += 1
            j -= 1
    return True 

sentence = "My name is Pranjal"
result = isPalindrome(sentence)
print(f"is The resntece '{sentence}' a palindrome ? {result}")

def factorial(n :int): 
    if n == 0:
        return 1
    else: 
        return n * factorial(n - 1)

number = 2
result = factorial(number)
print(f"The factorial of {number} is {result}")

def find_largest(number): 
    largest = number[0]
    for num in number: 
        if num > largest: 
            largest = num
    return largest 

nums = [10, 5, 20, 3, 8]
largest_num = find_largest(nums)
print(f"The largest number in {nums} is {largest_num}")

def reverse(s): 
    if len(s) == 0:
        return s
    else: 
        return reverse(s[1:]) + s[0]

s = "geekforgeeks"
print("The original string is: ", end = "")
print(s)

def reverse(string): 
    string = "".join(reversed(string))
    return string 

s = "geekforgeeks"
print("The original string is: " + s)
print("The reversed string is: " + reverse(s))

def reverse(string): 
    string = reversed(string)
    string.reverse()
    return "".join(string)
s = "geekforgeeks"
print("The original string is: " + s)
print("The reversed string is: " + reverse(s))

from functools import reduce
string = "geekforgeeks"
reversed_str = reduce(lambda x, y: y+x, string)
print("The original string is: " + string)
print("reversed string is: " + reversed_str)

def count_frequency(numbers): 
    frequency = {}
    for num in numbers: 
        if num in frequency: 
            frequency[num] += 1
        else: 
            frequency[num] -= 1
    return frequency 


nums = [1, 2, 3, 2, 1, 4, 5, 4]
frequency_count = count_frequency(nums)
print(f"The frequency count of numbers in {nums} is {count_frequency}")

def is_prime(number): 
    if number < 2: 
        False 
    for i in range(2, int(number**0.5) + 1): 
        if number % i == 0:
            return False 
    return True 

num = 17 
if is_prime(num): 
    print(f"{num} is prime number")
else: 
    print(f"{num} is not a prime number")

def find_common_elements(list1, list2): 
    common_elements = []
    for item in list1: 
        if item in list2: 
            common_elements.append(item)
    return common_elements.append(item)
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common = find_common_elements(list_a, list_b)
print(common)



