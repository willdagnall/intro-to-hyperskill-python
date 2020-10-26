import math

print("What do you want to calculate?")
print('type "n" - for number of monthly payments,')
print('type "a" - for annuity monthly payment amount,')
print('type "p" - for loan principal,')
decide_value = str(input())

if decide_value == 'n':
    print("Enter the loan principal:")
    loan_principal = int(input())
    print("Enter the monthly payment:")
    month_payment = int(input())
    print("Enter the loan interest:")
    loan_interest = float(input())
    nominal_i_rate = loan_interest/ (12 * 100)
    number_of_months = math.ceil(math.log(float(month_payment) / (float(month_payment) - nominal_i_rate * float(loan_principal)), nominal_i_rate+1))
    months = 12
    num_mon = (divmod(number_of_months, months))
    if num_mon[0] > 0 and num_mon[1] > 0:
        print(f"It will take {num_mon[0]} years and {num_mon[1]} months to repay this loan!")

    elif num_mon[0] > 0 and num_mon[1] == 0:
        if num_mon[0] > 1:
            print(f"It will take {num_mon[0]} years")
        else:
            print(f"It will take {num_mon[0]} year")

    elif num_mon[0] < 1 and num_mon[1] > 1:
        print(f"It will take {num_mon[1]} months")

if decide_value == 'a':
    print("Enter the loan principal:")
    loan_principal = int(input())
    print("Enter the number of periods:")
    num_of_periods = int(input())
    print("Enter the loan interest:")
    loan_int = float(input())
    i = loan_int / 12 / 100
    monthly_payments = loan_principal * ((i * math.pow(1 + i, num_of_periods)) / (math.pow(1+i , num_of_periods)-1))
    monthly_payments = math.ceil(monthly_payments)
    print(f"Your monthly payment = {monthly_payments}")

if decide_value == 'p':
    print("Enter the annuity payment:")
    annuity_payment = float(input())
    print("Enter the number of periods:")
    num_of_periods = int(input())
    print("Enter the loan interest:")
    loan_int = float(input())
    i = loan_int / 12 / 100
    loan_principal = annuity_payment / ((i * math.pow(1 + i, num_of_periods)) / (math.pow(1 + i, num_of_periods)-1))
    loan_principal = round(loan_principal)
    print(f"Your monthly payment = {loan_principal}!")
