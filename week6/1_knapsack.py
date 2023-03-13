from sys import stdin


def maximum_gold(capacity, weights):
    # 初始化一个二维数组
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(weights) + 1)]

    for i in range(1, len(weights) + 1):
        for w in range(1, capacity + 1):
            # 如果当前物品重量大于背包容量，则不能选
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                # 否则，可以选择装或者不装，取最大值
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + weights[i - 1])
    return dp[len(weights)][capacity]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))