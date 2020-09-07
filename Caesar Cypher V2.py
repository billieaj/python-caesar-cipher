'''''''''''''''''''''''''''''''''''
Caesar Cypher Version 2
Billie Johnson
This code is used to encrypt or decrypt text files that the user inputs (using the Caesar/Shift Cypher method) and can either save the encrypted text to another file, or print it.

'''''''''''''''''''''''''''''''''''

maxkeynum = 127 #maximum number for the encryption key (how many places you can move the characters)

def encrypt(text): #creates a function for the encryption of a file
    characters = []
    for char in text: #creates a loop for all the characters in the text file
        value = ord(char) #changes the character to an ordinal
        value += (key) #changes the ordinal (value) by the integer that was entered as key to encrypt
        if (value + key) >= 127: #if the value is changed to a number over 127, then it carries over back from 1. This is so that the characters stay within the ASCII character range.
            encr = (chr((value + key) - 127)) #changes the ordinal (value) back to a character and sets as encr          
        else:
            encr = chr(value) #changes the ordinal (value) back to a character and sets as encr
        characters.append(encr)
        encrypted_text = (''.join(characters)) #joins all the characters
    return encrypted_text #returns variable

'''''''''''''''''''''''''''''''''''
The above function is what encrypts the contents of the file that the user inputs, by shifting the characters.

'''''''''''''''''''''''''''''''''''

def decrypt(text): #creates a function for the decryption of a file
    characters = []
    for char in text: #creates a loop for all the characters in the text file
        value = ord(char) #changes the character to an ordinal
        value -= (key) #changes the ordinal (value) back by the integer that was entered as key to decrypt
        if (value - key) <= 0: #if the value is changed to a number under 0, then it carries over back from 127. This is so that the characters stay within the ASCII character range.
            encr = (chr((value - key) + 127)) #changes the ordinal (value) back to a character and sets as encr
        else:
            encr = chr(value) #changes the ordinal (value) back to a character and sets as encr
        characters.append(encr)
        encrypted_text = (''.join(characters)) #joins all the characters
    return encrypted_text #returns variable

'''''''''''''''''''''''''''''''''''
The above function is what decrypts the contents of the file that the user inputs, by shifting the characters the opposite way to which the encrypt function shifts them.

'''''''''''''''''''''''''''''''''''

while True: #makes program keep looping until the user decides to quit
    try:
        choice = input("Would you like to encrypt (enter e) or decrypt (enter d)? ") #asks user if they want to encrypt or decrypt and stores their choice
        if choice == "e": 
            key = int(input("Please input the encryption key (the number of places you want to shift letters) ")) #asks user to input an encryption key (integer) and stores the key
            if key <= maxkeynum: #makes sure that the key is not greater than the max number for the key
                file = input("Please enter the name of the file you want to encrypt ") #asks user to input filename and stores
                with open("{}".format(file), 'r') as f: #opens file and makes sure that nothing can be done without the file open
                    text = f.read()
                    returned_text = encrypt(text) #runs encrypt function
                    save_print = input("Would you like to save to a file (enter s) or print results (enter p)? ")
                    if save_print == "s":
                        with open("encrypted.txt", 'w') as encrypted_file: #opens file
                            print("{}".format(returned_text), file = encrypted_file) #prints results to open file
                            print("File has been saved.")
                    elif save_print == "p": #prints results if user entered p
                        print(returned_text)
                    else:
                        print("Invalid input.")
            else:
                print("Invalid input. Encryption key must be a whole number equal to, or below 127.")   
        elif choice == "d":
            key = int(input("Please input the encryption key to decrypt the file ")) #asks user to input the encryption key (integer) for the file and stores the key
            if key <= maxkeynum: #makes sure that the key is not greater than the max number for the key
                file = input("Please enter the name of the file you want to decrypt ") #asks user to input filename and stores
                with open("{}".format(file), 'r') as f: #opens file and makes sure that nothing can be done without the file open
                    text = f.read()
                    returned_text = decrypt(text) #runs decrypt function
                    save_print = input("Would you like to save to a file (enter s) or print results (enter p)? ")
                    if save_print == "s":
                        with open("decrypted.txt", 'w') as encrypted_file: #opens file
                            print("{}".format(returned_text), file = encrypted_file) #prints results to open file
                            print("File has been saved.")
                    elif save_print == "p": #prints results if user entered p
                        print(returned_text)
                    else:
                        print("Invalid input.")
            else:
                print("Invalid input.  Encryption key must be a whole number equal to, or below 127.")              
        else:
            print("Invalid input.") #if user enters something other than "e" or "d", program tells them that the input is invalid
    except:
        print("Invalid input.")
    choice = input("Do you want to perform another action (enter yes or no)? ")
    if choice == "no":
        break #stops program if user enters no
    elif choice != "yes":
        print("Invalid input.")
        break