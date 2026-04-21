from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load the environmental variables
load_dotenv()

# Initialize the model
llm_model = ChatOpenAI(model="gpt-5-nano", temperature=0.2)

# Invoke the LLM
response = llm_model.invoke("Give me the map cooordinates of Singapore")

# print the response
print(f"🤖 AI Response: {response.content}")

