num_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]
num = int(input( "Enter the number to replace the last element of each tuple: "))
new_listt = []
for i in num_list:
    update_no = i[:-1] + (num,)
    new_listt.append(update_no)
print(new_listt)
