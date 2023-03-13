def fibonacci_number(n):
    fibonacci_numbers = [0, 1]
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        for i in range(2, n + 1):
            fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
        return fibonacci_numbers[i]
if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
