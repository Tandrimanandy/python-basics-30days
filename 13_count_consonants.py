def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch == " ":
            continue
        if ch not in vowels:
            count += 1
    return count

if __name__ == "__main__":
    s = input("Enter the text: ")
    print(f'Number of consonants are {count_consonants(s)}')
