# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'valorant_match_stats.db'
def cont():
    cont = ""
    while cont != "Y" or cont != "N":
        cont = input("Continue? (y/n) ")
        cont = cont.upper()
        if cont == "Y":
            return()
        elif cont == "N":
            print("Thank you for using Jonathon's Valorant Stats database. Goodbye.\n")
            exit()
        else:
            print("That is not a valid decision, please try again\n")
def print_view(view_name):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()

    # Get the results from the view
    sql = f"select * from {view_name}"
    cursor.execute(sql)
    results = cursor.fetchall()

    # Get the field names to use as headings
    headings = headings = [description[0] for description in cursor.description]

    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()
    cont()

def select_view():
    print("You chose A: Select SQL queries from pre-made views.\n")
    choice = ""
    while choice != "Z":
        choice = input( "\nType the letter for the info you want.\n"
                        "A: Average Player Stats\n"
                        "B: Average Team Stats\n"
                        "C: Matches Won\n"
                        "D: MVP Details\n"
                        "E: Player's Best Matches\n"
                        "Z: Back\n\n"
                        "Enter your choice here: ")
        choice = choice.upper()
        if choice == "A":
            print("You chose A: Average Player Stats.\n")
            print_view("[Average Player Stats]")
        elif choice == "B":
            print("You chose B: Average Team Stats\n")
            print_view("[Average Team Stats]")
        elif choice == "C":
            print("You chose C: Matches Won\n")
            print_view("[Matches Won]")
        elif choice == "D":
            print("You chose D: MVP Details\n")
            print_view("[MVP Details]")
        elif choice == "E":
            print("You chose E: Player's Best Matches\n")
            print_view("[Player's Best Matches]")
        elif choice == "Z":
            print("Returning to main selection screen.\n")
        else:
            print("That is not a valid decision, please try again\n")

def basic_custom():
    print("You chose B: A basic custom view maker. (Parameter Queries)\n")
    choice = ""
    while choice != "Z":
        choice = input("Please choose a table:\n"
                            "A: Player Details\n"
                            "B: Match Details\n"
                            "C: Match Stats\n"
                            "Z: Exit\n")
        try:
            choice = choice.upper()
        except:
            ""
        # Player Details
        if choice == "A":
            print("You chose A: Player Details, Choose what columns you want to view.\n")
            column_list = input("The columns:\n"
                                "A: Player ID\n"
                                "B: Username\n"
                                "C: Level\n"
                                "D: Rank\n"
                                "Enter the columns you want to view (Seperated by a space e.g. 'A B C'): ").split()
            for i in range(len(column_list)):
                column_list[i] = column_list[i].upper()

        # Match Details
        elif choice == "B":
            print("You chose B: Match Details, Choose what columns you want to view.\n")
            column_list = input("The columns:\n"
                                "A: Match ID\n"
                                "B: Map\n"
                                "C: Team MVP\n"
                                "D: Match Length\n"
                                "E: Outcome (Win/Lose)\n"
                                "Enter the columns you want to view (Seperated by a space e.g. 'A B C'): ").split()
            for i in range(len(column_list)):
                column_list[i] = column_list[i].upper()
        # Match Stats
        elif choice == "C":
            print("You chose C: Match Stats, Choose what columns you want to view.\n")
            column_list = input("The columns:\n"
                                "A: Match ID\n"
                                "B: Player ID\n"
                                "C: Username\n"
                                "D: Agent\n"
                                "E: Combat Score\n"
                                "F: Kills\n"
                                "G: Deaths\n"
                                "H: Assists\n"
                                "I: Headshots\n"
                                "J: Eco Score\n"
                                "K: Accuracy\n"
                                "Enter the columns you want to view (Seperated by a space e.g. 'A B C'): ").split()
            for i in range(len(column_list)):
                column_list[i] = column_list[i].upper()
        elif choice == "Z":
            print("Returning to main selection screen.\n")
        else:
            print("That is not a valid decision, please try again\n")
        
        # select names
        query = naming_selection(column_list, choice)
        
def final_query(query, choice):
    if choice == "A":
        where = paramA()
    elif choice == "B":
        where = paramB()
    elif choice == "C":
        where = paramC()
    
    sql_input(query + where)

def paramA():
    # Params are Username & Level Range
    valid = False
    while valid != True:
        param_choice = input("Please select a filter/parameter:\n"
                            "A: Username\n"
                            "B: Level Range\n"
                            "Z: No Filter\n").upper()
        if param_choice == "A":
            valid = True
            return(" where username = '"+ input("Please enter a username (Make sure the spelling is correct):\n"))
        elif param_choice == "B":
            param = input("Please enter a minimum level:\n")
            valid = True
            try:
                return(f" where level > {int(param)} and level < "+int(input("Please enter a maximum level:\n")))
            except:
                valid = False
        elif param_choice == "Z":
            valid = True
            return()
        else:
            print("That is not a selection. Please try again.")
def paramB():
    # Params are Match ID, Map & Outcome
    valid = False
    while valid != True:
        param_choice = input("Please select a filter/parameter:\n"
                            "A: Match ID\n"
                            "B: Map\n"
                            "C: Outcome\n"
                            "Z: No Filter\n").upper()
        if param_choice == "A":
            valid = True
            try:
                return(" where match_id = '"+int(input("Please enter a Match ID:\n"))+"'")
            except:
                valid = False
        elif param_choice == "B":
            valid = True
            return(f" where map = '{input("Please enter a map (Make sure the spelling & is correct):\n").title()}'")
        elif param_choice == "C":
            param = input("Please enter an outcome (Win or Lose):\n").title().lower()
            if param == "win" or param == "lose":
                valid = True
                return(f" where outcome = '{param}'")
        elif param_choice == "Z":
            valid = True
            return()
        else:
            print("That is not a selection. Please try again.")
def paramC():
    # Params are Match ID, Username, Combat Score Range, Kills Range & Deaths Range
    valid = False
    while valid != True:
        param_choice = input("Please select a filter/parameter:\n"
                            "A: Match ID\n"
                            "B: Username\n"
                            "C: Combat Score Range\n"
                            "D: Kills Range\n"
                            "E: Deaths Range\n"
                            "Z: No Filter\n").upper()
        if param_choice == "A":
            valid = True
            try:
                return(f" where match_id = '{int(input("Please enter a Match ID:\n"))}'")
            except:
                valid = False
        elif param_choice == "B":
            valid = True
            return(f" where username = '{input("Please enter a username (Make sure the spelling is correct):\n")}'" )
        elif param_choice == "C":
            param = input("Please enter a minimum Combat Score:\n")
            valid = True
            try:
                return(f" where level > {int(param)} and level < {int(input("Please enter a maximum Combat Score:\n"))}")
            except:
                valid = False
        elif param_choice == "D":
            param = input("Please enter a minimum number of kills:\n")
            valid = True
            try:
                return(f" where level > {int(param)} and level < {int(input("Please enter a maximum number of kills:\n"))}")
            except:
                valid = False
        elif param_choice == "E":
            param = input("Please enter a minimum number of deaths:\n")
            valid = True
            try:
                return(f" where level > {int(param)} and level < {int(input("Please enter a maximum number of deaths:\n"))}")
            except:
                valid = False
        elif param_choice == "Z":
            valid = True
            return()
        else:
            print("That is not a selection. Please try again.")
def naming_selection(lst, tabl):
    newlist = []
    if tabl == "A":
        table = "player_details"
        for i in lst:
            if i == "A":
                newlist.append("player_id as 'player id'")
            elif i == "B":
                newlist.append("username")
            elif i == "C":
                newlist.append("level")
            elif i == "D":
                newlist.append("rank")
    elif tabl == "B":
        table = "match_stats"
        for i in lst:
            if i == "A":
                newlist.append("match_id as 'match id'")
            elif i == "B":
                newlist.append("map")
            elif i == "C":
                newlist.append("team_mvp as 'team mvp'")
            elif i == "D":
                newlist.append("match_length as 'match length'")
            elif i == "E":
                newlist.append("outcome")
    elif tabl == "C":
        table = "team_stats left join player_details on team_stats.player_id = player_details.player_id"
        for i in lst:
            if i == "A":
                newlist.append("match_id as 'match id'")
            elif i == "B":
                newlist.append("player_id as 'player id'")
            elif i == "C":
                newlist.append("username") 
            elif i == "D":
                newlist.append("agent")
            elif i == "E":
                newlist.append("combat_score as 'combat score'")
            elif i == "F":
                newlist.append("kills")
            elif i == "G":
                newlist.append("deaths")
            elif i == "H":
                newlist.append("assists")
            elif i == "I":
                newlist.append("headshots")
            elif i == "J":
                newlist.append("eco")
            elif i == "K":
                newlist.append("accuracy") 
            
    select_query = ""
    for i in newlist:
        select_query += i + ", "
    return("select " + select_query[:-2] + " from " + table)
def sql_input(inp):
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()

    # Get the results from the view
    sql = inp
    cursor.execute(sql)
    results = cursor.fetchall()

    # Get the field names to use as headings
    headings = headings = [description[0] for description in cursor.description]

    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()
    cont()

print("\n\n\n\nWelcome to Jonathon's Valorant Stats database.\n")
choice = ""
while choice != "Z":
    choice = input( "Type the letter for the setting you want.\n"
                    "A: Select SQL queries from pre-made views.\n"
                    "B: A basic custom view maker. (Parameter Queries)\n"
                    "C: An advanced SQL Query input.\n"
                    "Z: Exit\n\n"
                    "Enter your choice here: ")
    choice = choice.upper()
    if choice == "A":
        select_view()
    elif choice == "B":
        basic_custom()
    elif choice == 'C': 
        print("You chose C: An advanced SQL Query input")
        inp = input("Enter your query here:\n")
        sql_input(inp)
    elif choice == "Z":
        print("Thank you for using Jonathon's Valorant Stats database. Goodbye.\n")
    else:
        print("That is not a valid decision, please try again\n")