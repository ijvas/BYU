import csv

def main():

    products_dict = read_dictionary('products.csv', 0)
    
    print('')
    print('All products: ')
    print(products_dict)
    print('')

    with open('request.csv', 'rt') as request:
        reader = csv.reader(request)
        next(reader)

        print('Requested Items: ')

        for row in reader:
            requested_items = row[0]
            requested_price = row[1]
            items = products_dict[requested_items]
            print(f'{items[1]}: {requested_price} @ {items[2]}')


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

    with open(filename, 'rt') as products_file:

        reader = csv.reader(products_file)

        next(reader)

        for row in reader:

            if len(row) != 0:
                key = row[key_column_index]
                products[key] = row
                
    return products
    
if __name__ == '__main__':
    main()