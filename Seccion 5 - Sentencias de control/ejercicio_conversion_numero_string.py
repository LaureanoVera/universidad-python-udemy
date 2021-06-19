number = int(input('Number (1-3): '))
text_number = ''

if number == 1:
  text_number = 'Number One'
elif number == 2:
  text_number = 'Number Two'
elif number == 3:
  text_number = 'Number Three'
else:
  text_number = 'Sorry...'

print(f'{number} is {text_number}')