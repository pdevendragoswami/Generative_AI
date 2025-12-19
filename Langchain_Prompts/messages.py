from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

messsages = [
    SystemMessage(content = "You are a helpful assistant"),
    HumanMessage(content = "Tell me about Langchain")
]

result = model.invoke(messsages)

messsages.append(AIMessage(content=result.content))

print(messsages)