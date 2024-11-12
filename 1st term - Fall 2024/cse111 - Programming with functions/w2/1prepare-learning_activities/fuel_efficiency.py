def main():
    start = float(input('Enter the first odometer reading (miles): '))
    end = float(input('Enter the second odometer reading (miles): '))
    used_fuel = float(input('Enter the amount of fuel used (gallons): '))
    
    miles_p_gallon = miles_per_gallon(start, end, used_fuel)
    print(f'{miles_p_gallon:.1f} miles per gallon')

    ltrs_per_100km = lp100k_from_mpg(miles_p_gallon)
    print(f'{ltrs_per_100km:.2f} per 100 kilometres')
    

def miles_per_gallon(starting_miles, ending_miles, gallons_used):
    mpg = (ending_miles - starting_miles) / gallons_used
    return mpg

def lp100k_from_mpg(mpg):
    lp100k = 235.215 / mpg
    return lp100k

main()
