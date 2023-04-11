import time # Allows for short delays between outputs to allow for a smoother CLI experience

class Number:
    '''
    A 4 digit number.
    '''
    def __init__(self, number_str: str):
        '''
        Initializes the class
        
        :param str number_str: a 4 digit number as a string
        '''

        self.digits = [int(number_str[0]), int(number_str[1]), int(number_str[2]), int(number_str[3])]
    

    def encrypt(self):
        '''
        Encrypts the classes' digits
        '''
        encrypted_digits = []
        
        # Encrypts all of the digits using the specified encrytion algorithm 
        for i in self.digits:
            encrypted_digits.append((i + 7) % 10)
        
        # Swaps the desired digits
        encrypted_digits = swap_digits(encrypted_digits)

        # Updates self.digits
        self.digits = encrypted_digits


    def decrypt(self):
        '''
        Decrypts the classes' digits
        '''
        
        # Swaps the digits of the encrypted number to where they are supposed to be
        self.digits = swap_digits(self.digits)
        decrypted_digits = []
        
        # Decrypts all of the digits using the specified encrytion algorithm 
        for i in self.digits:
            if i > 6:
                 decrypted_digits.append(i - 7)
            else:
                 # When the digit is above 6, 10 must be added before 7 is subtracted 
                 # to undo the modulous 10 done in encryption
                 decrypted_digits.append(i + 10 - 7)

        # Updates self.digits
        self.digits = decrypted_digits
    

    def combine(self) -> str:
        '''
        Combines all of the numbers digits together so it can be displayed.
        
        :return: The combined digits as a string
        '''
        string_digits = [str(i) for i in self.digits]
        combined = ''.join(string_digits)
        return combined


def swap_digits(digits: list) -> list:
    '''
    Swaps the digits of a 4 digit list.

    :param list digits: a list of 4 digits specifically from the Number class
    :return: a list of the swapped digits
    '''

    #Temporarily stores the first and second digits so the digits can be swapped around
    dig_1 = digits[0]
    dig_2 = digits[1]

    #Swaps 1st and 3rd digits
    digits[0] = digits[2]
    digits[2] = dig_1

    #Swaps 2nd and 4th digits
    digits[1] = digits[3]
    digits[3] = dig_2

    return digits


def is_valid(input_num: str) -> bool:
    '''
    Checks the validity of an incoming input number

    :param str input_num: The number that is being validated
    :return: Whether or not the number is valid (True or False)
    '''

    # Checks if the number is either not 4 characters or not a number
    if len(input_num) != 4:
        return False
    elif input_num.isnumeric() == False:
        return False
    else:
        return True


# Main loop
while True:

    # The main loop uses uses infinite loops to allow for the user to retry data entry in the case of invalid data
    # Otherwise the loops are broken out of using break statements
    while True:
        time.sleep(1)
        print("\nWelcome! What are you trying to do? (type the number of the option you want)\n")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. File")
        print("4. Exit")
        menu_choice = input("").replace(' ', '')
        
        if menu_choice in ['1', '2', '3', '4']:
            break
        else:
            print("\nSorry! That wasn't an option.")
    
    if menu_choice == '1':
        while True:
            print("\nInput the number you wish to encrypt below (must be exactly 4 digits)\n")
            number = input('')
            
            if is_valid(number):
                # Converts the number into a Number object
                number = Number(number)

                # Encrypts the number
                number.encrypt()
                encrypted_num_string = number.combine()
                
                # Reads all of the previously encrypted numbers from the file
                try:
                    with open("encrypted_nums.txt", "r") as f:
                        old_numbers = f.read()
                except:
                    with open("encrypted_nums.txt", "w") as f:
                        f.write('')
                        old_numbers = ''

                # Writes the new encrypted number + the old numbers to the file so that the new number is on top    
                with open("encrypted_nums.txt", "w") as f:
                    if old_numbers == '':
                        f.write(encrypted_num_string)
                    else:
                        f.write(encrypted_num_string+'\n'+ old_numbers)
                
                print(f"\nNumber sucessfully encrypted as {encrypted_num_string} and saved to file\n")
                break

            else:
                print("\nSorry! That is an invalid number.")

    elif menu_choice == "2":
        while True:
            print("\nInput the number you wish to decrypt below (must be exactly 4 digits)\n")
            number = input('')
            
            if is_valid(number):
                # Converts the number into a Number object
                number = Number(number)

                # Decrypts the number
                number.decrypt()
                decrypted_num_string = number.combine()

                print(f"\nThe Decrypted Number is {decrypted_num_string}")
                break

            else:
                print("\nSorry! That is an invalid number.")
            
    elif menu_choice == '3':
        while True:
            while True:
                time.sleep(1)
                print("\nWhat would you like to do?\n")
                print("1. Show file")
                print("2. Show file (decrypted)")
                print("3. Exit")
                menu_choice = input("").replace(' ', '')

                if menu_choice in ['1', '2', '3']:
                    break
                else:
                    print("\nSorry! That wasn't an option.")
            
            if menu_choice == '1':
                print() # Blank line

                # Simply reads and displays the file
                with open("encrypted_nums.txt", 'r') as f:
                    print(f.read())

            elif menu_choice == '2':
                print() # Blank line

                # Goes through every line in the file, decrypts it, then displays it.
                with open("encrypted_nums.txt", 'r') as f:
                    for i in f.readlines():
                        # Converts the number into a Number object
                        num = Number(i.replace('\n', ''))
                        num.decrypt()

                        print(num.combine())

            else:
                break

    elif menu_choice == '4':
        break
