def calcular(n):

    resultado = [ ]

    a, b = 0, 1        

    while a < n:
        resultado.append(a)     
        a, b = b, a+b           
    return resultado 

res = calcular(100) 
print(res)