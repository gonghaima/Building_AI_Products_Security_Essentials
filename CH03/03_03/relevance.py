from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase
import ollama

context=f"""
Our shoes are sourced from a sustainable and eco-friendly manufacturer, and
no slave labour is used in their production. We stand by the quality of our 
footware and offer all customers a 30-day refund at no cost if they do not
fit or are otherwise unsuitable. All footware comes with instructions on
the maintenance required to keep them in tip top condition even when worn
in the harshest conditions.
"""
answer_relevancy_metric=AnswerRelevancyMetric(threshold=0.7)

while True:
  prompt = input("\n\nEnter your prompt: ")
  if prompt=="/bye":
     break
  response = ollama.chat(
     model = "mistral",
     messages = [{'role':'system','content':'Refer to the following Context when responding. Context: '+context},
                 {'role':'user','content':prompt}],
     stream=False
  )
  actual = response['message']['content']

  try:
     test_case=LLMTestCase(
        input=prompt,
        actual_output=actual,
        retrieval_context=[context]
     ) 
     evaluate([test_case],[answer_relevancy_metric])
  except:
    print("Failed to complete – rerun")
    continue
