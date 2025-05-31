from langchain_ollama import OllamaLLM

def test_ollama():
    llm = OllamaLLM(model="tinyllama", base_url="http://host.docker.internal:11434")
    response = llm.invoke("This is a test connection!")
    print(response)

test_ollama()