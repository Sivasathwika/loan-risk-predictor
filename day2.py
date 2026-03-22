loan_amount=50000
income=80000
credit_score=800

if credit_score>=750:
    print("Excellent credit - Low Risk")
elif credit_score>=650:
    print("Good credit - Medium Risk")
elif credit_score>=500:
    print("Fair credit - High Risk")
else:
    print("Poor credit - Rejection")

print("\n--- Loan Repayment Calculator ---")
loan=10000
monthly_payment=1500
month=1

while loan>0:
    loan=loan-monthly_payment
    if loan<0:
        loan=0
    print("Month",month,"-Remaining loan:",loan)
    month=month+1
print("LOan fully paid in",month-1,"months")


#writing to a file
print("\n--- Saving Loan Report ---")

report=open("loan_report.txt","w")
report.write("Loan Report\n")
report.write("Customer: Sathwika\n")
report.write("Loan Amount: 10000\n")
report.write("Monthly Payment: 1500\n")
report.write("Months to repay: 7\n")
report.close()

print("Report saved!")

reader=open("loan_report.txt","r")
content=reader.read()
reader.close()

print("\n--- Reading Loan Report ---")
print(content)
