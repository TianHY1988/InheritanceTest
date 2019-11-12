from payrollSystem import PayrollSystem
from employees.salaryEmployee import SalaryEmployee
from employees.hourlyEmployee import HourlyEmployee
from employees.commissionEmployee import CommissionEmployee
from employees.disgruntledEmployee import DisgruntledEmployee

# from employee import Employee

salary_employee = SalaryEmployee(1, 'John Smith', 1500)
hourly_employee = HourlyEmployee(2, 'Jane Doe', 40, 15)
commission_employee = CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
disgruntled_employee = DisgruntledEmployee(0, 'Anonymous')
# base_employee = Employee(4, 'Invalid')
payroll_system = PayrollSystem()
payroll_system.calculate_payroll([salary_employee, 
    hourly_employee, commission_employee, disgruntled_employee])
# payroll_system.calculate_payroll([base_employee])