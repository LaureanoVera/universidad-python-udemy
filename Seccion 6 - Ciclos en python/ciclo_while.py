condition = True
number = 0

while condition:
  number += 1
  print('Number: ', number)
  if number >= 10:
    condition = False
else:
  print('End of while loop')