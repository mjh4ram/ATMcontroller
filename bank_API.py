




'''
BankAPI class
To make things simpler and easier for the intergration process
in the future, I left the methods below blank
'''
class BankAPI:
    '''
    Sends encrypted PIN code to bank's authentication backend
    Returns 1 if the code is valid
    Returns 0 if the code is invalid
    Returns -1 if user account has been locked
    '''
    @staticmethod
    def send_PIN(self, bank, account_number, code):
        return 1


    '''
    Checks whether the selected account exists
    Returns 1 if the account exists
    Returns 0 if the account does not exists
    Returns -1 if session expired / error occured
    '''
    @staticmethod
    def check_account(self, bank, account_number, is_savings, token):
        return 1

    '''
    Retrieves balance from Bank backend server
    Returns balance if everything goes successfully
    Returns -1 if session expired / error occured
    '''
    @staticmethod
    def see_balance(self, bank, account_number, is_savings, token):
        return 1

    '''
    Deposits money
    Returns 1 if everthing goes successfully
    Returns -1 if session expired / error occured
    '''
    @staticmethod
    def deposit(self, bank, account_number, is_savings, token, amount):
        return 1

    '''
    Withdraws money
    Returns 1 if everthing goes successfully
    Returns 0 if insufficient funds
    Returns -1 if session expired / error occured
    '''
    @staticmethod
    def withdraw(self, bank, account_number, is_savings, token, amount):
        return 1
