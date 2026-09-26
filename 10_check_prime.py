def check_prime(n):
    if n <= 1:
        print(f' The {n} is not a Prime number')
        return
    i = 2
    is_prime = True
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(f' The {n} is a Prime number...')
    else:
        print(f' The {n} is not a Prime number...')

if __name__ == "__main__":
    num = int(input("Enter n is the number : "))
    check_prime(num)
