
class Account(object):
    """
    A class to model a Monopoly Player.
    """

    STARING_BALANCE: int = 500  # class variable

    def __init__(self) -> None:
        """
        Constructor for objects of class Player.
        Initialises balance to the class variable STARTING_BALANCE
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
        Sets the account_balance of the receiver to the value of the argument
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
