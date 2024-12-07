# Example 7

# As shown in example 7, if we write code that attempts to find a key in a dictionary and that key doesn’t exist in the dictionary, then the computer will raise a KeyError.



def main():
  try:
    # Create a dictionary with student IDs as
    # the keys and student names as the values.
    students = {
    "42-039-4736": "Clint Huish",
    "61-315-0160": "Amelia Davis",
    "10-450-1203": "Ana Soares",
    "75-421-2310": "Abdul Ali",
    "07-103-5621": "Amelia Davis"
    }
    # Attempt to find the key "50-420-1021",
    # which is not in the dictionary. This will
    # cause the computer to raise a KeyError.
    name = students["50-420-1021"]
    print(name)
  except KeyError as key_err:
    print(type(key_err).__name__, key_err)
if __name__ == "__main__":
  main()



#   > python key_error.py
# KeyError '50-420-1021'


































# it is common for a user to enter a key that is not in a dictionary. This is why the programs include an if statement above the line of code that searches the dictionary, like this:

# Get a student ID from the user.
id = input("Enter a student ID: ")
# Check if the student ID is in the dictionary.
if id in students:
  # Find the student ID in the dictionary and
  # retrieve the corresponding student name.
  name = students[id]
  # Print the student's name.
  print(name)
else:
  print("No such student")

