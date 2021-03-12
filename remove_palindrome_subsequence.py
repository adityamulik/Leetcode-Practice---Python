
# word = "baabb"  # drop b
# word = "abb"  # drop a
word = "ababbaba"  # drop a
# word = "bababb"  # drop a

# def palindrome(w):
#     if w[::-1] == w:
#         return "String is already a palindrome."
#     else:
#         pass


# def palindrome(s):
#     return 0 if s == "" else 1 if s == s[::-1] else 2

def palindrome(s):
    for i in range(0, int(len(s)/2)):
        if s[i] != s[len(s) - i - 1]:
            print(i)
            print(s[i], s[len(s)-i-1])
            return 2
    return 1


print(palindrome(word))
