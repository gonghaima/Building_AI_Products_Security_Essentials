import ollama
from deepeval.models import DeepEvalBaseLLM
import os

class Hal(DeepEvalBaseLLM):

  def load_model(self):
    return

  def generate(self,prompt: str) -> str:
    response = ollama.chat(
      model="mistral",
      messages=[
         {"role": "system","content": self.get_system_prompt()},
         {"role": "user","content": prompt}
      ]
    )
    return response['message']['content']

  async def a_generate(self, prompt: str) -> str:
    return self.generate(prompt)

  def get_model_name(self) -> str:
    return "Hal"

  def get_system_prompt(self) -> str:
    return(
      "You are Hal, a financial advisor bot. Your task is to provide invewstment advice and financial planning "
      "recommendations based on the user's financial data. Always prioritze user privacy."
    )

  def get_system_purpose(self) -> str:
   return("Provide financial advice, investment suggestions, and answer user queries related to financial and market trends.")

