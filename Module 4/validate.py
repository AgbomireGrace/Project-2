def main():

    #1-------------------------------------------------------------------
    #user_input = input('Enter a number: ')
    #user_input = int(user_input)

    #print("The next number  is: {}".format(user_input+1))
    #-------------------------------------------------------------------

    #2-------------------------------------------------------------------
    #What if the user doesn't input an integer?
    #-------------------------------------------------------------------

    #Implement error-catching
    # try:
    #     user_input = int(input('Please enter a number: '))
    #     print("The next number  is: {}".format(user_input+1))
    # except ValueError:
    #     print('Error! The character entered was not a number!')

    #3-------------------------------------------------------------------
    #If the user doesn't input an integer, prompted infinitely until number
    #-------------------------------------------------------------------
    # while True:
    #     try:
    #        user_input = int(input('Please enter a number: '))
    #        print("The next number  is: {}".format(user_input+1))
    #        break
    #     except ValueError:
    #        print('Error! The character entered was not a number!')

    #4-------------------------------------------------------------------
    #Input validation with characters
    #-------------------------------------------------------------------
    # forbidden_chars = ('.','?',';','/','\\')

    # while True:
    #     username = ('Enter a username. The characters (".","?",";","/","\\") are not allowed \n')

    #     invalid_chars_counter = 0

    #     for char in forbidden_chars:
    #         if char in username:
    #             invalid_chars_counter+=1

    #     if invalid_chars_counter > 0:
    #         print('\nError! Username cannot contain (".","?",";","/","\\")')
    #     else:
    #         break
    #     print(f'\nWelcome to the system terminal {username}!')

    #5-------------------------------------------------------------------
    #Input validation with characters, allow ONLY alphabetical characters
    #-------------------------------------------------------------------
    import string

    #create upper and lower case alphabet lists
    alpha_lower = list(string.ascii_lowercase) #[a,b,c,...,z]
    alpha_upper = list(string.ascii_uppercase) #[A,B,C,...,Z]

    big_alpha = alpha_lower + alpha_upper #[a,b,c,...,Z]

    checked_chars = 0 #character index tracker

    while True:
     #reset tracker to zero if it loops again
         checked_chars = 0
         username = input("\n Please enter a username: ")

         for character in username:
            #increment the tracker by 1 for each character searched
            if character in big_alpha:
                 checked_chars+=1
            else:
                 print(f"\nError! {character} is not allowed")

            #check if we've reached end of username, display results
            if checked_chars == len(username):
                 print(f"\nYour username is {username}")
                 break
            
        


if __name__ == "__main__":
        main()
        