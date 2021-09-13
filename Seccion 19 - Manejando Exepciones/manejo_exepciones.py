result = None

x = 10
y = 0

try:
    result = x / y
except Exception as e:
    print(f'An error occurred: {e}')
# except ZeroDivisionError as e:
#     print(f'An error occurred: {e}')
print(f'Result: {result}')
print('Countinue...')