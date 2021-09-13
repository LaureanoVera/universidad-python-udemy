result = None

try:
    x = int(input('First Number: '))
    y = int(input('Second Number: '))
    result = x / y

except ZeroDivisionError as zde:
    print(f'An error occurred: {zde}')
except TypeError as te:
    print(f'An error occurred: {te}')
except Exception as e:
    print(f'An error occurred: {e}')


print(f'Result: {result}')
print('Countinue...')
