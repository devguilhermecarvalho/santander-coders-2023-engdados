# Aula 04 - Extração de Dados
CSV, JSON e Parquet são tipos diferentes de formatos de arquivo que são utilizados para armazenar e representar dados de maneiras distintas. Cada um desses formatos tem suas próprias características e é adequado para diferentes cenários e necessidades de armazenamento e processamento de dados.

Resumidamente, a escolha entre CSV, JSON e Parquet depende do tipo de dados que você está manipulando, das necessidades de processamento e das ferramentas que você está utilizando. O CSV é simples e amplamente suportado, o JSON é flexível e legível por humanos, enquanto o Parquet é altamente eficiente para dados colunares em grande escala. Cada formato tem suas vantagens e desvantagens, e a escolha adequada deve ser feita com base nas características específicas do seu projeto.

- **Tipos da Arquivos**
    - **CSV (Comma-Separated Values - Valores Separados por Vírgula):**
      
    No formato CSV, os dados são armazenados em texto simples, onde cada linha representa uma entrada de dados e os campos são separados por vírgulas (ou outro delimitador, como ponto e vírgula).
    - **JSON (JavaScript Object Notation - Notação de Objetos JavaScript):**
      
     JSON é um formato de texto que armazena dados no formato de pares chave-valor. Os dados são estruturados em objetos e arrays.
     É usado para representar dados estruturados e complexos. Amplamente adotado em APIs REST para troca de dados entre servidores e clientes.
    - **Parquet:**
      
     O Parquet é um formato de armazenamento colunar binário. Ele armazena os dados de forma eficiente e compacta, organizando os valores das colunas em blocos.
     É especialmente adequado para armazenar e processar grandes volumes de dados, como em ambientes de Big Data e análise de dados.
     Oferece compressão eficiente e suporte à leitura paralela, tornando-o ideal para sistemas distribuídos, como o Hadoop.
     É usado em sistemas de armazenamento de dados em colunas, como o Apache Hive e o Apache Impala.
