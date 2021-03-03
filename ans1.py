def server_cost(d1, m1, y1, d2, m2, y2):
    cost = 0
    if (d1 == d2 and m1 == m2 and y1 ==y2): cost += 20
    elif (d1 != d2 and m1 == m2 and y1 == y2): cost += (30 * (abs(d1-d2)))
    elif (y1 == y2 and m1 != m2): cost += (1000 * (abs(m1-m2)))
    elif (y1 != y2): cost += 20000
    return cost
if __name__ == '__main__':
    d1M1Y1 = input().split()
    d1 = int(d1M1Y1[0])
    m1 = int(d1M1Y1[1])
    y1 = int(d1M1Y1[2])
    d2M2Y2 = input().split()
    d2 = int(d2M2Y2[0])
    m2 = int(d2M2Y2[1])
    y2 = int(d2M2Y2[2])
    result = server_cost(d1, m1, y1, d2, m2, y2)
    print(str(result) + '\n')
