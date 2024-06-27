my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
new_list = []

print('Aleatório>', my_list)

for x in range (50):
    for i in range(1, len(my_list)):
        if my_list[i] > largest:
            largest = my_list[i]
            
    new_list.append(largest)
    
    for z in range(len(my_list)):
        if my_list[z] == largest:
            my_list[z] = 0
            
    largest = my_list[0]
    
    if x == len(my_list)-1:
        break

print('Organizado>', new_list)

input()
