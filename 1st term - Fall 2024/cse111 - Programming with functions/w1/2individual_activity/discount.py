from datetime import datetime

today = datetime.now()
week_day = today.weekday()

price = 1
subtotal = 0

while (price != 0):
    price = int(input('Enter the price of the product: '))
    if(price != 0):
        quantity = int(input('How much products do you buy for that price: '))
        subtotal = price * quantity
        if( (subtotal >= 50) and (week_day == 1 or week_day == 2) ):
            discount_ten_percent = subtotal * 0.1
            subtotal_with_discount = subtotal - discount_ten_percent
            tax_six_percent = subtotal_with_discount * 0.06
            total = subtotal_with_discount + tax_six_percent
            print(f'Discount amount: {discount_ten_percent:.2f}')
            print(f'Sales tax amount: {tax_six_percent:.2f}')
            print(f'Total: {total:.2f}')    
        elif( (subtotal < 50) and (week_day == 1 or week_day == 2) ):
            amount_needed = 50 - subtotal
            print(f'The additional amount you need to purchase in order to receive the discount is {amount_needed:.2f}')
        else:
            tax_six_percent = subtotal * 0.06
            total = subtotal + tax_six_percent
            print(f'Sales tax amount: {tax_six_percent:.2f}')
            print(f'Total: {total:.2f}')    


    