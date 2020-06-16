import copy as cp

def read_data(filepath):
    with open(filepath) as f:
        f.readline()
        n, m = [int(x) for x in next(f).split()]
        data = [[int(x) for x in line.split()[1::2]] for line in f]
    data = list(filter(lambda x: len(x) > 1, data))
    return n, m, data

def loss_function(data, m):
    Sum_tmp = 0
    C_tmp = [0] * m
    for i in range(m):
        C_tmp[i] = Sum_tmp + data[0][i]
        Sum_tmp = C_tmp[i]
    for d in data[1:]:
        Sum_tmp = 0
        for i in range(m):
            C_tmp[i] = max(Sum_tmp, C_tmp[i]) + d[i]
            Sum_tmp = C_tmp[i]
    C_max = Sum_tmp
    return C_max

def neh(N, m):
    k = 1
    W = [[sum(x), x] for x in N]
    pi = []
    pi_star = []
    W.sort(key=lambda x: x[0])
    while len(W) != 0:
        j = W[len(W) - 1][1]
        pi_star.append(j)
        for l in range(0, k):
            pi.insert(l, j)
            if loss_function(pi, m) < loss_function(pi_star, m):
                pi_star = cp.copy(pi)
            del pi[l]
        pi = cp.copy(pi_star)
        k += 1
        del W[len(W) - 1]
    return loss_function(pi_star, m), pi


filepath = 'data/ta001.txt'
_, m, data = read_data(filepath)
C_max, pi = neh(data, m)
print(C_max)
print(pi)