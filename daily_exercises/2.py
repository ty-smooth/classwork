# Problem 1
print(50+50)
print(100-10)

# Problem 2
print(30+6)
print(6^6)
print(6**6)
print(6+6+6+6+6+6)

# Problem 3
print("Hello World")
print("Hello World : 10")

# Problem 4
loan_size = 800000
interest_rate = 6.0
length_months = 103

monthly_interest = 1+(interest_rate)/(12*100)
monthly_payment = loan_size*(monthly_interest**length_months)*(1-monthly_interest)/(1-monthly_interest**length_months)
print(monthly_payment)