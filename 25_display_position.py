def display_position(text):
    for i in range(len(text)):
        print(f'Position {i} : {text[i]}')

if __name__ == "__main__":
    s = input("TEXT Input : ")
    display_position(s.upper())
