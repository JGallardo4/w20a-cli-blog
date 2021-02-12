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

def get(command, arguments=[]):
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(command, arguments)
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

def put(command, arguments=[]):
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(command, arguments)
        connection.commit()
    except Exception as err:
        print(err)
        quit()    
    else:        
        if (cursor != None):
            cursor.close()
        if (connection != None):        
            connection.close()

def getPosts():
    return get("SELECT * FROM blog_post")
    

def createNewPost(user, content):
    put("INSERT INTO blog_post (username, content) VALUES (?, ?)", [user, content])
    print("\n✓ Post created!\n")

def login(username, password):
    return get("SELECT * FROM Users WHERE Username = ? and Password_String = ?", [username, password])

def createUser(username, password):
    put("INSERT INTO Users (Username, Password_String) VALUES (?, ?)", [username, password])
    print("\n✓ User created!\n")

class FailedLoginException(Exception):
    pass