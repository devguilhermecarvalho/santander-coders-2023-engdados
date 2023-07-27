import json
import time

def menu(): # Menu, está ligado diretamente a função Main
    menu = """
        Boas-vindas ao nosso sistema:
        =======================================    
        1 – Inserir usuário
        2 – Excluir usuário
        3 – Atualizar usuário
        4 – Informações de um usuário
        5 – Informações de todos os usuários
        6 – Sair
        =======================================
        Digite a opção deseja:
        """
    return input(menu)

def lerArquivo(lerArquivo=True): # Lê o arquivo json e armazena no dicionário > dados
    nomeArquivo = 'projetoModuloII.json'
    if lerArquivo:
        try:
            with open(nomeArquivo, 'r') as arquivo: # Somente a leitura do arquivi e a mudança da chamada
                dados = json.load(arquivo) # Armazenando o dicionário em uma variável > dados
                arquivo.close() # Fechando o arquivo
        except FileNotFoundError:
            print(f"Arquivo '{nomeArquivo}' não encontrado.")
    else:
        print("Leitura desabilitada.")
    return dados # A função retorna o dicionário que foi copiado do arquivo

def atualiza_arquivo(dados): # Essa função armazena a ação para atualizar o arquivo json, e só é acionada na função sair
    nomeArquivo = 'projetoModuloII.json'
    with open(nomeArquivo, 'w') as arquivo: # O 'w' não adiciona o usário no final. Ela cria um novo conteúdo do zero.
        json.dump(dados, arquivo, indent=4)

def inserir_usuario(dados): # Insere o usuário no dicionário
    novo_usuario = {
        "Status": True,
        "Nome": input(),
        "Telefone": input(),
        "Endereço": input()
    }
    chave_maxima = max(map(int, dados.keys()), default=0) + 1
    dados[str(chave_maxima)] = novo_usuario

    return novo_usuario

def usuarios_cadastrados(dados): # Lista somente os usuários que possuem o status: True
    usuarios_encontrados = []

    for chave, usuario in dados.items():
        if usuario.get("Status") is True:
            usuarios_encontrados.append({"Id:": chave, **usuario})

    if usuarios_encontrados:
        print(json.dumps(usuarios_encontrados, indent=4))
    else:
        print("Nenhum usuário cadastrado com status 'True'.")
    time.sleep(3)
    return
        
def sair(dados): # Função sair que armazena também as funções que modificam o arquivo json
    atualiza_arquivo(dados) # Chama a função atualiza arquivo
    print("""\t
    6 - Sair  
    ======================================================
    → Obrigado por utilizar o nosso sistema, volte logo!
    ======================================================
        """)

def main(dados): # Master
    while True:
        opcao = menu()        
        # Menu:
        if opcao == "1": # Inserir Usuário
            print(f"\n\t1 - Inserir Usuário")
            inserir_usuario(dados)
        elif opcao == "2": # Excluir Usuário
            print(f"\n\t2 - Excluir Usuário")
        elif opcao == "3": # Atualizar Usiário
            print(f"\n\t3 - Atualizar Usuário")
        elif opcao == "4": # Informações de um Usuários
            print(f"\n\t4 - Informações de um usuário")
        elif opcao == "5": # Informações de todos os usuários
            print(f"\n\t5 - Informações de todos os usuários")
            usuarios_cadastrados(dados)
        elif opcao == "6": # Sair
            sair(dados)
            break
        else:
            time.sleep(2)
            print(f"# Operação inválida, tente novamente. #")

dados = lerArquivo()
main(dados)