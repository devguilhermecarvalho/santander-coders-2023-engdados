# Aula 01 - Extração de Dados
Conceitos Praticos sobre ETL (Extract Transform Load), ELT (Extract Load Transform) e APIs Request.

## ETL e ELT
São acrônimos relacionados a processos de integração de dados que desempenham um papel fundamental na análise de dados e na tomada de decisões nas organizações. Ambos se concentram em mover, transformar e carregar dados de fontes diversas para um destino comum, como um armazém de dados, onde esses dados podem ser facilmente acessados e analisados.

- **ETL (Extract, Transform, Load):**

**Extração (Extract):** Nesta fase, os dados são coletados de várias fontes, que podem incluir bancos de dados, sistemas de arquivos, aplicativos web, planilhas e muito mais. A extração envolve a identificação e a recuperação dos dados necessários para a análise.

**Transformação (Transform):** Após a extração, os dados passam por um processo de transformação. Isso pode incluir a limpeza dos dados, a padronização de formatos, a agregação, a criação de campos calculados e a conversão de tipos de dados. O objetivo é preparar os dados para serem armazenados e analisados de forma eficaz.

**Carregamento (Load):** Nesta etapa final, os dados transformados são carregados em um repositório centralizado, como um data warehouse. Isso permite que os dados sejam facilmente acessados por ferramentas de análise, relatórios e consulta por parte dos usuários.

- **ELT (Extract, Load, Transform):**

**Extração (Extract):** Similar à etapa de extração do ETL, aqui os dados são coletados de várias fontes, como sistemas de origem, bancos de dados e aplicativos.

**Carregamento (Load):** A diferença principal entre ETL e ELT está na sequência das etapas. No ELT, os dados são carregados primeiro no armazém de dados sem uma transformação significativa. Os dados brutos são armazenados em seu formato original.

**Transformação (Transform):** A transformação dos dados ocorre após o carregamento no armazém de dados. Isso significa que a transformação ocorre no local de armazenamento, e as ferramentas de consulta e análise são usadas para transformar e preparar os dados conforme necessário.

A escolha entre ETL e ELT depende das necessidades específicas de uma organização e dos sistemas envolvidos. Alguns fatores a considerar incluem a complexidade dos dados, o volume de dados, a escalabilidade, os requisitos de desempenho e os recursos disponíveis. O ELT é muitas vezes preferido quando se lida com grandes volumes de dados ou quando a flexibilidade na manipulação dos dados é uma prioridade. O ETL tradicional é mais apropriado quando é necessário realizar transformações complexas antes do armazenamento dos dados.


### **APIs Requests**
A biblioteca "Requests" é uma biblioteca Python muito popular e amplamente usada para fazer solicitações HTTP a servidores web. Ela simplifica o processo de envio de solicitações e o tratamento das respostas.

APIs Requets são utilizadas para fazer solicitações a servidores web e receber respostas, geralmente em formato de dados, como JSON ou XML. Essas solicitações são usadas para buscar informações, enviar dados, interagir com serviços externos e muito mais.
