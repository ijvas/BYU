# Example 3

# The computer raises a ValueError when the code that calls a function passes an argument with the correct data type but with an invalid value.




def main():
  try:
    number = float(input("Please enter a number: "))
    print(number)
  except ValueError as val_err:
    print(val_err)
if __name__ == "__main__":
  main()



#   > python value_error.py
# Please enter a number: 45.7u
# could not convert string to float: '45.7u'