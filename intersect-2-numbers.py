def isPalindrome(s: str) -> bool:
    l = 0
    r = len(s) - 1
    while l <= r:

        if s[l] != s[r]:
            return False
        l += 1
        r -= 1

    return True

s = "racecar"
ans = isPalindrome(s)
print(ans)