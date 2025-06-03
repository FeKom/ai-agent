from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM





def chat_cfg():
    return OllamaLLM(
        model= "tinyllama",
        base_url= "http://localhost:11434",
        #Usa 4 threads da CPU
        num_thread= 4,
        #Mantem conteudo na RAM por 5 minutos
        keep_alive= "5m",
        #Carregado a cada 2-3 minutos o AI agente
        #keep_alive- "3m"
    )
    
        

