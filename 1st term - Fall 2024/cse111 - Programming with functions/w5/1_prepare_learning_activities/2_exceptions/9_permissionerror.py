# Example 9

# If we write a call to the open function that attempts to open a file and the person executing our program doesn’t have permission to access the file, the computer will raise a PermissionError.



def main():
  try:
    with open("contacts.csv", "rt") as contacts_file:
        for row in contacts_file:
            print(row)
  except PermissionError as perm_err:
    print(perm_err)
if __name__ == "__main__":
  main()


# > python permission_error.py
# [Errno 13] Permission denied: 'contacts.csv'