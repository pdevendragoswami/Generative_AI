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

final_template = template.invoke({"topic":"cricket"})
print(final_template)

result = model.invoke(final_template)

print(result)

parser = StrOutputParser()

final_output = parser.invoke(result)

print(final_output)
