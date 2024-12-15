def main():
  # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]

    fruit_list.reverse()

    fruit_list.append('orange')

    i = fruit_list.index('apple')
    fruit_list.insert(i, 'cherry')

    fruit_list.remove('banana')

    element = fruit_list.pop()

    fruit_list.sort()

    fruit_list.clear()

    print({element})
    print(fruit_list)

if __name__ == '__main__':
    main()