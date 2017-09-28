if __name__ == '__main__':
    count = int(raw_input())
    weights = map(int,raw_input().split())
    weights.sort()
    purchases = count
    comparator = -1
    i = 0
    while i < count:
        if weights[i] > comparator:
            comparator = weights[i] + 4
        else:
            purchases -= 1
        i += 1
    print(purchases)

