def last_ch_indexing(text):
    return text[-1]

def last_ch_loop(text):
    last = ""
    for ch in text:
        last = ch
    return last

if __name__ == "__main__":
    s = input("Enter text: ")
    print(f'Using text[-1] : {last_ch_indexing(s)} \n Using loop : {last_ch_loop(s)}')

