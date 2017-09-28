if __name__ == '__main__':
    count = int(raw_input())
    weights = map(int,raw_input().split())
    weights.sort()
    purchases = count
    comparator = -1
    for weight in weights:
        if weight > comparator:
            comparator = weight + 4
        else:
            purchases -= 1
    print(purchases)
