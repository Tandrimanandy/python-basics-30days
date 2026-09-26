def count_case(text):
    upper = 0
    lower = 0
    digit = 0
    space = 0
    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digit += 1
        elif ch == " ":
            space += 1
    return upper, lower, digit, space

if __name__ == "__main__":
    s = input("Input the TEXT : ")
    u, l, d, sp = count_case(s)
    print (f' Uppercase : {u} \n Lowercase : {l}  \n Digits :  {d}  \n Spaces : {sp}' )

