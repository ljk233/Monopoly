
# ============================================================================
# Monopoly, version 2
# ============================================================================

class Account(object):
    """
    The account class models simple bank accounts in a Monopoly game,
    allowing players to credit and debit money.
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
        self._balance: int = Account.STARTING_MONEY

    # ========================================================================
    # Getters and setters
    # ========================================================================

    def get_balance(self) -> int:
        """
        Returns the balance of the receiver

        @returns, int
        """

        return self._balance

    def set_balance(self, a_balance: int) -> None:
        """
        Sets the balance of the receiver to the value of the argument
        a_balance

        @param, a_balance, int
        @returns, None
        """

        self._balance = a_balance

    # ========================================================================
    # Instance methods
    # ========================================================================

    def describe(self) -> None:
        """
        Prints the balance of the receiver.

        @returns, None
        """

        print("Account balance: £" + str(self.get_balance()))

    def credit(self, an_amount: int) -> None:
        """
        Credits the receiver with the value of the argument an_amount.

        @param, an_ammount
        @returns, None
        """

        new_balance: int = self.get_balance() + an_amount

        self.set_balance(new_balance)

    def debit(self, an_amount: int) -> bool:
        """
        If the balance of the receiver is equal to or greater than
        the argument an_amount, the balance of the receiver is
        debited by an_amount, and the method returns true,
        otherwise false is returned.

        @params, an_amount, int
        @returns, bool
        """

        if self.get_balance() >= an_amount:
            self.set_balance(self.get_balance() - an_amount)
            return True
        else:
            return False
