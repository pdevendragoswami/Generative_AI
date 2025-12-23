from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")


template = PromptTemplate(
    template="Give me 5 funniest fact about {topic}",
    input_variables=["topic"]

)

parser = StrOutputParser()

chain = template | model | parser


result = chain.invoke({"topic":"cricket"})

print(result)

# visualize the chain 
chain.get_graph().print_ascii()