def change(money):
    # write your code here
    coin=[10,5,1]
    count= 0
    for i in coin:
        count=count+money//i
        money=money%i
    return count

if __name__ == '__main__':
    m = int(input())
    print(change(m))
