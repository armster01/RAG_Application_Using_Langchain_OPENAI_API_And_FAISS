from langchain.chat_models import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

llm_model = ChatOpenAI(openai_api_key = OPENAI_API_KEY, model_name = "gpt-3.5-turbo")

output_parser = StrOutputParser()

rag_chain = (
  {"context": retriever, "question": RunnablePassThrough()}
  | prompt
  | llm_model
  | output_parser
)

rag_chain.invoke ("How is the US supporting Ukraine economically and militarily? ")
