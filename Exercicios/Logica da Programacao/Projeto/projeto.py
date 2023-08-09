import json
import time

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
        Digite a opção desejada:
        """
    return input(menu)

def lerArquivo():
    path = 'projetoModuloII.json'
    if lerArquivo:
        try:
            with open(path, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            dados = {}
            print(f"Arquivo '{path}' não encontrado.")
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o arquivo JSON em '{path}'. Verifique o formato do arquivo.")
            return None
    else:
        print("Leitura desabilitada.")
    return dados

def atualiza_arquivo(dados):
    path = 'projetoModuloII.json'
    with open(path, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def inserir_usuario(dados):
  
    novo_usuario = {
        "Status": True,
        "Nome": "",
        "Endereço": "",
        "Telefone": ""
    }

    while not novo_usuario["Nome"].strip():
        novo_usuario["Nome"] = input("\tQual é o nome do usuário? ")
        if not novo_usuario["Nome"].strip():
            print("\tO nome não pode ser vazio. Insira o nome novamente.")
    
    while not novo_usuario["Endereço"].strip():
        novo_usuario["Endereço"] = input("\tQual é o endereço do usuário? ")
        if not novo_usuario["Endereço"].strip():
            print("\tO endereço não pode ser vazio. Insira o endereço novamente.")

    while not novo_usuario["Telefone"].strip():
        novo_usuario["Telefone"] = input("\tQual é o telefone do usuário? ")
        if not novo_usuario["Telefone"].strip():
            print("\tO telefone não pode ser vazio. Insira o telefone novamente.")

    print(f"{novo_usuario}\n")
    print("\n\tAs informações do usuário estão corretas?")
    resposta = input("\tDigite 's' para sim ou 'n' para não: ")
    if resposta.lower() == 's':
        chave_maxima = max(map(int, dados.keys()), default=0) + 1
        dados[str(chave_maxima)] = novo_usuario
        print("\tInformações salvas. O ID do novo usuário é", chave_maxima)
    else:
        print("\tAs informações não foram salvas.")
    return inserir_usuario

def excluir_usuario(dados):
    id_usuario = input("\tDigite o ID do usuário que deseja excluir: ")
    if id_usuario in dados:
        print("\tInformações do usuário:")
        print(f"{json.dumps(dados[id_usuario], indent=4)}")
        
        print("\n\tOpções de exclusão:")
        print("\t1 - Desabilitar usuário")
        print("\t2 - Excluir dados do usuário")
        opcao = input("\tDigite a opção desejada: ")
        
        if opcao == '1':
            if dados[id_usuario]["Status"] == True:
                dados[id_usuario]["Status"] = False
                print("\tUsuário desabilitado.")
                time.sleep(3)
            else:
                print("\tEste usuário já foi desabilitado.")
                time.sleep(3)
        elif opcao == '2':
            del dados[id_usuario]
            print("\tDados do usuário excluídos.")
            time.sleep(3)
        else:
            print("\tOpção inválida.")
            time.sleep(3)
    else:
        print(f"Usuário com ID {id_usuario} não encontrado.")
        time.sleep(3)

# FUNÇÕES DE EXIBIÇÃO DO USUÁRIO - 4 INFORMAÇÕES DE UM USUÁRIO
def listar_registro_por_id(dados, id_input):
    registro = dados.get(str(id_input))
    if registro:
        exibir_registro(registro)
    else:
        print(f"Registro com o ID {id_input} não foi encontrado.")

def listar_registro_por_nome(dados, nome_input):
    registros_encontrados = []
    for registro_id, registro in dados.items():
        if registro.get('Nome', '').lower() == nome_input.lower():
            registros_encontrados.append(registro)
    if registros_encontrados:
        for registro in registros_encontrados:
            exibir_registro(registro)
    else:
        print(f"Nenhum registro encontrado para o Nome '{nome_input}'.")

def listar_registro_por_telefone(dados, telefone_input):
    registros_encontrados = []
    for registro_id, registro in dados.items():
        if registro.get('Telefone', '') == telefone_input:
            registros_encontrados.append(registro)
    if registros_encontrados:
        for registro in registros_encontrados:
            exibir_registro(registro)
    else:
        print(f"Nenhum registro encontrado para o Telefone '{telefone_input}'.")

def listar_registro_por_endereco(dados, endereco_input):
    registros_encontrados = []
    for registro_id, registro in dados.items():
        endereco_registro = registro.get('Endereço', '').strip()
        if endereco_registro.lower() == endereco_input.lower():
            registros_encontrados.append(registro)
    if registros_encontrados:
        for registro in registros_encontrados:
            exibir_registro(registro)
    else:
        print(f"Nenhum registro encontrado para o Endereço '{endereco_input}'.")

def exibir_registro(registro):
    print(f"""        Registro encontrado:
        =======================================
        Status: {registro.get('Status')}
        Nome: {registro.get('Nome')}
        Telefone: {registro.get('Telefone')}
        Endereço: {registro.get('Endereço', 'Não encontrado')}
        =======================================
        """)
    time.sleep(7)
# FIM 4

def atualizar_usuario(dados):
    id_usuario = input("Insira o ID do usuário: ")
    while id_usuario not in dados:
        print("Usuário não encontrado!\n")
        id_usuario = input("Insira o ID do usuário: ")

    print(f"\nUsuário encontrado! ID: {id_usuario}")
    print("\nQual informação deseja alterar?")
    print("1 - Nome")
    print("2 - Telefone")
    print("3 - Endereço")
    opcoes = input("Digite o número da opção (separado por espaços para várias opções): ").split()

    if "1" in opcoes:
        novo_nome = input("Insira o novo nome: ")
        if novo_nome.strip() != "":
            dados[id_usuario]["Nome"] = novo_nome
            print("Nome atualizado com sucesso.")
    if "2" in opcoes:
        novo_telefone = input("Insira o novo telefone: ")
        if novo_telefone.strip() != "":
            dados[id_usuario]["Telefone"] = novo_telefone
            print("Telefone atualizado com sucesso.")
    if "3" in opcoes:
        novo_endereco = input("Insira o novo endereço: ")
        if novo_endereco.strip() != "":
            dados[id_usuario]["Endereço"] = novo_endereco
            print("Endereço atualizado com sucesso.")

    if any(opcoes):
        print("\nInformações atualizadas:")
        print(json.dumps(dados[id_usuario], indent=4))
        confirmacao = input("As atualizações estão corretas? Digite 's' para sim ou 'n' para não: ")
        if confirmacao.lower() != 's':
            print("As informações não foram salvas.")
            for opcao in opcoes:
                if opcao == "1":
                    dados[id_usuario]["Nome"] = dados[id_usuario]["Nome"]
                elif opcao == "2":
                    dados[id_usuario]["Telefone"] = dados[id_usuario]["Telefone"]
                elif opcao == "3":
                    dados[id_usuario]["Endereço"] = dados[id_usuario]["Endereço"]
        else:
            print("Informações do usuário salvas com sucesso.")
            
def submenu(dados):
    print("\tEscolha a forma de busca:\n")
    print("\t1 – ID")
    print("\t2 – Nome")
    print("\t3 – Telefone")
    print("\t4 – Endereço")
    print("\t5 – Voltar")
    opcao = input("\t=======================================\n\tDigite a opção desejada:")
    
    if opcao == "1":
        id_input = int(input("\tDigite o ID do registro que deseja listar: "))
        print()
        listar_registro_por_id(dados, id_input)
    elif opcao == "2":
        nome_input = input("\tDigite o nome do registro que deseja listar: ")
        print()
        listar_registro_por_nome(dados, nome_input)
    elif opcao == "3":
        telefone_input = input("\tDigite o telefone do registro que deseja listar: ")
        print()
        listar_registro_por_telefone(dados, telefone_input)
    elif opcao == "4":
        endereco_input = input("\tDigite o endereço do registro que deseja listar: ")
        print()
        listar_registro_por_endereco(dados, endereco_input)
    elif opcao == "5":
        main(dados)

def informacoes_usuario(dados): 
    submenu(dados)
    
    """
    id_usuario = input("Qual a ID do usuário? ")
    usuario = dados.get(id_usuario)
    if usuario and usuario.get("Status"):
        print("Informações do usuário:")
        print(f"ID: {id_usuario}")
        print(f"Nome: {usuario['Nome']}")
        print(f"Endereço: {usuario['Endereço']}")
        print(f"Telefone: {usuario['Telefone']}")
    else:
        print("Usuário não encontrado ou inativo.")
    """

def listar_registros(arquivo_json):
    if arquivo_json:
        for chave, registro in arquivo_json.items():
            if registro.get("Status") is True:
                print(f"\tRegistro {chave}:")
                for campo, valor in registro.items():
                    print(f"\t{campo}: {valor}")
                print()
    else:
        print("Nenhum registro encontrado.")

def sair(dados):
    atualiza_arquivo(dados)
    print("""\t
    6 - Sair  
    ======================================================
    → Obrigado por utilizar o nosso sistema, volte logo!
    ======================================================
        """)

def main(dados):
    while True:
        opcao = menu()        
        if opcao == "1":
            print(f"\n\t1 - Inserir Usuário")
            inserir_usuario(dados)
        elif opcao == "2":
            print(f"\n\t2 - Excluir Usuário")
            excluir_usuario(dados)
        elif opcao == "3":
            print(f"\n\t3 - Atualizar Usuário")
            atualizar_usuario(dados)
        elif opcao == "4":
            print(f"\n\t4 - Informações de um usuário")
            informacoes_usuario(dados)
            time.sleep(1)  # Pausa por 20 segundos
        elif opcao == "5":
            print(f"\n\t5 - Informações de todos os usuários")
            listar_registros(dados)
            time.sleep(8)  # Pausa por 20 segundos
        elif opcao == "6":
            sair(dados)
            break
        else:
            print(f"\tOperação inválida, tente novamente. #")
            time.sleep(3)

dados = lerArquivo()
main(dados)