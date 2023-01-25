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

culprit = generateGame()

#Function to select player actions and respond accordingly
def playerTurn(action: int, player, playerList: list):

    #Move to a new room
    if action == 1:
        player.room = player.note.pickRoom()
        print(f"You moved to {player.room}. ")
        if player.room == culprit['room']:
            print(f"You deduced that the murder happened in {player.room}! Added to your notebook.")
        else:
            print(f"You can't find any evidence that the murder happened in {player.room}. Added to your notebook.")
    
    #Interrogate another player to find out if they are the culprit
    elif action == 2:
        suspect = player.note.interrogatePlayer()
        print(f"You decided to interrogate {suspect}.")
        if suspect == culprit['suspect']:
            print(f"You deduced that the culprit was {suspect}! Added to your notebook.")
        else:
            print(f"You decided that {suspect} is innocent. Added to your notebook.")

    #Inspect a weapon to determine if it was used in the murder
    elif action == 3:
        weapon = player.note.inspectWeapon()
        print(f"You decided to inspect the {weapon}.")
        if weapon == culprit['weapon']:
            print(f"You deduced that the weapon used in the murder was the {weapon}! Added to your notebook.")
        else:
            print(f"You decided that the {weapon} was not used in the murder. Added to your notebook.")

    #Check a player's notepad
    elif action == 4:
        print(player.note)

    #Roll to succesfully print out (steal) another player's notepad
    elif action == 5:
        steal = int(input("Which player would you like to pickpocket?"))
        if random.getrandbits(1):
            print(f"You stole a notebook from player {steal}:\n")
            print(playerList[steal-1].note)
        else:
            print(f"You were caught trying to pickpocket player {steal}!")

    #Guess the culprit
    elif action == 6:
        who = input("WHO IS THE CULPRIT?")
        how = input("WHAT WAS THE MURDER WEAPON?")
        where = input("WHERE WAS THE CRIME COMMITTED?")
        guess = {
            'suspect' : who,
            'weapon' : how,
            'room' : where
            }
        if guess == culprit:
            print("You won! The game is now over.")
            return 1
        else: 
            num = 0
            for i in culprit.keys():
                if culprit[i] == guess[i]:
                    num+=1
            print(f"You guessed {num}/3 correct. Guess again.")

    return

#Notepad class, to hold information on suspects for players
class Notepad:
    def __init__(self, sus: list, wea: list, roo: list):
        self.sus = sus
        self.wea = wea
        self.roo = roo
        self.correct = []
        self.wrong = []

    #Randomly select a room, and remove it from the list so rooms cannot be randomly selected twice. Used when players search a room to add it to the notepad
    def pickRoom(self):
        random.shuffle(self.roo)
        if self.roo[-1] == culprit['room']:
            self.correct.append(self.roo[-1])
        else:
            self.wrong.append(self.roo[-1])
        return self.roo.pop()

    #Select a random player, then check if they are the culprit and move them accordingly
    def interrogatePlayer(self):
        random.shuffle(self.sus)
        if self.sus[-1] == culprit['suspect']:
            self.correct.append(self.sus[-1])
        else:
            self.wrong.append(self.sus[-1])
        return self.sus.pop()

    def inspectWeapon(self):
        random.shuffle(self.wea)
        if self.wea[-1] == culprit['weapon']:
            self.correct.append(self.wea[-1])
        else:
            self.wrong.append(self.wea[-1])
        return self.wea.pop()

    def __str__(self):
        return f"""
        CORRECT:
        {self.correct}
        INCORRECT:
        {self.wrong}
        UNKNOWN:
        {self.sus}
        {self.wea}
        {self.roo}
        """

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
        players.append(Player(i, Notepad(suspects, weapons, rooms), "Lobby"))

    #Main loop for each player's turn during the game
    while True:
        for p in players:
            move = int(input(f"""
            Player {p.num + 1}, select an action:
            1 - Move to (and search) a new room
            2 - Interrogate a suspect
            3 - Inspect a weapon
            4 - Check notepad
            5 - Steal a notepad
            6 - Guess the culprit
            """))
            if playerTurn(move, p, players) == 1:
                culprit = generateGame()
                return


#TESTING
if __name__ == '__main__':
    playGame()