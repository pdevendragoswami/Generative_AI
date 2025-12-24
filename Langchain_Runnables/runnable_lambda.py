from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

prompt = PromptTemplate(
    template="Write a joke about the {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

def word_counter(text):
    return len(text.split())


sequential_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    "joke":RunnablePassthrough(),
    "word_counter":RunnableLambda(word_counter)
})

final_chain = RunnableSequence(sequential_chain, parallel_chain)


result = final_chain.invoke({"topic":"AI"})

print(result)