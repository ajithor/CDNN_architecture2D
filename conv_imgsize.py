x = int(input("Enter the pixel value\n"))
y = int(input())
print("\nFor Convolving")
csx = int(input("Enter the stride_x"))
csy = int(input("Enter the Stride_y"))
cfx = int(input("Ener Fliter_x"))
cfy = int(input("Ener Fliter_y"))
cfno = int(input("Enter no. of filters"))
#cpa = input("Zero Padding? (S/V)")
zpx = int(input("Zero padding_X"))
zpy = int(input("Zero padding_Y"))
l = int(input("Enter no. of layers "))


print("\nFor pooling")
psx = int(input("Enter the stride_x"))
psy = int(input("Enter the Stride_y"))
pfx = int(input("Ener Fliter_x"))
pfy = int(input("Ener Fliter_y"))

for i in range(1,l+1):
	#CONV
	
	x = (x - cfx + (2 * zpx)) / csx +1		
	y = (y - cfy + (2 * zpy)) / csy +1

	print("CONV--> [", str(int(x)), " X ",str(int(y)), end = "]\n")
	#pool

	x = (x - pfx) / psx + 1
	y = (y - pfy) / psy + 1

	print("--> POOL--> [", str(int(x)), " X ", str(int(y)), end = "]\n")