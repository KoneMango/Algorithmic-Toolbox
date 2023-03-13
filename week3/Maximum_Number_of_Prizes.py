def optimal_summands(n):
    summands = []
    adder = 1
    while n!=0:
        summands.append(adder)
        n=n-adder
        adder=adder+1
        if n < adder:
            summands[-1]=summands[-1]+n
            n=0
    # write your code here
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
