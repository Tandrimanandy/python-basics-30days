def count_words(text):
    space_count = 0
    for ch in text:
        if ch == " ":
            space_count += 1
    return space_count + 1

if __name__ == "__main__":
    s = input("Enter the Text : ")
    print(f'Words Counts : {count_words(s)}')
    
