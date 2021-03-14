
# ============================================================================
# Monopoly, version 2
# - Updated constructor (account)
# - Add getter and setter for account balance (account)
# - Added methods to support account component objects
#    - give_money()
#    - take_money()
#    - transfer_money()
# - updated describe() for new account component object
# ============================================================================

from Monopoly_v2.MonopolyAccount import MonopolyAccount
from random import randint


class MonopolyPlayer(object):
    """
    A class to model a MonopolyPlayer.
    """

    # ========================================================================
    # Constructor
    # ========================================================================

    def __init__(self) -> None:
        """
        Constructor for objects of class MonopolyPlayer.
        Initialises the name and piece to the default values.
        Assigns account to a new initialised object of class MonopolyAccount.
        """
        super().__init__()
        self._name: str = ""
        self._piece: str = ""
        self._account: object = MonopolyAccount()

    # ========================================================================
    # @Properties
    # ========================================================================

    @property
    def name(self) -> str:
        """
        Returns the name of the receiver
        """

        return self._name

    @name.setter
    def name(self, a_name: str) -> None:
        """
        Sets the name of the receiver to the value of the argument a_name.
        """

        self._name = a_name

    @property
    def piece(self) -> str:
        """
        Returns the name of the receiver
        """

        return self._piece

    @piece.setter
    def piece(self, a_piece: str) -> None:
        """
        Sets the name of the receiver to the value of the argument a_name.
        """

        self._piece = a_piece

    @property
    def account_balance(self) -> int:
        """
        Returns the account balance of the receiver
        """

        return self._account.balance

    @account_balance.setter
    def account_balance(self) -> None:
        """
        Method removed. Now handled through MonopolyAccount class.
        """

        pass

    # ========================================================================
    # Class methods
    # ========================================================================

    @staticmethod
    def ROLL_DICE() -> None:
        """
        Simulates a player rolling the dice. Prints the sum of the dice roll.
        """

        d1: int = randint(1, 6)
        d2: int = randint(1, 6)
        d_total = d1 + d2

        print("You rolled " + str(d1) + " + " + str(d2) + " = " + str(d_total))

    # ========================================================================
    # Instance methods
    # ========================================================================

    def assign_to(self, a_name: str, a_piece: str) -> None:
        """
        Assigns the receiver to a player.
        Sets the name of the receiver to the value of the argument a_name.
        Sets the piece of the receiver to the value of the argument a_piece.
        Sets the account of the receiver to the value of the argument
        an_account.
        """

        self.name = a_name
        self.piece = a_piece

    def credit_account(self, an_amount: int) -> None:
        """
        Credits the receiver's account with the value of the argument
        an_amount.
        """

        return self._account.credit(an_amount)

    def debit_account(self, an_amount: int) -> bool:
        """
        If the balance of the receiver's account is equal to or greater
        than the argument an_amount, the balance of the receiver's account
        is debited by an_amount, and the method returns true, otherwise
        false is returned.
        """

        return self._account.debit(an_amount)

    def describe(self) -> None:
        """
        Prints the name, piece, and account of the receiver.
        """
        print("\nName: " + self.name +
              "\nPiece: " + self.piece)
        self._account.describe()

    def is_same_player_as(self, a_player) -> bool:
        """
        Returns true if the receiver is equivalent to (has the same state as)
        the argument a_player, otherwise false is returned.
        """

        same_name: bool = self.name == a_player.name
        same_piece: bool = self.piece == a_player.piece
        same_account: bool = self.account_balance == a_player.account_balance

        return same_name and same_piece and same_account

    def transfer_money(self, to_player: object, an_amount: int) -> bool:
        """
        If the balance of the receiver's account is equal to or greater
        than the argument an_amount, the balance of the receiver's account
        is debited by an_amount.

        The argument a_player is then credited by an_amount and the method
        returns true, otherwise false is returned.
        """

        if self.debit_account(an_amount):
            to_player.credit_account(an_amount)
            return True
        else:
            return False
