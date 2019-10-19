class BalanceEnquiry:
    def __init__(self, balanceAmount)
        self.balanceAmount = balanceAmount
    
    def printBalanceAmount(self)
        print(self.balanceAmount)
        
class CashTransfer:
    def __init__(cashTransfer, accountNumber, beneficiaryName, amountTransferred)
        self.accountNumber = accountNumber
        self.beneficiaryName = beneficiaryName
        self.amountTransferred = amountTransferred
        
class CashWithdrawal:
    def __init__(cashWithdrawal, amountTransferred, denomimation, currentBalance)
        self.amountTransferred = amountTransferred
        self.denomimation = denomimation
        self.currentBalance = currentBalance
        
class PinChage:
    def __init__(self, previousPIN, newPIN)
        self.previousPIN = previousPIN
        self.newPIN = newPIN
        
class PhoneChange:
    def __init__(self, newPhoneNumber)
        self.newPhoneNumber = newPhoneNumber
        
class Transaction:
    def __init__(self, transactionID, ATM_CardNumber, date, time, AT_MachineUID, status, responseCode, type)
        self.transactionID = transactionID
        self.ATM_CardNumber = ATM_CardNumber
        self.date = date
        self.time = time
        self.AT_MachineUID = AT_MachineUID
        self.status = status
        self.responseCode = responseCode
        self.type = type
        
 class ATM_Card:
    def __init__(self, ATM_CardNumber, accountNumber, PIN, name, dateOfIssue, expiryDate, address, twoFactorAuthStatus, phoneNumber, cardStatus)
        self.ATM_CardNumber = ATM_CardNumber
        self.accountNumber = accountNumber
        self.PIN = PIN
        self.name = name
        self.dateOfIssue = dateOfIssue
        self.expiryDate = expiryDate
        self.address = address
        self.twoFactorAuthStatus = twoFactorAuthStatus
        self.cardStatus = cardStatus
        
class AccountExtension:
    def __init__(self, accountNumber, name, phoneNumber, balance)
        self.accountNumber = accountNumber
        self.name = name
        self.phoneNumber = phoneNumber
        self.balance = balance

class AT_MachineRefill:
    def __init__(self, refillID, AT_MachineUID, amount, ATM_Branch, refillDate, previousBalance)
        self.refillID = refillID
        self.AT_MachineUID = AT_MachineUID
        self.amount = amount
        self.ATM_Branch = ATM_Branch
        self.refillDate = refillDate
        self.previousBalance = previousBalance
        
class AT_Machine:
    def __init__(self, AT_MachineUID, currentBalance, location, minimumBalance, status, lastRefillDate, nextMaintenanceDate)
        self.AT_MachineUID = AT_MachineUID
        self.currentBalance = currentBalance
        self.location = location
        self.minimumBalance = minimumBalance
        self.status = status
        self.lastRefillDate = lastRefillDate
        self.nextMaintenanceDate = nextMaintenanceDate
