def star_p(n):
    for i in range(1, n + 1):
        line = ""
        for j in range(i):
            line += "*"
        print(line)

if __name__ == "__main__":
    num = int(input("Enter n: "))
    star_p(num)
