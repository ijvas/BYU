import csv
from datetime import datetime
date_today = datetime.now()


def main():

    products_dict = read_dictionary('products.csv', 0)

    print('')
    print("Isma's Mart")

    try:
        with open('request.csv', 'rt') as request:
            reader = csv.reader(request)
            next(reader)

            subtotal = 0
            PRODUCT_NAME_INDEX = 1
            PRODUCT_PRICE_INDEX = 2
            num_of_items = 0

            for row in reader: 
                requested_item = row[0]
                requested_quantity = int(row[1])
                item = products_dict[requested_item]

                print(f'{item[PRODUCT_NAME_INDEX]}: {requested_quantity} ${item[PRODUCT_PRICE_INDEX]}')

                num_of_items = num_of_items + requested_quantity

                subtotal = subtotal + (requested_quantity * float(item[PRODUCT_PRICE_INDEX]))

                sales_tax = subtotal * 0.06

                total = subtotal + sales_tax

        print(f'Number of Items: {num_of_items}')
        print(f'Subtotal: ${subtotal:.2f}')
        print(f'Sales Tax : ${sales_tax:.2f}')
        print(f'Total: ${total:.2f}')
        print("Thank you for shopping at Isma's Mart!")
        print(f'{date_today:%a %b %d %I:%M:%S%p %Y}')

    except KeyError as key_error:
        print(type(key_error).__name__,key_error)
        print('One of the items is not in your inventory.')
    except FileNotFoundError as not_found_error:
        print(not_found_error)
        print("The file you entered doesn't exist..")
    except PermissionError as permission_error:
        print(permission_error)
        print("You don't have permission to acces to this file.")

    new_years_eve = datetime(2025,1,1)
    days_to_new_year = (new_years_eve - date_today).days
    print(f'{days_to_new_year} days until the New Years Sale begins')    
    print('')

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
      filename: the name of the CSV file to read.
      key_column_index: the index of the column
          to use as the keys in the dictionary.
    Return: a compound dictionary that contains
      the contents of the CSV file.
    """

    products = {}

    try:
        with open(filename, 'rt') as products_file:

            reader = csv.reader(products_file)

            next(reader)

            for row in reader:

                try:
                    if len(row) != 0:
                        key = row[key_column_index]
                        products[key] = row
                except KeyError as key_error:
                    print(key_error)

        return products

    except FileNotFoundError as not_found_error:
        print(not_found_error)
        print("The file you entered doesn't exist..")
    except PermissionError as permission_error:
        print(permission_error)
        print("You don't have permission to acces to this file.")
    
if __name__ == '__main__':
    main()