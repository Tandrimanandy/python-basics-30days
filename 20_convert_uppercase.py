def convert_upperc_builtin(text):
    return text.upper()

def convert_upperc_loop(text):
    result = ""
    for ch in text:
        if "a" <= ch <= "z":
            result += chr(ord(ch) - 32)
        else:
            result += ch
    return result

if __name__ == "__main__":
    s = input("Enter text: ")
    print(f'Using upper() Function : {convert_upperc_builtin(s)}')
    print(f'Using loop : {convert_upperc_loop(s)}')
