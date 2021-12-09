if __name__ == '__main__':
    tuple_len = int(raw_input())
    a = tuple(map(int, raw_input().split(' ')))
    print hash(a)
