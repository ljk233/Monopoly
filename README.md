# Monopoly

Release highlights

- Addition of the `Account` class
- Refactoring of `Player` class to use `Account`

## Account

A class to model a Monopoly Account.

### Constructor

`__init__()`
: Constructor for objects of class Account.
Initialises balance to the class variable STARTING_BALANCE.

### Class variable

- `(int)` STARING_BALANCE

### Instance variables

- `(int)` balance

### Instance methods

`credit(an_amount: int) -> None`
: Credits the receiver with the value an_amount.

`debit(an_amount: int) -> bool`
: Credits the receiver with the value an_amount.

`describe() -> None`.
: Prints the balance of the receiver.

`get_balance() -> int`.
: Returns the balance of the receiver.

`set_balance(an_amount: int) -> None`.
: Sets the balance of the receiver to the value of the argument an_amount.

## Player

A class to model a Monopoly player.

### Constructor

`__init__()`
: Constructor for objects of class Player.
Initialises name and piece.
Initialises and assigns a new object of type Account to account.

### Instance variables

- `(Account)` account_balance
- `(str)` name
- `(str)` piece

### Class methods

`ROLL_DIE() -> None`
: Simulates a player rolling the dice.
Prints the sum of the dice roll.

### Instance methods

`account_credit(an_amount: int) -> bool`
: Credits the receiver's account with the value an_amount.
See `Account.credit()` for the description.

`account_debit(an_amount: int) -> bool`
: Debits the receiver's account by the value an_amount.
See `Account.debit()` for the description.

`account_transfer(self, a_player: Player, an_amount: int) -> bool`
: If the receiver's account can be debited for the value an_amount,
then the receiver's account is debited by an_amount, and a_player
is credited by an_amount and return true.
Otherwise returns false.

`assign_to(a_name : str, a_piece : str) -> None`
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
