# Example 8

# If we write a call to the open function that attempts to open a file for reading and that file doesn’t exist, the computer will raise a FileNotFoundError.



def main():
  try:
    with open("products.vcs", "rt") as products_file:
        for row in products_file:
            print(row)
  except FileNotFoundError as not_found_err:
    print(not_found_err)
if __name__ == "__main__":
  main()



# > python file_not_found.py
# [Errno 2] No such file or directory: 'products.vcs'