from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0
    per=[]
    for i in range(len(values)):
        per.append(values[i]/weights[i])
    for i in range(len(values)):
        if capacity>=weights[per.index(max(per))]:
            maxPer=max(per)
            capacity=capacity-weights[per.index(maxPer)]
            value=value+values[per.index(maxPer)]

            del weights[per.index(maxPer)]
            del values[per.index(maxPer)]
            del per[per.index(maxPer)]
            # weights.remove(weights[per.index(maxPer)])
            # values.remove(values[per.index(maxPer)])
            # per.remove(maxPer)

        else:
            value=value+capacity*max(per)
            break
    # write your code here
    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    # print("{:.10f}".format(opt_value))
    print(opt_value)
