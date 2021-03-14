# testing the MonopolyAccount

from Monopoly_v2.MonopolyAccount import MonopolyAccount
from Monopoly_v2.MonopolyPlayer import MonopolyPlayer

# ============================================================================
# Testing MonopolyAccount
# ============================================================================

# declare and initialise
a1: MonopolyAccount = MonopolyAccount()
a2: MonopolyAccount = MonopolyAccount()

# test getter. Expected, 500
a1.balance

# test setter
a1.balance = 1000

# test describe. Expected, Account Balance £1000
a1.describe()

# reset account
a1.balance = 500

# test give_money. Expected, true
a1.debit(250)

# get balance. Expected, 250
a1.balance

# test take_money
a1.credit(125)

# get balance. Expected, 375
a1.balance

# test transfer. Expected, true
a1.transfer_money(a2, 100)

# get balance a, Expected, 275
a1.describe()

# get balance a2. Expected, 600
a2.describe()

# ============================================================================
# Testing MonopolyPlayer
# ============================================================================

p1: MonopolyPlayer = MonopolyPlayer()
p2: MonopolyPlayer = MonopolyPlayer()

# Assign p1 and p2
p1.assign_to("LK", "Dog")

# Testing describe
p1.describe()

p1.account_balance

p1.credit_account(100)
p1.account_balance

p1.debit_account(50)
p1.describe()

p1.transfer_money(p2, 300)
p1.describe()
p2.describe()
