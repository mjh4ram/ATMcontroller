from bank_API import BankAPI


# Bank account class
class Account:
    '''
    Constructor gets data from magnetic stripe
    data class is not implemented for the sake of simplicity
    '''
    def __init__(self, data):
        # name of the bank
        self.bank = data.bank
        # bank account number
        self.account_number = data.account_number
        # session token
        self.token = None
        # account (savings/checking)   0 - checking, 1 - savings
        self.is_savings = None



    def send_PIN(self, code):
        # if PIN code does not consist of 4 digits return 0
        if code < 1000 or code > 9999:
            return 0

        # bank_response: 1 = success 0 = invalid pin -1 = account locked/error
        # In real world case, the code needs to be encrypted
        bank_response = BankAPI.send_PIN(self.bank, self.account_number, code)

        # PIN code is correct
        if bank_response == 1:
            pass
            # set token
            # self.token = bank_response.token
        return bank_response


    def select_account(self, is_savings):
        # check whether the user has the selected account check 1 = exists 0 = x exists -1 = error
        check = BankAPI.check_account(self.bank, self.account_number, is_savings, token)

        # the selected account exists under the user's name
        if check:
            self.is_savings = is_savings
        return check

    def see_balance(self):
        # if session has expired/error occured return -1
        balance = BankAPI.see_balance(self.bank, self.account_number, is_savings, token)

        return balance


    def deposit(self, amount):
        # bank_response: 1 = success -1 = session expired /error occured
        bank_response = BankAPI.deposit(self.bank, self.account_number, is_savings, token, amount)

        return bank_response

    def withdraw(self, amount):
        # bank_response: 1 = success 0 = insufficient funds -1 = session expired/erro occured
        bank_response = BankAPI.withdraw(self,bank, self.account_number, is_savings, token, amount)

        return bank_response
