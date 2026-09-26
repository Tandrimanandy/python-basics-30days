def longest(text):
    best = ""
    word = ""
    for ch in text:
        if ch == " ":
            if length(word) > length(best):
                best = word
            word = ""
        else:
            word += ch
    if length(word) > length(best):
        best = word
    return best

def length(word):
    n = 0
    for ch in word:
        n += 1
    return n

if __name__ == "__main__":
    s = input("Enter a sentence: ")
    print(f"Longest word : {longest(s)}")