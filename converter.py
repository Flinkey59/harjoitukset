'''
Specify a currency (EUR, USD, GBP) and an amount to convert
The amount is a float
The return should be the converted amount with the appropriate symbol 
Example return: Your converted amount is EUR 4,000.35
'''

CURRENCIES = {'EUR', 'USD', 'GBP', 'JPY'}

RATIOS = {
    'EUR': {
      'USD': 1.07,
      'GBP': 0.87,
      'JPY': 160.85,
    },
    'USD': {
      'EUR': 0.93,
      'GBP': 0.81,
      'JPY': 150.39,
    },
    'GBP': {
      'EUR': 1.15,
      'USD': 1.23,
      'JPY': 184.88,
    },
    'JPY': {
      'EUR': 0.0062,
      'USD': 0.0066,
      'GBP': 0.0054,
    },
}

# CURRENCIES['EUR']['USD'] -> Euro to USD ratio

def convert_currency(start_currency: str, end_currency: str, amount: float) -> str:
  return 'Your original {} {:,.2f} has been converted to {} {:,.2f}'.format(start_currency, amount, end_currency, amount * RATIOS[start_currency][end_currency])

while True:
  start_currency = input('Provide the starting currency: ')

  if start_currency in CURRENCIES:
    break

  else:
    print('The input currency must be either EUR, USD, GBP or JPY.')

while True:
  try:
    amount = float(input('Provide the convertible amount as a number: '))

  except ValueError:
    print('You must input a number!')

  else:
    break

while True:
  end_currency = input('Provide the desired currency: ')

  if end_currency not in CURRENCIES or end_currency == start_currency:
    print('The input currency must be either EUR, USD, GBP or JPY and cannot be the same as\nthe starting currency.')

  else:
    break

print(convert_currency(start_currency, end_currency, amount))