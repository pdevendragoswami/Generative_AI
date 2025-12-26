from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
import time

start_time = time.time()
loader = DirectoryLoader(path="books",glob="*.pdf",loader_cls=PyPDFLoader)

docs = loader.load()

print(time.time()-start_time)

for document in docs:
    print(document.metadata)

