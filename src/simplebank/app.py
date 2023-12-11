import toga
from toga.style import Pack
from toga.style.pack import COLUMN

class SimpleBank(toga.App):
    def startup(self):
        # Create a main window
        main_box = toga.Box(style=Pack(direction=COLUMN, padding_top=10))

        # Create account balance label
        self.balance_label = toga.Label('Balance: $0', style=Pack(padding=10))

        # Create buttons
        deposit_button = toga.Button('Deposit', on_press=self.deposit, style=Pack(padding=5))
        withdraw_button = toga.Button('Withdraw', on_press=self.withdraw, style=Pack(padding=5))

        # Create input field
        self.amount_input = toga.TextInput(style=Pack(padding=5))

        # Add widgets to the main box
        main_box.add(self.balance_label)
        main_box.add(self.amount_input)
        main_box.add(deposit_button)
        main_box.add(withdraw_button)

        # Set the main window content
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box

        # Initialize balance
        self.balance = 0
        self.update_balance_label()

    def deposit(self, widget):
        try:
            amount = float(self.amount_input.value)
            self.balance += amount
            self.update_balance_label()
        except ValueError:
            self.main_window.info_dialog('Invalid Input', 'Please enter a valid number.')

    def withdraw(self, widget):
        try:
            amount = float(self.amount_input.value)
            if amount <= self.balance:
                self.balance -= amount
                self.update_balance_label()
            else:
                self.main_window.info_dialog('Insufficient Funds', 'You do not have enough funds.')
        except ValueError:
            self.main_window.info_dialog('Invalid Input', 'Please enter a valid number.')

    def update_balance_label(self):
        self.balance_label.text = f'Balance: ${self.balance:.2f}'

def main():
    return SimpleBank()