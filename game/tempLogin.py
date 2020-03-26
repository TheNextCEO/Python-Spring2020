from dbFunctions import *
db = nullEscDBClass()
db.startDB("mysql.djangosfantasy.com", "djangoadmin8", "best!Group")
print("### Welcome to the Null Escape Arcade ###")

def openGame(game):
    os.system("python3 "+game)

def first_Menu():
    menu1 = "4"
    print("1. Login\n2. Signup\n3. Exit")
    while menu1 != "3":
        menu1 = input(">")
        if menu1 == "1":
            print("\n### Login ###")
            username = input("Username: ")
            password = input("Password: ")
            stayin = input("Stay logged in? <y|n>: ")
            if stayin == "y" or stayin == "Y":
                stayin = 1
            else:
                stayin = 0
            result = db.loginUser(username, password, stayin)
            if result == 1:
                print("Login Accepted.\nWelcome back", db.unameGl)
                menu1 = "3"
            elif result == 2:
                print("\nUsername not registered!\n")
            elif result == 3:
                print("\nWrong password!\n")
            elif result == 4:
                print("\nAlready logged in!!\n")
                menu1 = "3"

        elif menu1 =="2":
            print("\n### Signup ###")
            username = input("Username: ")
            password = input("Password: ")
            result = db.signupUser(username, password)
            if result == 1:
                print("Welcome", db.unameGl, "enjoy our games!")
                menu1 = "3"
            elif result == 3:
                print("\nUsername already taken!\n")

        elif menu1 == "3":
            return 0


def main_menu():
    menu2 = "9"
    while menu2 != "3" and menu2 != "4":
        print("\n### Main Menu ###")
        print("1. Play Games!\n2. High scores\n3. Log out\n4. Exit")
        menu2 = input(">")
        if menu2 == "1":
            print("List of games:")
            print("1. Snake")
            print("2. Ice Breaker")
            menu3 = input(">")
            if menu3 == "1":
                openGame("Snake-V1.py")
            elif menu3 == "2":
                openGame("breakout_test.py")


        elif menu2 == "2":
            print("\n###highScores###")
            print("1. Your top ten\n2. Top ten of all")
            menu3 = input(">")
            if menu3 == "1":
                highScore = db.topScores("all", 1)
                l = 1
                for i in highScore:
                    n, g, s = i
                    print(str(l)+". "+n+"  Game: "+g+"  Score: "+str(s))
                    l += 1
            if menu3 == "2":
                highScore = db.topScores("all", 0)
                l = 1
                for i in highScore:
                    n, g, s = i
                    print(str(l)+". "+n+"  Game: "+g+"  Score: "+str(s))
                    l += 1
        elif menu2 == "3":
            db.logoutUser()
        elif menu2 == "4":
            return 0

#if user is staying logged in, no reason to have the login menu
theLoop = 1
while theLoop != 0:
    if db.isLoggedIn() == 0:
        theLoop = first_Menu()

    if db.isLoggedIn() == 1:
        theLoop = main_menu()
