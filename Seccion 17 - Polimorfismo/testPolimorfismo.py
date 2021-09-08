from Empleado import Employee

def printMessage(object):
  print(object)
  print(type(object))

employee = Employee('Laureano', 100.000)
printMessage(employee)