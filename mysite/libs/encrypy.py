import bcrypt

class Bcrypt:

  def hash_value(self, value, custom_salt:str):
    value = self._join_salt_with_value(value, custom_salt)
    rounds = 12
    salt = bcrypt.gensalt(rounds)

    _hash = bcrypt.hashpw(value, salt)
    return _hash.decode('utf-8')

  
  def match(self, value, _hash, custom_salt:str):
    value = self._join_salt_with_value(value, custom_salt)
    _hash = bytes(_hash, 'utf-8')

    match = bcrypt.checkpw(value, _hash)
    return match


  def _join_salt_with_value(self, value:str, salt:str) -> bytes: 
    value += salt
    value = value.encode()
    return value