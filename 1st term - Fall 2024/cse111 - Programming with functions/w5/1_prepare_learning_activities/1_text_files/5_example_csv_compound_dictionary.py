# Example 5
import csv
def main():
    # Index of the phone number column
    # in the dentists.csv file.
    PHONE_INDEX = 2
    # Read the contents of the dentists.csv into a
    # compound dictionary named dentists_dict. Use
    # the phone numbers as the keys in the dictionary.
    dentists_dict = read_dictionary("dentists.csv", PHONE_INDEX)
    # Print the dentists compound dictionary.
    print(dentists_dict)
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
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}
    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:
        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)
        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)
        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:
            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:
                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]
                # Store the data from the current
                # row into the dictionary.
                dictionary[key] = row_list
    # Return the dictionary.
    return dictionary
# Call main to start this program.
if __name__ == "__main__":
    main()







# > python example_5.py
# {'208-359-2224': ['Eagle Rock Dental Care', '556 Trejo Suite C', '208-359-2224', 7, 1205],
# '208-359-1500': ['Apple Tree Dental', '33 Winn Drive Suite 2', '208-359-1500', 10, 1520],
# '208-356-5600': ['Rockhouse Dentistry', '106 E 1st N', '208-356-5600', 12, 1982],
# '208-356-4240': ['Cornerstone Family Dental', '44 S Center Street', '208-356-4240', 8, 1453]}