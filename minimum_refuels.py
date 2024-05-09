def min_refuels(m, S):
    p = 0
    no_refills = 0
    while p < C+1:
        q = p
        while p < C+1 and S[p+1] - S[q] <= m:
            p += 1
        if q == p:
            return -1
        if p < C+1:
            no_refills += 1
    return no_refills