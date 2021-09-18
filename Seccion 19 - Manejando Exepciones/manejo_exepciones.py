from numeros_identicos_excepciones import NumerosIdenticosException

result = None

try:
    x = int(input('First Number: '))
    y = int(input('Second Number: '))
    if x == y:
        raise NumerosIdenticosException('Identicals Numbers')
    result = x / y
except ZeroDivisionError as zde:
    print(f'An error occurred: {zde}')
except TypeError as te:
    print(f'An error occurred: {te}')
except Exception as e:
    print(f'An error occurred: {e}')
else:
    print('No error ocurred')
finally:
    print('Ejecution finally block')

print(f'Result: {result}')
print('Countinue...')
