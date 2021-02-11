from account import Account

# ATM controller class
class ATM:
    def __init__(self):
        self.user_account = None

    '''
    When a card is inserted to the ATM, the magnetic stripe reader decodes
    the manetic stripe and calls insert_card method.
    This method serves to create Account object with the given user data from
    the magnetic stripe.
    '''
    def insert_card(self, data):
        if self.user_account is None:
            self.user_account = Account(data)
        else:
            self.close_session()
            self.insert_card(data)
        return 1

    '''
    This method serves to verify the PIN code. It interacts with bank systems
    via API and checks if it is valid. This method cannot be called before
    insert_card method
    '''
    def enter_PIN(self, code):
        # bank_response: 1 = success 0 = invalid pin -1 = account locked
        bank_response = self.user_account.send_PIN(code)

        return bank_response



    '''
    This method allows users to select savings/chekcing account. This method
    cannot be called before enter_PIN method
    '''
    def select_account(self, is_savings):
        # bank_response: 1 = success 0 = account does not exist
        bank_response = self.user_acount.select_account(is_savings)

        return bank_response


    '''
    This method allows users to see their balance. This method cannot be
    called before select_account method
    '''
    def see_balance(self):
        # if session has expired/ error occured return -1
        balance = self.user_account.see_balance

        return bank_response
    '''
    This method serves to deposit money. Amount should always be positive
    and this method cannot be called before select_account method
    '''
    def deposit(self, amount):
        # bank_response: 1 = success -1 = session expired /error occured
        bank_response = self.user_account.deposit(amount)

        return bank_response

    '''
    This method serves to withdraw money. Amount should always be positive
    and this method cannot be called before select_account method
    '''
    def withdraw(self, amount):
        # bank_response: 1 = success 0 = insufficient funds -1 = session expired/erro occured
        bank_response = self.user_acount.deposit(amount)

        return bank_response
    '''
    Flushes user_account variable
    '''
    def close_session(self):
        self.user_account = None
