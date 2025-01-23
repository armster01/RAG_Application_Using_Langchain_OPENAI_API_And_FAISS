from langchain.text_splitter import RecursiveCharacterTextSpliter

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)

text_chunks = text_splitter.split_documents(document)

print(text_chunks[0].page_content)
