def merge(array_1, array_2):
    result = [0] * (len(array_1) + len(array_2))
    l = 0
    r = 0
    k = 0
    while l < len(array_1) and r < len(array_2):
        if array_1[l] >= array_2[r]:
            result[k] = array_2[r]
            r += 1
        else:
            result[k] = array_1[l]
            l += 1
        k += 1
    while l < len(array_1):
        result[k] = array_1[l]
        l += 1
        k += 1
    while r < len(array_2):
        result[k] = array_2[r]
        r += 1
        k += 1
    return result


N = int(input())
lst_1 = list(map(int, input().split()))

M = int(input())
lst_2 = list(map(int, input().split()))

print(*merge(lst_1, lst_2))
