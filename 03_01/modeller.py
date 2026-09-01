import cherrypy, ollama, syslog


def check(type,content):
  # add guardrail check
  syslog.syslog("[AILog]["+type+"]"+content)
  return

class Modeller(object):
  @cherrypy.expose
  def index(self,prompt=""):
     check("prompt",prompt)
     response = ollama.chat(
       model="mistral",
       messages=[{ "role":"user","content":prompt}]
     )
     check("response",response['message']['content'])
     return response['message']['content']

cherrypy.config.update({'server.socket_host':'0.0.0.0','server.socket_port':5545})
cherrypy.quickstart(Modeller())

