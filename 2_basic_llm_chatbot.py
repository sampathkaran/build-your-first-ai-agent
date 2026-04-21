from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load the environmental variables
load_dotenv()

# Initialize the model
llm_model = ChatOpenAI(model="gpt-5-nano", temperature=0.2)


# Create the chat loop
while True:
    user_input = input("You: ")
    if user_input.lower()== 'exit':
        print("bye")
        break
    else: 
        # invoke the model
        response = llm_model.invoke(user_input)
        # print the response
        print(f"🤖 AI Response: {response.content}\n")