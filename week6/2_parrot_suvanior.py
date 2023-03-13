from sys import stdin

def partition3(values):
    third = sum(values) // 3
    if len(values) < 3 or sum(values) % 3 or max(values) > third:
        return 0

    table = [[0] * (len(values) + 1) for _ in range(third + 1)]
    taken = [[0] * (len(values) + 1) for _ in range(third + 1)]

    for i in range(1, third + 1):
        for j in range(1, len(values) + 1):
            if table[i][j-1] == 2:
                table[i][j] = 2
                continue

            if values[j-1] == i:
                table[i][j] = 1 if table[i][j-1] == 0 else 2
                taken[i][j] = j
                continue

            ii = i - values[j-1]

            available = True
            taken_id = taken[ii][j-1]
            if taken_id:
                for jj in range(1, j):
                    if taken[ii][jj] == taken_id:
                        if taken[i][jj]:
                            available = False
                            break

            if ii > 0 and table[ii][j - 1] > 0 and not taken[i][j - 1] and available:
                table[i][j] = 1 if table[i][j - 1] == 0 else 2

                taken[i][j] = j
                taken[i][j-1] = j

                matcher = values[j-1] + values[j-2]
                if taken_id:
                    for jj in range(1, len(values)):
                        if taken[ii][jj] == taken_id:
                            taken[i][jj] = j
                            matcher += values[jj-1]
                if matcher < i:
                    for jj in range(j-2, 0, -1):
                        if taken[i][jj] or matcher + values[jj-1] > i:
                            continue
                        matcher += values[jj-1]
                        taken[i][jj] = j
                        if matcher == i:
                            break
            else:
                table[i][j] = table[i][j - 1]

    return 1 if table[-1][-1] == 2 else 0


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))