import dbcreds
import mariadb
import sys

connection = None
cursor = None

def connect():
    return mariadb.connect(
        user=dbcreds.user,
        password=dbcreds.password,
        host=dbcreds.host,
        port=dbcreds.port,
        database=dbcreds.database
    )
def getPosts():
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM blog_post")
        result = cursor.fetchall()
    except:
        print("DB Error")
        quit()    
    else:        
        if (cursor != None):
            cursor.close()
        if (connection != None):        
            connection.close()
        return result

def createNewPost(user, content):
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO blog_post (username, content) VALUES (?, ?)",
            [user, content])
        connection.commit()
    except:
        print("DB Error")
        quit()    
    else:        
        if (cursor != None):
            cursor.close()
        if (connection != None):        
            connection.close()

def login(username, password):
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Users WHERE Username = ? and Password_String = ?", [username, password])
        result = cursor.fetchall()
        if result:
            return True
        else:
            raise FailedLoginException("Failed login")
    except FailedLoginException:
        return False
    except:
        print("DB Error")
        quit()    
    else:        
        if (cursor != None):
            cursor.close()
        if (connection != None):        
            connection.close()

def createUser(username, password):
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Users (Username, Password_String) VALUES (?, ?)",
            [username, password])
        connection.commit()
    except:
        print("DB Error")
        quit()    
    else:        
        if (cursor != None):
            cursor.close()
        if (connection != None):        
            connection.close()
        print("\n✓ User created!\n")

class FailedLoginException(Exception):
    pass