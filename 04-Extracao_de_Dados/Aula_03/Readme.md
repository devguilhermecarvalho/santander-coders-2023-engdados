# Aula 03 - Extração de Dados
Query Params, Path Params e Paginação em APis.
Esses conceitos são fundamentais ao projetar e usar APIs.

- **Query Params (Parâmetros de Consulta):**

O que são: Query params são parâmetros opcionais que podem ser incluídos em uma URL para personalizar uma solicitação de consulta a uma API. Eles geralmente são usados para filtrar, ordenar ou paginar os resultados de uma consulta.

Utilizamos para filtrar os recursos de uma API com base nos atributos de retorno.
    Iniciado pelo aractere "?"
    Expressões unidas pelo carectere "&"

Exemplo:
    ?start_date=2023-03-12&pages=1&size=10

Neste exemplo filtramos o campo start_date("Que fora inicialmente definido pelos desenvolvedores da API") bem como adicionamos parêmetros de Paginação


- **Path Params (Parâmetros de Caminho):**

O que são: Path params são parâmetros que fazem parte da própria URL e são usados para identificar recursos específicos em uma API. Eles são usados em URLs de maneira a representar a estrutura de rota da API.

Exemplo: Suponha que você esteja construindo uma API para consultar informações de usuários por meio de seus IDs. Você pode definir um caminho que inclua um parâmetro de caminho para o ID do usuário.


- **Paginação**
Utilizado para quando precisamos reduzir o número de dados retornados por uma consulta
    Pode ser por limitação da própria API quanto da minha ferramenta de consumo.
    Geralmente podemos definir número de paginas, seus respectivos tamanhos e qual página buscamos.

Paginação é um conceito usado em APIs para lidar com grandes conjuntos de dados. Em vez de retornar todos os resultados de uma vez, a API retorna um subconjunto de resultados (uma página) de cada vez.

Exemplo:
    http:api-host.com/v1/api/products?skip=0&size=10

Onde dizemos por skip que desejamos pular x elementos considerando o começo do retrno full e size determinando quantos recursos desejamos retornar, a automatização desse processo depende da implementação da API, onde algumas podem fornecer o número total de recursos, o número de páginas e etc.