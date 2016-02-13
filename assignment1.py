# Your function for calculating payment goes here
def caculateMonthlyPayments (principle, annual_interest_rate, duration):
    MONTH_PER_YEAR = 12
    # initialize the const and the return value.
    monthlypayment = 0

    # caculate n
    # n is the total number of monthly payments for the entire duration of the loan
    # n is equal to loan duration in years multiplied by 12
    n = duration * MONTH_PER_YEAR

    # if the annual_interest_rate is equal to zero
    # then return the monthly payment = principle/n
    if annual_interest_rate == 0:
        monthlypayment = principle/n
        return monthlypayment

    # else (the annual_interest_rate is NOT equal to zero)
    # Caculate the monthly interest rate r 
    # r should be calculated by first dividing the annual_interest_rate by 100 and then 
    # divide the result by 12 to make it monthly).
    # return the Monthly payment by the following equestion
    # MonthlyPayment = principle * r(1+r)^n / ((1+r)^n - 1)
    else:
        r = (annual_interest_rate/100)/MONTH_PER_YEAR
        monthlypayment = principle * r*(1+r)**n / ((1+r)**n - 1)
        return monthlypayment

# Your function for calculating remaining balance goes here
def CaculateRemainingLoanBalance (principle, annual_interest_rate, duration , number_of_payments):

    MONTH_PER_YEAR = 12
    # initialize the const and the return value.
    remainloadbalance = 0

    # caculate n
    # n is the total number of monthly payments for the entire duration of the loan
    # n is equal to loan duration in years multiplied by 12
    n = duration * MONTH_PER_YEAR

    # if the annual_interest_rate is equal to zero
    # then return the RemainLoadBalance = principle * (1 - number_of_payments/n) 
    if annual_interest_rate == 0:
        remainloadbalance = principle * (1 - number_of_payments/n) 
        return remainloadbalance

    # else (the annual_interest_rate is NOT equal to zero)
    # Caculate the monthly interest rate r 
    # r should be calculated by first dividing the annual_interest_rate by 100 and then 
    # divide the result by 12 to make it monthly).
    # return the remain load balance by the following equestion
    # RemainLoadBalance = principle * ( (1+r)^n - (1+r)^number_of_payments ) / ((1+r)^n - 1)
    else:
        r = (annual_interest_rate/100)/MONTH_PER_YEAR
        remainloadbalance = principle * ( (1+r)**n - (1+r)**number_of_payments ) / ((1+r)**n - 1)
        return remainloadbalance

# Your main program goes here

principle=float(input("Enter loan amount: "))
annual_interest_rate=float(input("Enter annual interest rate (percent): "))
duration=int(input("Enter loan duration in years: "))
monthlypayment = caculateMonthlyPayments(principle, annual_interest_rate, duration)

print (principle)
print (annual_interest_rate)
print ("LOAN AMOUNT: %.1f INTEREST RATE (PERCENT): %.1f" %(principle, annual_interest_rate))
print ("DURATION (YEARS): %d MONTHLY PAYMENT: %d" %(duration, monthlypayment))
totalpayment = 0
remainloadbalance = 0
MONTH_PER_YEAR = 12
for i in range(1,duration + 1):
    remainloadbalance = CaculateRemainingLoanBalance(principle, annual_interest_rate, duration, i*MONTH_PER_YEAR)
    print ("YEAR: %d BALANCE: %d TOTAL PAYMENT %d" %(i, remainloadbalance, monthlypayment*12*i))
