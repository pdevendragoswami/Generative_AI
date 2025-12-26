from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

url = "https://www.flipkart.com/apple-iphone-17-pro-cosmic-orange-256-gb/p/itm76fe37ca9ea8c?pid=MOBHFN6YR8HF5BQ9&lid=LSTMOBHFN6YR8HF5BQ9RBYDOE&marketplace=FLIPKART&q=iphone+17&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_ps&fm=search-autosuggest&iid=85b24b43-4223-4234-afd9-6ee748c53dc2.MOBHFN6YR8HF5BQ9.SEARCH&ppt=sp&ppn=sp&ssid=jku5tl2ma80000001763189818538&qH=c9eeb2d6cc488f0b"
loader = WebBaseLoader(web_path=url)

docs = loader.load()

print(len(docs))
print(docs)

model = ChatGroq(model="llama-3.1-8b-instant")

prompt = PromptTemplate(
    template="Answer the following question \n {question} based on the text \n {text}",
    input_variables=["question","text"]
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"question":"Give me the details","text":docs[0].page_content})

print(result)