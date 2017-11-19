import random

squares = [
    "Go",
    "Mediterranean Ave.",
    "Community Chest",
    "Baltic Ave.",
    "Income Tax",
    "Reading Railroad",
    "Oriental Ave.",
    "Chance",
    "Vermont Ave.",
    "Connecticut Ave.",
    "Jail - Just Visiting",
    "St. Charles Place",
    "Electric Company",
    "States Ave.",
    "Virginia Ave.",
    "Pennsylvania Railroad",
    "St. James Place",
    "Community Chest",
    "Tennessee Ave.",
    "New York Ave.",
    "Free Parking",
    "Kentucky Ave.",
    "Chance",
    "Indiana Ave.",
    "Illinois Ave.",
    "B. & O. Railroad",
    "Atlantic Ave.",
    "Ventnor Ave.",
    "Water Works",
    "Marvin Gardens",
    "Go To Jail",
    "Pacific Ave.",
    "North Carolina Ave.",
    "Community Chest",
    "Pennsylvania Ave.",
    "Short Line Railroad",
    "Chance",
    "Park Place",
    "Luxury Tax",
    "Boardwalk"
    ]
SQUARES_LENGTH = len(squares)
chance_cards = []
community_chest_cards = []

def roll_dice():
    return [random.randint(1,6),random.randint(1,6)]

player1 = {
    'pos': 0,
    'doubles_in_a_row': 0
}

for turn in range(1,100):
    dice = roll_dice()
    print(dice)
    if(dice[0] == dice[1]):
        player1['doubles_in_a_row'] = player1['doubles_in_a_row'] + 1
    else:
        player1['doubles_in_a_row'] = 0
    # TODO: if the player has rolled 3 doubles, go to jail!
    player1["pos"] = (player1["pos"] + dice[0] + dice[1]) % SQUARES_LENGTH

    print("Turn " + str(turn) + ": " + squares[player1['pos']])
