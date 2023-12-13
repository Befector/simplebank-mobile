import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class SimpleBank(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, padding_top=10))

        self.balance_label = toga.Label('Balance: $0', style=Pack(padding=10))

        deposit_button = toga.Button('Deposit', on_press=self.deposit, style=Pack(padding=5))
        withdraw_button = toga.Button('Withdraw', on_press=self.withdraw, style=Pack(padding=5))

        amount_label = toga.Label('Amount:', style=Pack(padding=5))
        self.amount_input = toga.TextInput(style=Pack(padding=5))

        self.transaction_table = toga.Table(['Transaction Type', 'Amount'], style=Pack(flex=1, padding=10))


        main_box.add(self.balance_label)
        main_box.add(amount_label)
        main_box.add(self.amount_input)
        main_box.add(deposit_button)
        main_box.add(withdraw_button)
        main_box.add(self.transaction_table)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box

        self.balance = 0
        self.transaction_history = []
        self.update_balance_label()

    def deposit(self, widget):
        try:
            amount = float(self.amount_input.value)
            if amount < 0:
                raise ValueError("Amount cannot be negative.")
                
            self.balance += amount
            self.update_balance_label()
            self.add_transaction('Deposit', amount)
            self.show_confirmation_dialog('Deposit Successful', f'You successfully deposited ${amount:.2f}.')
        except ValueError as e:
            self.main_window.info_dialog('Invalid Input', str(e))

    def withdraw(self, widget):
        try:
            amount = float(self.amount_input.value)
            if amount < 0:
                raise ValueError("Amount cannot be negative.")
                
            if amount <= self.balance:
                self.balance -= amount
                self.update_balance_label()
                self.add_transaction('Withdrawal', amount)
                self.show_confirmation_dialog('Withdrawal Successful', f'You successfully withdrew ${amount:.2f}.')
            else:
                self.main_window.info_dialog('Insufficient Funds', 'You do not have enough funds.')
        except ValueError as e:
            self.main_window.info_dialog('Invalid Input', str(e))

    def update_balance_label(self):
        self.balance_label.text = f'Balance: ${self.balance:.2f}'

    def add_transaction(self, transaction_type, amount):
        self.transaction_history.append((transaction_type, amount))
        self.update_transaction_table()

    def update_transaction_table(self):
        self.transaction_table.data = [(trans[0], f'${trans[1]:.2f}') for trans in self.transaction_history]

    def show_confirmation_dialog(self, title, message):
        self.main_window.info_dialog(title, message)

def main():
    return SimpleBank()