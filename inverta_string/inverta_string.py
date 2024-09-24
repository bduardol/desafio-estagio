string = input()
lista = []
revertida = ""

for i in string:
    lista.append(i)

for i in range(len(lista)):
    revertida += lista.pop()
    
print(revertida)



