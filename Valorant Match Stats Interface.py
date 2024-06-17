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
            print("You chose A: Album Info.\n")
            print_view("[Average Player Stats]")
        elif choice == "B":
            print("You chose B: Basic Info\n")
            print_view("[Average Team Stats]")
        elif choice == "C":
            print("You chose C: First 5 songs from each album\n")
            print_view("[Matches Won]")
        elif choice == "D":
            print("You chose D: Songs over 5 minutes\n")
            print_view("[MVP Details]")
        elif choice == "E":
            print("You chose E: Songs from over 5 years ago (Not Musical)\n")
            print_view("[Player's Best Matches]")
        elif choice == "Z":
            print("Returning to main selection screen.\n")
        else:
            print("That is not a valid decision, please try again\n")

def basic_custom():
    print("You chose B: A basic custom view maker.\n")
    choice = ""
    while choice != "Z":
        choice = input( "\nType the letter for the option you want.\n"
                        "A: Choose what columns to view.\n"
                        "B: Choose a parameter\n"
                        "Z: Back\n\n"
                        "Enter your choice here: ")
        choice = choice.upper()
        if choice == "A":
            print("You chose A: Choose what columns to view.\n")
            column_list = input("The columns:\n"
                                "A: Track Number\n"
                                "B: Track Name\n"
                                "C: Album\n"
                                "D: Artist\n"
                                "E: Release Year\n"
                                "F: Genre\n"
                                "G: Track Length\n"
                                "Enter the columns you want to view (Seperated by a space e.g. 'A B C'): ").split()
            for i in range(len(column_list)):
                column_list[i] = column_list[i].upper()
            print_basic_A(column_list)
        elif choice == "B":
            print("You chose B: Choose a parameter.\n")
            param = input(  "Do you wish to see a certain album or genre?\n"
                            "A: Album\n"
                            "B: Genre\n"
                            "Z: Back\n"
                            "Enter the letter here: ")
            param = param.upper()
            if param == "A":
                print("You chose A: Album.\n")
                album_list = input(  "The Albums:\n"
                        "A: Factorio OST\n"
                        "B: Fallen Kingdom\n"
                        "C: Hamilton OST\n"
                        "D: La La Land OST\n"
                        "E: Oliver! OST\n"
                        "F: Outer Wilds OST\n"
                        "G: Undetale OST\n"
                        "H: justan oval\n"
                        "Enter the album(s) you want to view (Seperated by a space e.g. 'A B C'): ").split()
                for i in range(len(album_list)):
                    album_list[i] = album_list[i].upper()        
                print_basic_B(album_list)
            elif param == "B":
                print("You chose B: Genre.\n")
                genre_list = input(  "The Genres:\n"
                        "A: Entertainment\n"
                        "B: Musical\n"
                        "C: Soundtrack\n"
                        "D: Video Games\n"
                        "Enter the album(s) you want to view (Seperated by a space e.g. 'A B C'): ").split()
                for i in range(len(genre_list)):
                    genre_list[i] = genre_list[i].upper()
                print_basic_C(genre_list)
            elif choice == "Z":
                print("Returning to previous selection screen.\n")
            else:
                print("That is not a valid decision, please try again\n")
        elif choice == "Z":
            print("Returning to main selection screen.\n")
        else:
            print("That is not a valid decision, please try again\n")
def print_basic_A(lst):
    newlist = []
    for i in lst:
        if i == "A":
            newlist.append("album_place")
        elif i == "B":
            newlist.append("name")
        elif i == "C":
            newlist.append("album")
        elif i == "D":
            newlist.append("artist")
        elif i == "E":
            newlist.append("release_year")
        elif i == "F":
            newlist.append("genre")
        elif i == "G":
            newlist.append("track_length")
    select_query = ""
    for i in newlist:
        select_query += i + ", "
    select_query = select_query[:-2]
    
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = f"SELECT {select_query} FROM music;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('music') AS tblInfo"
    cursor.execute(field_names)
    headings = newlist
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()
    cont()
def print_basic_B(lst):
    newlist = []
    for i in lst:
        if i == "A":
            newlist.append("'Factorio OST'")
        elif i == "B":
            newlist.append("'Fallen Kingdom'")
        elif i == "C":
            newlist.append("'Hamilton OST'")
        elif i == "D":
            newlist.append("'La La Land OST'")
        elif i == "E":
            newlist.append("'Oliver! OST'")
        elif i == "F":
            newlist.append("'Outer Wilds OST'")
        elif i == "G":
            newlist.append("'Undetale OST'")
        elif i == "H":
            newlist.append("'justan oval'")
    select_query = ""
    for i in newlist:
        select_query += "album = " + i + " or "
    select_query = select_query[:-3]
    
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = f"SELECT * FROM music WHERE {select_query} order by album"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('music') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()
    cont()
def print_basic_C(lst):
    newlist = []
    for i in lst:
        if i == "A":
            newlist.append("'Entertainment'")
        elif i == "B":
            newlist.append("'Musical'")
        elif i == "C":
            newlist.append("'Soundtrack'")
        elif i == "D":
            newlist.append("'Video Games'")
    select_query = ""
    for i in newlist:
        select_query += "genre = " + i + " or "
    select_query = select_query[:-3]
    
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = f"SELECT * FROM music WHERE {select_query} order by genre"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('music') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()
    cont()

def sql_input():
    print("You chose C: An advanced SQL Query input")
    inp = input("Enter your query here:\n")
    ''' Prints the specified view from the database in a table '''
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
                    "B: A basic custom view maker\n"
                    "C: An advanced SQL Query input\n"
                    "Z: Exit\n\n"
                    "Enter your choice here: ")
    choice = choice.upper()
    if choice == "A":
        select_view()
    elif choice == "B":
        basic_custom()
    elif choice == 'C':
        sql_input()
    elif choice == "Z":
        print("Thank you for using Jonathon's Valorant Stats database. Goodbye.\n")
    else:
        print("That is not a valid decision, please try again\n")