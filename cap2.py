class Employee:
    def __init__(self, salary_amt, emp_type, org_type, sum_insured):
        # Initialize an Employee object with salary_amt, empyment type, organization type, and sum insured
        self.salary_amt = salary_amt
        self.employment_type = emp_type
        self.organization_type = org_type
        self.sum_insured = sum_insured

class TaxCalculator:
    def __init__(self, employee, num_child, children_in_school):
        # initialize TaxCalculator instance with an Employee, specifying the number of children and their schooling status.
        self.employee = employee
        self.num_child = num_child
        self.children_in_school = children_in_school
    #Compute the taxable income, total deductions, and final tax immediately upon instantiation.
        self.taxable_income = self.calculate_taxable_income()
        self.total_deductions = self.calculate_total_deductions()
        self.final_tax = self.calculate_final_tax()

    def calculate_taxable_income(self):
    #Return the employee's salary amount as the taxable income.
        return self.employee.salary_amt

    def calculate_total_deductions(self):
        # Calculate total deductions based on employment type(emp_type), organization type(org_type), and number of children in school(num_child)
        total_deductions = 0

        # Add deductions for regular employees and government employees
        if self.employee.employment_type in ["Regular", "Irregular"]:
            total_deductions += self.employee.salary_amt * 0.11  # Employee contribution 
            total_deductions += self.employee.salary_amt * 0.16  # Pension contribution
            total_deductions += self.employee.salary_amt * 0.10  # Provident Fund contribution

        # Add deductions for private organizations
        if self.employee.organization_type == "Private":
            total_deductions += min(0.05 * self.employee.salary_amt, 0.1 * self.employee.salary_amt)  # Minimum 5% or 10% of total income

        # Adapt deductions for corporate agencies based on the pay revision rate.
        if self.employee.organization_type == "Corporate":
            total_deductions += self.employee.salary_amt * 0.16  # Pension
            total_deductions += self.employee.salary_amt * 0.06  # PF

        # Add education allowance for each child in school
        for child_school_status in self.children_in_school:
            if child_school_status.lower() == "yes":
                total_deductions += 350000  # Education allowance for each child in school
        return total_deductions
    
    def calculate_final_tax(self):
        # Calculate the final tax based on taxable income after deductions
        if self.taxable_income <= 300000:
            return 0  #Exempt individuals with earnings below the minimum taxable income.
        taxable_income_after_deductions = self.taxable_income - self.total_deductions
        if taxable_income_after_deductions <= 300000:
            return 0
        elif taxable_income_after_deductions <= 400000:
            return taxable_income_after_deductions * 0.10
        elif taxable_income_after_deductions <= 650000:
            return taxable_income_after_deductions * 0.15
        elif taxable_income_after_deductions <= 1000000:
            return taxable_income_after_deductions * 0.20
        elif taxable_income_after_deductions <= 1500000:
            return taxable_income_after_deductions * 0.25
        else:
            return taxable_income_after_deductions * 0.30

    def get_final_tax(self):
        #Return the previously calculated final tax.
        return self.final_tax
    
class GISCalculator:
   #Initialize a General insurance schemeCalculator instance with an Employee object.
    def __init__(self, employee):
        self.employee = employee

    def calculate_monthly_payment(self):
       # Calculate the monthly payment for GIS based on the sum assured.
        return self.employee.sum_insured / 12

name = input("Enter your Good Name: ")
position = input("Enter your hometown: ")
salary = float(input("Enter your salary: "))
#Verify if the salary is less than 300,000 and display a message.
if salary < 300000:
    print("Your salary must be at least 300,000.")
else:
    emp_type = input("Enter your employment type (Contract/Regular): ")
    org_type = input("Enter your organization type (Government/Private/Corporate): ")

    sum_insured = float(input("Enter the sum insured for GIS: "))
    num_child = int(input("Enter the number of children: "))

    #Request the user to indicate whether each child is attending school and store the responses in a list.
    children_in_school = [input(f"Is child {i+1} in school? (Yes/No): ") for i in range(num_child)]

    # Create an Employee object with the provided salary, employment type, organization type, and sum insured
    # Create a TaxCalculator object with the employee, number of children, and whether each child is in school
    # Create a GISCalculator object with the employee
    employee = Employee(salary, emp_type, org_type, sum_insured)
    tax_calculator = TaxCalculator(employee, num_child, children_in_school)
    gis_calculator = GISCalculator(employee)
#Then the code prints the final tax amount and the monthly GIS (General Insurance Scheme) payment for the employee.
    print(f"Your final tax amount is: {tax_calculator.get_final_tax()}")
    print(f"Your monthly GIS payment is: {gis_calculator.calculate_monthly_payment()}")
