def find_Boro_number(a, b, c):
    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c
    return largest

if __name__ == "__main__":
    x = int(input("Enter a: "))
    y = int(input("Enter b: "))
    z = int(input("Enter c: "))
    print(f'The Largest Number is {find_Boro_number(x, y, z)}')
