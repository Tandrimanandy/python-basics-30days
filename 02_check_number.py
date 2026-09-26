def check_number(n):
    if n > 0:
        print(f'{n} is a Positive Number......')
    elif n < 0:
        print(f'{n} is a Negetive Number......')
    else:
        print(f'{n} is Zero......')

if __name__ == "__main__":
    num = int(input("Enter n Number : "))
    check_number(num)
