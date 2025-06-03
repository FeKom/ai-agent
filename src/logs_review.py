import httpx
from langchain_community.document_loaders import TextLoader
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from model.chat import chat_cfg



loader = TextLoader('src/logs/election-management.log')
documents = loader.load()

def main():
    try:
        model = chat_cfg()

        base_prompt = PromptTemplate(
            input_variables=['logs', 'context'],
            template=''''
                You are an AI assistant specialized in analyzing logs for a company, analyze the logs and tell whats
                happend, based on the context: 
                {logs} 
                context: {context}
            '''

        )

        chain = base_prompt | model | StrOutputParser()

        response = chain.invoke(
            {
                'logs': '\n'.join([doc.page_content for doc in documents])[:4000],
                'context':  "This is a log from an application, where I'm using quarkus, with the quarkus dev command to run and it's giving this error"
            }
        )

        print(response)

    except httpx.ConnectError as e:
        print(f"Connection Error: Could not connect to the model server.")
        print(f"Error Details: {str(e)}")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")

main()