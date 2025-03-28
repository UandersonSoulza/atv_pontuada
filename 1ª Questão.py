import os
from time import sleep
os.system("cls || clear")

valor_credito = 0
preco_total = 0
pratos_solicitados = ""
total_pagar = 0
preco_total = 0

while True:
    print("""
    ================= MENU =================
    1 \t Picanha \t\tR$ 25,00
    2 \t Lasanha \t\tR$ 20,00
    3 \t Strogonoff \t\tR$ 18,00
    4 \t Bife acebolado \tR$ 15,00
    5 \t Pão com ovo \t\tR$ 5,00
    6 \t Feijoada \t\tR$ 5,00
    7 \t Carbonara  \t\tR$ 5,00
        Digite 0 para sair
          """)
   
    opcao = int(input("Digite o número da opção desejada: "))
   
    match opcao:
        case 1:
            prato = "Picanha"
            preco = 25
            print ("adicionado!")
            sleep(2)
        case 2:
            prato = "Lasanha"
            preco = 20
            print ("adicionado!")
            sleep(2)
        case 3:
            prato = "Strogonoff"
            preco = 18
            print ("adicionado!")
            sleep(2)
        case 4:
            prato = "Bife acebolado"
            preco = 15
            print ("adicionado!")
            sleep(2)
        case 5:
            prato = "Pão com ovo"
            preco = 5
            print ("adicionado!")
            sleep(2)
        case 6:
            prato = "Pão com ovo"
            preco = 5
            print ("adicionado!")
            sleep(2)
        case 7:
            prato = "Pão com ovo"
            preco = 5
            print ("adicionado!")
            sleep(2)
        case 0:
            print("\n=== Nota Fiscal ===")
            print(f"Pratos solicitados: {pratos_solicitados}")
            print(f"Valor da gorjeta: R$ {valor_credito}")
            print(f"Valor total da compra: R$ {total_pagar}")
            prato = ""
            preco = 0
        case _:
            break
   
    preco_total += preco
    pratos_solicitados += ", " + prato if pratos_solicitados else prato

    mais_pedidos = input("Deseja fazer um novo pedido?\nUse 'S' or 'N' para responder: ").lower()

    if mais_pedidos == "n":
        break 

   
if preco_total > 0:
    forma_pagamento = input("Qual a forma de pagamento? \n 1 para a vista \n 2 para crédito \n ->  ").lower()
    if forma_pagamento == "2":
        valor_credito = preco_total * 0.10
    if forma_pagamento == "1":
       desconto = preco_total * 0.10
       valor_credito -= desconto 
        
total_pagar = preco_total + valor_credito

print("\n=== Nota Fiscal ===")
print(f"Pratos solicitados: {pratos_solicitados}")
print(f"Valor do desconto: R$ {valor_credito}")
print(f"Valor total da compra: R$ {total_pagar}")