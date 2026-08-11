def fibonachi(nombre,ancien,lim,n = 0):
    if n < lim:
        n += 1
        return fibonachi(nombre + ancien, nombre ,lim)
    return nombre
print(fibonachi(1,0,5))

