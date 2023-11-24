import random
import string

def generatePassword():
  caracteres = string.ascii_letters + string.digits
  senha = ''.join(random.choice(caracteres) for _ in range(8))
  return senha