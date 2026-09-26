def reverse_number(n):
    negative = n < 0
    n = abs(n)
    reversed_num = 0
    while n != 0:
        last_digit = n % 10
        reversed_num *= 10 + last_digit
        n = n // 10
    if negative:
        reversed_num = -reversed_num
    return reversed_num

if __name__ == "__main__":
    num = int(input("Enter n: "))
    print(f'Reversed number is = {reverse_number(num)}')
