##pass_db setup

import os  

import sqlite3




def create_table(cursor):
    cursor.execute('''CREATE TABLE users(
                username TEXT NOT NULL,
                password_hash TEXT NOT NULL,
                secret_key TEXT NOT NULL 
                )''')
    
    conn.commit()
    conn.close()

def fetch_info(cursor):

    ##count up the rows

    cursor.execute("SELECT COUNT(*) FROM users")

    # fetch the row count from the result set
    row_count = cursor.fetchone()[0]

    print(f"Rows in users table: {row_count}")

    
    conn.close()


db_file_initial= input('Enter database filename:')

db_filename=db_file_initial+'.db'

while True: 
    if os.path.exists(db_filename):

        print('An existing database of this filename exists!')
        print(db_filename,'contains the following number of rows:')
        conn=sqlite3.connect(db_filename)
        cursor=conn.cursor()
        fetch_info(cursor)

        ##ask the user if they want to ovewrite it
        user_input=input('Do you want to overwrite the current database Y/N:').upper()
        if user_input== 'Y':
            last_try=input('Are you sure? This will delete all user data. Y/N:').upper()
            if last_try=='Y':
              
               
                #delete the file
                
                os.remove(db_filename)

                #reconnects with same filename to overwrite

                conn=sqlite3.connect(db_filename)

                cursor=conn.cursor()
                
                ##executes the table creation function

                create_table(cursor)
                print('File Overwritten')
                break
              
                


            else: 
                ##choosing not to overwrite
                exit()

        elif user_input== 'N':
                break

        else:
            print('Y/N input only')
            continue 
            
            

    else:
        
        conn=sqlite3.connect(db_filename)
        cursor=conn.cursor()
        create_table(cursor)
        print('New File Generated')
        break
        


