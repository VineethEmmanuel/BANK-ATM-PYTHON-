class ATM:
    def __init__(self,atmCard,pinNumber):
        self.atmCard    =   atmCard
        self.pinNumber  =   pinNumber  
        
    def balance(self):     
        print("Your balance is ₹50,000")
        
    def bankEnquiryWithdraw(self,amount):
        new_amount = 50000 - amount
        print("You have withdrawn "+str(amount) +". Your remaining balance is "+ str(new_amount))

    def bankEnquiryDeposit(self,amount):
        new_amount = 50000 + amount
        print("You have deposited "+str(amount) +". Your remaining balance is "+ str(new_amount))

def main():
        
     #Creating variables for card number and pin number
    card_no =   input("Insert your card number here :  ")
    pin_no  =   input("Insert your pin number here(Dont't worry its perfectly safe) :  ")
        
    #For new users
    new_user =  ATM(card_no,pin_no)
        
    #Choose the activity
    print("Which activity do you want to do?  : ")
    print("1.Balance Enquriy   2.withdrawl  3.deposit")
    activity = int(input("Enter the number of your activity :- "))
        
    if (activity == 1):
        new_user.balance()
        
    elif (activity == 2):
        amount = int(input("Enter the amount you want to withdraw:- "))
        new_user.bankEnquiryWithdraw(amount)

    elif (activity == 3):
        amount = int(input("Enter the amount you want to deposit:- "))
        new_user.bankEnquiryDeposit(amount)
        
    else:
        print("Please enter a valid number.")
        
if __name__ == "__main__":
    main()