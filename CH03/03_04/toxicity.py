from deepeval.metrics import ToxicityMetric
from deepeval.test_case import LLMTestCase
import ollama

tim = ToxicityMetric(threshold=0.5)

while True:
  prompt = input("\n\nEnter your prompt: ")
  if prompt=="/bye":
     break
  response = ollama.chat(
     model = "mistral",
     messages = [{'role':'user','content':prompt}],
     stream=False
  )
  actual = response['message']['content']
  print(actual)

  try:
     test_case=LLMTestCase(
       input=prompt,
       actual_output=actual,
     ) 
    tim.measure(test_case)
    print(tim.score)
    print(tim.reason)   
  except:
    print("Failed to complete – rerun")
    continue
