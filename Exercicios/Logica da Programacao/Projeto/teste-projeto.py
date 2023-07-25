import time
import json

# Sistema de Cadastro
    # Menu - concluído
def menu():
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

def lerArquivo(ler=True, nomeArquivo='projetoModuloII.json'):
    if ler:
        try:
            with open(nomeArquivo, 'r') as arquivo:
                dados = json.load(arquivo)
                return dados
        except FileNotFoundError:
            print(f"Arquivo '{nomeArquivo}' não encontrado.")
        except json.JSONDecodeError:
            print(f"Erro na leitura do arquivo '{nomeArquivo}': Formato JSON inválido.")
        except Exception as e:
            print(f"Erro na leitura do arquivo '{nomeArquivo}': {e}")
    else:
        print("Leitura desabilitada.")
    return None
    
def usuarios_cadastrados():
    data_dict = lerArquivo()
    if data_dict:
        for identificador, usuario in data_dict.items():
            print(f"""
        Identificador: {identificador}
        Informações do Usuário:\n\t{usuario}
                """)
    else:
        print("Nenhum usuário cadastrado.")
    return

def inserir_usuario():
    nome     = print(f"Digite o nome completo: ") # Obrigatório
    telefone = print(f"Digite o telefone: ")      # Obrigatório
    endereco = print(f"Digite o endereço completo: ") # Obrigatório
    id       = identificador
    status   = True

def filtrar_usuarios():
    id = x

def desativar_usuario():
    id       = x
    status   = x
    nome     = x
    telefone = x

def atualizar_usuario():
    id       = x

def exibir_usuario():
    id       = x

def listar_usuarios():
    id       = x

def sair():
    print("""\t
        6 - Sair  
        ======================================================
         → Obrigado por utilizar o nosso sistema, volte logo!
        ======================================================
         """)

def main():
    while True:
        time.sleep(0.5)
        opcao = menu()

        if opcao == "1":
            print(f"\n\t1 - Inserir Usuário")
        elif opcao == "2":
            print(f"\n\t2 - Exluir Usuário")
        elif opcao == "3":
            print(f"\n\t3 - Atualizar Usuário")
        elif opcao == "4":
            print(f"\n\t4 - Informações de um usuário")
        elif opcao == "5":
            print(f"\n\t5 - Informações de todos os usuários")
            usuarios_cadastrados()
        elif opcao == "6":
            sair()
            break
        else:
            print(f"### Operação inválida, tente novamente.")
main()