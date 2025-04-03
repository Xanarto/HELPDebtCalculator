#globals
HECS = 18550 #The total loan amount in AUD
salary = 63000 #Your yearly salary in AUD
Repaymentrate = 0.015 #This is what the HELP loan calls the intrest rate

#tallys
TotalInt = 0
TotalPayed = 0
yearsPassed = 0

while HECS > 0:
    print(f"Salary: ${salary:.2f}", end="")
    index = HECS * 0.039
    print(f" \tIndex: ${index:.2f}", end="")
    HECS += index
    print(f" \tDebt+: ${HECS:.2f}", end="")
    Repaymentrate += 0.005
    print(f" \tRate: {Repaymentrate*100:.2f}%", end="")
    payment = Repaymentrate * salary
    print(f" \tPayment: ${payment:.2f}", end="")
    HECS -= payment
    print(f" \tHECS: ${HECS:.2f}")
    salary += 5000
    TotalPayed += payment
    TotalInt += index
    yearsPassed += 1

TotalPayed += HECS
print(f"Time it took to pay the debt: {yearsPassed}")
print(f"Total Payed: ${TotalPayed:.2f}")
print(f"Total Index: ${TotalInt:.2f}")