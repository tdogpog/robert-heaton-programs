##add_user

import hashlib

import sqlite3

import pyotp 

## connect to the database first

class UserRegistration:
    def __init__(self,db_filename='2FA.db'):
        self.db_filename=db_filename
        self.conn=None
        self.cursor=None


    def username_dupe(self,username):
        self.cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        if self.cursor.fetchone():
            return True
        else:
            return False
        
    def connect_to_database(self):
        self.conn=sqlite3.connect(self.db_filename)
        self.cursor=self.conn.cursor()



    def register_new(self):

        self.connect_to_database()  


        print('Welcome, please register an account')

        username=input('Please create a username:')

        while self.username_dupe(username):
            print('Username taken, try another please.')
            username=input('Please create a username:')

        password=input('Please enter a password:')

        hashpass=hashlib.sha256(password.encode()).hexdigest()

        ##2FA key 
        secret_key=pyotp.random_base32()


        self.cursor.execute("INSERT INTO users (username,password_hash,secret_key) VALUES (?,?,?)",(username,hashpass,secret_key))

        print('Please open google auth, and enter the following key for 2FA (required):')

        print(secret_key)

        self.conn.commit()   

        self.conn.close()

        print('Account registered!')    



if __name__ == "__main__":
    registration = UserRegistration()
    registration.register_new()