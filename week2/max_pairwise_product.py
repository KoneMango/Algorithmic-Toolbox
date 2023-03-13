def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    max1=0
    max2=0
    # for first in range(n):
    #     for second in range(first + 1, n):
    #         max_product = max(max_product,
    #             numbers[first] * numbers[second])
    for first in range(n):
        max1=max(max1,numbers[first])
    numbers.remove(max1)
    for second in range(n-1):
        max2=max(max2,numbers[second])
    max_product=max1*max2
    return max_product


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
