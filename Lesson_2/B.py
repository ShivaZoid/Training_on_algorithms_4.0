def prefix_function(S):
    n = len(S)
    h = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and S[i] != S[j]:
            j = h[j - 1]
        if S[i] == S[j]:
            j += 1
        h[i] = j
    return h


def min_length(S):
    pi = prefix_function(S)
    n = len(S)
    max_length = pi[-1]
    result = n - max_length
    return result


S = str(input())
print(min_length(S))
