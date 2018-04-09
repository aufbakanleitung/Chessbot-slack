import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
from tabulate import tabulate

# initializing a connection to the google sheet
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(credentials)
sheet = client.open('Chessgames overview Groningen').worksheet("Gamelist")
sheet2 = client.open('Chessgames overview Groningen').worksheet("Scorelist")

pp = pprint.PrettyPrinter()
# --------Some practice commands----------
chess = sheet.get_all_records()
# pp.pprint(chess)
# pp.pprint(scorelistlist)
# print(scorelist)

# uniquePlayers =
# pp.pprint(players)


score_list = sheet2.get_all_records()


def get_players():
    players = sheet.col_values(2) + sheet.col_values(3)
    player_list = []

    for p in players:
        if p != "Name1" and p !="Name2":
            player_list.append(p)

    unique_players = list(sorted(set(player_list)))
    print(unique_players)
    return unique_players


def insert_row(sheetNumber):
    row = ["", 0, 0]
    index = sheetNumber.row_count + 1
    sheet.insert_row(row,index)


def create_players():
    players = get_players()
    player_dict = {'Name': '', 'Score': 0, 'Total games': 0}

    counter = 1
    for p in players:
        sheet2.update_cell(counter, 1, p)  # Name
        sheet2.update_cell(counter, 2, 0)  # scorelist
        sheet2.update_cell(counter, 3, 0)  # Total games
        counter += 1
    print(sheet2.get_all_records())
    return player_dict


def add_point(name, result1, result2):
    try:
        cell = sheet2.find(name)
        score = int(sheet2.cell(cell.row, cell.col + 1).value) + result1
        total_games = int(sheet2.cell(cell.row, cell.col + 2).value) + result2

        sheet2.update_cell(cell.row, cell.col + 1, score)  # add to Score
        sheet2.update_cell(cell.row, cell.col + 2, total_games)  # add to Total games
    except gspread.exceptions.CellNotFound:
        reload_scorelist()


def add_to_gamelist(name1, name2, result):
    import datetime
    date = str(datetime.date.today())
    row = [date, name1, name2, result]
    sheet.insert_row(row, sheet.row_count)


def add_to_scorelist(name1, name2, result):
    if result == "win":
        add_point(name1, 1, 1)
        add_point(name2, -1, 1)
        print(name1 + " has won the game")
    elif result == "lose":
        add_point(name1, -1, 1)
        add_point(name2, 1, 1)
        print(name1 + " has lost the game")
    elif result == "draw":
        add_point(name1, 0, 1)
        add_point(name2, 0, 1)
        print(name1 + " and " + name2 + " played stalemate")
    else:
        print("This is not a valid game result. Please input win/lose/draw")


def add_game(name1, name2, result):
    add_to_gamelist(name1, name2, result)
    add_to_scorelist(name1, name2, result)
    return "This chessgame is added to the databases:\n Challenger: " + name1 + "\n Challengee: " + name2 + "\n Result: " + result + " for the challenger"

# add_game("Herman van der Veer", "Ieremias Athanasiadis", "lose")


def count_games():
    name1 = sheet.col_values(2)
    name2 = sheet.col_values(3)
    result = sheet.col_values(4)
    for n in range(1,len(name1)):
        add_to_scorelist(name1[n], name2[n], result[n])


def reload_scorelist():
    create_players()
    count_games()


def print_gamelist():
    (name1, name2, result) = sheet.col_values(2), sheet.col_values(3), sheet.col_values(4)
    gamelist = tabulate({"Challenger": name1[1:], "Challengee": name2[1:], "Result": result[1:]}, headers="keys")
    print("Gamelist requested")
    return gamelist


def print_scorelist():
    (name, wins, total_games) = sheet2.col_values(1), sheet2.col_values(2), sheet2.col_values(3)
    scorelist = tabulate({"Name": name[1:], "Score": wins[1:], "Total games": total_games[1:]}, headers="keys")
    print("scorelist requested")
    return scorelist
