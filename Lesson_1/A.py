def partition(lst, pivot):
    less = [num for num in lst if num < pivot]
    equal = [num for num in lst if num == pivot]
    more = [num for num in lst if num > pivot]
    return less, equal, more


N = int(input())

lst = list(map(int, input().split()))

pivot = int(input())

result = partition(lst, pivot)

print(f'{len(result[0])}\n{len(result[1]) + len(result[2])}')
