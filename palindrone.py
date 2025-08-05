def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

text = input("Enter a string: ")
if is_palindrome(text):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
