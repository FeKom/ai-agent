# Agente de IA com Ollama + LangChain

## Este projeto implementa um agente de IA local utilizando as seguintes tecnologias:

- Ollama (em container Docker)
- Python 3.13
- uv como ferramenta de build
- LangChain para orquestração
- Modelo base: TinyLlama (configurável)
- Estrutura do Projeto


`   ia-agent/
    ├── src/
    │   └── logs_review.py           
    ├── docker-compose.yml        
    ├── pyproject.toml           
    ├── README.md                 
    └── .gitignore `
            
### Requisitos
Antes de executar o projeto, certifique-se de ter instalado:

***Docker***
***Docker Compose***
***Python 3.13 ou superior***
***uv (pip install uv ou via Rust/Cargo)***
***Como Rodar o Projeto***



Objetivo

O agente tem como finalidade ler os arquivos de log localizados no diretório:

`src/logs/`

A partir dos logs encontrados, o AI-Agent realiza uma análise detalhada e responde em linguagem natural o que está acontecendo na aplicação. Ele interpreta erros, identifica comportamentos suspeitos ou inesperados, e resume os eventos importantes, auxiliando no monitoramento e depuração do sistema.

⚙️ Tecnologia

Este projeto foi construído com o framework LangChain, que permite criar agentes inteligentes capazes de interagir com documentos, APIs e fluxos de dados de forma contextual e conversacional.

🚀 Como Executar

Para executar o projeto, é necessário ter o Docker e o Docker Compose instalados. Em seguida, rode o seguinte comando no terminal, a partir da raiz do projeto:

`docker-compose up --build`

Esse comando irá:

Construir a imagem do container, caso ainda não tenha sido construída;

Subir o container com o agente configurado;

Iniciar a análise dos arquivos de log presentes em src/logs/ automaticamente (dependendo da configuração do container).

 Estrutura do Projeto

.
├── docker-compose.yml
├── Dockerfile
├── src
│   └── model
│       └── chat.py
│   └── logs
│       └── election-management.log
│   └── test
│       └── chat_test.py
│   └── logs_review.py
└── README.md

src/logs/: Diretório onde os arquivos de log devem ser colocados.

`python /src/test/chat_test.py`: Script para testar a conexão com o ollama

`python /src/logs_review.py`: Script principal que contém a lógica de leitura e análise dos logs.


[!NOTE]
⚠️ Caso esteja utilizando uma imagem de modelo de IA local (como modelos LLM offline), o desempenho será significativamente melhor em sistemas com GPU instalada (NVIDIA, com drivers apropriados). Em ambientes com GPU, o tempo de resposta pode ser de 10 a 100 vezes mais rápido.

Em sistemas sem GPU, a IA será executada utilizando a CPU, o que pode resultar em tempos de execução muito mais lentos, especialmente ao processar grandes volumes de log ou modelos complexos.

Recomendado para ambientes Linux com GPU ou Windows com suporte à aceleração por hardware.
