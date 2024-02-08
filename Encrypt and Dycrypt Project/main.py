from alphabet import alphabet, alphabet_upside_down 
from deface import logo

#! Variable explanation ######################
    
    #* Command => default value not 
        #* Ussage running full program by getting instruction ex: encode, decode, quit.
    #* Logo    => print the deface of the program
    #* text    => takes input the text you want to encode or decode
    #* shift   => shift takes input the value to change the formation 

#! Encryption for loop explanation and decryption

    #* enc_text => encrypted text and added by indexing the letter by following the alphabet[enc_new_position]
    #* before_enc_text_position => find the position of the first letter of text variable in alphabet list
    #* enc_new_position => change the position in the alphabet list by sum the shift and before_enc_text_position

#Todo Print main Logo
print(logo[2])

#Todo Rules
print("Type 'Decode' for Decryption or 'Encode' for Encryption and quit for exit")

#Todo command function declaration to run while loop
command = 'not'
while 'quit' not in command:

    
    command = input("=> ").lower()
    if command == 'encode':

        #Todo Run Logo of Encryption 
        print(logo[0])

        #Todo start Input
        text = input("Enter the Text \n=> ").lower()
        shift = int(input("How many shift you want? Must be (1 to 20)\n=> "))

        #Todo Checking valid shift input
        if (shift >= 1 and shift <= 20):
            #Todo Start encryption function
            def encryption(text, shift):
                enc_text = ""
                for i in text:
                    before_enc_text_position = alphabet.index(i)
                    enc_new_position = before_enc_text_position + shift
                    enc_text += alphabet[enc_new_position]
                print(f"The encrypted text is {enc_text}\n")    
            #Todo Encrypt Function Call
            encryption(text, shift)

            #Todo wanna interested or not
            print("Do you want to quit? if not type encode or decode ")

        else:
            print("You have entered the wrong shift, please Try again")

    elif command == 'decode':
        
        #Todo Run Logo
        print(logo[1])

        #TODO start Input
        text = input("Enter the Text\n=> ").lower()
        shift = int(input("How many shift you want? Must be (1 to 20)\n=> "))

        #Todo Checking valid shift input
        if (shift >= 1 and shift <= 20):

            #Todo Start Decryption Function 
            def decryption(text, shift):
                dnc_text = ""  
                for i in text:
                    before_dnc_text_position = alphabet_upside_down.index(i)
                    dnc_new_position = before_dnc_text_position + shift
                    dnc_text += alphabet_upside_down[dnc_new_position]
                print(f"The decrypted Text is {dnc_text}\n")
            decryption(text, shift)

            #Todo wanna interested or not
            print("Do you want to quit? if not type encode or decode ")

        else:
            print("You have entered the wrong shift, please Try again")

    elif command == 'quit':
        
        #Todo exit the program
        print("Thank you for using this model\n")
        break

    else:
        print("You have enetered a wrong command. Please try again\n")
