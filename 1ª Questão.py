import os
from time import sleep
os.system("cls || clear")

valor_credito = 0
preco_total = 0
pratos_solicitados = ""
total_pagar = 0
preco_total = 0
cnt = 0
cnt1 = ""
preco = 0
formaci = 0

while True:
    print("""
    ================= MENU =================
    1 \t Picanha \t|R$ 25,00
    2 \t Lasanha \t|R$ 20,00
    3 \t Strogonoff \t|R$ 18,00
    4 \t Bife acebolado |R$ 15,00
    5 \t Pão com ovo \t|R$ 5,00
    6 \t Feijoada \t|R$ 15,00
    7 \t Carbonara  \t|R$ 28,00
    0 \t Fechar menu \t|
    """)
   
    opcao = input("Digite o número da opção desejada: ")
   
    match opcao:
        case "1":
            cnt = "1"
            prato = "Picanha"
            preco = 25
            print ("ADICIONANDO...")
            sleep(2)
        case "2":
            cnt = "2"
            prato = "Lasanha"
            preco = 20
            print ("ADICIONANDO...")
            sleep(2)
        case "3":
            cnt = "3"
            prato = "Strogonoff"
            preco = 18
            print ("ADICIONANDO...")
            sleep(2)
        case "4":
            cnt = "4"
            prato = "Bife acebolado"
            preco = 15
            print ("ADICIONANDO...")
            sleep(2)
        case "5":
            cnt = "5"
            prato = "Pão com ovo"
            preco = 5
            print ("ADICIONANDO...")
            sleep(2)
        case "6":
            cnt = "6"
            prato = "Feijoada"
            preco = 15
            print ("ADICIONANDO...")
            sleep(2)
        case "7":
            cnt = "7"
            prato = "Carbonara"
            preco = 28
            print ("ADICIONANDO...")
            sleep(2)
        case "0":
            os.system("cls || clear")
            print("\n=== Nota Fiscal ===")
            print(f"↓ Pedidos ↓ \n Código | {cnt1}\n Prato  | {pratos_solicitados}\n ----------------- \n↓ Valores cobrados e Descontos ↓")
            print(f" Subtotal: R$ {preco}")
            print(f" Forma de pagamento: {formaci}")
            print(f" Valor do desconto: R$ {valor_credito}")
            print(f" Valor total da compra: R$ {total_pagar}")
            break
        case _:
             continue
   
    preco_total += preco
    pratos_solicitados += "| " + prato if pratos_solicitados else prato
    cnt1 += "| " + cnt if cnt1 else cnt


    os.system("cls || clear")
    mais_pedidos = input("Deseja fazer um novo pedido?\nUse 'S' or 'N' para responder: ").lower()

    if mais_pedidos == "n":
        break 

   
if preco_total > 0:
    os.system("cls || clear")
    forma_pagamento = input("Qual a forma de pagamento? \n 1 para À vista \n 2 para Crédito \n ->  ").lower()
    if forma_pagamento == "2":
        formaci = "Crédito"
        valor_credito = preco_total * 0.10

    if forma_pagamento == "1":
        formaci = "À vista"
        desconto = preco_total * 0.10
        valor_credito -= desconto 
        
total_pagar = preco_total + valor_credito

os.system("cls || clear")
print("\n=== Nota Fiscal ===")
print(f"↓ Pedidos ↓ \n Código | {cnt1}\n Prato  | {pratos_solicitados}\n ----------------- \n↓ Valores cobrados e Descontos ↓")
print(f" Subtotal: R$ {preco}")
print(f" Forma de pagamento: {formaci}")
print(f" Valor do desconto: R$ {valor_credito}")
print(f" Valor total da compra: R$ {total_pagar}")