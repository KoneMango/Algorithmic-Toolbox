from itertools import permutations

def isBetter(new,old):
    larger = 0
    new_list = [str(new),str(old)]
    for permutation in permutations(new_list):
        larger = max(larger, int("".join(permutation)))
    now="".join(new_list)
    if larger == int(now):
        return True
    else:
        return False


def largest_number_naive(numbers):
    # numbers = list(map(str, numbers))
    largest = 0
    while numbers != []:
        maxnumber = 0
        for i in numbers:
            if isBetter(i,maxnumber): #i是新的,maxnumber是旧的
                maxnumber=i
        largest = int(str(largest) + str(maxnumber))
        numbers.remove(maxnumber)
    # for permutation in permutations(numbers):
    #     largest = max(largest, int("".join(permutation)))

    return largest


if __name__ == '__main__':
    _ = int(input())
    # input_numbers = input().split()
    input_numbers = list(map(int, input().split()))
    print(largest_number_naive(input_numbers))
