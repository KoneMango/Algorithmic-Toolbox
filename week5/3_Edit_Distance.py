def edit_distance(first_string, second_string):
    #dp solution
    first_string = " " + first_string
    second_string = " " + second_string
    dp = [[0 for i in range(len(second_string))] for j in range(len(first_string))]
    for i in range(len(first_string)):
        dp[i][0] = i
    for j in range(len(second_string)):
        dp[0][j] = j
    for i in range(1, len(first_string)):
        for j in range(1, len(second_string)):
            if first_string[i] == second_string[j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    return dp[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
