# ------------------------------------
# FUNCTION    Week 4  Lab 4
#             used in conjunction with Lab 
#             to provide logic to LAB 4 to connect to Database
#             created with sqlite3 module
# DATE        FALL 2021
# Python      3.8 or 3.9.6
# ---------------------------------
#Editting this file

# IMPORTS
import connect_DB1 as connect_DB

# Create VARIABLES

# Create Functions

# ACTUAL DO THINGS

'''
****Use only if database has been deleted**** 
Creates a file named logins.db that contains table called users.
Module also adds a user 'Admin' with password 'Admin' and role of 'admin'.
This user will serve as default admin user. 
'''
def create_DB():
    return Connect_DB.create()
    

def Check_user(user, password):
    db_result = connect_DB.check_for_user(user)
    
    if db_result == None:
        return [False] # return a list with one element 
    else:
        if db_result[1] != password:
            return [False] # return a list with one element 
    return [True, db_result[2]] # # return a list with two element, True and role 

def add_user(name, password, role):
    '''
    make proper checks, could be put in __IsPasswordValid(password)
    1) Can not have two users in with same username. 
    2) password of proper length ... affecting new users only
    3) no one can put admin as their role
    CALL >> def update_users(e_user,e_password, e_role):
    '''
    message = "change add_user method so it would call the update_users() method in connect_DB"
    send = [True, message]
    return send

def get_user_table():
    return "change method so it would call the read_all_users() method from dconnect_DB"

  
 

 

'''
optional use   
could use this as a function that check if password meet requirements
could be used if you want to allow users to change their passwords
'''
def __IsPasswordValid(password): # method not seen in modules that import them. But, developer knows about function could call it
    print("hello")


