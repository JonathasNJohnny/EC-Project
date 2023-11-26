import random
import string

def generatePassword():
  caracteres = string.ascii_letters + string.digits
  password = ''.join(random.choice(caracteres) for _ in range(8))
  return password