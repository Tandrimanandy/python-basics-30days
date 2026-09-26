def number_p(n):
    for i in range(1, n + 1):
        line = ""
        for j in range(1, i + 1):
            line += str(j)
        print(line)

if __name__ == "__main__":
    num = int(input("Enter n number : "))
    number_p(num)
