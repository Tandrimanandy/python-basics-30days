def character_frequency(text, ch):
    freq = 0
    for c in text:
        if c == ch:
            freq += 1
    return freq

if __name__ == "__main__":
    s = input("Input the TEXT : ")
    ch = input("Character of the TEXT : ")
    print(f'Frequency of the TEXT : {character_frequency(s, ch)}')
