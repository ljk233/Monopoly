
from __future__ import annotations
# from typing import TypeVar


class Player:

    def __init__(self) -> None:
        """
        Constructor for objects of class Player.
        Initialises name, piece, account_balance to the default values.
        """
        super().__init__()
        self._name: str = ""
        self._piece: str = ""
        self._account_balance: int = 0

    # ========================================================================
    # @Properties
    # ========================================================================

    @property
    def account_balance(self) -> int:
        return self._account_balance

    @account_balance.setter
    def account_balance(self, an_amount: int) -> None:
        self._account_balance = an_amount

    @property
    def name(self) -> str:

        return self._name

    @name.setter
    def name(self, a_name: str) -> None:
        self._name = a_name

    @property
    def piece(self) -> str:
        return self._piece

    @piece.setter
    def piece(self, a_piece: str) -> None:
        self._piece = a_piece

    # ========================================================================
    # Class methods
    # ========================================================================

    # No class methods

    # ========================================================================
    # Instance methods
    # ========================================================================

    def __eq__(self, p: Player) -> bool:
        """
        @Overrides.
        Returns true if the receiver is has the same state as
        the argument p, otherwise false is returned

        :param p (Player) A Player object

        :returns bool
        """

        same_name: bool = self.name == p.name
        same_piece: bool = self.piece == p.piece
        same_account: bool = self.account_balance == p.account_balance

        return same_name and same_piece and same_account

    def __repr__(self) -> str:
        """
        @Override.
        Returns a succinct representation of the object as a string.
        """
        return ("Monopoly.Player(\"" + self.name +
                "\", \"" + self.piece +
                "\", " + str(self.account_balance)
                + ")")

    def __str__(self) -> str:
        """
        @Override
        Returns a verbose description of the receiver as a string.

        :param None

        :return str
        """

        return (self.name + " is playing as the " + self.piece +
                " with an account balance of £" +
                str(self.account_balance))

    def assign(self, a_name: str, a_piece: str, an_amount: int) -> None:
        """
        Assigns the receiver to a player.
        Sets name to a_name, piece to a_piece, and account_balance to
        an-amount.

        :param a_name (str) The Player's name
        :param a_piece (str) The Player's piece
        :param an_amount (int) The Player's account balance

        :returns None
        """

        self.name = a_name
        self.account_balance = an_amount
        self.piece = a_piece
