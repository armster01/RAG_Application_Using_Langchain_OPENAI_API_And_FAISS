from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

embeddings = OpenAIEmbeddings(openai_api_key = OPENAI_API_KEY)

vectorstore = FAISS.from_documents(text_chunks,embeddings)

retriever = vectorstore.as_retriever()

from langchain.prompts import ChatPromptTemplate

template = """You are an assistant for question-answering task.
              Use the following pieces of retrieved context to answer the question.
              If you don't know the answer, just say that you don't know.
              Use ten sentences maximum and keep the answer consice.
              Question: {question}
              Context: {context}
              Answer:"""

prompt = ChatPromptTemplate.from_template(template)
