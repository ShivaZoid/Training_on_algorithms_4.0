def foo(lst, ft):
    pe, ps = ft[0], ft[1]
    lst_min = min(lst[pe:ps+1])
    res = max(lst[pe:ps+1])
    if res == lst_min:
        return 'NOT FOUND'
    return res


dl, st = map(int, input().split())
lst = list(map(int, input().split()))
p = [list(map(int, input().split())) for _ in range(st)]

for x in range(len(p)):
    print(foo(lst, p[x]))
