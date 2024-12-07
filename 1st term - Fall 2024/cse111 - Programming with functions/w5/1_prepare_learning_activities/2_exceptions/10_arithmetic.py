# Example 10
"""
The owner of Sam's Sandwich Shop requested this program,
which computes the number of sandwiches per employee
that his employees made in his restaurant in one day.
"""
def main():
  try:
    # Get the number of sandwiches made today and the
    # number of employees who worked today from the user.
    sandwiches = int(input("Number of sandwiches made today: "))
    employees = int(input("Number of employees who worked today: "))
    # Compute the number of sandwiches per employee
    # that were made today in the restaurant.
    sands_per_emp = sandwiches / employees
    # Print the results for the user to see.
    print(f"{sands_per_emp:.1f} sandwiches per employee")
  except ValueError as val_err:
    print(f"Error: {val_err}")
    print("You entered text that is not an integer. Please")
    print("run the program again and enter an integer.")
  except ZeroDivisionError as zero_div_err:
    print(f"Error: {zero_div_err}")
    print("You entered 0 for the number of employees.")
    print("Please run the program again and enter an integer")
    print("larger than 0 for the number of employees.")
    # Call main to start this program.
if __name__ == "__main__":
  main()










# > python example_10.py
# Number of sandwiches that were made today: 35u
# Error: invalid literal for int() with base 10: '35u'
# You entered text that is not an integer. Please
# run the program again and enter an integer.
# > python example_10.py
# Number of sandwiches made today: 350.4
# Error: invalid literal for int() with base 10: '350.4'
# You entered text that is not an integer. Please
# run the program again and enter an integer.
# > python example_10.py
# Number of sandwiches that were made today: 350
# Number of employees who worked today: 0
# Error: division by zero
# You entered 0 for the number of employees.
# Please run the program again and enter an integer
# larger than 0 for the number of employees.
# > python example_10.py
# Number of sandwiches that were made today: 350
# Number of employees who worked today: 8
# 43.8 sandwiches per employee