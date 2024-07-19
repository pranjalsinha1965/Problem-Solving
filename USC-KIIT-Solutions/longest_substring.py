def length_of_longest_substring(s):
    char_map = {}
    left = max_length = 0
    for right, char, in enumerate(s):
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
        char_map[char] = right
        max_length = max(max_length, right - left + 1)
    return max_length

a = "abbbbcda"
b = length_of_longest_substring(a)
print(b)
