
# ============================================================================
# Monopoly, version 2
# ============================================================================

class MonopolyAccount(object):
    """
    The account class models simple bank accounts in a Monopoly game,
    allowing players to give, take, and transfer money to other players.
    """

    # @Class variable
    STARTING_MONEY: int = 500  # the default starting money

    # ========================================================================
    # Constructor
    # ========================================================================

    def __init__(self) -> None:
        """
        Constructor for objects of class Account.
        Initialises the balance to the value of the class variable
        STARTING_MONEY
        """
        super().__init__()
        self._balance: int = MonopolyAccount.STARTING_MONEY

    # ========================================================================
    # @Properties
    # ========================================================================

    @property
    def balance(self) -> int:
        """
        Returns the balance of the receiver
        """

        return self._balance

    @balance.setter
    def balance(self, a_balance: int) -> None:
        """
        Sets the balance of the receiver to the value of the argument
        an_amount.
        """

        self._balance = a_balance

    # ========================================================================
    # Instance methods
    # ========================================================================

    def describe(self) -> None:
        """
        Prints the balance of the receiver.
        """

        print("Account balance: £" + str(self.balance))

    def credit(self, an_amount: float) -> None:
        """
        Credits the receiver with the value of the argument an_amount.
        """

        self.balance += an_amount

    def debit(self, an_amount: float) -> bool:
        """
        If the balance of the receiver is equal to or greater than
        the argument an_amount, the balance of the receiver is
        debited by an_amount, and the method returns true,
        otherwise false is returned.
        """

        if self.balance >= an_amount:
            self.balance -= an_amount
            return True
        else:
            return False
