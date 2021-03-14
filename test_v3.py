from Monopoly_v3.MonopolyBanker import MonopolyBanker
from Monopoly_v3.MonopolyPlayer import MonopolyPlayer

banker: MonopolyBanker = MonopolyBanker()
banker.describe()

banker.name = "Change name"

banker.ROLL_DICE()
banker.piece
banker.piece = "Shoe"

banker.describe()

p1: MonopolyPlayer = MonopolyPlayer()

p1.assign_to("Liam", "Car")

banker.transfer_money(p1, 500)
banker.describe()
