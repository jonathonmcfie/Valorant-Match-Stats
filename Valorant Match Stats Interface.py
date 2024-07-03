# Import the libraries to connect to the database and present the information in tables
import sqlite3
from easygui import *
from tabulate import tabulate
title = "Valorant Match Stats"
# This is the filename of the database to be used
DB_NAME = 'valorant_match_stats.db'
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
    choice = view_name[1:-1]
    if codebox(f"You selected {choice}.\nTo continue using the interface, click OK. Otherwise, press Esc or click Cancel", choice, tabulate(results,headings,tablefmt="simple_outline")):
        select_view()
    else:
        msgbox("Thank you for using Jonathon's Valorant Match Stats GUI")

    db.close()

def select_view():
    choices = ["Average Player Stats", "Average Team Stats", "Matches Won", "MVP Details", "Player's Best Matches"]
    choice = choicebox("Please choose a pre-made view", "Pre-Made Views", choices)
    if choice == choices[0]:
        print_view("[Average Player Stats]")
    elif choice == choices[1]:
        print_view("[Average Team Stats]")
    elif choice == choices[2]:
        print_view("[Matches Won]")
    elif choice == choices[3]:
        print_view("[MVP Details]")
    elif choice == choices[4]:
        print_view("[Player's Best Matches]")
    else:
        start()
def final_query(query, choice):
    if choice == "Player Details":
        where = paramA()
    elif choice == "Match Details":
        where = paramB()
    elif choice == "Match Stats":
        where = paramC()
    
    sql_input(query + where)

def paramA():
    # Params are Username & Level Range
    valid = False
    while valid != True:
        choices = ["Username", "Level Range", "No Filter"]
        param_choice = choicebox("Please select a filter/parameter", "Custom View (Choose Filter/Parameter)", choices)
        if param_choice == "Username":
            valid = True
            choice = enterbox("Please enter a username (Make sure the spelling is correct)","Custom View (Enter Username)")
            if choice == None:
                    paramA()
            return(" where username = '"+ choice+"'")
        elif param_choice == "Level Range":
            valid = True
            try:
                choice = multenterbox("Please enter a minimum & maximum level", "Custom View (Enter Levels)", ["Minimum Level", "Maximum Level"])
                if choice == None:
                    paramA()
                return(f" where level > {str(int(choice[0]))} and level < "+ str(int(choice[1])))
            except:
                valid = False
                msgbox("That is not a selection. Please try again.", "Custom View (Invalid Selection)")
        elif param_choice == "No Filter":
            valid = True
            return("")
        elif param_choice == None:
            valid = True
            basic_custom()
def paramB():
    # Params are Match ID, Map & Outcome
    valid = False
    while valid != True:
        choices = ["Match ID", "Gamemode", "Map", "Outcome", "No Filter"]
        param_choice = choicebox("Please select a filter/parameter", "Custom View (Choose Filter/Parameter)", choices)
        if param_choice == "Match ID":
            valid = True
            try:
                choice = integerbox("Please enter a Match ID", "Custom View (Enter Match ID)")
                if choice == None:
                    paramB()
                return(" where match_id = '"+str(int(choice))+"'")
            except:
                valid = False
        elif param_choice == "Gamemode":
            valid = True
            choice = enterbox("Please enter a gamemode (Make sure the spelling is correct)","Custom View (Enter Gamemode)")
            if choice == None:
                    paramB()
            return(" where gamemode = '"+ choice+"'")
        elif param_choice == "Map":
            valid = True
            choice = enterbox("Please enter a map (Make sure the spelling is correct)","Custom View (Enter Map)")
            if choice == None:
                    paramB()
            return(" where map = '"+ choice+"'")
        elif param_choice == "Outcome":
            choices = ["Win", "Lose"]
            choice = choicebox("Please enter an outcome:", "Custom View (Enter Outcome)", choices)
            if choice == None:
                    paramB()
            return(f" where outcome = '{choice.lower()}'")
        elif param_choice == "No Filter":
            valid = True
            return("")
        elif param_choice == None:
            valid = True
            basic_custom()
            exit()
        else:
            print("That is not a selection. Please try again.")
def paramC():
    # Params are Match ID, Username, Combat Score Range, Kills Range & Deaths Range
    valid = False
    while valid != True:
        choices = ["Match ID", "Username", "Combat Score Range", "KDA Range", "No Filter"]
        param_choice = choicebox("Please select a filter/parameter", "Custom View (Choose Filter/Parameter)", choices)
        if param_choice == "Match ID":
            valid = True
            try:
                choice = integerbox("Please enter a Match ID", "Custom View (Enter Match ID)")
                if choice == None:
                    paramC()
                return(" where match_id = '"+str(int(choice))+"'")
            except:
                valid = False
        if param_choice == "Username":
            valid = True
            choice = enterbox("Please enter a username (Make sure the spelling is correct)","Custom View (Enter Username)")
            if choice == None:
                    paramC()
            return(" where username = '"+ choice+"'")
        elif param_choice == "Combat Score Range":
            valid = True
            try:
                choice = multenterbox("Please enter a minimum & maximum combat score", "Custom View (Enter Combat Scores)", ["Minimum Combat Score", "Maximum Combat Score"])
                if choice == None:
                    paramC()
                return(f" where combat_score > {str(int(choice[0]))} and combat_score < "+ str(int(choice[1])))
            except:
                valid = False
                msgbox("That is not a selection. Please try again.", "Custom View (Invalid Selection)")
        elif param_choice == "KDA Range":
            valid = True
            try:
                choice = multenterbox("Please enter a minimum & maximum KDA", "Custom View (Enter KDAs)", ["Minimum KDA", "Maximum KDA"])
                if choice == None:
                    paramC()
                return(f" where kda > {str(int(choice[0]))} and kda < "+ str(int(choice[1])))
            except:
                valid = False
                msgbox("That is not a selection. Please try again.", "Custom View (Invalid Selection)")
        elif param_choice == "No Filter":
            valid = True
            return("")
        elif param_choice == None:
            valid = True
            basic_custom()
        else:
            print("That is not a selection. Please try again.")
def naming_selection(lst, tabl, choices):
    newlist = []
    if tabl == "Player Details":
        table = "player_details"
        for i in lst:
            if i == choices[0]:
                newlist.append("player_id as 'player id'")
            elif i == choices[1]:
                newlist.append("username")
            elif i == choices[2]:
                newlist.append("level")
            elif i == "*":
                newlist.append("*")
    elif tabl == "Match Details":
        table = "match_stats"
        for i in lst:
            if i == choices[0]:
                newlist.append("match_id as 'match id'")
            elif i == choices[1]:
                newlist.append("map")
            elif i == choices[2]:
                newlist.append("team_mvp as 'team mvp'")
            elif i == choices[3]:
                newlist.append("match_length as 'match length'")
            elif i == choices[4]:
                newlist.append("outcome")
            elif i == "*":
                newlist.append("*")
    elif tabl == "Match Stats":
        table = "team_stats left join player_details on team_stats.player_id = player_details.player_id"
        for i in lst:
            if i == choices[0]:
                newlist.append("match_id as 'match id'")
            elif i == choices[1]:
                newlist.append("team_stats.player_id as 'player id'")
            elif i == choices[2]:
                newlist.append("username") 
            elif i == choices[3]:
                newlist.append("agent")
            elif i == choices[4]:
                newlist.append("kda")
            elif i == choices[5]:
                newlist.append("combat_score as 'combat score'")
            elif i == choices[6]:
                newlist.append("kills")
            elif i == choices[7]:
                newlist.append("deaths")
            elif i ==choices[8]:
                newlist.append("assists")
            elif i == choices[9]:
                newlist.append("econ")
            elif i == "*":
                newlist.append("*")
            
    select_query = ""
    for i in newlist:
        select_query += i + ", "
    return("select " + select_query[:-2] + " from " + table)
def sql_input(inp):
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    if inp == None:
        start()
    # Get the results from the view
    sql = inp
    cursor.execute(sql)
    results = cursor.fetchall()

    # Get the field names to use as headings
    headings = headings = [description[0] for description in cursor.description]

    # Print the results in a table with the headings
    if codebox(f"Here is your custom view.\nTo continue using the interface, click OK. Otherwise, press Esc or click Cancel", "Finished View", tabulate(results,headings,tablefmt="simple_outline")):
        basic_custom()
    else:
        msgbox("Thank you for using Jonathon's Valorant Match Stats GUI")
    db.close()

def basic_custom():
    choices = ["Player Details", "Match Details", "Match Stats"]
    choice = choicebox("Please choose a table for your custom view", "Custom View (Choose Table)", choices)
     # Player Details
    if choice == "Player Details":
        choices = ["Player ID","Username","Level"]
        column_list = multchoicebox("You chose the Player Details table\n\nPlease choose what columns you want to view.\n", "Custom View (Choose Columns)", choices)
        
    # Match Details
    elif choice == "Match Details":
        choices = ["Match ID", "Gamemode", "Map", "Team MVP", "Match Length", "Outcome (Win/Lose)"]
        column_list = multchoicebox("You chose the Match Details table\n\nPlease choose what columns you want to view.\n", "Custom View (Choose Columns)", choices)
        
    # Match Stats
    elif choice == "Match Stats":
        choices = ["Match ID", "Player ID", "Username", "Agent", "Combat Score", "KDA", "Kills", "Deaths", "Assists", "Econ Score"]
        column_list = multchoicebox("You chose the Match Stats table\n\nPlease choose what columns you want to view.\n", "Custom View (Choose Columns)", choices)
        
    elif choice == None:
        start()    
    if column_list == None:
        basic_custom()
    # select names
    print("")
    query = naming_selection(column_list, choice, choices)
    final_query(query, choice)

def start():
    choices = ["Select SQL queries from pre-made views.", "A basic custom view maker. (Parameter Queries)", "An advanced SQL Query input."]
    choice = choicebox("Welcome to Jonathon's Valorant Stats database.\nPlease choose a setting.", title, choices)
    if choice == choices[0]:
        select_view()
    elif choice == choices[1]:
        basic_custom()
    elif choice == choices[2]: 
        headings = ["player_details", "team_stats", "match_stats"]
        columns = [['player_id', 'match_id', 'match_id'], ['username', 'player_id', 'gamemode'], ['level', 'agent', 'map'], ['', 'combat_score', 'team_mvp'], ['', 'kda', 'match_length'], ['', 'kills', 'outcome'], ['', 'deaths', ''], ['', 'assists', ''], ['', 'econ', '']]
        table = tabulate(columns,headings,tablefmt="simple_outline")
        inp = codebox(f"Avalible Tables & Columns:\n{table}\nEnter your SQL query here:", "Custom SQL Query", "SELECT \n\nFROM ")
        sql_input(inp)
    elif choice == None:
        msgbox("Thank you for using Jonathon's Valorant Match Stats GUI")
        quit()
start()