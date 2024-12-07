# Example 5
#  If we write code that tries to use an index that doesn’t exist in a list, when the computer executes that code, the computer will raise an IndexError. 

def main():
  try:
    # Create a list that contains three family names.
    surnames = ["Smith", "Lopez", "Marsh"]
    # Attempt to change the surname at index 3. Because
    # there are only three names in the surnames list and
    # therefore the last index is 2, this statement will
    # fail and cause the computer to raise an IndexError.
    surnames[3] = "Olsen"
  except IndexError as index_err:
    print(index_err)
if __name__ == "__main__":
    main()



# > python index_error_write.py
# list assignment index out of range