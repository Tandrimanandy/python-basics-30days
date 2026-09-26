def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

if __name__ == "__main__":
    s = input("Input : ")
    print(f'Output : {count_vowels(s)}')
