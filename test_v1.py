
# Testing MonopolyPlayer

# import the module
from Monopoly_v1.MonopolyPlayer import MonopolyPlayer

# declare and initialise Player 1
p1: MonopolyPlayer = MonopolyPlayer()

# Set the properties
p1.name = "Liam Kelly"
p1.piece = "Dog"
p1.account = 500

# Check the setters by describing the player
p1.describe()

# roll dice
MonopolyPlayer.ROLL_DICE()

# declare and initialise Player 2
p2: MonopolyPlayer = MonopolyPlayer()

# Set the properties by invoking setup_player()
p2.assign_to("George Holdsworth", "Car", 500)
p2.describe()

# test is p1 and p2 are same players. Expected, false
p1.is_same_player_as(p2)

# test if p1 and p1 are same players. Expected, true
p1.is_same_player_as(p1)
