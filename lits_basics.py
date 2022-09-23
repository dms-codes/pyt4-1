my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#
res = []
for i in range(len(my_list)):
    if my_list[i] not in my_list[i+1:]:
        res.append(my_list[i])
    
print("The list with unique elements only:")
my_list = res
print(my_list)
