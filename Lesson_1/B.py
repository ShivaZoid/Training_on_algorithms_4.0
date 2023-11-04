def partition(lst, pivot):
    less = [num for num in lst if num < pivot]
    equal = [num for num in lst if num == pivot]
    more = [num for num in lst if num > pivot]
    return less, equal, more


def quicksort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        left, center, right = partition(lst, pivot)
        return quicksort(left) + center + quicksort(right)


N = int(input())
lst = list(map(int, input().split()))

print(*quicksort(lst))
