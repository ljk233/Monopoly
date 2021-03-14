
from random import randint


class Player(object):
    """
    A class to model a Monopoly Player.
    """

    def __init__(self) -> None:
        """
        Constructor for objects of class Player.
        Initialises name, piece, account_balance to the default values.
        """
        super().__init__()
        self.name: str = ""
        self.piece: str = ""
        self.account_balance: int = ""

    # ========================================================================
    # Getters and setters
    # ========================================================================

    def get_account_balance(self) -> int:
        """
        Returns the account balance of the receiver.

        @params
        - None

        @returns
        - int
        """

        return self.account_balance

    def set_account_balance(self, an_amount: int) -> None:
        """
        Sets the account_balance of the receiver to the value of the argument
        an_amount.

        @params
        - (int) an_amount

        @returns
        - None
        """

        self.account_balance = an_amount

    def get_name(self) -> str:
        """
        Returns the name of the receiver.

        @params
        - None

        @returns
        - str
        """

        return self.name

    def set_name(self, a_name: str) -> None:
        """
        Sets the name of the receiver to the value of the argument a_name.

        @params
        - (str) a_name

        @returns
        - None
        """

        self.name = a_name

    def get_piece(self) -> str:
        """
        Returns the piece of the receiver.

        @params
        - None

        @returns
        - str
        """

        return self.piece

    def set_piece(self, a_piece: str) -> None:
        """
        Sets the piece of the receiver to the value of the argument a_name.

        @params
        - (str) a_name

        @returns
        - None
        """

        self.piece = a_piece

    # ========================================================================
    # Class methods
    # ========================================================================

    @staticmethod
    def ROLL_DICE() -> None:
        """
        Simulates a player rolling the dice.
        Prints the sum of the dice roll.

        @params
        - None

        @returns
        - None
        """

        d1: int = randint(1, 6)
        d2: int = randint(1, 6)
        print("You rolled " + str(d1) + " + " + str(d2) + " = " + str(d1 + d2))

    # ========================================================================
    # Instance methods
    # ========================================================================

    def assign_to(self, a_name: str, a_piece: str, an_amount: int) -> None:
        """
        Assigns the receiver to a player

        @params
        - (str) a_name
        - (str) a_piece
        - (int) an_amount

        @returns
        - None
        """

        self.set_name(a_name)
        self.set_piece(a_piece)
        self.set_account_balance(an_amount)

    def describe(self) -> None:
        """
        Prints the name, piece, and account of the receiver.
        """
        print("Player description" +
              "\n==================" +
              "\nName: " + self.get_name() +
              "\nPiece: " + self.get_piece() +
              "\nAccount balance: £" + str(self.get_account_balance()))

    def is_same_player_as(self, a_player) -> bool:
        """
        Returns true if the receiver is equivalent to (has the same state as)
        the argument a_player, otherwise false is returned

        @params
        - (Player) a_player

        @returns
        - bool
        """

        same_name: bool = self.get_name() == a_player.get_name()
        same_piece: bool = self.get_piece() == a_player.get_piece()
        same_account: bool = (self.get_account_balance() ==
                              a_player.get_account_balance())

        return same_name and same_piece and same_account
