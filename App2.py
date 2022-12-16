

def sol():
    C = 1
    L = 1
    V = 1
    P = 1
    cont = 0
    estInicial = [C, L, V, P]
    print(estInicial)
    estAceptacion = [0, 0, 0, 0]
    while estInicial  != estAceptacion :
        """if (C == 1) and (L != V) and (V != P):
            C = 0
            estInicial = [C, L, V, P]
            print(estInicial)"""
        #devuelve al campesino
        if (C == 0 and L != V and V != P):
            C = 1
            estInicial = [C, L, V, P]
        #pasa campseino y lobo
        elif (C == 1) and (L == 1) and (V != P):
            C = 0
            L = 0
            estInicial = [C, L, V, P]
        #pasa campesino y pasto
        elif (C == 1) and (P == 1) and (V != L):
            C = 0
            P = 0
            estInicial = [C, L, V, P]
        #pasa campseino y oveja
        elif (C == 1) and (V == 1):
            C = 0
            V = 0
            estInicial = [C, L, V, P]
        #devuelve campesino y pasto
        elif (C == 0) and (P == 0) and (L != V):
            C = 1
            P = 1
            estInicial = [C, L, V, P]
       
        #devuelve campseino y oveja
        elif (C == 0) and (V == 0) and (P != L):
            C = 1
            V = 1
            estInicial = [C, L, V, P]
        print(estInicial)
        

sol()

