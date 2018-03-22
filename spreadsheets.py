import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

# initializing a connection to the google sheet
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(credentials)
sheet = client.open('Chessgames overview Groningen').worksheet("Gamelist")
sheet2 = client.open('Chessgames overview Groningen').worksheet("Scorelist")
pp = pprint.PrettyPrinter()

# --------Some practice commands----------
chess = sheet.get_all_records()
scorelist = sheet2.get_all_records()
# pp.pprint(chess)
# pp.pprint(scorelistlist)
# print(scorelist)

# uniquePlayers =
# pp.pprint(players)


def getplayers():
    players = sheet.col_values(2) + sheet.col_values(3)
    playerList = []

    for p in players:
        if p != "Name1" and p !="Name2":
            playerList.append(p)

    uniquePlayers = list(sorted(set(playerList)))
    print(uniquePlayers)
    return uniquePlayers


def insertrow(sheetNumber):
    row = ["", 0, 0]
    index = sheetNumber.row_count + 1
    sheet.insert_row(row,index)


def addgame(name1, name2, result):
    import datetime
    date = str(datetime.datetime.today())
    row = [date, name1, name2, result]
    sheet.insert_row(row, sheet.row_count)
# addGame("Ieremias Athanasiadis", "Martin Platje", "win")


def createplayers():
    players = getplayers()
    playerDict = {'Name': '', 'Score': 0, 'Total games': 0}

    counter = 2
    for p in players:
        sheet2.update_cell(counter, 1, p)  # Name
        sheet2.update_cell(counter, 2, 0)  # scorelist
        sheet2.update_cell(counter, 3, 0)  # Total games
        counter += 1
    print(sheet2.get_all_records())
    return playerDict


def addpoint(name, result1, result2):
    cell = sheet2.find(name)
    score = int(sheet2.cell(cell.row, cell.col+1).value) + result1
    totalgames = int(sheet2.cell(cell.row, cell.col+2).value) + result2

    sheet2.update_cell(cell.row, cell.col+1, score)  # add to Score
    sheet2.update_cell(cell.row, cell.col+2, totalgames)  # add to Total games


def countgames():
    name1 = sheet.col_values(2)
    name2 = sheet.col_values(3)
    result = sheet.col_values(4)
    for n in range(1,len(name1)):
        if result[n] == "win":
            addpoint(name1[n], 1, 1)
            addpoint(name2[n], -1, 1)
            print(name1[n] + " has won the game")

        elif result[n] == "lose":
            addpoint(name1[n], -1, 1)
            addpoint(name2[n], 1, 1)
            print(name1[n] + " has lost the game")

        elif result[n] == "draw":
            addpoint(name1[n], 0, 1)
            addpoint(name2[n], 0, 1)
            print(name1[n] + " and " + name2[n] + " played stalemate")

        else:
            print("This is not a valid game result. Please input win/lose/draw")


def reloadscorelist():
    createplayers()
    countgames()

reloadscorelist()