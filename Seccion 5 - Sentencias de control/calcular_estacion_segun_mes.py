month = int(input('Provide a month (1-12): '))
station = None

if month == 1 or month == 2 or  month == 12:
  station = 'Winter'
elif month >= 3 and month <= 5:
  station = 'Spring'
elif month >= 6 and month <= 8:
  station = 'Summer'
elif month >= 9 and month <= 11:
  station = 'Fall'
else:
  station = 'wrong month'

print(f'For month {month} station is: {station}')