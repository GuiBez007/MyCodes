#Write an algorithm that will read the salary of a worker and print his new salary with 15% increase

salary = float(input('Type your salary: '))
new_salary = salary + ((salary /100) *15)
print('Your new salary with 15% increase is ${:.2f}'.format(new_salary))

input() #wait
