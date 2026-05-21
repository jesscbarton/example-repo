import math

# openning page
print('''Investment - to calculate the amount of interest you'll earn on your investments.
      Bond - to calculate the amount you'll have to pay on a home loan.''')

# user to enter investment or bond. Code will lower case response
choice = input("Enter either investment or bond from the menu above to proceed: ").lower()

# choice is bond
if choice == "bond":
    pv_of_house = int(input("What is the present value of house? "))
    interest2 = (float(input("What is the interest rate? ")) / 100)/12 #interest rate divided by 100 and then 12 to produce monthly interest rate. 
    months = int(input("How many months will it take to repay bond? "))
    bond_repayment = (interest2 * pv_of_house)/(1 - (1 + interest2)**(-months))
    bond_repayment = round(bond_repayment, 2)
    print(f"Your bond repayment will R{bond_repayment} per month.")

# else if choice is investment
elif choice == "investment":
    deposit = int(input("How much money are you depositing? "))
    interest1 = float(input("What is the interest rate? "))/100
    years = int(input("How many years are you planning to invest? "))
    interest = input("Would you prefer to do simple or compound interest? ").lower()

# if interest type is simple interest
    if interest == "simple":
        simple_i = deposit * (1 + interest1 * years)
        simple_i = round(simple_i, 2)
        print(f"Your investment of {deposit} will after {years} years will be R{simple_i}")

# if interest type is compound
    elif interest == "compound":
        compound_i = deposit * math.pow((1+interest1),years)
        compound_i = round(compound_i, 2)
        print(f"Your investment of {deposit} will after {years} years will be R{compound_i}.")

# if user enters something other than simple or compound
    else:
        print("Invalid input. Enter either simple or compound.")

# if the user enters something other than investment or bond
else:
    print("Invalid input. Enter either investment or bond.")
