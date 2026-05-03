age = int(input("Enter age: "))


age = int(input("Enter age :  "))
salary = int(input("Enter the Salary : "))
credit_Score = int(input("Enter the Credit Score:  "))

if age >= 18 and salary >= 25000:
  if credit_Score >=750 :
    print("Premium Loan ✅ ")
  elif credit_Score >=600:
    print("Standard Loan ✅")
  else:
    print("Loan Rejected ❌")
else:
  print("Not Eligible ❌" )