def is_palindrome(n: int) -> bool:
    rev_num = 0
    original_num = n
    while n > 0:
        last_digit = n % 10
        rev_num = (rev_num * 10) + last_digit
        n = n // 10
    return original_num == rev_num

def main():
    number = 4554

    if is_palindrome(number):
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")

if __name__ == "__main__":
    main()
