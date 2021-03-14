
from random import randint


class Account(object):
    """
    A class to model a Monopoly Account.
    """

    # ClassVar
    STARING_BALANCE: int = 500

    def __init__(self) -> None:
        """
        Constructor for objects of class Account.
        Initialises balance to the class variable STARTING_BALANCE.
        """
        super().__init__()
        self.balance: int = Account.STARING_BALANCE

    # ========================================================================
    # Getters and setters
    # ========================================================================

    def get_balance(self) -> int:
        """
        Returns the balance of the receiver.

        @params
        - None

        @returns
        - int
        """

        return self.balance

    def set_balance(self, an_amount: int) -> None:
        """
        Sets the balance of the receiver to the value of the argument
        an_amount.

        @params
        - (int) an_amount

        @returns
        - None
        """

        self.balance = an_amount

    # ========================================================================
    # Instance methods
    # ========================================================================

    def credit(self, an_amount: int) -> None:
        """
        Credits the receiver with the value an_amount.

        @params
        - (int) an_amount

        @returns
        - None
        """

        self.set_balance(self.get_balance() + an_amount)

    def debit(self, an_amount: int) -> bool:
        """
        If the balance of the receiver is greater than or equal to the value
        of an-amount, then debit the receiver by an_amount and return true.
        Otherwise returns false.

        @params
        - (int) an_amount

        @returns
        - bool
        """

        if self.get_balance() >= an_amount:
            self.set_balance(self.get_balance() - an_amount)
            return True
        else:
            return False

    def describe(self) -> None:
        """
        Prints the balance of the receiver.
        """

        print("Account balance: £" + str(self.get_balance()))


class Player(object):
    """
    A class to model a Monopoly Player.
    """

    def __init__(self) -> None:
        """
        Constructor for objects of class Player.
        Initialises name and piece.
        Initialises and assigns a new object of type Account to account.
        """
        super().__init__()
        self.name: str = ""
        self.piece: str = ""
        self.account: Account = Account()

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

        return self.account.get_balance()

    def set_account_balance(self, an_amount: int) -> None:
        """
        Sets the account_balance of the receiver to the value of the argument
        an_amount.

        @params
        - (int) an_amount

        @returns
        - None
        """

        self.account.set_balance(an_amount)

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

    def assign_to(self, a_name: str, a_piece: str) -> None:
        """
        Assigns the receiver to a player.

        @params
        - (str) a_name
        - (str) a_piece

        @returns
        - None
        """

        self.set_name(a_name)
        self.set_piece(a_piece)

    def account_credit(self, an_amount: int) -> bool:
        """
        Credits the receiver's account with the value an_amount.
        See Account.credit() for the description.

        @params
        - (int) an_amount

        @returns
        - None
        """

        self.account.credit(an_amount)

    def account_debit(self, an_amount: int) -> bool:
        """
        Debits the receiver's account by the value an_amount.
        See Account.debit() for the description.

        @params
        - (int) an_amount

        @returns
        - bool
        """

        return self.account.debit(an_amount)

    def account_transfer(self, a_player: object, an_amount: int) -> bool:
        """
        If the receiver's account can be debited for the value an_amount,
        then the receiver's account is debited by an_amount, and a_player
        is credited by an_amount and return true. Otherwise returns false.

        @params
        - (Player) a_player
        - (int) an_amount

        @returns
        - bool
        """

        if self.account_debit(an_amount):
            a_player.account_credit(an_amount)
            return True
        else:
            return False

    def describe(self) -> None:
        """
        Prints the name, piece, and account of the receiver.

        @params
        - None

        @returns
        - None
        """
        print("Player description" +
              "\n==================" +
              "\nName: " + self.get_name() +
              "\nPiece: " + self.get_piece())
        self.account.describe()

    def is_same_player_as(self, a_player: object) -> bool:
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
