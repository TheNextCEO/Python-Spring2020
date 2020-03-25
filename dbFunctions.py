import random
import string
import os.path
import mysql.connector
'''I'm using w3schools as a guide for starting up the
MySql. Link: https://www.w3schools.com/python/python_mysql_create_db.asp'''
#mysql -u cop452101 -p'V0PoX+4a1PY=' -h dbsrv2.cs.fsu.edu

'''
Class Notes:
***startDB() must be run before using other functions of this class

***Special note: unameGl will be a special varible to keep the username in once
logged in. Can use this variable to see if one is logged in.
##############################################################################################

startDB(Host, username, password)   // Used to check the connection and DATABASE.
                                    // make sure to use the credidentials of your local machine.
                                    // 1: DB has succefully connected

startGameCon()                      // Uses the login system from the main to test connect DB
                                    // ****This goes at the top of Games built****
                                    // 0: No fileSave.txt
                                    // 1: Connection established.
                                    // 2: incorrect key password, logged in elsewhere

signupUser(uname, pword)            // Used to add users to the user table
                                    // ### Returns ###
                                    // 0: the start function hasn't been used yet.
                                    // 1: username and password accepted.
                                    // 3: username already taken.

loginUser(uname, pword)             // Meant to be used to login the user, can
                                    // check unameGl to see if a user is currently logged in.
                                    // ### Returns ###
                                    // 0: the start function hasn't been used yet.
                                    // 1: Username and password accepted
                                    // 2: Username not registered
                                    // 3: Wrong Password.
                                    // 4: User already logged in

isLoggedIn()                        // This function Checks to see if there is a user logged if __name__ == '__main__':
                                    // ### Returns ###
                                    // 0: Not logged in
                                    // 1: There is a user Logged in

logoutUser()                        // Logs out the user and clears the unameGl variable

saveScore(game, score)              // Saves game and score with user already logged if.
                                    // ***Note: Requires user to be logged in first.
                                    // Score should be an int
                                    // ### Returns ###
                                    // 0: The start function hasn't been used yet.
                                    // 1: Save completed
                                    // 2: No user logged in to save

topScores(game = "all", user = 0, amount = 10)
                                    // Function to pull scores.
                                    // game:   all for all games or name a specific game
                                    // user:   0 is not based on logged in user; 1 is scores the user won
                                    // amount: How many scores to pull
                                    // ### Returns ###
                                    // 0: The start function hasn't been used yet.
                                    // Should return a tuple
                                    // 2: if 1 is used for user, then not logged in.
                                    // 3: No game not listed in database



'''
class nullEscDBClass(object):
    def __init__(self):
        self.dbHost = self.dbUser = self.dbPassword = self.mydbCon = self.unameGl = ""
        '''I will use this as a boolean in my other fuctions to make sure startDB() has been run'''
        self.dbStarted = 0
        if os.path.isfile("fileSave.txt") == True:
            fileSave = open("fileSave.txt", "r")
            if fileSave.readline().rstrip() == "1":
                tHost = fileSave.readline().rstrip()
                tDBuser = fileSave.readline().rstrip()
                tDBpass = fileSave.readline().rstrip()
                tUname = fileSave.readline().rstrip()
                tword = fileSave.readline().rstrip()
                fileSave.close()

                '''Used for connecting to mysl server'''
                mydb = mysql.connector.connect(
                    host = tHost,
                    user = tDBuser,
                    passwd = tDBpass,
                    database = "thenullescdb"
                )

                commands = mydb.cursor()
                sql = "SELECT * FROM users WHERE uname = %s"
                input = (tUname,)
                commands.execute(sql, input)
                result = commands.fetchone()
                if result[3] == tword:

                    self.dbHost = tHost
                    self.dbUser = tDBuser
                    self.dbPassword = tDBpass
                    self.unameGl = tUname

                    self.mydbCon = mysql.connector.connect(
                        host = self.dbHost,
                        user = self.dbUser,
                        passwd = self.dbPassword,
                        database = "thenullescdb"
                    )

                    self.key_rewrite()
                    self.dbStarted = 1


    '''Copied/Altered the is_empty function from: https://www.pythoncentral.io/how-to-check-if-a-list-tuple-or-dictionary-is-empty-in-python/'''
    def is_empty(self, any_structure):
        if any_structure:
            '''print('Structure is not empty.')'''
            return 0
        else:
            '''print('Structure is empty.')'''
            return 1

    '''Writes a new key to the file and db for the user'''
    '''This is to make my life easier, please do not use except in this file'''
    def key_rewrite(self):
        fileSave = open("fileSave.txt", "r")
        stay = fileSave.readline().rstrip()
        fileSave.close()

        fileSave = open("fileSave.txt", "w")
        commands = self.mydbCon.cursor()
        tempPass = ''.join([random.choice(string.ascii_lowercase + string.digits) for n in range(15)])
        sql = "UPDATE users SET tword = %s WHERE uname = %s"
        input = (tempPass, self.unameGl,)
        commands.execute(sql, input)
        self.mydbCon.commit()
        #This file will provide a temp password so that the real password isn't viewable from the file
        fileSave.write(stay+"\n"+self.dbHost+"\n"+self.dbUser+"\n"+self.dbPassword+"\n"+self.unameGl+"\n"+tempPass)
        fileSave.close()


    '''user: nullEscUser password: notASecurePassword123 // This is a note of my temp u/p of my local mysql'''
    def startDB(self, theHost, theUser, thePassword):
        if self.dbStarted == 1:
            #print("skipped")
            return 1

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
            if x == "thenullescdb":
                dbCheck = 1
                break

        if dbCheck == 1:
            '''Adding the db connection if it does exist'''
            self.mydbCon = mysql.connector.connect(
            host = self.dbHost,
            user = self.dbUser,
            passwd = self.dbPassword,
            database = "thenullescdb"
            )
            self.dbStarted = 1
            commands = self.mydbCon.cursor()
            return 1
        else:
            '''print("The database does NOT exist\nBuilding Database, and tables now")'''

            commands.execute("CREATE DATABASE thenullescdb")
            '''This is to have it select the Database after creating it.'''
            self.mydbCon = mysql.connector.connect(
            host = self.dbHost,
            user = self.dbUser,
            passwd = self.dbPassword,
            database = "thenullescdb"
            )
            commands = self.mydbCon.cursor()
            commands.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, uname VARCHAR(255), pword VARCHAR(500), tword VARCHAR(30))")
            commands.execute("CREATE TABLE gameScores (id INT AUTO_INCREMENT PRIMARY KEY, uname VARCHAR(255), game VARCHAR(255), score INT(20))")
            self.dbStarted = 1
            return 1

    def startGameCon(self):
        if os.path.isfile("fileSave.txt") == True:
            fileSave = open("fileSave.txt", "r")
            tHost = fileSave.readline().rstrip()
            tDBuser = fileSave.readline().rstrip()
            tDBpass = fileSave.readline().rstrip()
            tUname = fileSave.readline().rstrip()
            tword = fileSave.readline().rstrip()
            fileSave.close()

            '''Used for connecting to mysl server'''
            mydb = mysql.connector.connect(
                host = tHost,
                user = tDBuser,
                passwd = tDBpass,
                database = "thenullescdb"
            )
            print("Game Check")

            commands = mydb.cursor()
            sql = "SELECT * FROM users WHERE uname = %s"
            input = (tUname,)
            commands.execute(sql, input)
            result = commands.fetchone()
            if result[3] == tword:
                print("game check 2?")

                self.dbHost = tHost
                self.dbUser = tDBuser
                self.dbPassword = tDBpass
                self.unameGl = tUname

                self.mydbCon = mysql.connector.connect(
                    host = self.dbHost,
                    user = self.dbUser,
                    passwd = self.dbPassword,
                    database = "thenullescdb"
                )

                self.key_rewrite()
                self.dbStarted = 1
                return 1
            else:
                # if the temp key is Wrong
                return 2
        else:
            # If no file exits
            return 0



    def signupUser(self, uname, pword):
        commands = ""
        '''Checking if db has started'''
        if self.dbStarted == 1:
            ''' I havae a valid variable incase I want to add more stipulations for a valid signup'''
            valid = 1
            commands = self.mydbCon.cursor()
            sql = "SELECT uname FROM users WHERE uname = %s"
            input = (uname,)
            commands.execute(sql, input)
            result = commands.fetchone()
            if self.is_empty(result) == 0:
                valid = 0
                return 3
            if valid == 1:
                tempPass = ''.join([random.choice(string.ascii_lowercase + string.digits) for n in range(15)])
                sql = "INSERT INTO users (uname, pword, tword) VALUES (%s, %s, %s)"
                input = (uname, pword, tempPass,)
                commands.execute(sql, input)
                self.mydbCon.commit()
                self.unameGl = uname
                fileSave = open("fileSave.txt", "w")
                fileSave.write("0\n"+self.dbHost+"\n"+self.dbUser+"\n"+self.dbPassword+"\n"+uname+"\n"+tempPass)
                fileSave.close()
                return 1

        else:
            print("ERROR: use startDB(host, username, password) function before using the other class functions.")
            return 0

    def loginUser(self, uname, pword, stay=0):
        if self.dbStarted == 0:
            print("ERROR: use startDB(host, username, password) function before using the other class functions.")
            return 0
        commands = self.mydbCon.cursor()
        sql = "SELECT * FROM users WHERE uname = %s"
        input = (uname,)
        commands.execute(sql, input)
        result = commands.fetchone()
        if self.isLoggedIn() == 1:
            return 4
        if self.is_empty(result) == 1:
            return 2
        elif result[2] == pword:
            fileSave = open("fileSave.txt", "w")
            self.unameGl = uname
            # used some code (next line only) to build tempPass from: https://pythontips.com/2013/07/28/generating-a-random-string/
            tempPass = ''.join([random.choice(string.ascii_lowercase + string.digits) for n in range(15)])
            sql = "UPDATE users SET tword = %s WHERE uname = %s"
            input = (tempPass, uname,)
            commands.execute(sql, input)
            self.mydbCon.commit()
            #This file will provide a temp password so that the real password isn't viewable from the file
            fileSave.write(str(stay)+"\n"+self.dbHost+"\n"+self.dbUser+"\n"+self.dbPassword+"\n"+uname+"\n"+tempPass)
            fileSave.close()

            return 1
        else:
            return 3

    def isLoggedIn(self):
        if self.is_empty(self.unameGl) == 0:
            return 1
        else:
            return 0

    def logoutUser(self):
        self.unameGl = ""
        self.unameGl = ""
        if os.path.exists("fileSave.txt"):
            os.remove("fileSave.txt")

    def saveScore(self, game, score):
        if self.dbStarted == 0:
            print("ERROR: use startDB(host, username, password) function before using the other class functions.")
            return 0
        if self.isLoggedIn() == 0:
            return 2
        commands = self.mydbCon.cursor()
        sql = "INSERT INTO gameScores (uname, game, score) VALUES (%s, %s, %s)"
        input = (self.unameGl, game, score,)
        commands.execute(sql, input)
        self.mydbCon.commit()
        return 1

    def topScores(self, game = "all", user = 0, amount = 10):
        if self.dbStarted == 0:
            print("ERROR: use startDB(host, username, password) function before using the other class functions.")
            return 0
        if user == 1 and self.isLoggedIn() == 0:
            return 2
        '''I ran into a bug with the mysql not pulling right, turns out 'buffered=True' is need,
        I found this solution here: https://stackoverflow.com/questions/29772337/python-mysql-connector-unread-result-found-when-using-fetchone'''
        commands = self.mydbCon.cursor(buffered=True)
        sql = "SELECT * FROM gameScores WHERE game = %s"
        input = (game,)
        commands.execute(sql, input)
        result = commands.fetchone()
        if self.is_empty(result) == 1 and game != "all":
            return 3

        if game == "all" and user == 0:
            sql = "SELECT uname, game, score FROM gameScores ORDER BY score DESC LIMIT %s"
            input = (amount,)
            commands.execute(sql, input)
            result = commands.fetchall()
            return result
        elif game == "all" and user == 1:
            sql = "SELECT uname, game, score FROM gameScores WHERE uname = %s ORDER BY score DESC LIMIT %s"
            input = (self.unameGl, amount,)
            commands.execute(sql, input)
            result = commands.fetchall()
            return result
        elif user == 1:
            sql = "SELECT uname, game, score FROM gameScores WHERE uname = %s and game = %s ORDER BY score DESC LIMIT %s"
            input = (self.unameGl, game, amount,)
            commands.execute(sql, input)
            result = commands.fetchall()
            return result
        else:
            sql = "SELECT uname, game, score FROM gameScores WHERE game = %s  ORDER BY score DESC LIMIT %s"
            input = (game, amount,)
            commands.execute(sql, input)
            result = commands.fetchall()
            return result



if __name__=="__main__":
    dbTest = nullEscDBClass()
    dbTest.startDB("mysql.djangosfantasy.com", "djangoadmin8", "best!Group")

    iUser = input("Enter a username: ")
    iPassword = input("Enter a Password: ")

    log = dbTest.signupUser(iUser, iPassword)
    if log == 1:
        print("Login Accepted.\nWelcome back", dbTest.unameGl)
    elif log == 2:
        print("Username not registered")
    elif log == 3:
        print("Wrong password")
    elif log == 4:
        print("Already logged in")

    if dbTest.isLoggedIn() == 1:
        print("Logged In")
    else:
        print("Not Logged In")

    game = input("Save a game: ")
    score = input("enter a score: ")
    theSave = dbTest.saveScore(game, score)
    if theSave == 1:
        print("Saved Score")
    elif theSave == 2:
        print("Error: not logged in yet")
    highScore = dbTest.topScores("all", 0, 6)
    for i in highScore:
        print(i, "\n")
