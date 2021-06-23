# def add(a:int = 1, b:int = 1) -> int:
def add(a = 1, b = 1):
  return a + b

result = add()
print(result)
print(add(10,8))