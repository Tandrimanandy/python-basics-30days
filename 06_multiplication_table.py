def multiplication_table(n):
    for i in range(1, 11):
        print(f'When {n}  x is {i} Number is {n * i}')

if __name__ == "__main__":
    num = int(input("Enter n Number : "))
    multiplication_table(num)
