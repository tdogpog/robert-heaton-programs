##password hashing 

import hashlib

import json 

import sqlite3

import pyotp 

from add_user import UserRegistration 

class Main_Login_System:

    ##database is hardcoded, you must change it here
    ##if you want to make a new database use the setup_db script 

    def __init__(self,db_filename='2FA.db'):
        self.db_filename=db_filename
        self.conn=None
        self.cursor=None


    def is_valid_credentials(self,username,password):

        passhash=hashlib.sha256(password.encode()).hexdigest()

        self.cursor.execute("SELECT * FROM users where username=? AND password_hash=?", (username,passhash))

        ##.execute parses the list with the sql query we provided
        ##it sets the cursor up with this information
        ##we then fetch the information with .fetchone()

        ##we have to set it up like this because if we do .fetchone() again,
        ##we lose the correct row we are on. each subsequent .fetchone() command
        ##advances the row we are on. so we need to fetch it, then store it
        ##so we can do logic on it without advancing it by accidentaly calling
        ## .fetchone() again

        user_row=self.cursor.fetchone()

        if user_row:

            secret_key=user_row[2]

            totp=pyotp.TOTP(secret_key)

            gen_code=totp.now()

            code_match=input('Please enter 2FA Code:')

            if code_match==gen_code:
                return True
            else:
                print('2FA Failed, relog please')

        else: 
            return False

    def sql_connecting(self):
        
        self.conn=sqlite3.connect(self.db_filename)
        self.cursor=self.conn.cursor()


    def login_create(self):

        print('Welcome to the Login Portal!')


        print('Enter 1 to login to an existing account, or, enter 2 to create a new account')

        while True:
            create_or_login=input('Enter your input:')


            if create_or_login == '1':

                self.sql_connecting()

                while True:
                    username=input('Username:')

                    password=input('Password:')

                    run=self.is_valid_credentials(username,password)

                    if run is True:
                        print('Welcome', username+'!')
                        exit()
                    
                    if run is False:
                        print('No Account Found, Try Again')


            elif create_or_login == '2':

                registration=UserRegistration()
                registration.register_new()
                break

            else: 
                print('Please enter a 1 or 2')


if __name__ == "__main__":
    loginportal = Main_Login_System()
    loginportal.login_create()



##old way to do it from json/dictionaries
    
# def is_valid_credentails(user,pass):
    # for dict_entry in login_data:

    #     user=dict_entry.get('username')
    #     pass_=dict_entry.get('password')

    #     if user == username and pass_ == passhash:
    #         return True

        

# #we can try storing all thei users in key/value dict
# user_pass_dict={'Hi':'hi','G':'g','M':'m'} 

# for key,value in user_pass_dict.items():

#     shahash_value=hashlib.sha256(value.encode()).hexdigest()
#     user_pass_dict[key]=shahash_value

# print(user_pass_dict)
    
#syntax to open a file an assign it to a variable,
#then we ccan use json library to load the file into another var 
    
## old way to access it using a json, we moved to a sql file now 
# with open('userlogins.json','r') as file:
#     login_data=json.load(file)
    



