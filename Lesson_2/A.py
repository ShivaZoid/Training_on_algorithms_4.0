def equality(S, lst):
    results = []
    p = 10 ** 9 + 7
    x_ = 257
    h = [0] * (len(S) + 1)
    x = [0] * (len(S) + 1)
    x[0] = 1
    S = '' + S

    for i in range(1, len(S) + 1):
        h[i] = (h[i-1] * x_ + ord(S[i-1])) % p
        x[i] = (x[i-1] * x_) % p

    for arry in lst:
        length = arry[0]
        positions = arry[1:3]
        hash_1 = (h[positions[0] + length] + h[positions[1]] * x[length]) % p
        hash_2 = (h[positions[1] + length] + h[positions[0]] * x[length]) % p
        if hash_1 == hash_2:
            results.append('yes')
        else:
            results.append('no')

    return results


S = str(input())
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

for result in equality(S, lst):
    print(result)
