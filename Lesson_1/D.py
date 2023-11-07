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


def merge_sort(array):
    if len(array) == 0:
        return []
    if len(array) == 1:
        return array
    else:
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left, right)


N = int(input())
lst = list(map(int, input().split()))

answer = merge_sort(lst)

print(' '.join(str(x) for x in answer))
