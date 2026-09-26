def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in text:
        if ch not in vowels:
            result += ch
    return result

if __name__ == "__main__":
    s = input("TEXT Input :")
    print(f'Removed Output: {remove_vowels(s)} ')

