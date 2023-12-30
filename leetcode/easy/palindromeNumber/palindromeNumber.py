def isPalindrome(x: int) -> bool:
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    print(isPalindrome(121))
    print(isPalindrome(-121))
    print(isPalindrome(10))