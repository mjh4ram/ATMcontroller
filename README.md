## Structure 
- atm.py
atm.py is the topmost layer of this ATM controller.  It contains ATM class which contains all the methods to control the ATM machine. When this controller gets integrated with the ATM hardware, you only need to look for methods in this file. 

- account.py
account.py contains Account class and is in charge of operations that have to do with users accounts 

- bank_API.py 
bank_API.py contains BankAPI class which basically includes all the rest api methods to bank backend. When one needs to integrate this with an actual bank api, you only need to fill out this section 


## Problems that I simplified 
- It is most likely that each bank has their own rest APIs so having one method for each purpose might be less than enough 
- Confidential information such as passwords or PIN codes need to be encrypted before sent via https/http but I just neglected this for the sake of simplicity 


## Credit 
I could have a glimpse of how magnetic card transaction works from an article below 
https://money.howstuffworks.com/personal-finance/debt-management/magnetic-stripe-credit-card.htm
