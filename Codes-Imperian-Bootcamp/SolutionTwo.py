# Exaplin memory allocation using cell and block of memory ? Define dynamic array.

import ctypes

# Allocate single memory cell
def allocate_memory(value): 
    return ctypes.pointer(ctypes.c_int(value))

def modify_value(ptr, value): 
    ptr.contents.value = value 
    return ptr.contents.value 

ptr = allocate_memory(10)
print("Before modify:", ptr.contents.value)
print("After modify:", modify_value(ptr, 20))

# Dynamic array
def dynamic_array(n): 
    return list(range(n))

number = 10
result = dynamic_array(number)
print("Dynamic array:", result)

# Allocate block of memory
def allocate_block(n): 
    return (ctypes.c_int * n)()

def fill_block(ptr, n):
    for i in range(n):
        ptr[i] = i 
    return ptr 

number = 10
result = fill_block(allocate_block(number), number)
print("Ctypes block:", [result[i] for i in range(number)])

# fibonacci 

def fibonacci(n): 
    if n<= 1: 
        return n
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print("fibonacci(10): ", fibonacci(10))


def fibonacci_iter(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print("Fibonacci(10):", fibonacci_iter(10))  # Output: 55


# Power function
def power(base, exponent): 
    if exponent == 0: 
        return 1
    return base * power(base, exponent - 1)

print("Power(2, 3):", power(2, 3))

# Reverse array
def reverse_array(arr):
    if not arr:
        return
    print(arr[-1])
    reverse_array(arr[:-1])

print("Reversed array:")
reverse_array([1, 2, 3, 4, 5])

# Permutations
def permutations(s): 
    if len(s) == 0: 
        return [""]
    perms = []
    for i in range(len(s)): 
        for perm in permutations(s[:i] + s[i + 1:]): 
            perms.append(s[i] + perm)
    return perms 

print("Permutations of 'abc':", permutations("abc"))
