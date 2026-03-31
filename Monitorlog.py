import datetime
import random
import time

def gerar_logs():
    print("== GERADOR DE LOGS ==")
    
    for i in range(10):
        tempo = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        ip = f"{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
        
        print(f"[{tempo}] {ip}")

def analisar_logs():
    print("== ANALISADOR DE LOGS ==")

def gerar_e_analisar_logs():
    gerar_logs()
    analisar_logs()

def sair():
    print("== SAIR ==")

def menu():
    print(' == Menu ==')
    nome_arq = 'log.txt'
    print('1: Gerar logs')
    print('2: Analisar logs')
    print('3: Gerar e analisar logs')
    print('4: Sair')

while True:
    menu()
    escolha = int(input('Escolha uma opção: '))

    if escolha == 1:
        gerar_logs()

    elif escolha == 2:
        analisar_logs()

    elif escolha == 3:
        gerar_e_analisar_logs()

    elif escolha == 4:
        sair()
        break

    else:
        print("Opção inválida")