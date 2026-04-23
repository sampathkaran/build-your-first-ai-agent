from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
import requests
import os
from datetime import datetime

# load the environmental variables
load_dotenv()

# initialize the model
llm_model = ChatGoogleGenerativeAI(model="gemini-3.1-pro-preview", temperature=0.2)

# Define the Github API tool call
@tool
def get_repo_list(params,):
    """Fetches and lists repositories for a given GitHub username"""
    personal_access_token = os.getenv('personal_access_token')
    headers = { 'Authorization': f"Bearer {personal_access_token}" }
    api_result = requests.get('https://api.github.com/users/sampathkaran/repos', headers=headers)
    
    # Check if the request was successful
    if api_result.status_code == 200:
        # Parse the JSON response
        return api_result.json()  # This will give you the github data as a dictionary
    else:
        # Handle failed request
        return {'error': 'Failed to retrieve github information'}


# now we define the internet search capability as a tool
search_tool = TavilySearch(max_results=3)

# Add the tools to a list
tools = [search_tool, get_repo_list]

current_date = datetime.now().strftime("%B %d, %Y")

# Build the system prompt
system_prompt = f"""You are an intelligent assistant:

**Current Date: {current_date}**

### Available Tools
1. **Web Search Tool ** (search_tool):
   - Searches the internet for current information
   - Use for current events, general knowledge, external information
   - ONLY use this tool if asked by the user or mentioned in the question

2. **Github API Server ** (get_repo_list):
   - Use this to interact with GitHub repositories
   - Prefer this tool when the task involves code, repositories, or implementation details
"""

#invoke the llm with tools
agent = create_agent(model="gpt-5-nano", tools=tools)

#invoke and test it
response = agent.invoke({"messages": [{"role": "human", "content": "Who won the formula1 race in japan 2026?"}]})
#response = agent.invoke({"messages": [{"role": "human", "content": "List all the github repositories of Sampathkaran?"}]})
#print(response)
print(response['messages'][-1].content)