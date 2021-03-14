
# ============================================================================
# Actions
# - Refactor
#    - _account to Account class
#    - Constructor
# - Refactor get and set account balance
# - Add methods
#    - credit
#    - debit
#    - transfer
# ============================================================================


from random import randint
from .Account import Account


class Player(object):
    """
    A class to model a Monopoly Player.
    """

    def __init__(self) -> None:
        """
        Constructor for objects of class Player.
        Initialises the name, piece, and account balance of the object
        to the default values.
        """
        super().__init__()
        self._name: str = ""
        self._piece: str = ""
        self._account: Account = Account()  # init new Account object

    # ========================================================================
    # Getters and setters
    # ========================================================================

    def get_account_balance(self) -> int:
        """
        Returns the account balance of the receiver.

        @returns, int
        """

        return self._account.get_balance()

    def set_account_balance(self, an_amount: int) -> None:
        """
        Sets the account_balance of the receiver to the value of the argument
        an_amount.

        @param, a_piece, str
        """

        self._account.set_balance(an_amount)

    def get_name(self) -> str:
        """
        Returns the name of the receiver

        @returns, str
        """

        return self._name

    def set_name(self, a_name: str) -> None:
        """
        Sets the name of the receiver to the value of the argument a_name.

        @param, a_name, str
        """

        self._name = a_name

    def get_piece(self) -> str:
        """
        Returns the piece of the receiver

        @returns, str
        """

        return self._piece

    def set_piece(self, a_piece: str) -> None:
        """
        Sets the piece of the receiver to the value of the argument a_name.

        @param, a_piece, str
        """

        self._piece = a_piece

    # ========================================================================
    # Class methods
    # ========================================================================

    @staticmethod
    def ROLL_DICE() -> None:
        """
        Simulates a player rolling the dice. Prints the sum of the dice roll.

        @returns, None
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

        @params
        - a_name, str
        - a_piece, str

        @returns, None
        """

        self.set_name(a_name)
        self.set_piece(a_piece)

    def credit(self, an_amount: int) -> None:
        """
        Credits the receiver with the value of the argument an_amount.

        @param, an_ammount, int
        @returns, None
        """

        self._account.credit(an_amount)

    def debit(self, an_amount: int) -> bool:
        """
        If the balance of the receiver is equal to or greater than
        the argument an_amount, the balance of the receiver is
        debited by an_amount, and the method returns true,
        otherwise false is returned.

        @param, an_ammount, int
        @returns, bool
        """

        return self._account.debit(an_amount)

    def describe(self) -> None:
        """
        Prints the name, piece, and account of the receiver.
        """
        print("Player description" +
              "\n==================" +
              "\nName: " + self.get_name() +
              "\nPiece: " + self.get_piece())
        self._account.describe()

    def is_same_player_as(self, a_player) -> bool:
        """
        Returns true if the receiver is equivalent to (has the same state as)
        the argument a_player, otherwise false is returned.

        @param, Player

        @returns, bool
        """

        same_name: bool = self.get_name() == a_player.get_name()
        same_piece: bool = self.get_piece() == a_player.get_piece()
        same_account: bool = (self.get_account_balance() ==
                              a_player.get_account_balance())

        return same_name and same_piece and same_account

    def transfer(self, a_player: object, an_amount: int) -> bool:
        """
        If the balance of the receiver's account is equal to or greater
        than the argument an_amount, the balance of the receiver's account
        is debited by an_amount.

        The argument a_player is then credited by an_amount and the method
        returns true, otherwise false is returned.

        @params
        - a_player, Player
        - an_amount, int

        @returns, bool
        """

        if self.debit(an_amount):
            a_player.credit(an_amount)
            return True
        else:
            return False
