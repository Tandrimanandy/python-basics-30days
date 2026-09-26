def find_largest(S, T):
    if S > T:
        return S
    else:
        return T

if __name__ == "__main__":
    x = int(input("Enter S number : "))
    y = int(input("Enter T number : "))
    print("Largest =", find_largest(x, y))
