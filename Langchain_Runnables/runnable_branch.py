from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnablePassthrough, RunnableBranch
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summarize the following text - {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>50, RunnableSequence(prompt2,model, parser)),
    RunnablePassthrough
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)


result = final_chain.invoke({"topic":"Runnable Branch"})

print(result)