def piramide  (n):
    inicio = 1
    while inicio <= n:
        repeat = 1
        while repeat <= inicio:
            print (repeat, end = " ")
            repeat = repeat +1
        inicio = inicio + 1
        print (' ')
piramide(9)

#ficar atenta com a posição dos comandos