class Bank_Account:
    def __init__(self,account_number,balance,owner_name,date_opened):
        self.account_number=account_number
        self.balance=balance
        self.owner_name=owner_name
        self.date_opened=date_opened

    def deposit(self):
           self.initial_amount=int(input("Enter amount to be deposited:"))
           return self.initial_amount

    def withdraw(self):
          self.final_amount=int(input("Enter amount to be withdrawn:"))
          return self.final_amount

    def check_balance(self):
          remaining_amount=(self.initial_amount-self.final_amount)+self.balance
          print(f"Available balance is:Ksh.{remaining_amount}")

    def display_info(self):
          remaining_amount=(self.initial_amount-self.final_amount)+self.balance
          print(f"{self.owner_name} available balance is Ksh.{remaining_amount}")

    def close_account(self):
          print(f"Thank you for choosing us,{self.owner_name}")
    def get_details(self):
        print("client details")
        print(f"Name:{self.owner_name} -Account Number:{self.account_number} -Balance:{self.balance} -Date Opened:{self.date_opened}")
        print("-------------------")
client=Bank_Account("09745453434",100,"Emmanuel Muteti","1-1-2026")
print(type(client))
print(client)
client.get_details()
client.deposit()
client.withdraw()
client.check_balance()
client.display_info()
client.close_account()