import cherrypy, ollama, syslog
from toxicTrig import toxicTrig

tt = toxicTrig()

def check(type,content):
  dall = tt.text_analysis([content],batch_size=1)
  hits = 0
  for dx in dall:
    hits=hits+dall[dx]
  if hits>0: 
    syslog.syslog("[AILog]["+str(hits)+"]["+type+"]"+content)
  return

class Modeller(object):
  @cherrypy.expose
  def index(self,prompt=""):
     print(50*'-',"\nPROMPT:",prompt,"\n",50*'-')
     check("prompt",prompt)
     response = ollama.chat(
       model="mistral",
       messages=[{ "role":"user","content":prompt}]
     )
     check("response",response['message']['content'])
     return response['message']['content']

cherrypy.config.update({'server.socket_host':'0.0.0.0','server.socket_port':5545})
cherrypy.quickstart(Modeller())

