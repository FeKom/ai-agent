from langchain_ollama import OllamaLLM

def test_ollama():
    llm = OllamaLLM(model="tinyllama", base_url="http://localhost:11434")
    response = llm.invoke("this is a test connection: ping")
    print(response)

test_ollama()