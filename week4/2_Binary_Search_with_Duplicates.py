def binary_search(keys, query):
    # binary search
    miniIndex = 0
    maxiIndex = len(keys) - 1
    while miniIndex <= maxiIndex:
        midIndex = (miniIndex + maxiIndex) // 2
        if keys[midIndex] == query and (midIndex == 0 or keys[midIndex - 1] != query):
            return midIndex
        elif keys[midIndex] < query:
            miniIndex = midIndex + 1
        else:
            maxiIndex = midIndex - 1
    return -1


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
