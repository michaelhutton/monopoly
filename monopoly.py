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
    "Jail",
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
chance_cards = [
    "Advance to Go",
    "Advance to Illinois Ave.",
    "Advance to St. Charles Place",
    "Advance token to nearest Utility",
    "Advance token to the nearest Railroad",
    "Bank pays you dividend of $50",
    "Get out of Jail Free Card",
    "Go Back 3 Spaces",
    "Go to Jail",
    "Make general repairs on all your property",
    "Pay poor tax of $15",
    "Take a trip to Reading Railroad",
    "Take a walk on the Boardwalk",
    "You have been elected Chairman of the Board",
    "Your building loan matures - Collect $150"
]
community_chest_cards = [
    "Advance to Go",
    "Bank error in your favor - Collect $200",
    "Doctor's fees - Pay $50",
    "From sale of stock you get $50",
    "Get Out of Jail Free Card",
    "Go to Jail",
    "Grand Opera Night - Collect $50 from every player for opening night seats",
    "Holiday Fund matures - Receive $100",
    "Income tax refund - Collect $20",
    "Life insurance matures - Collect $100",
    "Pay hospital fees of $100",
    "Pay school fees of $150",
    "Receive $25 consultancy fee",
    "You are assessed for street repairs - $40 per house - $115 per hotel",
    "You have won second prize in a beauty contest - Collect $10",
    "You inherit $100"
]

def roll_dice():
    return [random.randint(1,6),random.randint(1,6)]

def pick_card(player, deck):
    # Take a random card from either the chance or cc deck
    # and return players new position
    last_card = len(deck)-1
    choice = random.randint(0,last_card)
    card = deck[choice]
    print("Started at: " + str(player["pos"]))
    if(card == "Advance to Go"):
        player["pos"] = 0
    elif(card == "Advance to Illinois Ave."):
        player["pos"] = 24
    elif(card == "Advance to St. Charles Place"):
        player["pos"] = 11
    elif(card == "Advance token to nearest Utility"):
        if(player["pos"] == 7):
            player["pos"] = 12 # Electric Company
        else: # Pos 22 and 36 go to the same place
            player["pos"] = 28 # Water Works
    elif(card == "Advance token to the nearest Railroad"):
        if(player["pos"] == 7):
            player["pos"] = 5 # Reading
        elif(player["pos"] == 22):
            player["pos"] = 25 # B and O
        elif(player["pos"] == 36):
            player["pos"] = 35 # Short Line
    elif(card == "Go Back 3 Spaces"):
        player["pos"] = player["pos"] - 3
    elif(card == "Go to Jail"):
        player["pos"] = 10
        player["in_jail"] = True
    elif(card == "Take a trip to Reading Railroad"):
        player["pos"] = 5
    elif(card == "Take a walk on the Boardwalk"):
        player["pos"] = 39
    print("Received card: " + card)
    print("Ended at: " + str(player["pos"]))
    return player

player1 = {
    "pos": 0,
    "doubles_in_a_row": 0,
    "in_jail": False
}

for turn in range(1,100):
    dice = roll_dice()
    print(dice)
    if(dice[0] == dice[1]):
        player1["doubles_in_a_row"] = player1["doubles_in_a_row"] + 1
    else:
        player1["doubles_in_a_row"] = 0
    # TODO: if the player has rolled 3 doubles, go to jail!
    player1["pos"] = (player1["pos"] + dice[0] + dice[1]) % SQUARES_LENGTH
    # TODO: Check if its a go to jail space

    if(squares[player1["pos"]] == "Chance"):
        print("chance!")
        print(player1)
        pick_card(player1, chance_cards)
        print(player1)
    if(squares[player1["pos"]] == "Community Chest"):
        print("CC!")
        pick_card(player1, community_chest_cards)

    print("Turn " + str(turn) + ": " + squares[player1["pos"]])
