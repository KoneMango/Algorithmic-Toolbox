from sys import stdin
from collections import namedtuple
import numpy

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    length = []
    resultline = 0
    segments.sort()
    min1 = min([segment.start for segment in segments])
    max1 = max([segment.end for segment in segments])

    for i in segments:
        length.append(i[1]-i[0])
    countline = 0

    while segments != []:
        record  = [[] for _ in range(10)]
        countlist = []
        for j in range(min1,max1+1):#从头开始的检查点
            count = 0

            for k in segments:#算第几根线有交点
                if j<=k[1] and j>=k[0]:
                    count = count +1
                    record[j].append(k)

                # if countlist[j]<= countlist[j-1]:#不能减
                #     countline = countline + 1
                #     points.append(j-1)
                #     for m in record:
                #         del segments[m]
            countlist.append(count)
        del_line = next(i for i, x in enumerate(countlist) if x == max(countlist))
        for m in record[del_line+1]:
            segments.remove(m)  #list indices must be integers or slices, not Segment
        resultline=resultline+1 #计算需要几条线
        points.append(del_line+1)
    return resultline, points
    
    # # write your code here
    # for s in segments:
    #     points.append(s.start)
    #     points.append(s.end)
    # return countline, points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(points)
    # print(len(points))
    # print(*points)
