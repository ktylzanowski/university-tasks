def joseph(n, k):
    if n == 1:
        return 1
    return (joseph(n-1, k)+k-1) % n+1
