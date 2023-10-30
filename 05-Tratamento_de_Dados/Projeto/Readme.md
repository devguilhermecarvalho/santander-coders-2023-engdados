# Análise e Transformação de Dados com Great Expectations e DBT

## Tecnologias Utilizadas

- **Linguagem:** Python e SQL
- **Banco de Dados:** PostgreSQL

## Bibliotecas Utilizadas

- **pandas**
- **sqlalchemy**
- **requests**
- **ipython-sql**
- **great_expectations**
- **psycopg2**
- **ydata_profiling**

## Instruções de Instalação

Para instalar todas as bibliotecas utilizadas, execute o seguinte comando:

```bash
pip install -r requirements.txt
```

### Fluxo de Trabalho

Este projeto envolve **ETL** - **(Extract, Transform, and Load)**, com foco na utilização das bibliotecas **Great Expectations** e **DBT**.

### Great Expectations

A biblioteca Great Expectations permite documentar e testar expectativas nos dados do DataFrame. Você pode definir regras, como restrições de integridade, valores esperados, distribuições e muito mais, para verificar a qualidade dos dados.

### DBT (Data Build Tool)

O DBT é uma ferramenta de transformação de dados que permite criar, documentar e testar transformações SQL nos dados do DataFrame. Com o DBT, você pode definir modelos de transformações em SQL para o banco de dados.

### Fluxo de Trabalho Integrado

Este fluxo de trabalho visa garantir a qualidade dos dados, documentar as expectativas e facilitar a manutenção das transformações de dados. É uma abordagem abrangente que utiliza tecnologias e bibliotecas poderosas para melhorar o processo de análise e transformação de dados.
