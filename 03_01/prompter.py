import sys, requests

x = 0
with open(sys.argv[1],'r') as f:
  for prompt in f:
     response = requests.get('http://192.168.1.41:5545/?prompt='+prompt)
     x = x+1
print(str(x)+" prompts sent")
