def count_characters(text):
    count = 0
    for ch in text:
        count += 1
    return count

if __name__ == "__main__":
    s = input("Enter the text: ")
    print(f'Number of characters are {count_characters(s)}...')
