def fibonachi(n,ancien,lim):
    if n < lim:
        return fibonachi(n + ancien,n ,lim)
    return n
print(fibonachi(1,0,1000))

