from random import randint


def partition3(array, left, right):
    pivot = array[left]
    m1 = left
    m2 = right
    i = left + 1
    while i <= m2:
        if array[i] < pivot:
            array[m1], array[i] = array[i], array[m1]
            m1 = m1 + 1
            i = i + 1
        elif array[i] > pivot:
            array[m2], array[i] = array[i], array[m2]
            m2 = m2 -1
        else:
            i = i + 1
    print(m1, m2)
    return m1, m2



    # write your code here


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
