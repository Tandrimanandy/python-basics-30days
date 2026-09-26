def reverse_string_loop(text):
    reversed_text = ""
    for ch in text:
        reversed_text += ch
    return reversed_text

def reverse_string_slicing(text):
    return text[::-1]

if __name__ == "__main__":
    s = input("Enter text: ")
    print(f'Reversed (loop) : {reverse_string_loop(s)}')
    print(f'Reversed (slicing) : {reverse_string_slicing(s)}')
