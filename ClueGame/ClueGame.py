import random

#Define goals for player to uncover
suspects = [
    'Prof. Plum',
    'Col. Mustard',
    'Ms. Scarlett',
    'Mrs. White',
    'Rev. Green',
    'Mrs. Peacock'
    ]

weapons = [
    'Pewter',
    'Rope',
    'Candlestick',
    'Revolver',
    'Lead Pipe',
    'Wrench'
    ]

rooms = [
    'Hall',
    'Lounge',
    'Dining Room',
    'Kitchen',
    'Ballroom',
    'Conservatory',
    'Billiard Room',
    'Library',
    'Study'
    ]

#Randomize who, how, where so each game is different. Lists remain unaltered to pass through into player and notepad classes
def generateGame():
    random.shuffle(suspects)
    random.shuffle(weapons)
    random.shuffle(rooms)
    whodunnit = {
        'suspect': suspects[-1],
        'weapon': weapons[-1],
        'room': rooms[-1]
        }
    
    return whodunnit

#Function to select player actions and respond accordingly
def playerTurn(action: int, player: Player):
    if action == 1:
        player.room = player.note.pickRoom
    return

#Notepad class, to hold information on suspects for players
class Notepad:
    def __init__(self, sus: list, wea: list, roo: list):
        self.sus = sus
        self.wea = wea
        self.roo = roo

    #Randomly select a room, and remove it from the list so rooms cannot be randomly selected twice. Used when players search a room to add it to the notepad
    def pickRoom():
        random.shuffle(self.roo)
        return self.roo.pop()

#Player class, holds info on notepad, name, past actions
class Player:
    def __init__(self, num: int, note: Notepad, room: str):
        self.num = num
        self.note = note
        self.room = room

    def __str__(self):
        return f"Player {self.num}"

#Main function to play the game
def playGame():
    culprit = generateGame()

    start = int(input("""
    Welcome to CLUE! Options:
    1 - Start new game
    2 - Exit
    """))

    if start == 2:
        return
    elif start != 1:
        print("Please enter either 1 or 2.")
        return

    pnum = int(input("""
    How many players will be in this game? (must be 5 or less)
    """))

    players = []

    for i in range(pnum):
        players.append(Player(i, Notepad(), "Lobby"))

    #Main loop for each player's turn during the game
    while True:
        for p in players:
            move = input(f"""
            Player {p.num}, select an action:
            1 - Move to (and search) a new room
            2 - Interrogate
            3 - Check notepad
            4 - Steal a notepad
            5 - Guess the culprit
            """)






#TESTING
if __name__ == '__main__':
    playGame()