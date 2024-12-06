import csv

def main():
    
    provinces_list = read_file('provinces.txt')

    provinces_list.pop(0)
    provinces_list.pop()

    for i in range (len(provinces_list)):
        if provinces_list[i] == 'AB':
            provinces_list[i] = 'Alberta'

    counter = provinces_list.count('Alberta')

    print(provinces_list)
    print(f'Alberta appears {counter} times in the modified list.')


def read_file(file_name):

    with open(file_name, 'rt') as file:

        provinces = []

        for line in file:

            clean_line = line.strip()

            provinces.append(clean_line)
        
    return provinces

if __name__ == '__main__':
    main()