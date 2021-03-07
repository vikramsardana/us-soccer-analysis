import pandas as pd
import numpy as np
from builtins import str
from _ast import Str
from statsbombpy import sb

def getInput(text):
    return str(input(text))

def getMatchEvents(id, team):
    events = sb.events(match_id=id)
    usa = "United States Women's"
    opponent = team + " Women's"
    usaEvents = events.loc[(events['possession_team'] == usa)]
    opponentEvents = events.loc[(events['possession_team'] == opponent)]
    while True:
        print(" ")        
        print("*************")
        print(" ")
        toLook = getInput("What do you want to look at?\nChoices are 'total events', 'pass outcomes', 'pass type', 'positions', 'counterpress', 'under pressure', or 'done'.\n")   
        if toLook.upper() == "DONE":
            return
        elif toLook.upper() == "TOTAL EVENTS":
            print(usa + " total event count: " + str(sum(usaEvents['position'].value_counts())))
            print(opponent + " total event count: " + str(sum(opponentEvents['position'].value_counts())))
        elif toLook.upper() == "PASS OUTCOMES":
            print(usa + " Pass Outcomes\n")
            print(usaEvents['pass_outcome'].value_counts())
            print("total: " + str(sum(usaEvents['pass_outcome'].value_counts())))
            print(opponent + " Pass Outcomes\n")
            print(opponentEvents['pass_outcome'].value_counts())
            print("total: " + str(sum(opponentEvents['pass_outcome'].value_counts())))            
        elif toLook.upper() == "PASS TYPE":
            print(usa + " Pass Types\n")
            print(usaEvents['pass_type'].value_counts())
            print(opponent + " Pass Types\n")
            print(opponentEvents['pass_type'].value_counts())
        elif toLook.upper() == "POSITIONS":
            print(usa + " Position Frequencies\n")
            print(usaEvents['position'].value_counts())
            print(opponent + " Position Frequencies\n")
            print(opponentEvents['position'].value_counts())
            
        elif toLook.upper() == "COUNTERPRESS":
            print(usa + " Counterpress\n")
            print(usaEvents['counterpress'].value_counts())
            print(opponent + " Counterpress\n")
            print(opponentEvents['counterpress'].value_counts())
        elif toLook.upper() == "UNDER PRESSURE":
            print(usa + " Under Pressure\n")
            print(usaEvents['under_pressure'].value_counts())
            print(opponent + " Under Pressure\n")
            print(opponentEvents['under_pressure'].value_counts())
            
            
if __name__ == '__main__':
    while True:
        print(" ")
        print("===============================")
        print(" ")
        command = getInput("Which game do you want to look at?\nChoices (opponents) are Thailand, Chile, Sweden, Spain, France, England, or Netherlands, or exit/quit.\n")   
        if command.upper() == "QUIT" or command.upper() == "EXIT":
            print("OK! Thank you for exploring!")
            break     
        elif command.upper() == "THAILAND":
            getMatchEvents(22943, "Thailand")
        elif command.upper() == "CHILE":
            getMatchEvents(22974, "Chile")
        elif command.upper() == "SWEDEN":
            getMatchEvents(68345, "Sweden")
        elif command.upper() == "SPAIN":
            getMatchEvents(69161, "Spain")
        elif command.upper() == "FRANCE":
            getMatchEvents(69202, "France")
        elif command.upper() == "ENGLAND":
            getMatchEvents(69258, "England")
        elif command.upper() == "NETHERLANDS":
            getMatchEvents(69321, "Netherlands")
        else:
            print("Sorry, that's not a valid command")