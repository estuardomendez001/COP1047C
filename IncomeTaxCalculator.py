

gross_income = 150000.00   #gross income
num_dependents = 3   #number of dependents
standard_deduction = 10000


print("Enter the gross income: ", f'{gross_income:.2f}')
print("Enter the number of dependents: ", num_dependents)


#sum of gross income after deductions
sum = (gross_income - standard_deduction - (num_dependents * 3000))


income_tax = sum * .20
print("The income tax is: ", income_tax)


