def sum_natural(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


if __name__ == "__main__":
    num = int(input("Enter n the Number : "))
    print(f"Sum of the Number is {sum_natural(num)}")
