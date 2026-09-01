from langchain_google_genai import GoogleGenerativeAI,GoogleGenerativeAIEmbeddings 
from langchain.agents import AgentExecutor, initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain.tools import BaseTool, StructuredTool, tool
from langchain.agents.agent_types import AgentType
import subprocess, os

api_key=os.environ['GOOGLE_API_KEY']
llm = GoogleGenerativeAI(model="gemini-pro",google_api_key=api_key)

@tool
def generate_code(query: str)->str:
      "Generate code for a given problem"
      prompt = f"""
      Write a code snippet in Python for the given Problem. 
      OUTPUT JUST CODE SNIPPET AND NOTHING ELSE. 
      Always include the os and sys libraries. 
      Do not include the command 'rm' in your code snippet.
      """
      result = llm(prompt+" Problem:{}".format(query))
      if "```python" in result:
           result = result[10:-3]
      with open("temp.py", "w") as file:
           file.write(result)
      output = subprocess.run(['python', "./temp.py"], capture_output=True, text=True, timeout=10)
      return result if output.returncode == 0 else output.stderr

@tool
def test_code(query: str)->str:
    "Tests a given code and output results"
     print("Now testing code....")
    content = ''
    with open("./temp.py", 'r') as file:
        content = file.read()
    result = ("Write a code snippet to execute the given Code.  Codes:{}".format(content))
    if "```python" in result:
        result = result[10:-3]
    with open("temp-test.py", "w") as file_test:
            file_test.write(result)
    result = subprocess.run(['python',"./temp-test.py"], capture_output=True, text=True, timeout=10)
    return result.stdout if result.returncode == 0 else result.stderr

tools=[generate_code,test_code]
memory = ConversationBufferMemory(memory_key="chat_history")
agent_chain=initialize_agent(tools, llm, verbose=True, memory=memory)

while True:
   query = input("\nEnter programming task: ")
   if query=="/bye":
        break
    agent_chain.run({'input':query})
