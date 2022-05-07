import json

def error_response(message:str, field:str):
  error = {field:[{'message':message}]}
  error = json.dumps(error)
  return error