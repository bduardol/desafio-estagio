'''4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP  R$67.836,43
• RJ  R$36.678,66
• MG  R$29.229,88
• ES  R$27.165,48
• Outros  R$19.849,53
Escreva um programa na linguagem que desejar onde calcule o percentual de 
representação que cada estado teve dentro do valor total mensal da distribuidora. '''


dicionario = [ 
    ["SP", 6783643], 
    ["RJ",3667866], 
    ["MG", 2922988], 
    ["ES", 2716548] , 
    ["outros", 1984953]]


total = 0
for i in dicionario:
    total+=i[1]

porcetagem = []

for i in dicionario:
    porcetagem.append([i[0], i[1]/total])
    
for i in porcetagem:
    if i[0] == "Outros":
        print(f'Os {i[0]} estados representam {i[1]*100:.2f}% do faturamento mensal')
    else:
        print(f'O estado {i[0]} representa {i[1]*100:.2f}% do faturamento mensal')