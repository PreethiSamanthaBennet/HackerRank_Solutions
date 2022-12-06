if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[(arr.index(max(arr)))-1])
