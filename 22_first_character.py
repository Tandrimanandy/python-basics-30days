def first_character(text):
    for ch in text:
        print(f'First character: {ch}')
        break

if __name__ == "__main__":
    s = input('Enter The TEXT : ')
    first_character(s.upper())
