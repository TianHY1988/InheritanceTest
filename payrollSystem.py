'''
The PayrollSystem implements a .calculate_payroll() method 
that takes a collection of employees and prints their id, 
name, and check amount using the .calculate_payroll() method 
exposed on each employee object.
'''
class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            print('')

