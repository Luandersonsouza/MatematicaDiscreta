def Euclides(a, b):
    """ Pelo metodo de euclides, calcula o mdc, retornando-o junto com a lista dos quocientes (metodo tabela) """
    
    quocientes = []
 
    while((a % b) != 0):
        quocientes.append(a // b)
        a = a % b
        a, b = b, a
    quocientes.append(a // b)
 
    return b, quocientes
 
def table(lista):
    """ usa o metodo da tabela para encontrar s e t """
 
    if(len(lista) == 1):
        lista.append(lista[0] + 1)
        lista[0] = 1
 
    elif(len(lista) == 2):
        lista.reverse()
        lista[0] = -1
        lista[1] *= -1
 
    else:
        lista.pop()
        lista.reverse()
 
        x = 1
 
        for i in range(len(lista)):
            if(i > 0):
                lista[i] *= lista[i - 1]
                lista[i] += x
                x = lista[i-1]
    
    if (len(lista) % 2 == 0): lista[-2] *= -1
    else: lista[-1] *= -1
 
    return lista[-2], lista[-1]
 
def combLinear(a, b):
    """ encontra a combinação linear do mdc de a e b """
    
    inverted = False
 
    if (a < b):
        inverted = True
        a, b = b, a
    
    mdc, lista = Euclides(a, b)
 
    s, t = table(lista)
 
    if (inverted):
        s, t = t, s
        a, b = b, a
 
    print("{} = ({}*{}) + ({}*{})".format(mdc, s, a, t, b))



print("Digite o valor de p:") 
p = int(input())
print("Digite o valor de q:") 
q = int(input())
 
combLinear(p, q)