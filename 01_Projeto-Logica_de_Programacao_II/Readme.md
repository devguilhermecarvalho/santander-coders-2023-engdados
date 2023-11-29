# Satander Coders 2023 - Engenharia de Dados

> Módulo 01 - Lógica de Programação II
> Aluno: Guilherme Carvalho - Turma: 1011
> **Projeto:**

## Resumo: Projeto de Sistema de Gerenciamento de Usuários

### **Tecnologias Utilizadas:**

* Linguagem de Programação: Python
* Armazenamento de Dados: Arquivo JSON
* Técnicas: Manipulação de arquivos JSON, interação por meio de console, tratamento de exceções.

---

### **Conceitos e Técnicas:**

> * Utilização de funções para modularizar o código.
> * Manipulação de arquivos JSON para armazenar e recuperar dados.
> * Utilização de estruturas de controle, como loops e condicionais.
> * Interatividade com o usuário por meio do console.
> * Tratamento de exceções para lidar com possíveis erros durante a execução.

---

### **Objetivos do Projeto:**

Desenvolver um sistema simples de gerenciamento de usuários que permite as seguintes operações:

**Inserir Usuário (Opção 1):**

* Coleta informações do usuário (Nome, Endereço, Telefone).
* Validação para garantir que as informações não estejam vazias.
* Atribuição de um ID único ao novo usuário.
* Armazenamento das informações em um arquivo JSON.

**Excluir Usuário (Opção 2):**

* Busca um usuário pelo ID.
* Permite desabilitar ou excluir completamente os dados do usuário.
* Atualiza o status do usuário para desabilitado ou remove completamente o registro.

**Atualizar Usuário (Opção 3):**

* Permite a atualização do Nome, Telefone e Endereço de um usuário existente.
* Possibilidade de atualizar múltiplos campos simultaneamente.
* Exibe as informações atualizadas e solicita confirmação.

**Informações de um Usuário (Opção 4):**

* Permite a busca de informações de um usuário pelo ID.
* Oferece sub-opções para busca por ID, Nome, Telefone ou Endereço.

**Informações de Todos os Usuários (Opção 5):**

* Lista todas as informações de usuários ativos presentes no arquivo JSON.
* Pausa de 8 segundos para fácil visualização.

**Sair (Opção 6):**

* Atualiza o arquivo JSON antes de encerrar o programa.
* Exibe uma mensagem de despedida.

### **Conclusão:**

O projeto visa oferecer um sistema básico de gerenciamento de usuários com funcionalidades de inserção, exclusão, atualização e consulta, proporcionando uma experiência interativa através do terminal.
