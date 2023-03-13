# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next  = 1
    newto=(to + 1)%60
    newfrom=from_%60
    if newfrom>newto:
        newto+=60
    for i in range(newto):
        if i >= newfrom:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
