def gcd(a, b):
    if a<b:
        a, b = b, a
    while(1):
        if a%b == 0:
            return b
        else:
            a, b = b, a%b


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
