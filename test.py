
from __future__ import annotations
from Monopoly import Player


class Test:

    @staticmethod
    def player_init(self):
        """
        Tests that a Player class initialises as expected.
        """

        # declare new Player object
        p: Player = Player()

        assert p.name == "", "Name did not initialse to empty string"
        assert p.piece == "", "Piece did not initialse to empty string"
        assert p.account_balance == 0, ("Account balance not did not " +
                                        "initialse to 0")

        print("Test passed: Object initiated as expected.")

    @staticmethod
    def player_set():
        """
        Tests that we can set the properties of Player.
        """

        # declare new Player object
        p: Player = Player()

        p.name = "Player 1"
        p.piece = "Duck"
        p.account_balance = 500

        assert p.name == "Player 1", "Name did not set correctly"
        assert p.piece == "Duck", "Piece did not set correctly"
        assert p.account_balance == 500, ("Account balance not did not " +
                                          " set correctly")

        print("Test passed: Object was set as expected.")

    @staticmethod
    def player_assign():
        """
        Tests the assign method.
        """

        # declare new Player object
        p: Player = Player()

        p.assign("Player 1", "Duck", 500)

        assert p.name == "Player 1", "Name did not set correctly"
        assert p.piece == "Duck", "Piece did not set correctly"
        assert p.account_balance == 500, ("Account balance not did not " +
                                          " set correctly")

        print("Test passed: Object was assigned as expected.")

    @staticmethod
    def player_to_string():
        """
        Tests the __str__ dunder method.
        """

        # declare new Player object
        p: Player = Player()

        p.assign("Player 1", "Duck", 500)

        a_str: str = (p.name + " is playing as the " + p.piece +
                      " with an account balance of £" +
                      str(p.account_balance))

        assert str(p) == a_str, "Strings are not equal"

        print("Test passed: " + str(p))

    @staticmethod
    def player_representation():
        """
        Tests the representation of the Monopoly.Player class.
        """

        # declare new Player object
        p: Player = Player()

        p.assign("Player 1", "Duck", 500)

        return p

    @staticmethod
    def player_equals():
        """
        Tests if the equals method returns as expected.
        """

        # declare three Player objects
        p1: Player = Player()
        p2: Player = Player()
        p3: Player = Player()

        p1.assign("Player 1", "Duck", 500)
        p2.assign("Player 1", "Duck", 500)
        p3.assign("Player 3", "Dog", 300)

        assert p1 == p2, "Same objects returning False"
        assert p1 != p3, "Diff objects returning True"

        print("Test passed.")
