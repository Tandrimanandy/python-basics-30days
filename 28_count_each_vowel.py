def count_each_vowel(text):
    a = e = i = o = u = 0
    for ch in text.lower():
        if ch == "a":
            a += 1
        elif ch == "e":
            e += 1
        elif ch == "i":
            i += 1
        elif ch == "o":
            o += 1
        elif ch == "u":
            u += 1
    return a, e, i, o, u

if __name__ == "__main__":
    s = input(" Text Input: ")
    a, e, i, o, u = count_each_vowel(s)
    print(f'Output: \n a = {a} \n e = {e} \n i = {i} \n o = {o} \n u = {u}' )
