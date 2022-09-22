blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	
height = 0
while blocks>height:   
    blocks-=height+1   
    height += 1

print("The height of the pyramid:", height)
