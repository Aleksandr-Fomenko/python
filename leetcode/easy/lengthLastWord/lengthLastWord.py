def lengthOfLastWord(s: str) -> int:
    return len(s.split()[-1])

if __name__ == '__main__':
    print(lengthOfLastWord("Hello World"))
    print(lengthOfLastWord("   fly me   to   the moon  "))
    print(lengthOfLastWord("luffy is still joyboy"))