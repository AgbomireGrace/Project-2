import bcrypt
import getpass

#Register user
def register_user():

    #Ask the user to create their username
    user = input("\nCreate a username: ")

    #Ask the user to create their password
    # password = input("\nCreate a password: ").encode("utf-8")

    #ask the user to create their password, hiding the input
    password = getpass.getpass("Create a password: ").encode("utf-8")

    # Hash the password using bcrypt
    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(password, salt)

    print(f"\n{user}, your password has been securely stored")

    return (user, hashed_pw)

#Authenticate the user by checking their password
def authenticate_user (stored_user, stored_pw_hash):
    pw_attempt = 0 #track password attempts
    success_login = False

    while pw_attempt < 5:
        #Ask the user for their username to authenticate
        user_attempt = input("\nEnter your username to authenticate: ")

        #Ask the user for their password to authenticate
        # password_attempt = input("\nEnter your password to authenticate: ").encode("utf-8")

        #ask the user to create their password, hiding the input
        password_attempt = getpass.getpass("\nEnter your password to authenticate: ").encode("utf-8")

        if stored_user == user_attempt:
            #Compare the password attempt with the stored hash
            if bcrypt.checkpw(password_attempt, stored_pw_hash):
                print("\nAuthentication successful! You have access.\n")
                success_login = True
            # else:
            #     print("\nAuthentication failed")
                break



        if stored_user != user_attempt or bcrypt.checkpw(password_attempt, stored_pw_hash):
          if pw_attempt < 1:
            print("\nAuthentication failed! Incorrect Credentials, please try again")
            pw_attempt+=1
            print(f"You've attempted the password {pw_attempt} times")
        elif pw_attempt < 3:
            print("\nAuthentication failed! Incorrect Credentials, please try again")
            pw_attempt+=1
            print(f"You've attempted the password {pw_attempt} times")
        elif pw_attempt == 3:
            print("\nAuthentication failed! Incorrect Credentials, you have one more attempt")
            pw_attempt+=1
            print(f"You've attempted the password {pw_attempt} times")
        else:
            break

    if pw_attempt >= 4 and success_login == False:
        pw_attempt+=1
        print(f"You've attempted the password {pw_attempt} times")
        print("Maximum attempts reached. System locked for 10 minutes. \n")

#Main  logic
def main():
    print("Welcome to the secure authentication system!")

    #Register the user and get the hashed password
    creds = register_user()
    # print(creds)

    #Authenticate the user with their password
    authenticate_user(creds[0],creds[1])

if __name__ == "__main__":
    main()
    
