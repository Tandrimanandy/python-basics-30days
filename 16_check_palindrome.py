def check_palindrome(text):
    reversed_text = text[::-1]
    if text == reversed_text:
        print(f'({text}) This text is  -> Palindrome')
    else:
        print(f'({text}) This text is  -> Not Palindrome')

if __name__ == "__main__":
    s = input("Enter The text: ")
    check_palindrome(s)
