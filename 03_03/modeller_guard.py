import cherrypy, ollama, syslog
from llm_guard import scan_output, scan_prompt
from llm_guard.input_scanners import Anonymize, PromptInjection, TokenLimit, Toxicity
from llm_guard.output_scanners import Deanonymize, NoRefusal, Relevance, Sensitive
from llm_guard.vault import Vault

vault = Vault()
input_scanners = [Anonymize(vault), Toxicity(), TokenLimit(), PromptInjection()]
output_scanners = [Deanonymize(vault), NoRefusal(), Relevance(), Sensitive()]
prompt_in = ""

def check(type,content):
  if type=="prompt":
    processed, results_valid, dictout = scan_prompt(input_scanners, content)
  else:
    processed, results_valid, dictout = scan_prompt(output_scanners, prompt_in, content)

  hits = 0
  for dx in dictout:
    hits = hits+dictout[dx]
  if hits>0:
    syslog.syslog("[AILog]["+type+"]"+content)
  return processed

class Modeller(object):
  @cherrypy.expose
  def index(self,prompt=""):
     prompt_in = check("prompt",prompt)
     response = ollama.chat(
       model="mistral",
       messages=[{ "role":"user","content":prompt_in}]
     )
     check("response",response['message']['content'])
     return response['message']['content']

cherrypy.config.update({'server.socket_host':'0.0.0.0','server.socket_port':5545})
cherrypy.quickstart(Modeller())



