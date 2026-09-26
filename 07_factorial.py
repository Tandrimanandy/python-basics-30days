def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *=  i
    return result

if __name__ == "__main__":
    num = int(input("Enter n is the Number : "))
    print(f"Factorial of the Number : {factorial(num)}")
