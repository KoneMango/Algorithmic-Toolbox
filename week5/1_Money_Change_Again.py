def change(money):
    coins = [4, 3, 1]
    #动态规划
    dp = [money+1] * (money+1)
    dp[0] = 0
    for i in range(1, money+1):
        for j in coins:
            if i >= j:
                dp[i] = min(dp[i], dp[i-j]+1)
    if dp[money] > money:
        return -1
    else:
        return dp[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
