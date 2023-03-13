def canPlaceFlowers(flowerbed, n):
    count = 0
    flowerbed=[0]+flowerbed+[0]
    for i in range(1,len(flowerbed)-1):
        if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
            flowerbed[i]=1
            count=count+1
    return count>=n

if __name__ == '__main__':
    flowerbed=[1,0,0,0,1,0,0]
    n = 2
    print(canPlaceFlowers(flowerbed,n))