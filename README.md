# Monopoly

## Player

A class to model a Monopoly player.

### Constructor

`__init__()`
: Constructor for objects of class Player.
Initialises name, piece, account_balance to the default values.

### Instance variables

- (int) **account_balance**
- (str) **name**
- (str) **piece**

### Class methods

`ROLL_DIE() -> None`
: Simulates a player rolling the dice.
Prints the sum of the dice roll.

### Instance methods

`assign_to(a_name : str, a_piece : str, an_amount: int) -> None`
: Assigns a player to the receiver.

`describe() -> None`.
: Prints the name, piece, and account_balance of the receiver.

`get_account_balance() -> int`.
: Returns the account_balance of the receiver.

`get_name() -> str`.
: Returns the name of the receiver.

`get_piece() -> str`.
: Returns the piece of the receiver.

`is_same_player_as(a_player: Player) -> bool`.
: Returns true if the receiver is equivalent to (has the same state as) the argument a_player, otherwise false is returned.

`set_account_balance(an_amount: int) -> None`.
: Sets the account balance of the receiver to the value of the argument an_amount.

`set_name(a_name: str) -> None`.
: Sets the name of the receiver to the value of the argument a_name.

`set_piece(a_piece) -> None`
: Sets the piece of the receiver to the value of the argument a_piece.
