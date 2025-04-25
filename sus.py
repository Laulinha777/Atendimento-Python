#Projetinho de Fila Médica em Python
#Objetivo: Criar um sistema de gerenciamento de senhas, para uma clínica médica de atendimentos.
import time

class Paciente:
    def __init__(self, nome, setor, senha, preferencial=False):
        self.nome = nome
        self.setor = setor
        self.senha = senha
        self.preferencial = preferencial

    def __str__(self):
        return f"{self.nome} | Setor: {self.setor} | Senha: {self.senha}"

class Consultorio:
    def __init__(self, nome, limite, sigla):
        self.nome = nome
        self.limite = limite
        self.sigla = sigla
        self.contador_normal = 1
        self.contador_pref = 1

    def gerar_senha(self, preferencial=False):
        if preferencial:
            senha = f"{self.sigla}P{self.contador_pref:03d}"
            self.contador_pref += 1
        else:
            senha = f"{self.sigla}N{self.contador_normal:03d}"
            self.contador_normal += 1
        return senha

class FilaAtendimentos:
    def __init__(self):
        self.fila_pref = []
        self.fila_normal = []

    def adicionar_pacientes(self, paciente):
        if paciente.preferencial:
            self.fila_pref.append(paciente)
        else:
            self.fila_normal.append(paciente)

    def chamar_paciente(self):
        if self.fila_pref:
            return self.fila_pref.pop(0)
        elif self.fila_normal:
            return self.fila_normal.pop(0)
        else:
            return None

consultorios_info = [
    {'setor': 'CG - Clínica Geral', 'sigla': 'CG', 'limite': 60},
    {'setor': 'GIN - Ginecologia', 'sigla': 'GIN', 'limite': 40},
    {'setor': 'PED - Pediatria', 'sigla': 'PED', 'limite': 40},
    {'setor': 'GER - Geriatria', 'sigla': 'GER', 'limite': 40},
    {'setor': 'ORT - Ortopedia', 'sigla': 'ORT', 'limite': 40}
]

consultorios = [Consultorio(c['setor'], c['limite'], c['sigla']) for c in consultorios_info]

fila_atendimentos = FilaAtendimentos()

def tempo_espera(fila):
    paciente = fila.chamar_paciente()
    if paciente:
        print(f"\n👩‍⚕️ Atendendo: {paciente}")
        time.sleep(5)  #Apenas uma simulaçãozinea
        print(f"✅ Atendimento finalizado para {paciente.nome}.")
        print(f"☞☞Chamando o próximo paciente.\n")
    else:
        print("⏳ Nenhum paciente na fila.\n")

def adicionar_paciente():
    print("Escolha o setor de atendimento:")
    for i, consultorio in enumerate(consultorios, start=1):
        print(f"{i}. {consultorio.nome}")

    escolha = int(input("Digite o número do consultório desejado: "))- 1
    consultorio = consultorios[escolha]

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    resposta = input("Deseja atendimento preferencial? (s/n): ").strip().lower()
    preferencial = resposta == 's'

    senha = consultorio.gerar_senha(preferencial)
    novo_paciente = Paciente(nome, consultorio.nome, senha, preferencial)
    fila_atendimentos.adicionar_pacientes(novo_paciente)

    print(f"\n🆕 Paciente adicionado: {nome} | Setor: {consultorio.nome} | Senha: {senha}\n")

def mostrar_filas():
    print("\n📋 Fila Preferencial:")
    if not fila_atendimentos.fila_pref:
        print("Não existe pacientes nesta fila.")
    for i, paciente in enumerate(fila_atendimentos.fila_pref, start=1):
        print(f"{i}. {paciente}")

    print("\n📋 Fila Normal:")
    if not fila_atendimentos.fila_normal:
        print("Não existe pacientes nesta fila.")
    for i, paciente in enumerate(fila_atendimentos.fila_normal, start=1):
        print(f"{i}. {paciente}")
    print("\n")

def menu():
    while True:
        print("⫸Menu de Atendimentos⫷")
        print("1. Gerar senha para paciente")
        print("2. Chamar próximo paciente")
        print("3. Exibir status da fila")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_paciente()
        elif escolha == '2':
            tempo_espera(fila_atendimentos)
        elif escolha == '3':
            mostrar_filas()
        elif escolha == '4':
            print("Encerrando sistema. Até logo! 👋")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o menu
menu()
