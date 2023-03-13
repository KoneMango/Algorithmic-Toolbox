def majority_element_naive(elements):
    dic={}
    for i in elements:
        if i not in dic:
            dic[i] = 0
        else:
            dic[i] = dic[i]+1

    for _,value in dic.items():
        if value>=len(elements)//2:
            return 1
    return 0

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
