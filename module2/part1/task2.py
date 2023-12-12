# Getting 3 values from the user
# Reused from the solution in task 1
monthlySalary = int(input("Зарплата за місяць: "))
monthlyBankLoan = int(input("Сума місячного платежу за кредитом у банку: "))
taxes = int(input("Заборгованість за комунальні послуги: "))

# Taking the monthly salary and taking money to: Monthly bank loan and taxes.
sum = monthlySalary - monthlyBankLoan - taxes

print(f"Сума після оплати: {sum}")