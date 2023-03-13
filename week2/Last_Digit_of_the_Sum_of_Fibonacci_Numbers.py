def fibonacci_sum(n):
    if n <= 1:
        return n
    # sum =[]
    # record = []
    # previous, current, _sum = 0, 1, 1

    # for i in range(n - 1):
    #     previous, current = current, previous + current
    #     _sum += current
    #     sum.append(_sum)
    #     if sum[i]%10==2 and sum[i-1]%10==1:
    #         record.append(i)
    previous1, current1, _sum1 = 0, 1, 1

    for _ in range((n - 1)%60):
        previous1, current1 = current1, previous1 + current1
        _sum1 += current1

    return _sum1 % 10



if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
    # for i in range(1, n+1):
    #     print(fibonacci_sum(i))
    # print(fibonacci_sum(n))
