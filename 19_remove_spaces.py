def remove_spaces(text):
    result = ""
    for ch in text:
        if ch != " ":
            result += ch
    return result

if __name__ == "__main__":
    s = input("Input the TEXT : ")
    print(f'Remove the Space in TEXT : {remove_spaces(s)}')
