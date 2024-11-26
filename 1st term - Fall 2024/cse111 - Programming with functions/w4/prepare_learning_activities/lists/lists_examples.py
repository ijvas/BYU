
def main():
    fabrics = []
    print('')
    print("We've created the fabrics list without elements.")
    print(f'{fabrics}')

    fabrics.append('velvet')
    fabrics.append('denim')
    fabrics.append('gingham')
    print('')
    print("We've added 3 elements to the fabrics list.")
    print(f'{fabrics}')

    
    fabrics.insert(0, 'chiffon')
    print('')
    print("We've inserted chiffon element in the 0 index of the list.")
    print(f'{fabrics}')


    print('')
    print('Is Gingham in the list?')
    if 'gingham' in fabrics:
        print('Gingham is in the list')
    else:
        print('Gingham is not in the list')


    print('')
    print('We putted taffeta instead of velvet')
    i = fabrics.index('velvet')
    fabrics[i] = 'taffeta'
    print(f'{fabrics}')



    # Remove the last element of the fabrics list:
    fabrics.pop()
    print('')
    print("We've removed the last element from the list.")
    print(f'{fabrics}')


    # Remove denim from the fabrics list:
    fabrics.remove('denim')
    print('')
    print("We've removed denim from the fabrics list.")


    n = len(fabrics)
    print('')
    print(fabrics)
    print(f'The fabrics list contains {n} elements.')



if __name__ == '__main__':
    main()