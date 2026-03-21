name="Sathwika"
age=21
cgpa=9.11

print("Name:",name)
print("Age:",age)
print("CGPA:",cgpa)

gpa_percentage=cgpa*10
print("Percentage:",gpa_percentage)

skills=["Java","Python","SQL"]
print("My skills:",skills)
print("First skill:",skills[0])

skills.append("Machine Learning")
print("Updated skills:",skills)

for skill in skills:
    print("I know:",skill)



student={
    "name":"Sathwika",
    "cgpa":9.11,
    "branch":"CSIT",
    "college":"GRIET"
}

print("Student details:",student)
print("Name:",student["name"])
print("CGPA:",student["cgpa"])

for key, value in student.items():
    print(key,":",value)


def calculate_risk(income, loan_amount):
    ratio = loan_amount/income
    if ratio > 0.5:
        return "High Risk"
    elif ratio > 0.3:
        return "Medium Risk"
    else: 
        return "Low Risk"
    
print(calculate_risk(50000,10000))
print(calculate_risk(50000,20000))
print(calculate_risk(50000,30000))