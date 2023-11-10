def z_function(S):
    n = len(S)
    h = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            h[i] = min(r - i + 1, h[i - l])
        while i + h[i] < n and S[h[i]] == S[i + h[i]]:
            h[i] += 1
        if i + h[i] - 1 > r:
            l, r = i, i + h[i] - 1
    return h


S = str(input())
print(*z_function(S))
