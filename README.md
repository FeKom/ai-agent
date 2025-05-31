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



1. Iniciar os containers
bash



`docker-compose up -d`

Isso inicia o serviço do Ollama na porta 11434.

2. Baixar uma imagem do modelo

Exemplo com TinyLlama:
bash


1
`ollama run tinyllama`
Se quiser usar outro modelo, execute `ollama run <nome-do-modelo>`.

Para entrar dentro do container do Ollama:
bash


1
`docker exec -it ollama bash`
E então rodar:

bash


1
ollama run <nome-do-modelo>

3. Instalar dependências Python

Se estiver usando ambiente virtual:

bash


1
2
uv venv
source .venv/bin/activate
Instale as dependências:

bash


1
uv sync
Ou, se preferir instalar diretamente:

bash


1
uv pip install -r requirements.txt

4. Executar o agente

bash


1
`python src/logs_review.py`

O script agent.py utiliza o LangChain para interagir com o modelo carregado no Ollama.

Exemplo de Uso
Adicionar um log no `src/logs/...` e rodar o agente para ler os logs e receber um review

bash


1
docker-compose down
Para remover todas as imagens e volumes não utilizados:

bash


1
docker system prune -a
Dependências Principais
langchain
uv
requests (opcional, para chamadas HTTP diretas à API do Ollama)
