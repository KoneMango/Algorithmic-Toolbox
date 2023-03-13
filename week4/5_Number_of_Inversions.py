from itertools import combinations


def inversions_naive(a):
    #devide and conquer
    count = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                count+=1
    return count


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(inversions_naive(elements))
