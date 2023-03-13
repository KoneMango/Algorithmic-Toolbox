from sys import stdin


def min_refills(distance, tank, stops):
    fuel_stop=0
    count = 0
    stops.append(distance)
    for i in range(1,len(stops)):
        if stops[i]-stops[i-1]>tank:
            return -1
    
    for i in range(1,len(stops)):
        if tank < stops[i]-fuel_stop:
            count=count+1
            fuel_stop=stops[i-1]
    return count


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
