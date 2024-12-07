# Example 2

# The computer raises a TypeError when the code that calls a function passes an argument with the wrong data type. 



def main():
  try:
    text = input("Please enter a number: ")
    integer = round(text)
    print(integer)
  except TypeError as type_err:
    print(type_err)
if __name__ == "__main__":
  main()




#   > python type_error.py
# Please enter a number: 25.7
# type str doesn't define __round__ method