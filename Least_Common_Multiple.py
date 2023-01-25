def lcm(a, b):
    product=a*b
    if a<b:
        a, b = b, a
    while(1):
        if a%b == 0:
            divisor = b
            break
        else:
            a, b = b, a%b
    return int(product/divisor)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

