def terms(name, *names, **terms):
  for key, value in terms.items():
    print(f'{key}: {value}')

terms(Name='Laureano', Age=18, Date='17/12/2002')
