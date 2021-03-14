
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

from .MonopolyAccount import MonopolyAccount
from .MonopolyPlayer import MonopolyPlayer


class MonopolyBanker(MonopolyPlayer):
    """
    A class to model a Monopoly Banker.
    """

    # ========================================================================
    # Constructor
    # ========================================================================

    def __init__(self) -> None:
        """
        Constructor for objects of class MonopolyBanker.
        Initialises the name to "Banker", piece to "None"
        and account to new MonopolyBankerAccount object.
        """
        super().__init__()

        # update properties
        self._name = "The Banker"
        self._piece = "None"
        # self._account = MonopolyAccount()

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
        @Overrides. Banker's name cannot be set.
        """

        print("The Banker cannot change its name!")

    @property
    def piece(self) -> str:
        """
        Returns the name of the receiver
        """

        return self._piece

    @piece.setter
    def piece(self, a_name: str) -> None:
        """
        @Overrides. Banker's piece cannot be set
        """

        print("The Banker does not have a Monopoly piece!")

    # ========================================================================
    # Class methods
    # ========================================================================

    @staticmethod
    def ROLL_DICE() -> None:
        """
        @Overrides. The Banker cannot roll a dice.
        """

        print("The Banker cannot roll a dice!")

        pass

    # ========================================================================
    # Instance methods
    # ========================================================================

    def assign_to(self, a_name: str, a_piece: str) -> None:
        """
        @Overrides.
        The Banker cannot be assigned to a person.
        """

        pass

    def transfer_money(self, to_player: object, an_amount: int) -> None:
        """
        @Override.
        Credits the argument a_player by the argument an_amount.
        """

        self.debit_account(an_amount)
        to_player.credit_account(an_amount)
