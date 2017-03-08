import requests,re
import apiai
import json, requests
import pprint as pp

msg = "WHat is Cancer ?"
print ("Call Hua")
domain = "https://api.api.ai/v1/"
client_base = "65b21fedac084c16a9098ea44674270a"
ai = apiai.ApiAI(client_base)
request = ai.text_request()
request.session_id = "spitdisease"
request.query = msg
response = request.getresponse()
print json.dumps(response, indent=4)
