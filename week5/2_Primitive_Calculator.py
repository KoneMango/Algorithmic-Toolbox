def compute_operations(n):
    sequence = [n+1] * (n + 1)
    sequence[0] = 0
    sequence[1] = 0
    prev = [0] * (n + 1)
    for i in range(2, n + 1):
        if i - 1 >= 1:
            # if sequence[i - 1] + 1 < sequence[i]:
            #     sequence[i] = sequence[i - 1] + 1
            #     prev[i] = i - 1
            if sequence[i - 1] + 1 < sequence[i]:
                prev[i] = i - 1
            sequence[i] = min(sequence[i], sequence[i-1] + 1)

        if i % 2 == 0:
            # if sequence[i // 2] + 1 < sequence[i]:
            #     sequence[i] = sequence[i // 2] + 1
            #     prev[i] = i // 2
            if sequence[i // 2] + 1 < sequence[i]:
                prev[i] = i // 2
            sequence[i] = min(sequence[i], sequence[int(i//2)] + 1)

        if i % 3 == 0:
            # if sequence[i // 3] + 1 < sequence[i]:
            #     sequence[i] = sequence[i // 3] + 1
            #     prev[i] = i // 3
            if sequence[i // 3] + 1 < sequence[i]:
                prev[i] = i // 3
            sequence[i] = min(sequence[i], sequence[int(i//3)] + 1)

    result = []
    while n > 0:
        result.append(n)
        n = prev[n]   
    return result[::-1]

if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)