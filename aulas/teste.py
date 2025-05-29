# Sistema de Cadastro de Alunos

alunos = {}  # Dicionário para armazenar os alunos

def cadastrar_aluno():
    """Função para cadastrar um novo aluno"""
    print("\n--- Cadastro de Aluno ---")
    id_aluno = input("Digite o ID do aluno: ")
    nome = input("Digite o nome do aluno: ")
    idade = input("Digite a idade do aluno: ")
    curso = input("Digite o curso do aluno: ")
    
    alunos[id_aluno] = {
        'nome': nome,
        'idade': idade,
        'curso': curso
    }
    print(f"Aluno {nome} cadastrado com sucesso!")

def listar_alunos():
    """Função para listar todos os alunos cadastrados"""
    print("\n--- Lista de Alunos ---")
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for id_aluno, info in alunos.items():
            print(f"ID: {id_aluno} | Nome: {info['nome']} | Idade: {info['idade']} | Curso: {info['curso']}")

def buscar_aluno():
    """Função para buscar um aluno pelo ID"""
    print("\n--- Buscar Aluno ---")
    id_aluno = input("Digite o ID do aluno: ")
    aluno = alunos.get(id_aluno)
    
    if aluno:
        print(f"\nDados do aluno:")
        print(f"ID: {id_aluno}")
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Curso: {aluno['curso']}")
    else:
        print("Aluno não encontrado.")

# Menu principal
while True:
    print("\n--- Sistema de Cadastro de Alunos ---")
    print("1. Cadastrar novo aluno")
    print("2. Listar todos os alunos")
    print("3. Buscar aluno por ID")
    print("4. Sair")
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == '1':
        cadastrar_aluno()
    elif opcao == '2':
        listar_alunos()
    elif opcao == '3':
        buscar_aluno()
    elif opcao == '4':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")