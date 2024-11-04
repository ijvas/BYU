from datetime import datetime

today = datetime.now()
week_day = today.weekday()

subtotal = float(input('Please, enter the subtotal: '))

if(week_day != 1 and week_day != 2):
    print(f'today is another day')
else
    