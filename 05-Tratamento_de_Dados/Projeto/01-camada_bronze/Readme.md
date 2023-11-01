# Extração dos dados

Os dados foram extraídos do site http://insideairbnb.com/rio-de-janeiro em formato .csv

* **Listings data**

  * Download link:
  * http://data.insideairbnb.com/brazil/rj/rio-de-janeiro/2023-09-22/data/listings.csv.gz
  * Tamanho: 19,3 MB
* **Detailed Calendar Data**

  * Download link:
  * http://data.insideairbnb.com/brazil/rj/rio-de-janeiro/2023-09-22/data/calendar.csv.gz
  * Tamanho: 31,1 MB
* **Detailed Review Data**

  * Download link:
  * http://data.insideairbnb.com/brazil/rj/rio-de-janeiro/2023-09-22/data/reviews.csv.gz
  * Tamanho: 69,9 MB

## Conversão dos arquivos CSV para Parquet

**Desempenho CSV, compressão Gzip:**

* `listings.csv` - Tamanho: 19.3 mb
* `calendar.csv` - Tamanho: 31.1 mb
* `reviews.csv` - Tamanho: 69.1 mb

**Desempenho Parquet, compressão Brotli:**

* `listings.parquet` - Tamanho: 1.1 mb
  * **Diminuição percentual de: 94.3 %**
* `calendar.parquet` - Tamanho: 3.5 mb
  * **Diminuição percentual de: 88.8 %**
* `reviews.parquet` - Tamanho: 1.3 mb
  * **Diminuição percentual de: 98.1 %**

## Criação e prévia analise do Dataframe

A partir dos dados obtidos, o Pandas foi empregado para criar um dataframe e conduzir uma análise preliminar dos dados. Para essa análise exploratória, utilizamos a biblioteca "ydata_profiling", que gera relatórios detalhados em formato HTML por meio do "ProfileReport". Adicionalmente, o dataframe foi inserido em um banco de dados Postgre sem qualquer alteração, preparando-o para a próxima camada (Silver).