def check_eligibility(age,income):
    if age<18:
        print("Too young")
        return False
    elif income<20000:
        print("Income too low")
        return False
    else:
        return True

def loan_summary(customer_name,loan_amount,interest_rate):
    print("Customer Name: ",customer_name)
    print("Loan Amount: ",loan_amount)
    print("Interest Rate: ",interest_rate)
    print("Total amount to pay after 1 year: ",round((loan_amount+(loan_amount*interest_rate/100)),2))

def loan_risk_score(credit_score,income,loan_amount):
    score=int(100)
    if credit_score<600:
        score=score-30
    if credit_score>=600 and credit_score<750:
        score=score-10
    if income<30000:
        score=score-20
    if loan_amount>0.5*income:
        score=score-25

    if score>=70:
        return "Low Risk"
    elif score>50 and score<70:
        return "Medium Risk"
    else:
        return "High Risk"
    
def monthly_emi(loan_amount,interest_rate,years):
    monthly_rate=interest_rate/(12*100)
    months=years*12
    EMI=(loan_amount*monthly_rate*(1+monthly_rate)**months)/((1+monthly_rate)**months-1)
    print("Monthly EMI:",round(EMI,2))

def loan_decision(customer_name,age,income,loan_amount,interest_rate,credit_score,years):
    if(check_eligibility(age,income)):
        print("Eligible for loan")
        loan_summary(customer_name,loan_amount,interest_rate)
        final_decision=loan_risk_score(credit_score,income,loan_amount)
        monthly_emi(loan_amount,interest_rate,years)  
        if final_decision=="Low Risk":
         print("Loan Approved")
        elif final_decision=="Medium Risk":
         print("Loan Approved with conditions")
        else:        
         print("Loan Rejected")  
    else:
        print("Not eligible for loan")

def main():
    customer_name=input("Enter your name:")
    age=int(input("Enter your age:"))
    income=int(input("Enter your income:"))
    loan_amount=int(input("Enter loan amount:"))
    interest_rate=int(input("Enter interest rate:"))
    credit_score=int(input("Enter credit score:"))
    years=int(input("Enter loan tenure in years:"))
    loan_decision(customer_name,age,income,loan_amount,interest_rate,credit_score,years)

main()