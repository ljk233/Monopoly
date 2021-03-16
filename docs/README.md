# Monopoly

## Dependencies

`from __future__ import annotations`
: Allows type hinting for classes defined further on in the module.

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

### Instance methods

`__eq__(self, p: Player) -> bool`
: @Overrides.
Returns true if the receiver is has the same state as the argument p, otherwise false is returned.

`__repr__(self) -> str`
: @Overrides.
Returns a succinct representation of the receiver as a string.

`__str__(self) -> str`
: @Overrides.
Returns a verbose description of the receiver as a string.

`assign(a_name : str, a_piece : str, an_amount: int) -> None`
: Assigns a player to the receiver.
Sets name to a_name, piece to a_piece, and account_balance to an-amount.
