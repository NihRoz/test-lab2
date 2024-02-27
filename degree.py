import os
from dotenv import load_dotenv
 
def power(a, n):
    """
    Возвращает значение a в степени n.
    """
    result = a ** n
    return result

 
if __name__ == '__main__':
  load_dotenv()
  try:
    n = int(os.getenv('n'))
    a = int(os.getenv('a'))
  except:
    n = 4
    a = 2
    
  result = power(a, n)
  print(f"{a} в степени {n} равно {result}")

  f = open("output/result.txt", "w")
  f.write(str(result))
  f.close()
