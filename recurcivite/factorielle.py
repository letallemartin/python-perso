def factorielle(n):
    if n  <= 1 :
        return n
    return n * factorielle(n-1)

print(factorielle(9))