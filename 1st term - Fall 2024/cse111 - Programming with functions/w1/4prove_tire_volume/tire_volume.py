import math
from datetime import datetime



date_today = datetime.now()



tire_width = int(input('Enter the width of the tire in mm (ex 205): '))
tire_aspect_ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
wheel_diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

tire_volume = (math.pi * tire_width**2 * tire_aspect_ratio * (tire_width * tire_aspect_ratio + 2540 * wheel_diameter))/10000000000
tire_volume = round(tire_volume, 2)

print(f'The approximate volume is {tire_volume} liters')



wants_to_buy = input('Do you want to buy that tire? (yes/no): ')

if(wants_to_buy.upper() == 'YES'):
    customer_name = input('Enter your full name: ')
    phone_number = input('Enter your phone number: ')
    with open('volumes.txt', 'at') as volumes_file:
        print(' ', file=volumes_file) 
        print(f'Name: {customer_name}, Phone Number: {phone_number}', file=volumes_file)
        print(f'Date:{date_today:%Y-%m-%d}, Width:{tire_width}, Aspect Ratio:{tire_aspect_ratio}, Wheel diameter:{wheel_diameter}, Tire Volume:{tire_volume}', file=volumes_file)
else:
    print('Ok, have a nice day!')