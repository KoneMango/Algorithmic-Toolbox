def calculate(a, b, operator):
    # 计算 a operator b 的值
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b

def evaluate_expression(input):
    operators, operands = [], []
    # 将表达式中的运算符和操作数分别存储到 operators 和 operands 列表中
    for char in input:
        if char in ['+', '-', '*']:
            operators.append(char)
        else:
            operands.append(int(char))
    # 用动态规划的思想计算表达式的最大值
    n = len(operands)
    # 初始化 m 和 M 数组
    m = [[None for _ in range(n)] for _ in range(n)]
    M = [[None for _ in range(n)] for _ in range(n)]
    # 对角线上的元素为单独的操作数
    for i in range(n):
        m[i][i] = operands[i]
        M[i][i] = operands[i]
    # 计算其他位置的值
    for s in range(1, n): # s表示范围大小
        for i in range(0, n - s): # i表示范围的起点
            j = i + s # j表示范围的终点
            # 计算 m 和 M 数组中 i 到 j 范围内的最小值和最大值
            min_value = float('inf')
            max_value = float('-inf')
            for k in range(i, j):
                a = calculate(M[i][k], M[k+1][j], operators[k])
                b = calculate(M[i][k], m[k+1][j], operators[k])
                c = calculate(m[i][k], M[k+1][j], operators[k])
                d = calculate(m[i][k], m[k+1][j], operators[k])
                min_value = min(min_value, a, b, c, d)
                max_value = max(max_value, a, b, c, d)
            # 更新 m 和 M 数组中 i 到 j 范围的最小值和最大值
            m[i][j] = min_value
            M[i][j] = max_value
    # 返回整个表达式的最大值
    return M[0][n-1]

if __name__ == "__main__":
    expression = input() # 读取表达式
    # 计算表达式的最大值并输出
    print(evaluate_expression(expression))