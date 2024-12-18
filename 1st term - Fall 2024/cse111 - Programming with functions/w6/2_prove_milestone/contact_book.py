
def main():
    
    while True:
        choice = int( input('1.Add new Contact \n2.Search Contact \n3.Display Contacts \n4.Edit Contacts \n5.Delete Contact \n6.Exit \nEnter what you want to do: '))

        if choice == 1:
            name = input('Enter contact first name: ')
            lastname = input('Enter contact last name: ')
            birthdate = input('Enter contact birth date: ')
            phone_number = input('Enter contact phone number: ')
            email= input('Enter contact email: ')
            add_contact(name, lastname, birthdate, phone_number, email)
            print(f'{name} successfully added')
            print(' ')

        elif choice == 2:
            search_name = input('Enter contact first name: ')
            search_contact(search_name)

        elif choice == 3:
            if not contact_dict:
                print('The contact book is still empty.')
            else: 
                display_contact_list(contact_dict)

        elif choice == 4:
            contact_to_be_edited = input('Enter the contact first name you want to edit: ')
            edit_contact(contact_to_be_edited)


        # elif choice == 5:
        #     delete_contact(contact_dict)



        else:
            break


contact_dict = {}

def add_contact(name, lastname, birthdate, phone_number, email):
    contact_dict[name] = name, lastname, birthdate, phone_number, email
    return contact_dict[name]


def search_contact(search_name):
    if search_name in contact_dict:
        value = contact_dict[search_name]
        searched_contact_name = value[0]
        searched_contact_lastname = value[1]
        searched_contact_birthdate = value[2]
        searched_contact_phone_number = value[3]
        searched_contact_email = value[4]
        print(f'First name: {searched_contact_name}')
        print(f'Last name: {searched_contact_lastname}')
        print(f'Birth Date: {searched_contact_birthdate}')
        print(f'Phone Number: {searched_contact_phone_number}')
        print(f'Email: {searched_contact_email}')
        print(' ')
    else:
        print('The name you have entered is not in the contact list yet')
        print('')


def display_contact_list(contac_dict):
    for key in contact_dict:
        value = contac_dict[key]
        print('')
        print(f'Name: {key}, Last name: {value[1]}, Birthdate: {value[2]}, Phone number: {value[3]}, Email: {value[4]}')
        print('')




def edit_contact(contact_to_be_edited):

        

if __name__ == '__main__':
    main()    