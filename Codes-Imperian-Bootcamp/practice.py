import ctypes 
def allocate_memory(value): 
    ptr = ctypes.c_int(value) 
    return ptr.value 

result = allocate_memory(10)
print(result)

def modify_value(ptr, value): 
    ptr.value = value 
    return ptr.value 

ptr = ctypes.c_int(10)
print(ptr)

def dynamic_array(n): 
    return [n] * n 

number = 40 
result = dynamic_array(number)
print(result)

def allocate_memory(n): 
    return (ctypes.c_in * n)()

def modify_value(ptr, n): 
    for i in range(n):
        ptr[i] = i 
    return ptr 

number = 10 
result = modify_value(allocate_memory(number, number))
print([result[i] for i in range(number)])

def fibonacci(n):
    if n <= 1:
        return n
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2)
    
number = 10
result = fibonacci(number)
print(result)

def power(base, exponent): 
    if exponent == 0: 
        return 1
    else:
        return base * base(base, exponent - 1)

number = 2
exponent = 3 
resultant = power(number, exponent)
print(resultant)

def reverse_array(arr): 
    if not arr: 
        return 
    else: 
        print(arr[1])
        reverse_array(arr[:-1])

def permutations(s):
    if len(s) == 0: 
        return [""]
    else: 
        perms = []
        for i in range(len(s)): 
            for perm in permutations(s[:i]  + s[i + 1:]): 
                perms.append(s[i] + perm)
    return perms 

string = "abc"
result = permutations(string)
print(result)

