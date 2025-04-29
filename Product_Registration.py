count = 0
total = 0
most_expensive_price = 0
most_expensive_name = ''
over_thousand = 0

while True:
    product = str(input('Enter the product name: ')).strip()
    price = float(input('Enter the price: R$'))

    while price < 0:
        price = float(input('ERROR! Enter a valid product price: R$'))

    if price > 1000:
        over_thousand += 1

    count += 1
    total += price

    if price > most_expensive_price:
        most_expensive_price = price
        most_expensive_name = product

    continue_choice = str(input('Do you want to continue? [Y/N] ')).strip()
    while continue_choice not in 'NnYy':
        continue_choice = str(input('ERROR! Do you want to continue? [Y/N] ')).strip()
    if continue_choice in 'Nn':
        break

print(f'Total products registered: {count}')
print(f'The most expensive product was {most_expensive_name}, costing R${most_expensive_price:.2f}')
print(f'{over_thousand} products cost more than R$1000.00')
print(f'Total purchase amount: R${total:.2f}')
if total > 5000:
    print('PURCHASE ABOVE AVERAGE!')
    print(f'Your purchase cost R${total:.2f}, which is above the general average (R$5000)!')
print('!!THANK YOU FOR YOUR PREFERENCE!!')