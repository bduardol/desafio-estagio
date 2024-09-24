def fibonacci(x):
    a = 0 
    b = 1
    if x == a or x == b:
        return True

    while b <= x:
        a, b = b, a + b
        
        if b == x:
            return True
    return False

numero = int(input())

if fibonacci(numero):
    print(f"O numero {numero} pertence a sequencia de finonacci!")
else:
    print(f'Esse numero n pertence não vei')