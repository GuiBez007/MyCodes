# Write a code that can approve a -bank loan- to buy a house.
# Ask the house value, the buyer salary and how many years he'll pay.
# The monthly -render- cannot be upper 30% of the salary or else the loan will be denied

house_value = float(input('Type the total house value: '))
salary = float(input('Type your salary: '))
months = int(input('How many years do you wish to pay this house?: ')) * 12
render = house_value / months

if render > (salary * 0.3):
    print('RENDER DENIED!')
else:
    print('RENDER ALLOWED!')

input() #wait