import requests
from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS

url = "https://raw.githubusercontent./langchain-ai/langchain/master/docs/docs/modules/state_of_the_union.txt"

response = requests.get(url)

response.text

rawdata = response.text

#To download in the local system
with open("state_of_the_union.txt","w") as f:
  f.write(rawdata)

loader = TextLoader('PATH of the COLAB')
document = loader.load()

print(document[0].page_content)
