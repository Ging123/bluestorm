import jwt

class Jwt:
  
  def encode(self, payload, secret:str):
    token = jwt.encode(payload, secret, algorithm="HS256")
    return token

  
  def decode(self, token:str, secret:str):
    data = jwt.decode(token, secret, algorithm="HS256")
    return data