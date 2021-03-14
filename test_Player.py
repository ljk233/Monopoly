
# Testing MonopolyPlayer

# import the module
from Monopoly import Player

# ============================================================================
# Declare and initialise Player 1 and Player 2
# ============================================================================

p1: Player = Player()
p2: Player = Player()

# ============================================================================
# Set the properties
# ============================================================================

p1.set_account_balance(500)
p1.set_name("Player 1")
p1.set_piece("Dog")
p2.assign_to("Player 2", "Duck", 500)

# ============================================================================
# TEST: get attributes, check value
# ============================================================================

assert p1.get_account_balance() == 500
assert p1.get_name() == "Player 1"
assert p1.get_piece() == "Dog"

assert p2.get_account_balance() == 500
assert p2.get_name() == "Player 2"
assert p2.get_piece() == "Duck"

# ============================================================================
# TEST: p1 is equal to p1, p1 is not equal to p2
# ============================================================================

assert p1.is_same_player_as(p1) is True
assert p1.is_same_player_as(p2) is False
