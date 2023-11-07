def radix_sort(arr):
    print('Initial array:')
    print(', '.join(arr))
    print('**********')
    max_len = max(len(s) for s in arr)
    buckets = [list() for _ in range(10)]
    exp = 1
    phase = 1
    while max_len >= exp:
        for s in arr:
            index = int(s[-exp]) if exp <= len(s) else 0
            buckets[index].append(s)
        arr = []

        print(f'Phase {phase}')
        for i, x in enumerate(buckets):
            if x:
                print(f'Bucket {i}: {", ".join(x)}')
            else:
                print(f'Bucket {i}: empty')
        print('**********')
        for bucket in buckets:
            arr.extend(bucket)
            bucket.clear()
        exp += 1
        phase += 1
    print('Sorted array:')
    return arr


N = int(input())
lst = [input() for _ in range(N)]

sorted_lst = radix_sort(lst)
print(', '.join(sorted_lst))
