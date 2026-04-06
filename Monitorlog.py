import datetime
import random

def gerar_logs():
    print("== GERADOR DE LOGS ==")

    arquivo = open("log.txt", "w")

    for i in range(20):
        tempo = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"

        status = random.choice([200, 200, 200, 404, 500])
        tempo_resp = random.randint(50, 2000)

        linha = f"[{tempo}] {ip} - {status} - {tempo_resp}ms\n"

        arquivo.write(linha)

    arquivo.close()

    print("Logs gerados e salvos em log.txt")


def separar(linha):
    partes = []
    atual = ""

    for c in linha:
        if c == " ":
            if atual != "":
                partes.append(atual)
                atual = ""
        else:
            atual += c

    if atual != "":
        partes.append(atual)

    return partes


def analisar_logs():
    print("== ANALISADOR DE LOGS ==")

    try:
        arquivo = open("log.txt", "r")
    except:
        print("Arquivo não encontrado! Gere os logs primeiro.")
        return

    total = 0
    erros = 0
    lentos = 0

    for linha in arquivo:
        total += 1

        partes = separar(linha)

        ip = partes[2]
        status = int(partes[4])
        tempo = int(partes[6].replace("ms", ""))

        if status >= 500:
            erros += 1

        if tempo > 1000:
            lentos += 1

    arquivo.close()

    print("\n=== RELATÓRIO ===")
    print("Total de logs:", total)
    print("Erros (500):", erros)
    print("Requisições lentas:", lentos)


    if erros > 5:
        print(" Sistema CRÍTICO")
    elif lentos > 5:
        print(" Sistema em ATENÇÃO")
    else:
        print(" Sistema SAUDÁVEL")


def gerar_e_analisar_logs():
    gerar_logs()
    analisar_logs()

def sair():
    print("Encerrando sistema...")

def menu():
    print('\n== MENU ==')
    print('1: Gerar logs')
    print('2: Analisar logs')
    print('3: Gerar e analisar logs')
    print('4: Sair')

while True:
    menu()
    
    try:
        escolha = int(input('Escolha uma opção: '))
    except:
        print("Digite um número válido")
        continue

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