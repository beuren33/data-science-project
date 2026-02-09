## Data Project

### ML Pipeline - Workflow

1. Ingestão de Dados
2. Avaliação dos dados (EDA)
3. Transformação dos Dados
4. Treinamento do Modelo
5. Avaliação do Modelo

# Workflow
1. Atualizar config.yaml
2. Atualizar schema.yaml
3. Atualizar params.yaml
4. Atualizar entity
5. Atualizar o gerenciador de configuração na configuração de origem.
6. Atualizar components
7. Atualizar pipeline
8. Atualizar main.py

# Projeto de Data Science: Previsão da Qualidade do Vinho

## Introdução

Este projeto demonstra a construção de um pipeline de Machine Learning de ponta a ponta, desde a ingestão de dados até a predição, com foco em práticas de MLOps que garantem reprodutibilidade, manutenibilidade e escalabilidade. O objetivo central é prever a qualidade de vinhos com base em suas características físico-químicas, utilizando um workflow que evoluiu de uma análise exploratória inicial para uma arquitetura de software modular e robusta.

## A Evolução Arquitetural: De Notebooks a Código Modular

A jornada deste projeto iniciou-se, como é comum em muitos projetos de Data Science, com a utilização de Jupyter Notebooks. Os notebooks no diretório `research/` foram fundamentais para a fase de exploração, permitindo uma interação ágil com os dados, a realização de análises exploratórias (EDA) e a prototipação inicial de cada etapa do pipeline: ingestão, validação, transformação, treinamento e avaliação do modelo.

Entretanto, a transição de um ambiente de pesquisa para um sistema de produção exige uma abordagem mais estruturada. A utilização exclusiva de notebooks em um contexto de produção apresenta desafios significativos, como:

- **Dificuldade de Reutilização:** O código em notebooks tende a ser linear e menos componentizado, dificultando o reaproveitamento de funções e lógicas em diferentes partes do sistema ou em outros projetos.
- **Complexidade na Manutenção:** À medida que o projeto cresce, a gestão de um ou vários notebooks monolíticos torna-se complexa, propensa a erros e difícil de depurar.
- **Falta de Reprodutibilidade:** Garantir que um notebook execute da mesma forma em diferentes ambientes ou momentos pode ser um desafio, especialmente no que tange ao gerenciamento de dependências e estado.

Diante desses desafios, o projeto adotou uma arquitetura de programação modular. A lógica de cada etapa, antes contida em um notebook, foi refatorada e encapsulada em componentes Python independentes, localizados no diretório `src/DataScienceProject/components`. Essa transição representa um passo crucial em direção a um sistema mais maduro e alinhado com as melhores práticas de engenharia de software e MLOps.

## Princípios Fundamentais da Arquitetura

A arquitetura atual do projeto é fundamentada em princípios que visam a clareza, a flexibilidade e a eficiência operacional.

### Pipeline Orientado por Configuração

O comportamento de todo o pipeline é controlado por arquivos de configuração em formato YAML, o que permite uma modificação rápida e segura do fluxo de trabalho sem a necessidade de alterar o código-fonte. Os principais arquivos são:

- **`config.yaml`**: Define os caminhos para os artefatos gerados, a URL da fonte de dados e a estrutura dos diretórios para cada etapa do pipeline.
- **`params.yaml`**: Armazena os hiperparâmetros do modelo (neste caso, `alpha` e `l1_ratio` para o `ElasticNet`), permitindo a fácil experimentação e ajuste fino.
- **`schema.yaml`**: Descreve o esquema dos dados de entrada, incluindo os tipos de dados de cada coluna e a identificação da coluna alvo (`TARGET_COLUMN`).

### Componentes Modulares

Cada etapa do pipeline de Machine Learning é implementada como um componente distinto no diretório `src/DataScienceProject/components`. Essa separação de responsabilidades (ingestão, validação, transformação, etc.) torna o código mais limpo, fácil de testar e manter. Cada componente é uma classe que executa uma tarefa específica, recebendo sua configuração de um objeto `ConfigurationManager`.

### Pipelines Estruturados

O diretório `src/DataScienceProject/pipeline` contém os scripts que orquestram a execução dos componentes. O arquivo `main.py` atua como o ponto de entrada principal, invocando cada pipeline de estágio em sequência. Essa abordagem garante que as etapas sejam executadas na ordem correta e facilita o rastreamento do progresso e a identificação de falhas.

### Configuração Baseada em Entidades

Para garantir a consistência e a segurança de tipos, o projeto utiliza `dataclasses` (em `src/DataScienceProject/entity/entity_config.py`) para representar as configurações de cada componente. O `ConfigurationManager` é responsável por ler os arquivos YAML e popular essas `dataclasses`, fornecendo uma interface de acesso aos parâmetros de configuração que é robusta e à prova de erros de digitação.

## Flexibilidade e Extensibilidade

A principal vantagem da arquitetura adotada é a sua flexibilidade. A modularidade e a centralização das configurações permitem que o pipeline seja adaptado para diferentes cenários com o mínimo de esforço. Por exemplo, para utilizar uma nova fonte de dados, basta seguir estes passos:

1.  **Atualizar `config.yaml`**: Modificar a chave `source_url` na seção `data_ingestion` para apontar para o novo dataset.
2.  **Ajustar `schema.yaml`**: Revisar o esquema de colunas e a coluna alvo para que correspondam à nova fonte de dados.

Com essas simples modificações, todo o pipeline de ingestão, validação, treinamento e avaliação é capaz de operar sobre o novo conjunto de dados, sem que uma única linha de código da lógica principal precise ser alterada. Essa capacidade de adaptação é um diferencial fundamental para a rápida iteração e a aplicação do modelo a diferentes problemas de negócio.

## Como Utilizar o Projeto

Para executar o pipeline completo, siga os passos abaixo:

1.  **Clone o repositório:**
    git clone https://github.com/beuren33/data-science-project.git
    cd data-science-project
    ```

2.  **Instale as dependências:**
    pip install -r requirements.txt
    ```

3.  **Execute o pipeline de treinamento:**
    python main.py
    ```

4.  **Inicie a aplicação web para predições:**
    python app.py
    ```
    Acesse `http://localhost:8080` em seu navegador para interagir com o modelo.

## Próximos Passos e Melhorias

A estrutura atual do projeto serve como uma base sólida para futuras expansões e melhorias, especialmente no que tange à automação e orquestração de pipelines.

### Implementando um Pipeline ETL Automatizado com Apache Airflow

O Apache Airflow é uma ferramenta padrão da indústria para orquestrar workflows complexos. Integrar este projeto com o Airflow seria um passo natural para automatizar a execução do pipeline de ponta a ponta. Aqui estão algumas ideias para essa implementação:

- **Fonte de Dados via API:** Em vez de um arquivo estático, o pipeline poderia ser alimentado por uma API. Por exemplo, poderíamos consumir dados de uma API de e-commerce que fornece avaliações de vinhos em tempo real ou de uma base de dados de um fornecedor.

- **Estrutura da DAG no Airflow:** Uma DAG (Directed Acyclic Graph) no Airflow poderia ser estruturada da seguinte forma:

  1.  **`Extract` (Extração):** Um `PythonOperator` que invoca a lógica de `data_ingestion`, mas modificada para consumir dados de uma API. Este operador faria a chamada à API, receberia os dados (provavelmente em formato JSON) e os salvaria em uma área de *staging* (por exemplo, um bucket S3 ou um diretório local).

  2.  **`Transform` (Transformação):** Outro `PythonOperator` que executa a lógica de `data_validation` e `data_transformation`. Ele leria os dados brutos da área de *staging*, aplicaria as validações de esquema, realizaria as transformações necessárias (como normalização ou codificação de variáveis) e salvaria os dados processados em um novo local.

  3.  **`Load` (Carregamento e Treinamento):** Um terceiro `PythonOperator` que aciona o `data_train_pipeline`. Ele carregaria os dados transformados e executaria o treinamento do modelo, versionando o modelo resultante (por exemplo, com MLflow, que já está parcialmente integrado) e salvando as métricas de avaliação.

- **Flexibilidade com Airflow:** A beleza do Airflow é que cada uma dessas tarefas pode ser um script Python que chama os componentes modulares que você já construiu. A DAG apenas orquestraria a execução desses componentes na ordem correta, gerenciando dependências, tentativas e logs de forma automática.

### Integração com GitHub Actions para CI/CD

O GitHub Actions pode ser utilizado para criar um pipeline de Integração Contínua (CI) e Entrega Contínua (CD) robusto, garantindo a qualidade e a automação do deploy.

- **Workflow de CI:** Um workflow de CI poderia ser acionado a cada `push` ou `pull request` para o repositório. As etapas incluiriam:

  1.  **Linting e Formatação:** Executar ferramentas como `flake8` ou `black` para garantir a consistência do estilo do código.
  2.  **Testes Unitários:** Rodar testes unitários para cada componente modular, garantindo que cada peça do quebra-cabeça funcione como esperado de forma isolada.
  3.  **Teste de Integração:** Executar o `main.py` com um pequeno subconjunto de dados para garantir que o pipeline completo execute sem erros.

- **Workflow de CD:** Após a aprovação de um `pull request` na branch principal, um workflow de CD poderia ser acionado para:

  1.  **Treinamento do Modelo:** Executar o pipeline completo de treinamento com os dados mais recentes.
  2.  **Versionamento do Modelo:** Registrar o novo modelo e suas métricas em uma ferramenta como o MLflow.
  3.  **Deploy da Aplicação:** Construir uma imagem Docker da aplicação Flask e fazer o deploy em um ambiente de produção (como um serviço de contêiner na nuvem), disponibilizando a nova versão do modelo para os usuários finais.

Ao combinar a arquitetura modular existente com a orquestração do Airflow e a automação do GitHub Actions, este projeto pode evoluir para um sistema de MLOps completo, robusto e altamente automatizado.
