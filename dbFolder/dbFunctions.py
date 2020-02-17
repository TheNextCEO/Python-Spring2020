import mysql.connector
'''I'm using w3schools as a guide for starting up the
MySql. Link: https://www.w3schools.com/python/python_mysql_create_db.asp'''

'''
Class Notes:
***startDB() must be run before using other functions of this class

startDB(Host, username, password)   // Used to check the connection and DATABASE.
                                    // make sure to use the credidentials of your local machine.

signupUser(self, uname, pword)      // Used to add users to the user table

'''
class nullEscDBClass(object):
    def __init__(self):
        self.dbHost = self.dbUser = self.dbPassword = self.mydbCon = ""
        '''I will use this as a boolean in my other fuctions to make sure startDB() has been run'''
        self.dbStarted = 0
    '''user: nullEscUser password: notASecurePassword123 // This is a note of my temp u/p of my local mysql'''
    def startDB(self, theHost, theUser, thePassword):
        self.dbHost = theHost
        self.dbUser = theUser
        self.dbPassword = thePassword
        '''This is a boolean to check if the database exists'''
        dbCheck = 0
        '''Used for connecting to mysl server'''
        mydb = mysql.connector.connect(
            host = self.dbHost,
            user = self.dbUser,
            passwd = self.dbPassword
        )

        commands = mydb.cursor()
        commands.execute("SHOW DATABASES")
        dBases = [commands for commands, in commands]

        '''Checking to see if the database exists'''
        for x in dBases:
            if x == "theNullEscDB":
                dbCheck = 1
                break

        if dbCheck == 1:
            '''Adding the db connection if it does exist'''
            self.mydbCon = mysql.connector.connect(
            host = self.dbHost,
            user = self.dbUser,
            passwd = self.dbPassword,
            database = "theNullEscDB"
            )
            self.dbStarted = 1
            commands = self.mydbCon.cursor()
        else:
            print("The database does NOT exist\nBuilding Database, and tables now")

            commands.execute("CREATE DATABASE theNullEscDB")
            '''This is to have it select the Database after creating it.'''
            self.mydbCon = mysql.connector.connect(
            host = self.dbHost,
            user = self.dbUser,
            passwd = self.dbPassword,
            database = "theNullEscDB"
            )
            commands = self.mydbCon.cursor()
            commands.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, uname VARCHAR(255), pword VARCHAR(500))")
            commands.execute("CREATE TABLE gameScores (id INT AUTO_INCREMENT PRIMARY KEY, uname VARCHAR(255), game VARCHAR(255), score INT(20))")
            self.dbStarted = 1

    def signupUser(self, uname, pword):
        commands = ""
        '''Checking if db has started'''
        if self.dbStarted == 1:
            commands = self.mydbCon.cursor()
        else:
            print("ERROR: use startDB() function before using the other class functions.")


if __name__=="__main__":
    dbTest = nullEscDBClass()
    dbTest.startDB("localhost", "nullEscUser", "notASecurePassword123")
    print(dbTest.dbUser)
