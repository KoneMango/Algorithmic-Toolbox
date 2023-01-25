def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    
    previous1 = 0
    current1  = 1
#计算pisano周期
    for i in range(0, n + 1):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            break

    for _ in range((n - 1)%(i+1)):
        previous1, current1 = current1, previous1 + current1

    return current1 % m



if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
