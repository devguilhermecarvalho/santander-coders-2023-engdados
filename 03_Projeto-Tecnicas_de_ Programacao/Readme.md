# Satander Coders 2023 - Engenharia de Dados

> Módulo 03 - Técnicas de Programação
> Aluno: Guilherme Carvalho - Turma: 1011

---

## **Projeto: Processamento de Dados de Escolas**

### **Objetivo do Projeto:**

O projeto tem como objetivo processar dados relacionados a escolas, material didático e subprefeituras, buscando padronizar e organizar as informações para análises posteriores. O resultado final é um dataframe consolidado com informações sobre escolas, incluindo dados sobre material didático, e agrupados por subprefeitura.

### **Tecnologias Utilizadas:**

* Linguagem de Programação: **Python**
* Biblioteca para análise e tratamento de dados: **Pandas**
* Biblioteca para remover acentos e caracteres especiais: **Unidecode**
* Manipulação de strings e extração de informações: **Regex (Expressões Regulares)**

### **Técnicas e Conceitos Utilizados:**

1. **Leitura de Arquivos CSV:**
   * Utilização da biblioteca Pandas para ler arquivos CSV.
2. **Padronização de Textos:**
   * Remoção de acentos e padronização de maiúsculas para os campos de bairro, nome de escola, endereço, e subprefeitura.
3. **Renomeação de Colunas:**
   * Renomeação de colunas do dataframe.
4. **Substituição de Abreviações:**
   * Substituição de abreviações por seus equivalentes expandidos.
5. **Manipulação de Strings:**
   * Remoção de caracteres especiais, abreviações e substituição de padrões.
6. **Manipulação de Coordenadas Geográficas:**
   * Arredondamento das coordenadas de latitude e longitude.
7. **Agrupamento e Fusão de Dataframes:**
   * Fusão de dataframes relacionados a escolas, material didático e subprefeituras.
8. **Remoção de Dados Redundantes:**
   * Remoção de duplicatas com base em informações-chave.
9. **Agregação de Dados:**
   * Cálculo da quantidade total de material didático por subprefeitura.
10. **Exportação de Resultados:**
    * Salvamento do dataframe final em um arquivo CSV.
    * Salvamento dos dados agregados por subprefeitura em um arquivo CSV.

**Salvamento de Resultados:**

O dataframe final é salvo como 'dataframe_final.csv'.
Os dados agregados por subprefeitura são salvos como 'dados_por_prefeitura.csv'.

## **Conclusão:**

O projeto de processamento de dados de escolas demonstra uma abordagem sistemática e eficiente para a organização e padronização de informações. Ao utilizar bibliotecas como Pandas e Unidecode, juntamente com técnicas de manipulação de strings e expressões regulares, foi possível realizar a limpeza e estruturação dos dados de forma robusta.

A classe ProcessadorDeDados oferece funcionalidades para leitura de arquivos CSV, padronização de textos, renomeação de colunas, manipulação de coordenadas geográficas, fusão de dataframes e agregação de dados. A aplicação dessas técnicas resulta em um dataframe final que reflete a uniformização e consistência das informações.

Além disso, a exportação dos resultados para arquivos CSV permite a utilização fácil e rápida dos dados processados em análises subsequentes proporcionando um conjunto de dados organizado, padronizado e pronto para análises mais aprofundadas, contribuindo significativamente para a eficiência na manipulação e compreensão das informações relacionadas a escolas, material didático e subprefeituras.
